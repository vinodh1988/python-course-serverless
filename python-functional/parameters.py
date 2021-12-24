def myfun(*multi,**kwparams):
    print(multi)
    #print(type(multi))
    print(kwparams)

# myfun(1)
# myfun(1,2)
# myfun(1,2,3,4,5,sno=1)
# myfun(name="rakesh")
# myfun(35634,sno=[34,34,34],name="Harry"

def printkey(**kwparams):
    for x in kwparams.keys():
        print(x,'=',kwparams[x])

printkey(sno=1,name="roger",city="mumbai")