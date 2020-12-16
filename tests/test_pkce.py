import random
import string

import pkce
import pytest


CORRECT_LENGTHS = range(43, 129)
INCORRECT_LENGTHS = list(range(43)) + list(range(129, 200))


@pytest.mark.parametrize('length', CORRECT_LENGTHS)
def test_generate_code_verifier(length):
    verifier1 = pkce.generate_code_verifier(length)
    verifier2 = pkce.generate_code_verifier(length)
    assert len(verifier1) == length
    assert len(verifier2) == length
    assert verifier1 != verifier2


@pytest.mark.parametrize('length', INCORRECT_LENGTHS)
def test_generate_code_verifier_too_short_or_too_long(length):
    with pytest.raises(ValueError):
        pkce.generate_code_verifier(length)


@pytest.mark.parametrize('length', INCORRECT_LENGTHS)
def test_generate_pkce_pair_too_short_or_too_long(length):
    with pytest.raises(ValueError):
        pkce.generate_pkce_pair(length)


def test_get_code_challenge():
    abc = 'abcdefghijklmnopqrstuvwxyz'
    challenge = pkce.get_code_challenge(abc + abc.upper())
    assert challenge == 'OWQpS2ZGE3mNGkd-uK0CEYtI0MVzjEJ2EyAvLtEjtfE'


@pytest.mark.parametrize('length', INCORRECT_LENGTHS)
def test_get_code_challenge_too_short_or_too_long(length):
    verifier = ''.join(random.choices(string.ascii_letters, k=length))
    with pytest.raises(ValueError):
        pkce.get_code_challenge(verifier)
