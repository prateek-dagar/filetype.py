# Contributing to filetype.py

Thank you for your interest in contributing to `filetype.py`! We welcome contributions of all kinds, including bug fixes, feature requests, new file type matchers, and documentation improvements.

## Development Setup

To set up a local development environment:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/prateek-dagar/filetype.py.git
   cd filetype.py
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the package in editable mode with development dependencies:**
   ```bash
   pip install -e .
   pip install pytest pytest-benchmark pytest-cov pytest-html ruff codespell pre-commit
   ```

4. **Set up pre-commit hooks:**
   ```bash
   pre-commit install
   ```
   This automatically runs linting (`ruff`), formatting (`ruff format`), and spell checking (`codespell`) on every commit.

---

## Code Quality & Style

We use `ruff` to ensure a consistent code style and formatting across the project.

* **Linting:** Run `ruff check .`
* **Formatting:** Run `ruff format .`
* **Spelling:** Run `codespell .`

Please verify that all formatting, linting, and spelling checks pass locally before pushing your changes.

---

## Running Tests

We use `pytest` for unit testing and benchmarking. You can run the test suite using:

```bash
pytest
```

---

## Submitting Pull Requests

1. **Create a new branch** for your changes.
2. **Write clear commits** describing the "why" behind the changes.
3. **Add test cases** for any new features or bug fixes.
4. **Submit a Pull Request** against the `master` branch.
