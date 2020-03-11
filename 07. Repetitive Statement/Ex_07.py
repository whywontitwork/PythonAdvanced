### enumerate ###

'''

    - for문 안에서 데이터와 인덱스를 동시에 얻을수 있는 구문

    [형식]
    for 인덱스변수, 데이터변수 in enumerate(반복가능객체):
        명령어

'''

datas = ["data1","data2","data3","data4"]

for i,j in enumerate(datas):
    print(i,j)
print()

# 예제 1
datas = [-3,1,5,-5,7,-7,9,10,-343]
for i,j in enumerate(datas):
    if j < 0:
        datas[i] = 0

print(datas)
print()
