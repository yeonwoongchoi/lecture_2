def arg_kwarg_param(*args, **kwargs):
    print(len(args))
    print(len(kwargs))
    print(args, kwargs)
    return args, kwargs

#arg_kwarg_param(10,20)
#arg_kwarg_param(10,20, a=30, b=40)
result1, result2 = arg_kwarg_param(10,20, a=30, b=40)
#print(result1)
#print(result2)
result1, result2 = arg_kwarg_param(10,20, a=30, b=40)
print(result2)