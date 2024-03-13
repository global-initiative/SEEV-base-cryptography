from typing import Optional, Union, Tuple
from Crypto.PublicKey.ECC import EccPoint
from Crypto.Math.Numbers import Integer
from seev_cryptography.lib.ecc.type_mapping.crypto_curves import CryptoCurve


class NamedCurveEccPoint(EccPoint):
    """
    The point of this class is that in some cases, such as serialisation and de-serialisation to/from the database, we need to know the name of the curve the point is on.
    This is available as a private attribute of the EccPoint instance, however Legrandin recommended not accessing it as it may be removed in future.
    """
    def __init__(self, x: Union[int, Integer], y: Union[int, Integer], curve: Optional[CryptoCurve] = ...) -> None:
        super().__init__(x, y, curve=curve)
        self.curve_name = curve

    @classmethod
    def from_ecc_point(cls, ecc_point: EccPoint, curve_name: CryptoCurve):
        return cls(ecc_point.x, ecc_point.y, curve=curve_name)

    def to_ecc_point(self) -> EccPoint:
        return EccPoint(self.x, self.y, curve=self.curve_name)

    def decompose(self) -> Tuple[EccPoint, CryptoCurve]:
        return self.to_ecc_point(), self.curve_name