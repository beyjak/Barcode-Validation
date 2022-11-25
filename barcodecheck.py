# Check validity of 13-digits, 12-digits, 8-digits barcode
def barcodeCheckDigit(upc): 
	upclist = [int(d) for d in str(upc)]
	if len(upclist) == 13:
		odds = (upclist[1] * 3) + (upclist[3] * 3) + (upclist[5] * 3) + (upclist[7] * 3) + (upclist[9] * 3) + (upclist[11] * 3)
		evens = upclist[0] + upclist[2] + upclist[4] + upclist[6] + upclist[8] + upclist[10]
		sum = (evens + odds)
		checkdigit = 0
		while sum % 10 != 0:
			checkdigit = checkdigit + 1
			sum = sum + 1
		if checkdigit == upclist[-1]:
			bit = True
			print (str(upc) + " Barcode valid")
		else:
			bit = False
			print (str(upc) + " Barcode NOT valid")
		return bit

	elif len(upclist) == 12:
		odds = (upclist[0] * 3) + (upclist[2] * 3) + (upclist[4] * 3) + (upclist[6] * 3) + (upclist[8] * 3) + (upclist[10] * 3)
		evens = upclist[1] + upclist[3] + upclist[5] + upclist[7] + upclist[9]
		sum = (evens + odds)
		checkdigit = 0
		while sum % 10 != 0:
			checkdigit = checkdigit + 1
			sum = sum + 1
		if checkdigit == upclist[-1]:
			bit = True
			print (str(upc) + " Barcode valid")
		else:
			bit = False
			print (str(upc) + " Barcode NOT valid")
		return bit

	elif len(upclist) == 8:
		odds = (upclist[0] * 3) + (upclist[2] * 3) + (upclist[4] * 3) + (upclist[6] * 3)    
		evens = upclist[1] + upclist[3] + upclist[5]
		sum = (evens + odds)
		checkdigit = 0
		while sum % 10 != 0:
			checkdigit = checkdigit + 1
			sum = sum + 1
		if checkdigit == upclist[-1]:
			bit = True
			print (str(upc) + " Barcode valid")
		else:
			bit = False
			print (str(upc) + " Barcode NOT valid")
		return bit

	else:
		print("Invalid UPC, Please try again...")
		bit = False
		return bit
      
 # Main program run START
if __name__ == '__main__':     
    barcode = input("PLEASE ENTER BARCODE: ")
    barcodeCheckDigit(barcode)