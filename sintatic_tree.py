class char:
	def __init__( self , item):
		self .item = item

	def __str__( self ):
		return self .item

	def __contains__( self , item):
		return self .item == item

class union:
	def __init__( self , left , right ):
		self . left = left
		self . right = right

	def __str__( self ):
		return '(' + str( self . left ) + '|' + str( self . right ) + ')'

	def __contains__( self , item):
		return item in self . left or item in self . right

class cat:
	def __init__( self , left , right ):
		self . left = left
		self . right = right

	def __str__( self ):
		return  '(' + str( self . left ) + '.' + str( self . right ) + ')'

	def __contains__( self , st ):
		for i in range(0, len(st) + 1):
			if st [: i ] in self . left and st[i :] in self . right : return True
		return False

class star:
	def __init__( self , item):
		self .item = item

	def __str__( self ):
		return str( self .item) + '*'

	def __contains__( self , st ):
		if st == '': return True
		for i in range(1, len(st) + 1):
			if st [: i ] in self .item and st[i :] in self : return True
		return False