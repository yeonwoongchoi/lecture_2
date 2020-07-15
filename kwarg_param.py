def kwarg_param(**kwargs):
    print('인자의 갯수' , len(kwargs))
    print('인자는: ', kwargs)
    #print('key값은:' , kwargs.keys)
kwarg_param(first = 'a', second ='b'
, third='c')