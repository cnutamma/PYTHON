num=[1,4,2,7,3,0,3,1,2]
#here, we need to convert list items into the dict keys bcoz in dict keys can't be duplicate and we convert dict to list again
mylist=list(dict.fromkeys(num))
print(mylist)
