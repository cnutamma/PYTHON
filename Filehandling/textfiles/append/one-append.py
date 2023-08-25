file=open("data3.txt",'a')
file.write("Gm,srinivas\n")
file.write("Have a great day,")
file.write("Welcome.\n")
file.close()

#here over riding doesn't takes place.
#if we are executing n times we get n number of lines in the text file.
#because cursor is at last line of the text code for each append 