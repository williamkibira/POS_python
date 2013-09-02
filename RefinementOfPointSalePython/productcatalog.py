import product
import database as db
import barcode


class ProductCatalog:
	
	
	def __init__(self):
		self.__database = db.DataBase()
		self.__MyProduct = None
		self.__productExists = False 
	
	def createProduct(self,Product):
		self.__MyProduct = Product
		self.__database.insertProduct(self.__MyProduct)
		
	def lookUpItem(self,BarCode):
		self.__database = db.DataBase()
		self.__MyProduct = self.__database.lookUpItem(BarCode.getBarCode())
		if self.__MyProduct is None:
			self.__productExists = False
		else:
			self.__productExists = True
			
	def productExist(self):
		return self.__productExists
		
	def getProduct(self):
		return self.__MyProduct
		
	def showAllItems(self):
	
		self.__database.itemDisplay()
	
	

