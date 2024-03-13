from typing import Literal, Union

"""
We are just defining literal types for curve names that we can use elsewhere to make sure we get the names right with the help of the IDE.
All name from:
https://pycryptodome.readthedocs.io/en/latest/src/public_key/ecc.html
"""


NistCurveP192 = Literal[
	'NIST P-192', 'p192', 'P-192', 'prime192v1', 'secp192r1',
]

NistCurveP224 = Literal[
	'NIST P-224', 'p224', 'P-224', 'prime224v1', 'secp224r1',
]

NistCurveP256 = Literal[
	'NIST P-256', 'p256', 'P-256', 'prime256v1', 'secp256r1',
]

NistCurveP384 = Literal[
	'NIST P-384', 'p384', 'P-384', 'prime384v1', 'secp384r1',
]

NistCurveP521 = Literal[
	'NIST P-521', 'p521', 'P-521', 'prime521v1', 'secp521r1'
]

NistCurve = Union[
	NistCurveP192,
	NistCurveP224,
	NistCurveP256,
	NistCurveP384,
	NistCurveP521
]

EddsaCurveEd25519 = Literal[
	'ed25519', 'Ed25519',
]

EddsaCurveEd448 = Literal[
	'ed448', 'Ed448'
]

EddsaCurve = Literal[
	EddsaCurveEd25519,
	EddsaCurveEd448
]

CryptoCurve = Union[NistCurve, EddsaCurve]


