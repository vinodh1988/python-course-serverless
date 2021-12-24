def mymap(func,mylist):
    result=[]
    for x in mylist:
        result.append(func(x))
    return result

def stringProcess(x):
     return "{} -> {}".format(x,len(x))

print(mymap(stringProcess,["Raj","Ravi","India","International","World"]))