# How individual paper DOIs are minted

This hub does not issue DOIs. Neither does GitHub. A DOI is a persistent identifier registered with a registration agency (DataCite for Zenodo; Crossref for journals).

## Recommended path

1. Create a public child repository from paper-doi-template.
2. Sign in at https://zenodo.org and link GitHub.
3. Open https://zenodo.org/account/settings/github/ , Sync now, toggle the child repository on.
4. Confirm CITATION.cff and .zenodo.json. If both exist, Zenodo prefers .zenodo.json for deposit metadata; GitHub still uses CITATION.cff for the cite widget.
5. In the child repo: Releases, Draft a new release, tag v1.0.0, Publish.
6. Zenodo archives the snapshot and mints a concept DOI (always latest) and a version DOI (this tag).
7. Copy both DOIs into the child README badge, child CITATION.cff, this hub papers/catalog.json, and this hub README table.

Sandbox first if you have never used the integration: https://sandbox.zenodo.org

## Twenty papers

Do not mint twenty DOIs from one mega-repo. Spawn twenty child repositories, enable each in Zenodo, publish twenty v1.0.0 releases. The hub README then lists twenty named rows.
