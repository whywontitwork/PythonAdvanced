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


# 리스트 슬라이싱
nums = [10,20,30,40,50,60,70]

print(nums)
print(nums[:5])    # 0 ~ 4번째(-1) 까지
print(nums[5:])    # 5번째 부터 끝까지
print(nums[2:6])   # 2번째 5번째(-1)까지
print(nums[2:-1])  # 2번째부터 5번째 까지
print()

