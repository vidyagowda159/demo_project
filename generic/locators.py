def attach_locators(locators):
	def wrapper(cls):
		for name, loc_tuple in locators.items():
			setattr(cls, name, loc_tuple)
		return cls
	return wrapper
