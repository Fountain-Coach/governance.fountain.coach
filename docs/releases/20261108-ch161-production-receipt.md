# Chapter 161 — Governance production receipt · 8 November 2026

Canonical source owner: Fountain-Coach/governance.fountain.coach, main commit 7d4200951eb28376238ae72a2f8cddca5c8c25e4, merged Governance PR #4. The approved edition contains Chapter 161, its reviewed original SVG, adopted chapter status and 162 numbered chapter routes.

Public overview: https://governance.fountain.coach/
Public Chapter 161: https://governance.fountain.coach/chapters/161-host-enrollment-client-consent-and-access-management/
Original illustration: https://governance.fountain.coach/assets/illustrations/161-host-enrollment-client-consent-and-access-management.svg

## Publisher and composed release

The established standalone Fountain-Coach/EstatePublisher Swift SSH-delivery CLI, source revision 77e6e6679af7a71cdffb26e54d7b1fe815048ea6, executed one typed prepare, preflight and deliver transaction against the existing HetznerCaddyStatic profile for governance.fountain.coach. Its 16 automated tests passed before deployment.

The published static site is a composed edition, as it was for Chapter 160. The previous immutable release was independently copied and checked against its complete manifest: 301 files. Of those, 294 remain byte-for-byte identical, seven existing navigation/status files were updated, and two files were added (Chapter 161 and SVG). The normative Chapter 161 article was verified identical to canonical Git after removing private staging route prefixes. The composed publication has 303 files; the raw authored site/ has a distinct 298-file inventory. Do not conflate those two inventories.

Predecessor release: static-20261026-ch160-f3d388c.
New active release: static-20261108-ch161-7d42009.
Public Caddy document root: /srv/fountain-static-publications/governance.fountain.coach/current.
Canonical source revision: 7d4200951eb28376238ae72a2f8cddca5c8c25e4.
Publisher inventory SHA-256: 2fda9926251da5451130af9b20769a8cea54a25809b5b35cfa01272b17688b5f.
Terminal result: activated=true; state=active; exact published bytes verified independently via HTTPS.

## Independent public HTTPS acceptance

The native publisher verified eight selected public files:

- /index.html SHA-256 b00f0d7edd09861491cc538d8f6546438087c2cd9b0bedf73479db5f67d0bccb
- /chapters/01-reading-index/index.html SHA-256 814d0d7669d71276eba1ef8d3181eb57b130461f68aac56afca55e4cf10c2948
- /chapters/160-skill-sovereignty-and-governed-distribution/index.html SHA-256 daa5ad6b1f3aabf1e8590fd05bc3347c5e3385fdceb2a04039a34f366583a878
- /chapters/161-host-enrollment-client-consent-and-access-management/index.html SHA-256 799a5d9a3e972bc8797b93cedac4e9d97678aace688e8440128fef56148b21ff
- /assets/illustrations/161-host-enrollment-client-consent-and-access-management.svg SHA-256 caaf0bc54342b39d7ba380b7668784848c2a38aafda67f5e362c94acb19218cc
- /chapter-status.json SHA-256 194a199b66742c7af1c06e2c71cfefc9dad269c8425a0b5e90ccb38795826576
- /route-manifest.json SHA-256 8d4e1047b615fd986b19257d87fe83b748531e20a083b885ce6f18db953b2034
- /publication-manifest.json SHA-256 91aaef7b2d16839da4aeba9e5065a0d926060d6f3abac3d9cdb7a628daeb6bef

A separate Mac-side HTTPS checker downloaded all 303 exact public paths, verified HTTP 200 and SHA-256 against the complete release manifest, and found zero mismatches. Caddy was independently read back as active and its configuration as valid. Its current symlink targets the new immutable release and its predecessor remains present. The public overview, chapter and original SVG each returned HTTP 200 with successful TLS verification.

Chrome independently rendered the production overview and Chapter 161 at 1465x1024; visual inspection confirmed one Fountain Coach masthead, the latest/previous chapter distinction, and the Chapter 161 reading frame.

This is proof of the exact composed public release, not a claim that every published byte must equal the earlier, differently composed authored site/ file. The canonical source inventory is verified separately with scripts/verify_publication.py.

## Scope and rollback

The chapter is adopted governance only. This publication does not assert that a multi-user Host enrollment website, passkey admin surface or client-grant revocation UI has already been implemented.

The prior immutable release remains at /srv/fountain-static-publications/governance.fountain.coach/releases/static-20261026-ch160-f3d388c. An authorized EstatePublisher recovery may restore it if required; no rollback was requested or performed.

Evidence in this directory:
- 20261108-ch161-publication-manifest.json: complete 303-file immutable release inventory.
- 20261108-ch161-publisher-receipt.json: native terminal result and eight selected HTTP witnesses.
- 20261108-ch161-full-https-parity.json: complete independent public readback.
- 20261108-ch161-composition-proof.json: inheritance and exact controlled changes.
