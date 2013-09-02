import MySQLdb as db
import sys
import product

class DataBase:

	def __init__(self):
		self.__createDB = "CREATE DATABASE IF NOT EXISTS PointOfSale"
		self.__usedatabase = "USE PointOfSale"	        	              
		self.__connector = db.connect('localhost', 'root', '', 'Inventory');
		
		with self.__connector:
					cursor = self.__connector.cursor()
				        #cursor.execute(self.__createDB)
				        #cursor.execute(self.__usedatabase)
					cursor.execute("CREATE TABLE IF NOT EXISTS inventory(name varchar(25) not null,\
			                                barcode int(14) primary key not null,metric int(6) not null,\
			                                metricunit varchar(10) not null,price int(8) not null,description varchar(100) null)")
				
	def itemLookUp(self,barCode):
	
		with self.__connector:
					cursor = self.__connector.cursor(db.cursors.DictCursor)
					cursor.execute("SELECT * FROM inventory where barcode = %s",barCode)
					
					rows = cursor.fetchall()
						
					product = Product(row["name"],row["bar_code"],row["price"])
						
					
					return product
				
	def itemDisplay(self):
	
		with self.__connector:
					cursor = self.__connector.cursor(db.cursors.DictCursor)
					cursor.execute("SELECT * FROM inventory")
					print "PRODUCT NAME:   BARCODE:   PRICE: "
					rows = cursor.fetchall()
					
					for row in rows:
						print rows["name"],rows["barcode"],rows["price"],["amount"]
	
	
	def insertProduct(self,Product):
	
		with self.__connector:
					cursor = self.__connector.cursor()
					cursor.execute( " INSERT INTO inventory\
							 (name,barcode,metric,metricunit,price,description)\
       							 values (%s, %s, %s, %s, %s)",product.getProductName(),
       							 product.getProductBarCode(),
       							 product.getProductMetric(),
       							 product.getProductMetricUnit(),
       							 product.getProductPrice(),
       							 product.getProductDescription()) 
       							 

