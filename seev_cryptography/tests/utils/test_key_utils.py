from Crypto.PublicKey.ECC import EccKey, EccPoint

from seev_cryptography.lib.ecc.curves.nist256 import Nist256
from seev_cryptography.lib.utils.key_utils import KeyGenerationUtils, EccKeySerialisationUtils, EccPointSerialisationUtils


class TestEccKeySerialisationUtils:
	def test_pub_priv_pair_import_and_export(self):
		key: EccKey = KeyGenerationUtils.generate_eddsa_key_pair('ed25519')
		bin: bytes = EccKeySerialisationUtils.export_public_private_key_pair_as_binary(key)
		re_key: EccKey = EccKeySerialisationUtils.import_public_private_key_pair_from_binary(bin)

		assert re_key == key
		assert key.has_private() is True
		assert re_key.has_private() is True
		assert key.public_key() == re_key.public_key()

	def test_pub_import_and_export(self):
		key: EccKey = KeyGenerationUtils.generate_eddsa_key_pair('ed25519')
		pub = key.public_key()
		bin: bytes = EccKeySerialisationUtils.export_public_key_as_binary(pub)
		re_pub: EccKey = EccKeySerialisationUtils.import_public_key_from_binary(bin)

		assert pub == re_pub
		assert pub.has_private() is False
		assert re_pub.has_private() is False
		assert pub.public_key() == re_pub.public_key()


class TestEccPointSerialisationUtils:
	def test_import_and_export_ecc_point_as_key(self):
		key: EccKey = KeyGenerationUtils.generate_ecc_key_pair(Nist256().pycryptodome_name)
		point: EccPoint = key.pointQ
		bin: bytes = EccPointSerialisationUtils.export_ecc_point_as_binary_public_key(point, Nist256().pycryptodome_name)
		re_point: EccPoint = EccPointSerialisationUtils.import_ecc_point_from_binary_public_key(bin)

		assert re_point == point

