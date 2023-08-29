import json

f=open('one.json','w')

emp_dict={
    'id':1,
    'name':'srinivas',
    'avail':True,
    'loc':None

}
json.dump(emp_dict,f)

f.close()