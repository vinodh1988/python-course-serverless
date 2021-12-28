# a closure is a function object which remembers values that are stored in enclosing scope

a=889
def outer(param):
    print(param)
    global a
    a=230 #local scope
    print(a)
    def inner(inside):
        print("proccessing inner and outer together {} {} {}".format(param,inside,a))
    print('outer',a)
    return inner

outer("India")("Asia")

store=outer("China")

store("Asia")
store("Big Country")
store("Near to India")

print(a)