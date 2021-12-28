# a closure is a function object which remembers values that are stored in enclosing scope

a=889
def outer(param):
    print(param)
    a=230 #local scope
    print(a)
    def inner(inside):
        nonlocal a
        a=350
        print("proccessing inner and outer together {} {} {}".format(param,inside,a))
    inner(30)
    print('outer',a)
    return inner

outer("India")("Asia")  #need might just to call the inner function only once

store=outer("China")

store("Asia")
store("Big Country")
store("Near to India")

print(a)