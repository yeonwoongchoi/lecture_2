def get_root(a,b,c):
    x1 = (-b +(b**2-4*a*c)**(1/2))/(2*a)
    x2 = (-b -(b**2-4*a*c)**(1/2))/(2*a)
    return x1,x2

#한반에 전체를 반환받는법
root = get_root(1,5,6)
print(root)

#각각을 따로 따로 변환 받는법
root1, root2 = get_root(1,5,c=6)
print('r1값은', root1)
print('r2값은', root2)

#위치인자와 키워드 인자를 혼합하는 경우 반드시 위치 인자 뒤에 키워드 인자가 와야한다.
