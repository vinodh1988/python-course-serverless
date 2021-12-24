a=[2344,345,3456,34,356,5467,23,68,67]

def checkType(a):
    if a%2==0:
        return "EVEN"
    else:
        return "ODD"

result=map(checkType,a)

print(result)
print(list(result))