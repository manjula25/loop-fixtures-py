# loop-fixtures-py

Small, deliberately buggy Python fixture project for the
[software-factory-loop](https://github.com/manjula25/software-factory-loop)
harness POC. **Not a real library** — it exists so the harness has a known-buggy
target with filed issues to work through.

Seeded state: three open issues, three failing tests on a clean checkout
(`pytest` exits 1 with exactly those failures). Everything else is green.

## Install and test

```bash
pip install -e ".[test]"
pytest
```

Fully offline: no network, no services.

## The seeded issues

See the issue tracker — each describes a user-visible symptom (one with an
attached traceback) and nothing about the cause.
