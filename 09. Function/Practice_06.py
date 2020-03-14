# remove함수를 구현해보세요.

def my_remove(datas , value):
    for i,j in enumerate(datas):
        if j == value:
            del datas[i]
    return datas

lis1 = [1,2,3,4,5,6,7,8,9]
print(lis1)

lis1.remove(7)
print(lis1)
print()


lis2 = [1,2,3,4,5,6,7,8,9]
print(lis2)

my_remove(lis2 , 7)
print(lis2)

