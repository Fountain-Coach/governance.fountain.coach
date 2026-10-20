# governance.fountain.coach — the authoritative published edition

**Canonical public host:** https://governance.fountain.coach/

This repository is the **Git source of truth for the complete public Governance
edition** of the Fountain Coach estate. The tree under [site/](site/) is an
exact byte-for-byte snapshot of the currently published domain at admission on
14 October 2026. It is not a new book, curated extract, reconstruction by an
LLM, or a republication of ten selected chapters.

The entire present publication is represented: **294 publicly served files,
160 complete numbered chapter routes, the homepage, five legal/accessibility
pages, assets, published chapter-status map, and published route/publication
manifests.** The site is browsable at the canonical HTTPS domain. The
repository's `site/` subtree is the only eligible input for subsequent
Governance editions.

## Source-of-truth rule

1. **This Git repository owns the next Governance public edition.** Editorial
   changes to public Governance content and its assets belong in `site/`
   here, with a reviewed Git commit and explicit author publication authority.
2. The former `midi2-gpu-fabric`/estate `estate/sites/governance.fountain.coach/`
   is now a **derived deployment working tree**, not another independent
   writer of governance. Before packaging, it must be projected from a pinned
   commit here, verified, and independently published under
   `governance.fountain.coach`.
3. The `Reframe-Refactoring` engineering repository may contribute to rule
   authorship and provenance, but **cannot silently overwrite this public
   edition**. A change only becomes an edition through review and commit here.
4. The public HTTPS website is the independent read-back witness. A Git commit
   or source copy is not proof that a deployment occurred.
5. Fountain Press may load a **complete edition from this repository**.
   It must not assert that a chosen subset is the entire Governance domain
   or substitute a narrative summary for the original content.

## Initial live-parity audit

The admission process made HTTP GET requests for every file in the known
public projection, and compared SHA-256 hashes. 288 local estate files already
matched the public bytes. The following four had drifted locally, so **the
live public version** was adopted here:

- `site/assets/estate-core.js`
- `site/publication-manifest.json`
- `site/route-manifest.json`
- `site/route-map.yaml`

This is a witness of public bytes at the capture time, not an assertion that
those four earlier estate-local variants were correctly published.

**Known live inconsistency (preserved, not silently repaired):** the live
`route-manifest.json` names 159 routes but omits the *served* Chapter 158
route and the five auxiliary policy routes. All six HTML documents are still
tracked in this repository and served on HTTPS. This should be corrected in a
separately reviewed future publication, not changed in an initial
byte-identical mirror.

## Verify the complete edition

```sh
python3 scripts/verify_publication.py
python3 scripts/verify_publication.py --against-live
```

The first command verifies the entire `site/` inventory, hashes,
chapter-status and route-manifest consistency, and fails on source drift. The
second independently fetches **all 292 served files** and requires identical
SHA-256 digests. The recorded checksums are in `publication-files.sha256`,
and capture metadata in `docs/live-parity-audit.json`.

The repo includes no secrets, source archive, model prompt fixture, build
cache, paid API grants or GitHub Actions/CI. It contains only files already
served publicly and build/verification metadata outside `site/`.

## Publishing and derivative renderings

- The public directory is `site/`, **not the repository root**. Scripts
  and docs must never become exposed web content.
- No GitHub push deploys anything automatically. Deployment must be
  authorized and performed by the existing EstatePublisher static profile,
  with route-scope, deterministic packaging, rollback and HTTPS read-back.
- The estate-local import is mechanical, never a second editorial authority:
  use `scripts/reconcile_estate.py` to inspect the proposed difference;
  `--apply` is an explicit local materialization, not a public release.
- Linotype book pages and catalogues are **projections** of this repository's
  content. A book reader may paginate differently by device but must preserve
  the complete original text, image inventory, original chapter IDs,
  publication states and source links.

## Why this repository exists

Governance is a public constitutional reference, with a specific maintained
status for each chapter. Reducing it to an invented book arc made it weaker,
not clearer. The repository therefore preserves the **complete published
edition** and gives the domain one clearly owned, reproducible source.

## Footer-legal edition update (included in October 2026 publication)

The current Git source moves Company Status & Transparency into the mandatory footer legal group and removes Status from header rails. The initial 2026-10-14 exact-live-snapshot audit remains historical evidence for its original Git commit. **The revised source has been served from the production release and independently witnessed over HTTPS on 2026-10-20.** Six historical HTML fragments without a complete body/footer preserve their fragment structure and require source repair before they can carry a full legal footer.

## Chapter 159 — Userland production edition (2026-10-20)

The `feature/ch159-userland` branch contains the **published Governance edition** of
Chapter 159, `Userland: The Writer's Books Outlive the Device`, plus a
technical plate, amended sidebar and pager navigation, status metadata,
edition route maps, and regenerated checksums. The original 14 October
live-parity snapshot and six known manifest omissions remain historical
records; the 294-file/160-chapter release is now live and independently SHA-256 verified.
`python3 scripts/verify_publication.py` verifies candidate files locally.
`--against-live` is appropriate **only after** independently authorized
publication. Documentation source is retained in
`docs/chapters/159-userland-the-writers-books-outlive-the-device.md`.
The chapter specifies desired behavior, not a passed iPad ↔ Userland recovery test.

## FCIS 159 production publication witness

The 20 October 2026 edition is live and full-inventory SHA-256 verified. Read the exact immutable release, scoped Caddy change, recovery and witness evidence in [the production release receipt](docs/releases/20261020-userland159-production-receipt.md). The original 14 October snapshot remains a historical admission record; Userland runtime implementation is still proposed, not claimed.
