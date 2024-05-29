def create_count_attr(cls):        # cls --> Sample
	setattr(cls, "count", 0)
	return cls

@create_count_attr      # Sample = create_count(Sample) = updated_Sample
class Sample:

	def spam(self):
		pass

# s = Sample()
# print(dir(s))
#
#
# @create_count_attr
# class Demo:
# 	pass
#
# print(Demo.count)

from generic.excel_lib import read_locators

locators = read_locators("login_objects")
print(locators)

def _create(dictionary):
	def create_class_attr(cls):
		for key, value in dictionary.items():
			setattr(cls, key, value)
		return cls
	return create_class_attr


@_create(locators)          # @create_class_attr -> Sample = create_class_attr(Sample)
class Sample:

	def spam(self):
		pass

s = Sample()
# print(dir(s))


class A:

	def spam(self):
		pass


class B:

	def __init__(self, a):
		self.a = a
		self.a_obj = A()    # aggregation

	def display(self):
		pass

# a = A()
# s = Sample()
# b = B(a)        # composition
# b = B(s)





