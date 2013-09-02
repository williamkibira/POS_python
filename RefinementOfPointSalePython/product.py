import barcode

class Product:


	def __init__(self,name,barcode,metric,metricunit,price,description):
		self.__name = name
		self.__barcode = barcode
		self.__price = price
		self.__metric = metric
		self.__metricunit = metricunit
		self.__description = description
	
	def getProductName(self):
		return self.__name
	def getProductBarCode(self):
		return self.__barcode
	def getProductPrice(self):
		return self.__price
	def getProductMetric(self):
		return self.__metric
	def getProductMetricUnit(self):
		return self.__metricunit	
	def getProductDescription(self):
		return self.__description
