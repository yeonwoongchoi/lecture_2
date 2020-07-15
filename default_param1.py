def div(a, b = 2):
    return a / b
print('div(4) =',div(4))
# 위치인자로 넣은 결과
print('div(200 , 5) =',div(200, 5))

#위치인자와키워드 인자를 혼용
print('div(200 , b=5) =',div(200, b=5))
print('div(a=200 , b=5) =',div(a=200, b=5))
print('div(b=5 , a=200) =',div(b=5, a=200))

# div() got an unexpected keyword argument 'bc'
# print('div(bc=5 , ac=200) =',div(bc=5, ac=200))

# SyntaxError: positional argument follows keyword argument
# print('div(b=5 , a=200) =',div(b=5, a=200))