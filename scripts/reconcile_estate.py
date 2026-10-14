#!/usr/bin/env python3
"""Materialize Git-authoritative public Governance bytes into an estate checkout.

Dry-run by default. This does NOT deploy, modify DNS, or claim HTTPS release.
Never traverses outside a named governance.fountain.coach destination.
"""
import argparse
from pathlib import Path
import os
import shutil
import sys
from verify_publication import SITE, local_audit

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--estate-site",required=True,type=Path,
                    help="Full path to estate/sites/governance.fountain.coach")
    ap.add_argument("--apply",action="store_true")
    args=ap.parse_args()
    target=args.estate_site.resolve()
    if target.name!="governance.fountain.coach" or "sites" not in target.parts:
        raise ValueError("Refusing to write outside estate/sites/governance.fountain.coach")
    if not target.is_dir():raise ValueError("Unknown estate site target")
    hashes=local_audit()
    expected=set(hashes)
    current={p.relative_to(target).as_posix() for p in target.rglob("*") if p.is_file()}
    extra=sorted(current-expected)
    if extra:raise ValueError("Estate contains extra files; never silently delete: "+str(extra))
    change=[]
    for rel in sorted(expected):
        src=SITE/rel;dst=target/rel
        if not dst.exists() or src.read_bytes()!=dst.read_bytes():change.append(rel)
    print("GOVERNANCE_AUTHORITATIVE_SOURCE",SITE)
    print("DERIVED_ESTATE_TARGET",target)
    print("FILES",len(hashes),"DRIFT",len(change),"APPLY",args.apply)
    for rel in change:print("DIFF",rel)
    if args.apply:
        for rel in change:
            src=SITE/rel;dst=target/rel
            dst.parent.mkdir(parents=True,exist_ok=True)
            tmp=dst.with_name(dst.name+".governance-authority-tmp")
            shutil.copyfile(src,tmp)
            os.replace(tmp,dst)
        print("LOCAL_MATERIALIZATION_COMPLETE",len(change),
              "HTTPS_RELEASE_NOT_PERFORMED")
    elif change:
        print("READ_ONLY_DIFF_NOT_IMPORTED; pass --apply to update only this site",
              file=sys.stderr)

if __name__=="__main__":main()
