from mydecorators import resourceHandler,takeBackup

@resourceHandler
def process(filename):
    print('playing with resources here that is ',filename)
    print('manipulating and writing the resources')

@resourceHandler
def dbactivity(db):
    print('working with db resources of db ',db)
    print('playing with db data')

@takeBackup(location="e:\\takeit")
def dbfun(db):
    print("Performing a db activity of db",db)
    print("playing with db data") 

#process('file name e.txt')
#dbactivity('mysql database')
dbfun("Oracle")