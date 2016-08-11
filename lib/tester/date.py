from .base 		 import FieldTester
from .exceptions import TestIsNotPassed
from .. 		 import tools
import copy
import arrow

class DateTester(FieldTester):
	def __init__(self, **kwargs):
		super(DateTester, self).__init__(**kwargs)

	def test(self, object_to_test=None, link=None):
		try:
			assert object_to_test is not None, "object_to_test is not defined."
			if len(object_to_test) == 0: 
				raise TestIsNotPassed("No test object.")
			str_date = copy.copy(object_to_test)
			str_date = self._prepare_value(str_date)

			if type(str_date) is str:
				str_date = tools._date_parser(str_date)
				if str_date is None: raise TestIsNotPassed("Cannot parse date.")
			elif type(str_date) is list:
				str_date = [tools._date_parser(r) for r in str_date]
				if None in str_date: raise TestIsNotPassed("Cannot parse date.")
			print("[test][debug][{}] Data: {}".format(self.source.CRAWLER_NAME, str_date))
		except AssertionError:
			raise TestIsNotPassed("Assertion is not satisfied.")
		except AttributeError:
			raise TestIsNotPassed("Cannot parse date.")
