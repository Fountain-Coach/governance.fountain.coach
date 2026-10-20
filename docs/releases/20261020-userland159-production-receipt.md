# Production publication receipt — FCIS 159 Userland

Date: 2026-10-20
Canonical domain: https://governance.fountain.coach/
Chapter: https://governance.fountain.coach/chapters/159-userland-the-writers-books-outlive-the-device/

## Authority and source

The writer explicitly requested production publication of the illustrated and interlinked chapter.
Owning repository: Fountain-Coach/governance.fountain.coach.
Authored chapter and cross-reference commit: e6af2bd.
Publication-state correction commit: 923d5f9.
Published static payload: site/ only, with no private source, secrets, tooling or build artifacts.

The final verifier command was python3 scripts/verify_publication.py --against-live.
Result: GOVERNANCE_HTTPS_READBACK_VERIFIED 294 files SHA256-identical (exit code 0).
The edition has 160 chapters, 160 declared index routes and six historically documented route-manifest omissions.
Chapter 159 has thirteen contextual links to governing predecessors; ten predecessor chapters reciprocally link to 159.

## Production effect

Existing Hetzner Caddy origin: 65.109.14.71.
First full release: /srv/fountain-static-publications/governance.fountain.coach/releases/static-20261020-e6af2bd
Final metadata-corrected release: /srv/fountain-static-publications/governance.fountain.coach/releases/static-20261020-923d5f9
Live symlink: /srv/fountain-static-publications/governance.fountain.coach/current -> releases/static-20261020-923d5f9
Preserved pre-release predecessor: releases/static-20261013-0ec39995d01f
Saved pre-change configuration: /etc/caddy/Caddyfile.gov159.rollback-20261020

Caddy was changed by removing only the restricted path matcher of @governanceNewEdition while retaining the exact host governance.fountain.coach and its existing immutable release-root handler. This makes all files in the Git-owned edition consistently served by Caddy. No sibling host handler, DNS record, SSL certificate, secret, or application service was changed.

One initial Caddy reload was refused because the candidate config had mode 600. Automatic rollback restored the old symlink and readable Caddyfile and the service stayed active. The file mode was corrected to 644, config validation passed, reload succeeded and the edition was promoted. A second atomic symlink promotion published the final metadata-consistent release without another config change.

## Independent public witness and scope

Public read-back passed for all 294 inventoried files, not merely the home page. Verified includes the new Chapter 159 HTML, its SVG illustration, Chapter 13 and Chapter 117 cross-links, Chapter 158, the index, chapter-status, CSS, publication manifest and legal pages.

Chapter 159 is published governance doctrine for a PROPOSED Userland product. No iPad-to-Linux manuscript storage, sync or recovery acceptance is claimed. The image-generation PNG assets remain separate social-posting outputs; the chapter retains its governed technical SVG.

## Rollback

Authorized recovery can atomically repoint only the Governance current symlink to releases/static-20261013-0ec39995d01f or its saved first Chapter 159 release. To also restore the former mixed route model, copy the saved Caddyfile with original permissions, validate and reload Caddy, and independently witness the public site. Do not modify other domains or delete retained releases.
