# Dummy Decoy Scientific Hub

[![Hub status](https://img.shields.io/badge/hub-index%20only-0B3D91?style=flat-square)](https://github.com/DeontewattsV1/dummy-decoy-scientific-hub)
[![Per-paper DOI](https://img.shields.io/badge/DOI-one%20per%20manuscript-blue?style=flat-square)](docs/DOI-MINTING.md)
[![Storage policy](https://img.shields.io/badge/storage-links%20not%20blobs-2ea44f?style=flat-square)](docs/STORAGE-POLICY.md)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey?style=flat-square)](LICENSE)
[![ORCID](https://img.shields.io/badge/ORCID-Deonte%20Watts-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/)
[![Template](https://img.shields.io/badge/spawn-paper--doi--template-6f42c1?style=flat-square)](https://github.com/DeontewattsV1/paper-doi-template)

This is the **dummy decoy repository**: a thin public catalog, not a warehouse.

Each scientific manuscript lives in its **own GitHub repository**. Each of those repositories mints its **own Zenodo DOI** when a GitHub Release is published. This hub stores **names, links, badges, and DOIs** — not 20 copies of PDFs, figures, or datasets.

Why a decoy hub:

- Conserves GitHub storage and LFS quotas.
- Gives every paper an independent citation target.
- Lets an AI (or you, in the GitHub UI) spawn a precise child repository from [`paper-doi-template`](https://github.com/DeontewattsV1/paper-doi-template) without stuffing this repo.
- Keeps the public front door stable even while child papers move, version, or embargo.

## How a paper gets a DOI

GitHub does not mint DOIs. CERN’s [Zenodo](https://zenodo.org) does, via the official GitHub integration.

```
manuscript files
      ↓
child repository  (one paper = one repo)
      ↓
GitHub Release (tag v1.0.0)
      ↓
Zenodo webhook archives the snapshot
      ↓
concept DOI  (always latest)  +  version DOI  (this release)
      ↓
this hub catalog is updated with name + DOI + badge
```

Operator checklist is in [`docs/DOI-MINTING.md`](docs/DOI-MINTING.md).
Upload / user-data rules are in [`docs/UPLOAD-USER-DATA.md`](docs/UPLOAD-USER-DATA.md).
AI spawn protocol is in [`AI_INSTRUCTIONS.md`](AI_INSTRUCTIONS.md).

## Paper catalog

Machine index: [`papers/catalog.json`](papers/catalog.json)

| Paper | Child repository | Concept DOI | Version DOI | Status |
| --- | --- | --- | --- | --- |
| Example placeholder manuscript | [paper-doi-template](https://github.com/DeontewattsV1/paper-doi-template) | *pending first Zenodo release* | *pending* | template |
| *(add row after each spawn)* | | | | |

Replace the pending cells with the real Zenodo badge after the first release:

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.CONCEPT.svg)](https://doi.org/10.5281/zenodo.CONCEPT)
```

Colored local badge (works before Zenodo exists):

```markdown
[![DOI pending](https://img.shields.io/badge/DOI-pending%20release-lightgrey?style=flat-square)](docs/DOI-MINTING.md)
```

After mint:

```markdown
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.1234567-blue?style=flat-square)](https://doi.org/10.5281/zenodo.1234567)
```

## Spawn a new paper repository

**Native GitHub (no extra API client required of you):**

1. Open [`paper-doi-template`](https://github.com/DeontewattsV1/paper-doi-template).
2. Click **Use this template** → **Create a new repository**.
3. Name it `paper-<short-slug>` (example: `paper-mcds-hypothesis`).
4. Keep it **public** if you want a DOI (Zenodo only archives public GitHub releases by default).
5. Drop the manuscript under `manuscript/`, figures under `figures/`, data pointers under `data/`.
6. Edit `CITATION.cff` and `.zenodo.json`.
7. Connect the repo at [zenodo.org/account/settings/github/](https://zenodo.org/account/settings/github/).
8. Publish GitHub Release `v1.0.0`.
9. Paste the minted DOI back into this hub’s `papers/catalog.json` and this README table.

**From chat (this GitHub account is already connected to Grok):**

Tell the assistant:

> Spawn a new paper repository from `paper-doi-template` titled TITLE with slug `paper-<slug>`. Fill CITATION.cff for Deonte Watts. Add a catalog row in `dummy-decoy-scientific-hub`. Do not upload binary datasets into the hub.

The assistant uses the connected GitHub tools (`create_repository`, `push_files`) — you do not paste tokens.

## What this hub is allowed to hold

Allowed: catalog JSON, README cards, badges, licenses, workflow definitions, issue templates, links.

Not allowed: manuscript PDFs, raw data dumps, large figures, packages that belong in GitHub Packages of the *child* repo.

See [`docs/STORAGE-POLICY.md`](docs/STORAGE-POLICY.md).

## Related identity

- Author GitHub: [DeontewattsV1](https://github.com/DeontewattsV1)
- Public research home (existing): [The-Architects-Signal.github](https://github.com/DeontewattsV1/The-Architects-Signal.github)
- Existing forge agent: [repository-forge-agent](https://github.com/DeontewattsV1/repository-forge-agent)

Replace the empty ORCID badge once your ORCID iD is pasted into `CITATION.cff`.
