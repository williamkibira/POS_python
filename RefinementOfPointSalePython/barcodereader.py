import barcode

class BarCodeReader:
	def __init__(self):
		self.__barcode = None
	
	def getBarCode(self):
		if self.__barcode == None:
			return None
		else:
		
			return self.__barcode
			
	def scanBarCode(self):
	
	# __itemcode will come from a barcode reader
	        self.__itemcode = raw_input("BarCODE Please")
		self.__barcode = BarCode.BarCode(self.__itemcode)
	
		
