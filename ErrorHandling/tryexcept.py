# Python program to handle simple runtime error
#Python 3

a = [1, 2, 3]
try:
	# Throws error since there are only 3 elements in array
	print ("Fourth element = %d" %(a[3]))

except:
	print ("An error occurred")
	
finally:
	print("final block executes everytime")
