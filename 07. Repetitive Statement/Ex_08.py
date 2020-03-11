### 리스트 안 for문 ###

'''

    - for문을 기준으로 오른쪽 부분은 데이터 생성 부분
    - 왼쪽부분은 리스트에 저장되는 데이터 부분

'''


datas = []
for i in range(1,51):
    datas.append(i)
print(datas)

datas2 = [i for i in range(1,51)]
print(datas2)


datas = []
for i in range(1,51):
    datas.append(i*10)
print(datas)


datas3 = [i*10 for i in range(1,51)]
print(datas3)



