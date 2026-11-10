#!/usr/bin/env python3
"""Reassemble the uploaded data parts; no network or project code is executed."""
import hashlib,json,zipfile
from pathlib import Path
root=Path(__file__).resolve().parent
m=json.loads((root/"manifest.json").read_text())
dest=root/m["archive_name"]
h=hashlib.sha256()
with dest.open("wb") as out:
 for part in m["parts"]:
  p=root/part["zip"]
  if not p.exists(): raise SystemExit(f"Missing upload: {p.name}")
  with zipfile.ZipFile(p) as z:
   data=z.read(part["chunk"])
  if len(data)!=part["bytes"] or hashlib.sha256(data).hexdigest()!=part["sha256"]: raise SystemExit(f"Corrupt part: {p.name}")
  out.write(data); h.update(data)
if dest.stat().st_size!=m["archive_size"] or h.hexdigest()!=m["sha256"]: raise SystemExit("Archive hash or size mismatch")
print("Verified:",dest)
print("Extract in a NEW directory, then read START_HERE_MUSE.md.")
