# pkce (Proof Key for Code Exchange)

Simple Python module to generate PKCE code verifier and code challenge.


## Installation

```bash
pip install pkce
```

## Usage

```python
>>> import pkce
>>> code_verifier, code_challenge = pkce.generate_pkce_pair()
```

```python
>>> import pkce
>>> code_verifier = pkce.generate_code_verifier(length=128)
>>> code_challenge = pkce.get_code_challenge(code_verifier)
```

## Additional information

Spec for the PKCE protocol can be found [here](https://tools.ietf.org/html/rfc7636).
