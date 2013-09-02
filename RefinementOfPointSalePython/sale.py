import product as pdt
import salelineitem 
import barcode
import productcatalog as catalog
import barcodereader as code_reader

class Sale:
	
	
	def __init__(self):
		self.__ShoppingCart = list()
		self.__GrandTotal = None
		self.__catalog = catalog.ProductCatalog()
		self.__lineItem = None
	
	
	
	def appendSale(self,barcode,NumberOfItems):
	
# We Start Off a new sale saying SaleEnd is False
		self.__catalog.lookUpItem(self.__barcode)
		if self.__catalog.productExist():
			self.__lineItem = SaleLineItem(self.__catalogue.getProduct(),NumberOfItems)
			self.__ShoppingCart.append(self.__lineItem)
						
		else:
			print "This Product Doesn't Exsit In The Inventory"
						
			
			
					
	
	def removeLineItem(self,BarCode):
	
		for self.__ShoppingCart in i:
			product = self.__ShoppingCart.getProduct()
			if product.getProductBarCode() == BarCode.getBarCode():
				self.__ShoppingCart.remove(product)
			else:
				print "PRODUCT NOT IN CART"
				
				
	
	def removePartOfLineItem(self,BarCode,numberOfItems):
	
		for self.__ShoppingCart in i:
			product = self.__ShoppingCart.getProduct()
			if product.getProductBarCode() == BarCode.getBarCode():
				self.__ShoppingCart.decrementNumberOfItems(numberOfItems)
				
			else:
				print "FAILED TO DEDUCT ITEMS"
				
				
	
	def addPartOfLineItem(self,BarCode,numberOfItems):
		
		for self.__ShoppingCart in i:
			product = self.__ShoppingCart.getProduct()
			if product.getProductBarCode() == BarCode:
				self.__ShoppingCart.incrementNumberOfItems(numberOfItems)
				
			else:
				print "FAILED TO INCREMENT ITEMS"
	
	def calculateGrandTotal(self):
		self.__GrandTotal = 0
		for self.__ShoppingCart in i:
			self.__GrandTotal += self.__ShoppingCart.subTotalOfProduct()
			
	
# Over and Done with Methods of the Program

	def getGrandTotal(self):
	
		return self.__GrandTotal

        def sendLineItems(self):
	    
	        return self.__ShoppingCart