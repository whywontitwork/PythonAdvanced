# count 함수를 구현해보세요.

def my_count(datas,value):

    cnt = 0
    for i in datas:
        if i == value:
            cnt += 1
    return cnt


lis1 = [1,2,3,1,1,1,1,2,3,4,5,2]

print(lis1.count(1))
print(lis1.count(2))
print()

print(my_count(lis1,1))
print(my_count(lis1,2))