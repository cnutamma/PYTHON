#How to write data into text files

file=open("data2.txt",'w')
file.write("Gm,srinivas\n")
file.write("Have a great day")
file.close()

#if we are executing it n of times also it gives only 2 lines of output because the cursor is at staring point of the page and over riding takes place.
#over riding takes place.