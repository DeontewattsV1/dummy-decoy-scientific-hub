#!/usr/bin/env python3
import json
from pathlib import Path
catalog = json.loads(Path('papers/catalog.json').read_text())
print('| Paper | Child repository | Concept DOI | Version DOI | Status |')
print('| --- | --- | --- | --- | --- |')
for paper in catalog.get('papers', []):
    title = paper.get('title', '')
    repo = paper.get('repo', '')
    concept = paper.get('concept_doi') or '*pending*'
    version = paper.get('version_doi') or '*pending*'
    status = paper.get('status', '')
    slug = repo.rsplit('/', 1)[-1] if repo else ''
    print(f'| {title} | [{slug}]({repo}) | {concept} | {version} | {status} |')
