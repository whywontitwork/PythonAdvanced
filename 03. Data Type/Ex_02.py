### 자료형2 ###

'''

    리스트 ( list )
    
    - 복수의 데이터를 묶어서 저장하여 데이터의 저장,유지,사용을
      용이하게 하는 자료구조
    
    [형식]
    리스트명 = [데이터1,데이터2,데이터3,....]
    
    - 타 언어의 배열과는 다릅니다.

'''


# 리스트 생성하기
listDatas1 = []                          # 빈 리스트
listDatas2 = [1, 2, 3, 4, 5]             # 정수 리스트
listDatas3 = [1.1, 2.2, 3.3, 4.4, 5.5]   # 실수 리스트
listDatas4 = ["한놈","두시기","석삼"]    # 문자열 리스트
listDatas5 = [7, 10.10 , "문자열"]       # 복합
listDatas6 = [[1, 2, 3],[4, 5, 6]]       # 중첩 리스트

print(listDatas1)
print(listDatas2)
print(listDatas3)
print(listDatas4)
print(listDatas5)
print(listDatas6)
print()


# 리스트 요소 접근하기
nums = [1, 2, 3, 4, 5]

print(nums)         # 전체
print(nums[0])      # 0번째
print(nums[1])      # 1번째
print(nums[2])      # 2번째
print(nums[3])      # 3번째
print(nums[4])      # 4번째
print()


# 리스트 요소 수정하기
nums = [1,2,3]
print(nums[0])
print(nums[1])
print(nums[2])

nums[0] = 100         # 0번째 값 수정
nums[1] = 200         # 1번째 값 수정
nums[2] = 300         # 2번째 값 수정
print(nums[0])
print(nums[1])
print(nums[2])
print()


# 리스트 요소 삭제하기
nums = [1,2,3]
print(nums)
nums[2] = 0      # 1) 0 혹은 의미없는 데이터 삽입
print(nums)
del nums[2]      # 2) del 키워드를 이용하여 실제로 데이터 삭제
print(nums)
print()


# 리스트 인덱싱
strDatas = ["Python" , "C" , "JAVA" , "C++"]

print(strDatas[0]  , strDatas[-4])  # Python
print(strDatas[1]  , strDatas[-3])  # C
print(strDatas[2]  , strDatas[-2])  # JAVA
print(strDatas[3]  , strDatas[-1])  # C++
print()


# 중첩 리스트 인덱싱
datas = [1,2,['a','b',['Python','is fun!']]]
print(datas)
print(datas[0])
print(datas[1])
print(datas[2])
print(datas[2][0])
print(datas[2][1])
print(datas[2][2])
print(datas[2][2][0])
print(datas[2][2][1])
print()


# 리스트 슬라이싱
nums = [10,20,30,40,50,60,70]

print(nums)
print(nums[:5])    # 0 ~ 4번째(-1) 까지
print(nums[5:])    # 5번째 부터 끝까지
print(nums[2:6])   # 2번째 5번째(-1)까지
print(nums[2:-1])  # 2번째부터 5번째 까지
print()

# 중첩 리스트 슬라이싱
datas = [1,2,3,["Python" , "is fun"],4,5]
print(datas)
print(datas[2:5])
print()


# 리스트 관련 함수
# append() : 추가하기 ( 1개만 가능 , 리스트의 맨뒤에 추가만 가능 )
nums = [1,2,3,4]
print(nums)

nums.append(5)    # 맨위에 5 추가
print(nums)
nums.append(1.5)  # 맨뒤에 1.5 추가
print(nums)
#nums.append(3,4)  # error 단일 데이터만 추가가능
print()


# 삭제하기 1) remove
nums = [1,2,3,4,5,6,7,8,9]
print(nums)
nums.remove(8)      # ()안의 값을 삭제한다. - 8 삭제
print(nums)
nums.remove(5)      # - 5삭제
print(nums)
print()

# 삭제하기 2) pop
nums = [1,2,3,4,5,6,7,8,9]
print(nums)
nums.pop(8)      # ()안의 인덱스를 삭제한다. - 8번째 위치한 9삭제
print(nums)
nums.pop(5)      # - 5번째 위치한 6삭제
print(nums)
print()

# extend, insert, sort, count, index 공부해 보세요.


'''

    2) 튜플 ( tuple ) 
    
    - 튜플의 데이터들의 변화가 불가능하다는 점을 제외하곤
      리스트와 거의 같다.
      
    - 리스트관련 함수가 튜플에는 적용되지 않는다.
    
    [형식]
        튜플명 = (요소1,요소2,요소3)
    
'''


# 튜플 만드는 방법
tuple1 = ()
tuple2 = (1)            # 단일데이터는 튜플이 아니다.
                        # 단일데이터는 예외적으로 다음과 같이 만든다. tuple2 = (1,)
tuple3 = (1,2,3)
tuple4 = 1,2,3          # 예외적으로 변수하나에 여러데이터를 대입하면
                        # 자동적으로 튜플로 만들어서 저장한다.
tuple5 = ([1,2,3],(1,2,3),1,2,3)

print( type(tuple1)  , tuple1 )
print( type(tuple2)  , tuple2 )
print( type(tuple3)  , tuple3 )
print( type(tuple4)  , tuple4 )
print( type(tuple5)  , tuple5 )
print()

# 튜플 요소 수정 ( 수정 불가능 )

tupleDatas = (1,2,3)
#tupleDatas[0] = 100    # 수정 불가
#tupleDatas[1] = 200
#print(tupleDatas)
#print()


# 튜플 요소 제거 ( 제거 불가능 )
tupleDatas = (1,2,3)
#del tupleDatas[0]  # 제거 불가능
#print(tupleDatas)
#print()


# 튜플 인덱싱
strDatas = ("Python" , "C" , "JAVA" , "C++")

print(strDatas[0]  , strDatas[-4])  # Python
print(strDatas[1]  , strDatas[-3])  # C
print(strDatas[2]  , strDatas[-2])  # JAVA
print(strDatas[3]  , strDatas[-1])  # C++
print()


# 튜플 슬라이싱
nums = (10,20,30,40,50,60,70)

print(nums)
print(nums[:5])    # 0 ~ 4번째(-1) 까지
print(nums[5:])    # 5번째 부터 끝까지
print(nums[2:6])   # 2번째 5번째(-1)까지
print(nums[2:-1])  # 2번째부터 5번째 까지
print()


'''

    3) 딕셔너리 (사전)
    
    - 키:벨류 형태로 데이터를 저장하는 자료 구조
    
    [형식]
    변수 = {키1:벨류1 ,키2:벨류2,...}

'''

# 딕셔너리 만들기
#1) 키값에는 리스트와,사전형태를 제외한 자료형이 가능합니다.
dict1 = {1:'python'}
dict2 = {1.1:'python'}
dict3 = {'string' : 'python'}
dict4 = {(1,2,3)  : 'python'}

#dict5 = {[1,2,3] : 'python'}           # error
#dict6 = {{'key':'value'} : 'python'}   # error

print(dict1)
print(dict2)
print(dict3)
print(dict4)
print()


#2) 벨류값은 모든 자료형이 가능합니다.
dict1 = {'keyData' : 1}
dict2 = {'keyData' : 1.1}
dict3 = {'keyData' : 'stringData'}
dict4 = {'keyData' : [1,2,3]}
dict5 = {'keyData' : (1,2,3)}
dict6 = {'keyData' : {"subKeyData":"value"}}

print(dict1)
print(dict2)
print(dict3)
print(dict4)
print(dict5)
print(dict6)
print()


# 딕셔너리 데이터 접근방법
client1 = {"name":"홍길동" , "age":19 , "contact":"010-1234-5678"}

print(client1)
print(client1["name"]    , client1.get("name"))
print(client1["age"]     , client1.get("age"))
print(client1["contact"] , client1.get("contact"))
print()


# 딕셔너리의 요소 추가
client1['height'] = 180.5      #변수명[새로운 키] = 새로운 벨류   형태로 추가
client1['weight'] = 80.5
print(client1)
print()


# 딕셔너리의 요소 수정
client1['contact'] = "010-9876-5432"   #변수명[기존키] = 새로운 벨류
client1['age']     = 29
print(client1)
print()


# 딕셔너리의 요소 삭제
del client1['height']           # del 변수명[기존의 키값]
del client1['weight']
print(client1)
print()


# 딕셔너리 관련 함수
# keys() : 키 리스트 만들기
client1 = { 'name'    : '귀도반로섬',
            'age'     : 20,
            'contact' : '010-1234-1234',
            'grade'   : 'A+' }

print(client1 .keys())
print(type(client1 .keys()))    # dict_keys형태로 반환된다.
print(list(client1.keys()))     # 리스트형태로 형변환 할 경우
                                # 리스트 문법이 적용된다. (추가 작업이 가능)
print()

# values() : value 리스트 만들기
print(client1.values())
print(list(client1.values()))
print()


# items() : 키,벨류 모두 가져오기
print(client1.items())
print()










