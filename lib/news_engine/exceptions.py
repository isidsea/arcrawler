class TooManyObjectsFound(Exception):
	def __init__(self,value):
		self.value = value
	#end def

	def __str__(self):
		return repr(self.value)
	#end def
#end class

class BadURLFormat(Exception):
	def __init__(self,value):
		self.value = value
	#end def

	def __str__(self):
		return repr(self.value)
	#end def
#end class