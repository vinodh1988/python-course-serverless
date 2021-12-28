def resourceHandler(fun):
    def logicController(*args,**kwargs):
        print("Checking the resource and its authenticity")
        print("going to the actuall function to run")
        fun(*args,**kwargs)
        print("Deallocting the memory alloted for the process")
        print("####### Process terminated ###################")
    return logicController