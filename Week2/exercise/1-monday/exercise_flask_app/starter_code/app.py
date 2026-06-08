"""
Week 2 Exercise — Flask API with file-backed JSON storage.

TODO:
- Implement GET /findings  -> return list from data/findings.json
- Implement POST /findings -> body: {"title": "...", "severity": "..."}
      assign id = max existing id + 1, append, save file with json.dump + with open
"""

from __future__ import annotations

import json
from pathlib import Path

from flask import Flask, jsonify, request

app = Flask(__name__)
DATA_FILE = Path(__file__).resolve().parent / "data" / "findings.json"


def load_findings() -> list[dict]:
    with open(DATA_FILE, "r", encoding="utf-8") as file_handle:
        return json.load(file_handle)


def save_findings(items: list[dict]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as file_handle:
        json.dump(items, file_handle, indent=2)
        file_handle.write("\n")


@app.get("/findings")
def list_findings():
    return jsonify(load_findings())


@app.post("/findings")
def create_finding():
    payload = request.get_json(silent=True) or {}
    title = payload.get("title")
    severity = payload.get("severity")

    if not title or not severity:
        return jsonify({"error": "title and severity are required"}), 400

    findings = load_findings()
    next_id = max((finding.get("id", 0) for finding in findings), default=0) + 1
    created_finding = {"id": next_id, "title": title, "severity": severity}
    findings.append(created_finding)
    save_findings(findings)

    return jsonify(created_finding), 201


if __name__ == "__main__":
    app.run(debug=True)
