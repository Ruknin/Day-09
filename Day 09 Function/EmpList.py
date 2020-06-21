"""
emp1 = {'Id':1,'name':'Nazmul','salary':123}
emp2 = {'Id':2,'name':'Saiful','salary':45}
emp3 = {'Id':3,'name':'Atiq','salary':789}
emp4 = {'Id':4,'name':'Monjur','salary':632}

print("%s %s %s" %(emp1['Id'],emp1['name'],emp1['salary']))
"""
employees= [
{'Id':1,'name':'Nazmul','salary':123},
{'Id':2,'name':'Saiful','salary':45},
{'Id':3,'name':'Atiq','salary':789},
{'Id':4,'name':'Monjur','salary':632}
]

'''print("%-5s %-25s %10s"%('Id','name','salary'))
print(42*"=")
for emp in employees:
    print("%-5s %-25s %10s" %(emp['Id'],emp['name'],emp['salary']))'''

print("\n\n%-5s %-20s %10s"%('Id','name','salary'))
print(40*"=")
for emp in employees:
    print("{0:<5}{1:20}{2:>10}" .format(emp['Id'],emp['name'],emp['salary']))