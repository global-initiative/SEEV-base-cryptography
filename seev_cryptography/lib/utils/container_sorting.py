from typing import Union, Any, Collection, Type, Tuple


def get_b_type(cont: Any, types: Collection[Type] = (dict, list, tuple)) -> Type:
	"""
	Gets the base type of a given parameter amongst the provided types
	Raises an exception otherwise.

	:param cont: the object to get the type of
	:param types: the candidate types
	:return: the matched type - raises a ValueError if none match

	"""
	# Django serializer output comes with some odd types from rest_framework.utils.serializer_helpers
	# namely ReturnDict and ReturnList in out cases. Those are modified versions of a Ordered dict and list
	# but expect a 'serializer' kwarg to be instantiated. sort_container() performs parameterless container
	# instantiation and requires a parameterless type to perform
	for t in types:
		if isinstance(cont, t): return t
	raise ValueError(f"No known base type for parameter {cont} of type {type(cont)} amongst suggested types {types}")

def sort_container(cont: Union[dict, list, tuple], cont_t: Tuple[Type] = (dict, list, tuple)) -> Union[dict, list, tuple]:
	"""
	Sort a given container from the most inner element outward. The order of the elements
	is based upon their string representation. "pure" collections (collections that do not
	contain any other containers) are left untouched.

	:param cont: the container to sort
	:param cont_t: the types of containers to recursively sort
	:return: a sorted copy of the container
	"""
	# recursion depth exit condition
	if not isinstance(cont, cont_t): return cont

	# returns "pure" collection as they are
	if not isinstance(cont, dict):
		only_base_type: bool = True
		for v in cont: only_base_type &= not isinstance(v, cont_t)
		if only_base_type: return cont

	# setup of type specific manipulation functions
	s_cont = get_b_type(cont)()  # new empty container, regardless of the type, for sorted data
	get_val = (lambda k: cont[k]) if isinstance(cont, dict) else (lambda k: k)
	set_val = (lambda k, v: s_cont.__setitem__(k, v)) if isinstance(cont, dict) else (lambda _, v: s_cont.append(v))

	# sort the container
	for key in sorted(cont, key=str):	set_val(key, sort_container(get_val(key)))

	return s_cont
