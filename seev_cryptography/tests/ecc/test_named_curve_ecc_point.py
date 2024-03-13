from seev_cryptography.lib.ecc.named_curve_ecc_point import NamedCurveEccPoint
from seev_cryptography.lib.utils.key_utils import KeyGenerationUtils


def test_named_curve_ecc_point():
    point = KeyGenerationUtils.generate_ecc_key_pair('NIST P-256').pointQ
    np = NamedCurveEccPoint.from_ecc_point(point, 'NIST P-256')
    re_point = NamedCurveEccPoint.to_ecc_point(np)
    assert point == re_point

