from functools import wraps

def takeBackup(location="d:\\backup"):
    def targetouter(targetfun):
        @wraps(targetfun)
        def inner(*args,**kwargs):
            targetfun(*args,**kwargs)
            print("Taking backup of the resources in the location",location)
        return inner
    return targetouter
