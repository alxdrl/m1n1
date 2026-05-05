# M1N1 Proxy Client

A Python package for interacting with Apple Silicon devices using the M1N1 proxy.

## Installation

Install from PyPI:

```bash
pip install m1n1-proxyclient
```

or, if need to use m1n1/ishell.py

```bash
pip install "m1n1-proxyclient[interactive]"
```

Or from source:

```bash
poetry install
```

## Packaging / Versioning

We expect upstream tags without post segment:

downstream tag v1.6.0rc1-100 -> downstream v1.6.0rc1.post100
upstream tag v1.6.0rc1       -> downstream v1.6.0rc1.post100
upstream tag v1.5.2          -> downstream v1.5.2.post100
commit after tag v1.5.2      -> downstream v1.5.2.post100.devN
dirty local tree             -> not intended for publishing

sdist includes experiments/ and hv/ which are not included in wheel.

## Usage

[Add usage examples here]

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Copyright The Asahi Linux Contributors