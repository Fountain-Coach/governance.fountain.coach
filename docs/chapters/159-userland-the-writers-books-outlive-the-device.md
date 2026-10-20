# 159 — Userland: The Writer's Books Outlive the Device

> Governance chapter 159. Reframe is the writing instrument. Userland is the writer's durable home. A manuscript must survive the loss of the application, the device, and the hosting machine. An independently provisioned Linux host can keep the writer's library without requiring Apple iCloud, a Fountain Coach account, a particular provider, or a continuously connected model.

![A Reframe iPad holds a local working manuscript. A secure synchronization boundary leads to a writer-owned Linux Userland holding portable book sources and governed working state; a separate recoverable copy can restore the library to another host.](/assets/illustrations/159-userland-the-writers-books-outlive-the-device.svg)

## The disappearance test

A writer opens Reframe on an iPad, chooses an Empty and begins to write. The page is intimate; it is also a computing surface. Deleting the app ordinarily deletes its private local documents. A broken tablet can disappear just as completely. Neither the elegance of the interface nor a working conversation with a model says where the manuscript now lives.

Apple offers iCloud as a familiar continuity mechanism. Reframe must offer another choice: **Userland**, a writer-controlled home for books, operated on any compatible, provisioned Linux machine. The iPad is a working place, not the permanent custodian of the writer's life in words. A Mac mini at home, a rented VPS, an institutional server, or another Linux host may serve the same Userland contract. The server's vendor and network address are replaceable; the books' identities and provenance are not.

This is not a demand that a writer administer Linux. Reframe mediates enrollment, synchronization, recovery and status in terms of books. Host setup and credentials are supported by named, governed instruments; no writer-facing flow asks for shell incantations.

## What a book is

A book is a durable, writer-owned entity with a stable identity, an authored source and a revision lineage. Opening **Empty** starts a new book identity, even if no prose has been committed yet. Its authored material is preserved in portable, human-readable source files and declared assets rather than hidden inside a conversation transcript or a model provider's database. A Book Library release is a separately approved publication, not the same thing as an editable book.

The local iPad holds a working copy of the book and a journal of unsynchronized changes. After Userland acknowledges a verified revision, the provisioned host holds a recoverable copy with its book identity, source digest, revision ancestry and declared assets. A local manuscript may be edited without a network connection. Its unsynchronized changes remain locally authoritative until reconciled; they are **not remotely safe** until the remote receipt is verified.

Portable source bundles are the authored document. Git supplies revision custody and migration-friendly history. FountainStore records the governed working state, semantic projections, session evidence and handoff receipts. The bookshelf manifest is rebuildable navigation, not the only surviving copy of the writer's prose. The model and MIDI2 carry intentions and replies, never the sole manuscript authority.

## The writer's Userland

Userland is a capability, not a Fountain Coach tenant. A compatible Linux host exposes an authenticated, encrypted synchronization and recovery interface with bounded book operations. Enrollment proves control of that host and authorizes the particular device; knowing an IP address, discovering a MIDI2 instrument, possessing an HTTPS certificate, or logging into an OpenAI model does not confer manuscript permission.

A writer may operate more than one Reframe device against the same Userland. Each device keeps its own local working state and synchronization cursor. The server maintains approved book revisions and enough history to reconcile changes; the iPad reports whether a passage is local only, syncing, safely received, conflicted or recoverable. No interface may call a request that has merely been transmitted a committed revision.

Userland MUST NOT depend on iCloud, Apple ID, a Fountain Coach-hosted account, a model subscription, or the future general-purpose `auth.<owned-domain>` product. It MAY use a separately admitted writer-owned domain and a provisioned domain-auth service later. Identity, content custody, host management and model-provider invitations remain separate authorities.

## The sync receipt, not the spinner

Every changed book revision has a source identity, parent revision, content digest and idempotency key. A synchronization acknowledgment MUST identify the host's durable acceptance of the exact revision and assets, not merely a successful socket write or HTTP status. The client SHALL retain its local journal until read-back confirms the stored revision and its ancestry. A failed transfer leaves the locally saved work intact and visibly unsynchronized.

On concurrent devices, revisions can diverge. Userland MUST NOT silently overwrite one writer's work with another device's later timestamp. Concurrent edits require a governed reconciliation: explicit conflict presentation, source-preserving branches or a demonstrably safe automatic merge with verifiable lineage. A device resuming after weeks offline cannot simply declare its draft the new universal head.

Book deletion is a different, separately approved operation with a recoverable interval and a clear account of which devices and backups have seen the deletion. Removing the Reframe app from an iPad is **not** a command to delete the corresponding books in Userland.

## Two different kinds of losing the iPad

If a book's last revision was durably acknowledged by Userland, uninstalling Reframe should remove only the device's working cache and keys. After reinstall, the writer can enroll the new app installation and restore the same bookshelf, manuscripts, assets and revision history. The new installation cannot inherit vanished local keys merely because it appears on the same hardware. Independent recovery material and owner confirmation must exist outside the erased app.

If the writer was offline with unsynchronized changes, deleting the app may destroy those changes. The interface MUST distinguish **Saved on this iPad** from **Safely synchronized to Userland**, warn before a destructive action where the platform permits it, and never claim that remote recovery can reconstruct material it never received. A host outage must never turn an offline draft into an empty manuscript or silently throw away queued revisions.

Userland itself can fail. One Linux disk is not a backup strategy. The writer's recovery profile SHALL include an independently retained, integrity-checked copy or equivalent tested restoration route. Migration to a new Linux host re-establishes the same book identities, verifies source content and Git ancestry, restores governed working state where appropriate, and re-enrolls devices without transferring the old host's private signing credentials as plaintext.

## The Composer is a visitor

The Composer is the writer's conversational and writing instrument. The model may answer, suggest, transform or annotate. A conversation transcript can be stored as separately governed working material, but it is not automatically a manuscript revision. Accepting a model suggestion into the book requires an explicit writer-owned edit and a new source revision. A successful Codex turn, MIDI2 correlation or decrypted model reply cannot be substituted for durable manuscript read-back.

The same rule applies to publication. Saving a passage is not exporting a Fountain Project, pushing a Git revision to an outside service, creating a Book Library candidate or publishing a public domain. These are different operations with different permissions, receipts and opportunities for refusal. Userland makes writing durable without quietly making it public.

## A recovery ceremony with an end

The writer should not have to reconstruct an institution of servers and accounts to recover a book. Recovery is a finite encounter: identify a provisioned Userland, prove authority through a surviving recovery mechanism, read a verified inventory, select the books to restore, and witness exact content and revision read-back. The interface explains what is recovered and what is missing. It does not pretend that one host, one device, or one copy will survive every accident.

The canonical end-to-end scenario is **`userland-host-enrollment-and-book-recovery`**. It begins with a fresh Reframe installation and a newly created Empty. A passage is committed locally, synchronized with independent host read-back, and found again after the app is deleted and reinstalled. A second device recovers the same book. An offline divergent revision is refused or reconciled without loss. A second provisioned Linux host restores from a verified export after the first host is made unavailable. At each stage, the bookshelf, the actual manuscript, the revision graph and the receipts must agree.

This scenario is **proposed**, not a passed device or server test. The current R38 native iPad Composer keeps its draft in process memory and labels it unsaved. The October Solstice Writer Desk demonstrated separate FountainStore revision and stale-write protections, but it did not prove an iPad/Userland round trip. The authenticated Ubuntu CodexKit runtime and physical MIDI2 discovery are model-transport evidence, not book-storage acceptance.

## Relation to existing governance

[Chapter 13, *Storage and Performance*](https://governance.fountain.coach/chapters/13-storage-and-performance/) distinguishes portable source from ephemeral caches and indexes. [Chapter 56, *The Book Library Is Reframe's Sole Reading Provider*](https://governance.fountain.coach/chapters/56-the-book-library-is-a-portable-source-provider/), [Chapter 59, *The Fountain-Coach Git Library and Reframe Project Flow*](https://governance.fountain.coach/chapters/59-copilot-initiated-library-curation/), [Chapter 61, *The Fountain Project Round Trip*](https://governance.fountain.coach/chapters/61-the-fountain-project-round-trip/) and [Chapter 64, *FountainProjectKit — Durable Fountain Project Custody*](https://governance.fountain.coach/chapters/64-fountain-project-kit-durable-draft-custody/) establish the portable book, Git lineage, and draft custody; Userland makes their survival across an erased installation an explicit test.

[Chapter 55, *One Store Authority Across Repositories*](https://governance.fountain.coach/chapters/55-one-store-authority-across-repositories/) and [Chapter 95, *FountainStore Is the Headless Linux Persistence Authority*](https://governance.fountain.coach/chapters/95-fountainstore-headless-linux-authority/) separate FountainStore authority from authored files; [Chapter 117, *FountainStore Snapshot Export and Git Recovery Projection*](https://governance.fountain.coach/chapters/117-fountainstore-snapshot-export-and-git-recovery-projection/) requires verifiable snapshot recovery rather than declaring Git a running Store. [Chapter 135, *Reframe iPad as a Scenario-Driven Creative Host*](https://governance.fountain.coach/chapters/135-reframe-ipad-scenario-driven-creative-host/) identifies the native device where these guarantees must become observable.

[Chapter 139, *Owner Trust Root, SecretStore Custody, and Recovery*](https://governance.fountain.coach/chapters/139-owner-trust-root-secretstore-custody-and-recovery/) and [Chapter 143, *Simplicity Is Key: One Bootstrap, One Trusted Session*](https://governance.fountain.coach/chapters/143-simplicity-is-key-one-bootstrap-one-trusted-session/) protect owner trust and finite enrollment. [Chapter 157, *The Writer Owns the Public Domain*](https://governance.fountain.coach/chapters/157-the-writer-owns-the-public-domain/) protects the writer's namespace; [Chapter 158, *Publishing Is Not a Distributed Transaction*](https://governance.fountain.coach/chapters/158-publishing-is-not-a-distributed-transaction/) keeps publication separate from live application state. Chapter 159 binds these earlier principles into a **device-loss and host-loss contract** for books; none of their security or publication boundaries is superseded.

## Governing sentence

**The writer may lose an iPad, uninstall Reframe, leave a provider, or replace a Linux host without losing any manuscript revision that Userland has durably acknowledged. Reframe presents the work; Userland keeps it; Git makes its authored history portable; FountainStore records the governed work around it. Nothing calls itself recovered until the actual book can be read.**
