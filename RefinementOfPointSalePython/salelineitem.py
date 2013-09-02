import product

class SaleLineItem:
	
	def __init__(self,product,numberofitems):
		self.__product = product
		self.__numberofitems = numberofitems
		
	def getProduct(self):
		return self.__product
		
	def getNumberOfItems(self):
		return self.__numberofitems
		
		
	def decrementNumberOfItems(self, newItemNumber):
		if self.__numberofitems > newItemNumber:
			self.__numberofitems -= newItemNumber
		else:
		   print "ERROR : Greater than Stored Value"
		   
	def incrementNumberOfItems(self, newItemNumber):
		self.__numberofitems += newItemNumber
		
	def subTotalOfProduct(self):
		return self.__numberofitems*self.__product.getProductPrice()
	
	
		

