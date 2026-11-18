#!/usr/bin/env python3
"""Offline structural/privacy linter for the public workflow template copies.

This does not execute n8n or verify runtime results.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = sorted((ROOT / "workflows").glob("*.json"))
assert len(FILES) == 4, "Expected exactly four exported workflow files"
for path in FILES:
    workflow = json.loads(path.read_text())
    names = {node["name"] for node in workflow["nodes"]}
    assert len(names) == len(workflow["nodes"]), f"Duplicate node names in {path.name}"
    assert set(workflow["connections"]).issubset(names), path.name
    for source, outputs in workflow["connections"].items():
        for targets in outputs.get("main", []):
            for target in targets:
                assert target["node"] in names, f"Broken edge in {path.name}: {source}"
    text = path.read_text()
    assert "arunganesan.app.n8n.cloud" not in text
    assert "Partner Alpha API Auth" not in text
    assert "instanceId" not in text and "cachedResultUrl" not in text
    assert "errorWorkflow" not in text and '"credentials"' not in text
    assert workflow["active"] is False
    print(f"OK: {path.name}: {len(workflow['nodes'])} nodes")
print("Structural and selected privacy checks passed. Live tests still required.")
