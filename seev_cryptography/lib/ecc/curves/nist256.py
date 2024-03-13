from typing import Literal, ClassVar

from Crypto.Math.Numbers import Integer
from seev_cryptography.lib.ecc.ecc_curve import EccCurve


class Nist256(EccCurve):
    """	This class stores the variables of the Nist256 curve"""
    order:  ClassVar[Integer] = Integer(115792089210356248762697446949407573529996955224135760342422259061068512044369)
    prime: ClassVar[Integer] = Integer(115792089210356248762697446949407573530086143415290314195533631308867097853951)
    a: ClassVar[Integer] = Integer(-3)
    b: ClassVar[Integer] = Integer(41058363725152142129326129780047268409114441015993725554835256314039467401291)
    Gx: ClassVar[Integer] = Integer(48439561293906451759052585252797914202762949526041747995844080717082404635286)
    Gy: ClassVar[Integer] = Integer(36134250956749795798585127919587881956611106672985015071877198253568414405109)
    modulus_bits: ClassVar[Integer] = Integer(256)
    pycryptodome_name: ClassVar[Literal['NIST P-256']] = 'NIST P-256'