# AI operating instructions — Dummy Decoy Scientific Hub

You are operating against the GitHub account already connected to this session.
Owner login: `DeontewattsV1`.
Hub: `DeontewattsV1/dummy-decoy-scientific-hub`.
Template: `DeontewattsV1/paper-doi-template`.

Do **not** ask the user for a GitHub personal access token. Use connected tools:
`github___create_repository`, `github___push_files`, `github___create_or_update_file`,
`github___get_file_contents`, `github___create_branch`, `github___create_pull_request`.

You cannot mint a Crossref or DataCite DOI yourself. A real DOI appears only after
the human enables Zenodo on the child repo and a GitHub Release is published.

## Goal

One scientific manuscript → one child repository → one Zenodo concept DOI
+ one version DOI per release. The hub only stores the index.

## Spawn procedure (mandatory order)

1. Confirm the paper title, short slug, license, and whether the repo must be public.
   Default visibility for DOI-seeking papers: **public**.
2. Create the child repository:
   - name: `paper-<slug>` using lowercase kebab-case, max 100 chars
   - `private: false` unless the user explicitly embargoes
   - `autoInit: true`
   - description: the paper title, truncated to 350 chars
3. Copy the file set from `paper-doi-template` (see Child file set).
   Substitute placeholders: PAPER_TITLE, PAPER_SLUG, author Watts / Deonte,
   owner DeontewattsV1, current year. Leave ORCID blank unless supplied.
   DOI fields stay PENDING until Zenodo returns values.
4. Do **not** upload binary manuscripts into the hub.
   Put manuscript text/PDF **only** in the child repo under `manuscript/`.
5. Append one object to `dummy-decoy-scientific-hub/papers/catalog.json`.
6. Add one row to the catalog table in `dummy-decoy-scientific-hub/README.md`.
7. Open a short issue on the hub titled `spawned: paper-<slug>` with the child URL.
8. Tell the user the three human-only steps:
   - Enable the child repo in Zenodo GitHub settings
   - Confirm the repo license and authors
   - Publish release `v1.0.0`
9. After the user pastes the minted DOI, update `CITATION.cff`, `.zenodo.json`,
   child README badges, hub catalog, and hub README.

## Storage conservation rule

If the user says upload 20 manuscripts: create 20 child repositories, not 20 folders of binaries in the hub.

## What you must refuse

- Inventing a DOI that was not issued by Zenodo, Crossref, DataCite, or Figshare.
- Putting all 20 papers full text into this hub.
- Enabling Zenodo for the user (they must toggle the webhook).
- Publishing a GitHub Release that contains secrets or restricted human data.
