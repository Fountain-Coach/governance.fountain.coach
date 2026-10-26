#!/usr/bin/env python3
"""Verify the exact Git-owned governance.fountain.coach publication edition.

Usage:
  python3 scripts/verify_publication.py
  python3 scripts/verify_publication.py --against-live

The first verification is entirely local, immutable and deterministic.
The optional HTTPS witness compares every tracked public byte with the server.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/"site"

def sha(data):
    return hashlib.sha256(data).hexdigest()

def recorded():
    entries={}
    for line in (ROOT/"publication-files.sha256").read_text().splitlines():
        digest,sep,path=line.partition("  ")
        if not sep or len(digest)!=64 or path in entries:raise ValueError("Invalid file checksum line")
        if Path(path).is_absolute() or ".." in Path(path).parts:raise ValueError("Unsafe file name: "+path)
        entries[path]=digest
    return entries

def local_audit():
    expected=recorded()
    current={}
    for f in SITE.rglob("*"):
        if f.is_symlink():raise ValueError("No symlinks in public publication "+str(f))
        if f.is_file():current[f.relative_to(SITE).as_posix()]=sha(f.read_bytes())
    if current!=expected:
        missing=sorted(set(expected)-set(current))
        unexpected=sorted(set(current)-set(expected))
        changed=sorted(n for n in current.keys()&expected.keys() if current[n]!=expected[n])
        raise ValueError(f"Publication tree drift: missing={missing} unexpected={unexpected} changed={changed}")
    routes=json.loads((SITE/"route-manifest.json").read_text())
    assert routes["host"]=="governance.fountain.coach"
    published_routes=routes["routes"]
    assert len(published_routes)==161, "The candidate route manifest must describe 161 indexed routes"
    route_pages=set()
    for route in published_routes:
        for public_path in route["publicPaths"]:
            clean=public_path.lstrip("/")
            if clean not in current:raise ValueError("Missing declared public route "+clean)
            route_pages.add(clean)
    all_chapters={x for x in current if x.startswith("chapters/") and x.endswith("/index.html")}
    if len(all_chapters)!=161:raise ValueError("Candidate chapter inventory must contain 161 chapter pages")
    # This edited edition retains the six already-witnessed historical
    # manifest omissions. Chapter 159 is explicitly added. This is source
    # candidate integrity, NOT a renewed live HTTPS parity claim.
    unmapped=(all_chapters|{"index.html"}|
             {f"{x}/index.html" for x in
              ("legal","privacy","accessibility","copyright","compliance")})-route_pages
    expected_unmapped={"chapters/158-publishing-is-not-a-distributed-transaction/index.html"}|{
        f"{x}/index.html" for x in
        ("legal","privacy","accessibility","copyright","compliance")}
    if unmapped!=expected_unmapped:
        raise ValueError("Unexpected live route-manifest omission: "+str(sorted(unmapped)))
    status=json.loads((SITE/"chapter-status.json").read_text())
    if status["latestChapter"].get("number")!="160":
        raise ValueError("Governance chapter status unexpected")
    print("GOVERNANCE_SOURCE_CANDIDATE_VERIFIED",len(current),"matching files",
        len(all_chapters),"complete chapter routes",len(route_pages),"declared routes",
        "latestChapter",status["latestChapter"]["number"],
        "knownUnmappedRoutes",len(expected_unmapped))
    return expected

def live_audit(files):
    def fetch(item):
        rel,digest=item
        proc=subprocess.run(["/usr/bin/curl","-sSL","--fail","--max-time","16",
                             "https://governance.fountain.coach/"+rel],
                            capture_output=True)
        if proc.returncode:return rel,"UNREACHABLE "+proc.stderr.decode(errors="replace")[:150]
        value=sha(proc.stdout)
        return rel,None if value==digest else "SHA256 mismatch: "+value
    mismatches=[]
    with ThreadPoolExecutor(max_workers=8) as pool:
        for future in as_completed([pool.submit(fetch,item) for item in files.items()]):
            name,result=future.result()
            if result:mismatches.append((name,result))
    if mismatches:
        for rel,error in sorted(mismatches):print("DRIFT",rel,error,file=sys.stderr)
        raise ValueError(str(len(mismatches))+" file(s) differ from live governance domain")
    print("GOVERNANCE_HTTPS_READBACK_VERIFIED",len(files),"files SHA256-identical")

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--against-live",action="store_true")
    args=parser.parse_args()
    files=local_audit()
    if args.against_live:live_audit(files)

if __name__=="__main__":main()
