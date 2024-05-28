

def attach_locators(locators):
	def wrapper(cls):
		for name, loc in locators.items():
			setattr(cls, name, loc)
		return cls
	return wrapper