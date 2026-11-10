# Robinhood options bot — Muse research handoff

This public copy contains the Python options bot, strategy and to-do list, anonymized trade histories, historical market data, tests, and backtesting/paper-research tools. Live trading is disabled in the copy. Actual account state, identifiers, balances, broker credentials, and raw account journals were excluded or redacted. Some opaque files and private databases were omitted; see `PUBLIC_SANITIZATION_REPORT.json` inside the archives for the detailed scope. Trade history and strategy data are intentionally public.

## Download for Muse

- `00_MUSE_STARTER_PUBLIC.zip` is a smaller starter; it does not include the full historical dataset.
- `01_COMPLETE_PROJECT_AND_HISTORY_PUBLIC.zip` contains the full **public-safe** dataset. It uses Git LFS; when cloning, install Git LFS and run `git lfs pull` to retrieve the actual file.
- `UPLOAD_PARTS/` contains smaller ZIP files and `00_RESTORE_INSTRUCTIONS.zip`. Download all numbered ZIP parts and the instructions ZIP, place them in the same folder, extract the instructions ZIP and run `python3 RESTORE.py`. This verifies the parts and reassembles the complete public-safe archive.

Extract into a new directory and read `START_HERE_MUSE.md` and `TODO.txt`. The public trade ledger includes records from overlapping experiments and controls; do not assume they are independent. Reinstall dependencies from `pyproject.toml`. Fresh paper trading requires an authorized market-data connection; the archive itself grants no broker access or authority to place live orders.
