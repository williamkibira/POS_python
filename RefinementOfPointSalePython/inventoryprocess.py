# This manages the inventory class

import inventory
import sys

class InventoryProcess:
        def __init__(self):
	  self.__inventory = inventory.Inventory()
	  
	def menu(self):
	  
	    print '1: To add Product'
	    print '2: To show all products'
	    print '0: To end program'
	    
	    
	    
	def inventoryactivity(self):
	    menu()
	    option = int(raw_input("Enter Option Here!"))
	    if option == 1:
	       self.addProduct()
	    elif option == 2:
	       self.showproducts()
	    elif option == 0:
	       sys.exit(0)
	    else:
	      print 'wrong input'
	    self.inventoryactivity()
	    
	def addProduct(self):
	    self.__inventory.addNewProduct()
	    
	    
	def showproducts(self):
	    self.__inventory.showAllProducts()