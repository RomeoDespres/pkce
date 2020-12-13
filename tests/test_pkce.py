import pkce
import pytest


def test_generate_code_verifier():
    length = 128
    verifier1 = pkce.generate_code_verifier(length)
    verifier2 = pkce.generate_code_verifier(length)
    assert len(verifier1) == length
    assert len(verifier2) == length
    assert verifier1 != verifier2


def test_generate_code_verifier_too_short():
    with pytest.raises(ValueError):
        pkce.generate_code_verifier(42)


def test_generate_pkce_pair_too_short():
    with pytest.raises(ValueError):
        pkce.generate_pkce_pair(42)


def test_get_code_challenge():
    abc = "abcdefghijklmnopqrstuvwxyz"
    challenge = pkce.get_code_challenge(abc + abc.upper())
    assert challenge == "OWQpS2ZGE3mNGkd-uK0CEYtI0MVzjEJ2EyAvLtEjtfE"


def test_get_code_challenge_too_short():
    with pytest.raises(ValueError):
        pkce.get_code_challenge("abcdef")
