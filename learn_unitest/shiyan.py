def printmsg(*args):
    print(args)
printmsg([{'a':1,'b':2,'expected':3},{'a':3,'b':-2,'expected':1}])
printmsg(*[{'a':1,'b':2,'expected':3},{'a':3,'b':-2,'expected':1}])