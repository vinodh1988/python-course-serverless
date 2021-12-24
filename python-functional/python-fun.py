def fun(task):
    print('the function is executing ',task)

def doItMyWay(task):
    print('quickly performing ',task)

#taskExecutor is a function which carries a list and function as a parameter
def taskExecutor(mylist,callme):
    for x in mylist:
        print('performing task setup and going to invoke')
        callme(x)
        print('performing the post activities and going to wrap the task')
        print('-------------------------------------')

# the function which is passed as parameter to another function - callback function
taskExecutor(["Building","Compiling","Packing","Deploying"],fun)
taskExecutor(["Building","Compiling","Packing","Deploying"],doItMyWay)