def foo(*args):
    print('인자의 갯수' , len(args))
    print('인자는: ', args)


#foo(10,20,30,40)
foo(a=10, b=20, c=30, d=40)