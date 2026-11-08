# Governance — current execution

## Chapter 160 · skill portability and execution authority (30 October 2026)

**State:** AUTHORED AMENDMENT IN PROGRESS. **Scope:** amend the *existing, current* Chapter 160 in canonical `site/` to distinguish skill distribution, account-wide discovery, API-project copies, per-project execution permission, and commercial/rights exposure. Preserve all 161 chapter routes, status and prior live release.

**Governance reading record**
- **Chapters read:** 07 (goal fidelity, fixed scope); 08 (artifact-backed proof); 94 (credentials do not imply permission); 131 (exact operation/target/expiry approval); 160 (organization Git is canonical; installations are projections).
- **Forbidden:** treating a globally discovered skill as project authorization; assuming ChatGPT account and OpenAI API projects are the same deployment; treating upload or Git history as live execution; silently broadening distribution or changing active versions; publishing private contents or claiming commercial rights without consent.
- **Conflict:** Chapter 160 already governs authorship but does not explicitly constrain invocation outside the originating project. Extend Chapter 160 without changing source ownership or inventing another FCIS Kit.
- **Excluded:** skill installation, remote API mutation, credential use, Kit implementation, new chapter, route or asset; production publication needs separate authority and live evidence.

**Next:** edit only canonical Chapter 160 body and governing sentence; recompute tracked inventory and edition metadata; run full source verification and independently inspect resulting commit. Record exact source commit here. Do not claim the public domain has changed.

## Governance editorial correction - text-first, no mandatory illustrations (6 November 2026)

**Writer decision:** Illustrations do not improve Governance domain reasoning and are not part of mandatory Governance. Do NOT add a chapter, figure quota, hero, per-chapter social card, new Reader, or generated artwork as a precondition of authority or publication. The governing standard is in docs/GOVERNANCE-EDITORIAL-POLICY.md and the root AGENTS.md operational contract. Required: complete text, stable addresses, machine-readable interpretation, current/reference status, evidence and independent source/publisher witnesses.

**Governance reading record**
- **Chapters read:** 07 goal fidelity; 08 source and independent release evidence; 92 source/publishing identity; 127 existing publication layout; 160 organization-owned Skill authority.
- **Forbidden:** equating a missing image with a missing rule, mandating decorative artwork, manufacturing an image to complete a chapter, promoting private staging cards or replacing the authored book, deleting old source figures just for visual simplicity.
- **Conflict:** earlier Linotype/Press social guidance and this repository's uncommitted 161-card candidate were broader than the author's new decision. The writer's explicit domain-specific correction supersedes that unshipped image work; source-authored original diagrams remain optional, not normative.
- **Excluded:** deleting historical figure assets, rewriting any chapter or status, public EstatePublisher delivery, private WLAN rollback, another publication engine, and illustrated works in other Fountain Press domains.

**Implemented local correction:** The source candidate on codex/press-social-public-20261106 was never committed or deployed. Its 161 generated JPEGs, manifest and scripts were reversibly moved to /tmp/governance-retired-social-candidate-20261106; the 161 modified chapter heads, edition.json and publication-files.sha256 were restored byte-for-byte from canonical HEAD after checking that all bodies were unchanged. The original public release static-20261026-ch160-f3d388c and private WLAN v164 remain untouched, with v164 an archival staging witness, not a production mandate.

**Next source acceptance:** Check AGENTS.md and the editorial policy against canonical Governance identity; reconcile the existing linotype-estate-template and estate-publisher-deployment FCIS skill package requirements, run full canonical skill and source tests, commit reviewed changes separately. Do not claim a new public edition or rewritten Reader until an actual publisher release is independently verified.

## Chapter 161 — Owner-managed Host access (2026-11-08)

**Requested observable result:** a reviewed source-owned Chapter 161 with one meaningful, optional accessibility-labeled diagram, staged for proofreading only. No production promotion is approved.

**Reading record:** 07 (goal fidelity forbids speculative infrastructure dependencies), 08 (independent artifact/HTTPS witnesses), 142 (FountainAuthKit is authorization authority; authentication is not consent), 152 (Host owns finite execution, MCP is an adapter), 157 (writer's own domain/identity cannot be replaced by vendor tenancy). The public-edition reading index, site/chapter-status.json and editorial policy were also checked.
**Forbidden:** invent a second permissions database in a dashboard; let OAuth registration grant capability; reuse another Host's token; assume a provider account owns the Host; call an untested UI live; publish to production without review.
**Conflicts:** Author's explicit Chapter 161 illustration request versus Governance's text-first optional-figure editorial policy. Resolved by one source-authored explanatory SVG with caption and full alt, explicitly non-normative; the neutral site social identity remains unchanged, and figures are not made a prerequisite for subsequent chapters.
**Excluded:** implementing passkey login, inviting actual users, OAuth migration, Hetzner Host cutover, changing the currently deployed authorization service, the historical six unmapped routes, and production Governance promotion.

**Source work:** New site/chapters/161-host-enrollment-client-consent-and-access-management/index.html and one optional illustration under site/assets/illustrations. Updated chapter navigation, chapter-status and route/publication manifests, route map, checksum inventory and edition pendingPublication; preserved 161 preceding chapters and old production witness fields. Updated scripts/verify_publication.py only for the intentional route/chapter count and latest source number. The one-off composition helpers remain outside the canonical repository.

**Source QA:** 298 matching public files, 162 chapter pages, 162 declared routes, zero new collisions, existing six source-manifest omissions preserved, required cross-links and image present, SVG parses, semantic heading and caption, JSON-LD and metadata present. Local verifier passes. Visual/browser AX/VRT and staging HTTPS must be independently witnessed, not inferred from source checks.

**Staging delivery boundary:** The current Hetzner Caddyfile has only the live governance.fountain.coach production document root. The private WLAN HTTPS service at 192.168.8.50:8443 is an unrelated First Readings Python stage and returns 404 for Governance. The /srv/estate-staging directory exists but has no active Governance Caddy route. Do NOT transfer the source into production using SSH or invent an ungoverned staging HTTP server. Next: resolve a review-only Governance route through the native typed publication/preview owner and verify the exact staging HTTPS URL. A source Git push is not deployment.

## Chapter 161 iPad proofreading corrections (2026-11-08)
The reader supplied direct visual evidence that the FountainStore label overflowed its figure and that the private Governance staging overview remained semantically on Chapter 160 although Chapter 161 was reachable. The original staging v173 admitted only the chapter HTML and SVG, not the domain's overview or reading-index state.

The canonical review branch now has a redrawn 1200 × 820 SVG with separated action note, multiline capability cards, a wider and two-line evidence box, and a properly padded non-normative caption. SVG was rasterized and visually inspected before acceptance. The canonical overview title/identity now says Fountain Coach Governance and distinguishes Chapter 160 as latest **published** from Chapter 161 as latest **proofreading** candidate. Chapter 161 retains its proposed status in chapter-status.json. This is not permission to publish to production.

A subsequent immutable owner-WLAN staging release must carry the matching review overview, chronological reading index, Chapter 160 previous/next navigation, new Chapter 161 and diagram, and status/route metadata as a single semantically coherent staged edition. All non-Governance estate material must remain byte-identical and be covered by the source-lock acceptance guard.
