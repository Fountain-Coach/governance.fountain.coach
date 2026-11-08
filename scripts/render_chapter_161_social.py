#!/usr/bin/env python3
"""Reproducible social-media crop of the original, approved Governance 161 figure.

The canonical illustration is not redrawn or modified. This crops only its top
editorial title region while retaining 100% native scale and all four governed
relationship boxes, arrow connections, and the explanatory footer. Social-only
PNG is a derivative presentation asset, never a second governance authority.
"""
from pathlib import Path
from hashlib import sha256
import subprocess, tempfile, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
SLUG="161-host-enrollment-client-consent-and-access-management"
SOURCE=ROOT/"site/assets/illustrations"/(SLUG+".svg")
TARGET=ROOT/"site/assets/social"/(SLUG+"-caaf0bc5.png")
EXPECTED_SOURCE="caaf0bc54342b39d7ba380b7668784848c2a38aafda67f5e362c94acb19218cc"
def main():
    original=SOURCE.read_text()
    assert sha256(original.encode()).hexdigest()==EXPECTED_SOURCE, "Refuse unreviewed source figure"
    assert 'viewBox="0 0 1200 820"' in original
    # 1200x630: preserve all diagram geometry at 1:1 size, removing the title
    # and the now-partial outer plate frame. The footer remains in view.
    cropped=original.replace('viewBox="0 0 1200 820"',
                              'viewBox="0 185 1200 630"',1)
    frame='<rect x="28" y="28" width="1144" height="764" rx="2" fill="none" stroke="#9da39f" stroke-width="2"/>'
    assert cropped.count(frame)==1
    cropped=cropped.replace(frame,"",1)
    ET.fromstring(cropped)
    TARGET.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="governance161-social-") as tmp:
        svg=Path(tmp)/"cropped.svg"
        svg.write_text(cropped)
        subprocess.run(["rsvg-convert","--width","1200","--height","630",
                        "--output",str(TARGET),str(svg)],check=True)
    image=TARGET.read_bytes()
    assert image[:8]==b"\x89PNG\r\n\x1a\n"
    assert int.from_bytes(image[16:20],"big")==1200
    assert int.from_bytes(image[20:24],"big")==630
    assert len(image)>12000
    print("SOURCE_ILLUSTRATION_SHA256="+EXPECTED_SOURCE)
    print("SOCIAL_IMAGE="+str(TARGET))
    print("SOCIAL_SHA256="+sha256(image).hexdigest())
    print("SOCIAL_SIZE=1200x630")
if __name__=="__main__":main()
