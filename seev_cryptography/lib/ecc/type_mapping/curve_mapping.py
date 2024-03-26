from typing import Dict, Optional, Type
from seev_cryptography.lib.ecc.type_mapping.crypto_curves import CryptoCurve
from seev_cryptography.lib.ecc.ecc_curve import EccCurve
from seev_cryptography.lib.ecc.curves.nist256 import Nist256


"""
This module maps the pycryptodome curve names to subclasses of EccCurve.
https://pycryptodome.readthedocs.io/en/latest/src/public_key/ecc.html
The purpose of this is three-fold:
- Retrieve pycryptodome curve parameters from the pycryptodome name stored in the db 
- Allow future possibility to use different curves for the ECC
- Avoid magic strings throughout the codebase
"""

curve_mapping: Dict[CryptoCurve, Optional[Type[EccCurve]]] = {
	'NIST P-192': None, 'p192': None, 'P-192': None, 'prime192v1': None, 'secp192r1': None,
	'NIST P-224': None, 'p224': None, 'P-224': None, 'prime224v1': None, 'secp224r1': None,
	'NIST P-256': Nist256, 'p256': Nist256, 'P-256': Nist256, 'prime256v1': Nist256, 'secp256r1': Nist256,
	'NIST P-384': None, 'p384': None, 'P-384': None, 'prime384v1': None, 'secp384r1': None,
	'NIST P-521': None, 'p521': None, 'P-521': None, 'prime521v1': None, 'secp521r1': None,
	'ed25519': None, 'Ed25519': None,
	'ed448': None, 'Ed448': None
}

