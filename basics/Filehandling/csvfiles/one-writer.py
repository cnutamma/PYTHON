import csv


f=open('one.csv','w',newline="")

cp=csv.writer(f)
cp.writerow([id,"name","sal"])
cp.writerow([1,"srinu",45000])
cp.writerow([2,"gopi",55000])
cp.writerow([3,"vamsi",65000])

f.close()