# pop함수를 구현해보세요.

def my_pop(datas,idx):

    del datas[idx]

    return datas



n_datas1 = [1,2,3,4,5]
n_datas2 = [1,2,3,4,5]

print(n_datas1)
n_datas1.pop(1)
print(n_datas1)
print()


print(n_datas2)
my_pop(n_datas2 , 1)
print(n_datas2)








