import saleprocess as sp
import inventoryprocess as store


def main():
        newsale = sp.SaleProcess()
        storesession = store.InventoryProcess()
        
        print "PYTHON POS SYSTEM :::: SORRY WE ARE ONLY CMD :("
        menu = "PLEASE CHOOSE 1: FOR INVENTORY \n 2: FOR POS TERMINAL\n\
	        SELECT 0 TO CLOSE PROGRAM !!\n"
	print menu
        option = int(raw_input("ENTER YOUR CHOICE"))
	
	while option != 0:
		if option == 1:
	# Here we Just call Up the inventory
		    storesession.inventoryactivity()   
		if option == 2:
		    newsale.saleloop()     	
	        print menu
	        option = raw_input("ENTER YOUR CHOICE")	
	print "THANK YOU {^_^}"	
		
if  __name__ =='__main__':main()