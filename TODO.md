# TODO

## Future Enhancements & CI/CD Security
- [ ] Conduct market research on CI security and code quality tools:
  - [ ] Evaluate **GitHub Advanced Security (GHAS)** / **CodeQL** (native GitHub integration, vulnerability scanning).
  - [ ] Evaluate **SonarQube** / **SonarCloud** (code quality, test coverage analytics, code smells).
- [ ] Integrate the chosen security scanner and quality gate tools into the GitHub Actions workflow (`.github/workflows/test.yml`).

## Packaging & Type Safety
- [ ] Add type stubs (`.pyi` files) and a `py.typed` marker file for PEP 561 compliance.
- [ ] Update packaging configuration ([setup.py](file:///Users/prateekdagar/workspace/filetype.py/setup.py), [MANIFEST.in](file:///Users/prateekdagar/workspace/filetype.py/MANIFEST.in)) to include type stubs.
- [ ] Implement package build verification (e.g. running `twine check` or `check-manifest`) in the CI pipeline.

## File Signature Coverage Expansion
- [-] Cross-reference signatures/magic bytes from other open-source libraries to port missing types (refer to [Issue #45](https://github.com/h2non/filetype.py/issues/45)):
  - [-] Check signatures in [fleep-py](https://github.com/floyernick/fleep-py/blob/master/fleep/data.json).
  - [-] Check signatures in [puremagic](https://github.com/cdgriffith/puremagic/blob/master/puremagic/magic_data.json).
  - [-] Check signatures in [fido](https://github.com/openpreserve/fido/blob/master/fido/conf/format_extensions.xml).
  - [-] Check signatures in other tools (`Whatype`, `pyfsig`, `cigma`).
- [ ] Add real/minimal binary sample files to [tests/fixtures/](file:///Users/prateekdagar/workspace/filetype.py/tests/fixtures) for newly added types (DjVu, Mobi, Pcap, Pcapng, Chm, Class, Dex) to make integration tests more realistic.

