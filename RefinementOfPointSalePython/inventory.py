###############################################################################
#THIS CLASS IS FOR ADDING PRODUCTS AND CHECKING ON THEM IN THE DATABASE SYSTEM#
#                  						              #
###############################################################################
import productcatalog as catalog
import barcodereader as codereader

class Inventory:
	def __init__(self):
		self.__productname = None
		self.__productbarcode = None
		self.__productmetric = None
		self.__productmetricunit = None
		self.__productdescription = None
		self.__productprice = None
	        self.__catalogue = catalog.ProductCatalog()
	# GET THE USERS INPUT AT THIS POINT 	
	def addNewProduct(self):
		self.__productname = raw_input("Enter the product name.")
		reader = codereader.BarCodeReader()
		reader.scanBarCode()
		barcode = reader.getBarCode.getBarCode()
		self.__productbarCode =  barcode
		self.__productmetric = raw_input("Enter The Metric")
		self.__productamount = raw_input("Enter Metric Amount")
		self.__productprice = raw_input("Enter the Price")
		self.__productdescription = raw_input("Enter the Description")
		
		product = Product(self.__productname,
				  self.__productbarcode,
				  self.__productprice,
				  self.__productmetric,
				  self.__productmetricunit,
				  self.__productdescription)
		
		self.__catalog.createProduct(product)
		
	def showAllProducts(self):
	
		# load up the catalogue to show all the Inventory stock
		
		self.__catalog.showAllItems()

