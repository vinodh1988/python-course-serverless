def resourceHandler(targetfunction):
    def logicController(*args,**kwargs):  # args and kwargs are params of target function
        print("Checking the resource and its authenticity")
        print("going to the actuall function to run")
        targetfunction(*args,**kwargs)
        print("Deallocting the memory alloted for the process")
        print("####### Process terminated ###################")
    return logicController