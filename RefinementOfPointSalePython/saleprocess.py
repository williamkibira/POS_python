#THIS BASICALLY HANDLES ALL ISSUES TO DO WITH A SALE AND THE REGISTERY

import sale
import barcodereader
import register
import sys

class SaleProcess:

    def __init__(self):
        self.__barcodereader = barcodereader.BarCodeReader()
        self.__sale = sale.Sale()
        self.__register = None
        
    def menu(self):
	print '1: to add a line item to the cart'
	print '2: to remove items from a line item'
	print '3: to add  items to a line item'
	print '4: to delete a line item'
	print '5: to register and item'
	print '0: to exit sale'
	
    
	    
    def addlineitem(self):
          self.__barcodereader.scanBarCode()
          numberofitems = raw_input('Enter Number of items')
          self.__sale.appendSale(self.__barcodereader.getBarCode(),numberofitems)
         
    def removeitems(self):
         number = raw_input('Enter barcode')
         numberofitems = raw_input('Enter Number of items to remove')
         self.__sale.removePartOfLineItem(self.__barcodereader.getBarCode(),numberofitems)
    def additems(self):
         self.__barcodereader.scanBarCode()
         numberofitems = raw_input('Enter Number of items to add')
         self.__sale.removePartOfLineItem(self.__barcodereader.getBarCode(),numberofitems)
    def deletelineitem(self):
         self.__barcodereader.scanBarCode()
         self.__sale.removeLineItem(self.__barcodereader.getBarCode)
    def registersale(self):
         self.__register = register.Register(sale)
         self.__register.changeCalculator()
	 self.__register.printReciept()
	
    def saleloop(self):
            self.menu()
            your_input = int(raw_input("ENTER YOU OPTION!"))
            if your_input == 1:
	       self.addlineitem()
            if your_input == 2:
	       self.removeitems()
            if your_input == 3:
               self.additems()
            if your_input == 4:
	       self.deletelineitem()
            if your_input == 5:
               self.registersale()
            if your_input == 0:
	       sys.exit(0)
	    
	    self.saleloop()    