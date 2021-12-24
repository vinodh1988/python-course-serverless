def mymap(func,mylist):
    result=[]
    for x in mylist:
        result.append(func(x))
    return result

def stringProcess(x):
     return "{} -> {}".format(x,len(x))

print(mymap(stringProcess,["Raj","Ravi","India","International","World"]))

print(mymap(lambda a:a*a,[2,4,56,5,46,45,6]))

print(mymap(lambda a: "EVEN" if a%2==0 else "ODD",[34,56,241,234,111,215,124,153]) )