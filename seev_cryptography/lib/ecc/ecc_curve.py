from abc import ABC
from typing import cast, ClassVar

from Crypto.Math.Numbers import Integer
from Crypto.PublicKey.ECC import EccPoint

from seev_cryptography.lib.ecc.type_mapping.crypto_curves import CryptoCurve


class EccCurve(ABC):
	"""
	Subclasses stores the variables of different ECC curves, due to the fact that we need access to the parameters of the curve for the try-and-increment method of generator creation,
	which is attached to this class.
	Recommended we do this by Legrandin, as the _curve attribute of EccPoint may be removed in future.
	https://github.com/global-initiative/SEEV-api/issues/11

	We are technically dealing with Weierstrass curves here, which are plane curves with the following equation:
	y = (x**3 + a * x +  b).sqrt(p)
	https://en.wikipedia.org/wiki/Elliptic_curve#Elliptic_curves_over_the_real_numbers
	"""
	# The order of the curve, the number of points that exist on it
	order: ClassVar[Integer]

	# The prime number which defines the modulo for the curve.
	# The variable p in the equation: y = (x**3 + a * x +  b).sqrt(p)
	prime: ClassVar[Integer]

	# This is not an attribute of the pycryptodome implementation, needed for the curve equation
	# The variable a in the equation:  y = (x**3 + a * x +  b).sqrt(p)
	a: ClassVar[Integer]

	# The variable b in the equation: y = (x**3 + a * x +  b).sqrt(p)
	b: ClassVar[Integer]

	# The x coordinate of the default generator for the curve
	Gx: ClassVar[Integer]

	# The y coordinate of the default generator for the curve
	Gy: ClassVar[Integer]

	# The value of the pycryptodome modulus_bits attribute of the curve, the number of bits which encode its coordinates
	modulus_bits: ClassVar[Integer]

	# The pycryptodome name for the curve https://pycryptodome.readthedocs.io/en/latest/src/public_key/ecc.html
	pycryptodome_name: ClassVar[CryptoCurve]

	@classmethod
	def get_affine_y_coordinate(cls, x_coordinate: Integer) -> Integer:
		"""
		Given a potential affine x coordinate, calculate the equivalent affine y coordinate, if it exists. If not, raise ValueError.
		The Weierstrass form of the equation for an elliptic curve is given by:
		y = (x**3 + curve.a * x + curve.b).sqrt(curve.p)
		This calculation will throw a value error if the brackets evaluate to a number which is not a valid square (modulo the prime)
		In this case, (x,y) is not a valid affine coordinate i.e. not a point on the curve (the curve is made up of a series of discrete points)
		Args:
			 x_coordinate: The potential affine x coordinate
		Returns:
			the equivalent affine y coordinate if it exists
		Raises:
			ValueError, if the x coordinate is not a valid affine coordinate
		"""
		return (cast(int, x_coordinate) ** 3 + cls.a * x_coordinate + cls.b).sqrt(cls.prime)

	@classmethod
	def get_generator(cls) -> EccPoint:
		"""
		Get the default generator for the curve as a pycryptodome EccPoint
		Returns:
			An EccPoint instance describing the default generator for the curve
		"""
		return EccPoint(cls.Gx, cls.Gy, cls.pycryptodome_name)

