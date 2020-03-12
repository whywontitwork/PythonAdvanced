# pow함수 구현해보기
print(pow(2,5))
print(pow(3,3))
print(pow(4,2))

def my_pow(arg1,arg2):
    result = 1
    for i in range(arg2):
        result *= arg1
    return result

print(my_pow(2,5))
print(my_pow(3,3))
print(my_pow(4,2))