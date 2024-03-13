from typing import get_args
import gmpy2
from Crypto.PublicKey.ECC import EccPoint
from seev_cryptography.lib.ecc.type_mapping.crypto_curves import NistCurveP256
from seev_cryptography.lib.ecc.curves.nist256 import Nist256


def test_check_constants():
    """Checking that the saved constants match the pycryptodome ones"""
    # ignore the import warning
    from Crypto.PublicKey.ECC import _curves
    constants = _curves['NIST P-256']
    assert Nist256.pycryptodome_name in get_args(NistCurveP256)
    assert Nist256.prime == constants.p
    assert Nist256.b == constants.b
    assert Nist256.order == constants.order
    assert Nist256.Gx == constants.Gx
    assert Nist256.Gy == constants.Gy
    assert Nist256.modulus_bits == constants.modulus_bits
    assert Nist256.a == -3

def test_get_generator():
    get_generator = Nist256.get_generator()

    assert isinstance(get_generator, EccPoint)
    assert get_generator.x == int(gmpy2.mpz("0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296", base=16))
    assert get_generator.y == int(gmpy2.mpz("0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5", base=16))
    assert get_generator.is_point_at_infinity() is False




