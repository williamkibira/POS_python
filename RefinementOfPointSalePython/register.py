# The register class

import salelineitem
import product

import sale
import subprocess

class Register:

	def __init__(self,sale):
		self.__shoppingcart = list()
		self.__balance = None
		self.__sale  = sale
	
	
		
	
	def changeCalculator(self):
	        print self.__sale.getGrandTotal()
	        givenMoney = raw_input("Enter Payment")
		self.__balance = givenMoney - self.__sale.getGrandTotal()
		if self.__balance < 0:
			print "Money is Insufficient"
			self.changeCalculator()
		else:
			print "Successful Transaction "
			
	
		
	def printReciept(self):
	
	# We get the sale from the  THIS PRINT IS FOR LINUX ONLY
		self.__shoppingcart = self.__sale.sendLineItems()
		lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
		lpr.stdin.write("|*************************************************|")
		for cart in self.__shoppingcart:
			product = cart.getProduct()
			lineItemNumber = cart.getNumberOfItems()
			lineItemTotal = cart.getSubTotal()
			
			lpr.stdin.write("NAME:%s \t PRICE:%s \t No_ITEMS:%s \t SUB_TOTAL:%s",
			product.getProductName(),product.getProductPrice(),
			lineItemNumber,lineItemTotal)
	        lpr.stdin.write("GRAND TOTAL IS :%s",self.__sale.getGrandTotal())
	        lpr.stdin.write("BAL: %s",self.getBalance())
	def getBalance(self):
	
		return self.__balance
		
	
	
	