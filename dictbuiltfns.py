dictdemo={"id":101,"name":"srinu","age":"M","sal":45000}

'''
built-in functions:
1)keys
2)values
3)items
4)clear
5)pop
6)popitem
7)len
'''
print(dictdemo.keys())
print(dictdemo.values())
print(dictdemo.items())
print(len(dictdemo))
print(dictdemo.clear())


#pop function it is used to removes the specified key value pairs.
dictdemo.pop("name")  #here we need to give compulsary key value otherwise it gives keyerror it requires at least one argument
print(dictdemo)

#popitem function is used to remove the random key value pairs which is before of 3.7 version.But after 3.7 version it removes the last entered key values
dictdemo.popitem()    #here no argument is required.
print(dictdemo)