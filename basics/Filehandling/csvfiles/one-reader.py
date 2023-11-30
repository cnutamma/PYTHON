import csv
file=open("data1.csv",'r')
csv_obj=csv.reader(file)




# print(list(csv_obj))
# output:[['hello', 'gm', 'srinivas'], ['hello', 'gaftn', 'srinivas'], ['hello', 'gdevng', 'srinivas'], ['hello', 'gdnt', 'srinivas']]




print(csv_obj)

# for data in csv_obj:
#     for name in data:
#         print(name)
#     print()

# '''
# output:
# hello
# gm
# srinivas

# hello
# gaftn
# srinivas

# hello
# gdevng
# srinivas

# hello
# gdnt
# srinivas
# '''