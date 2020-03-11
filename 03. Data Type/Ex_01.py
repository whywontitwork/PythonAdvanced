### 자료형 ( Data Type ) ###

'''

    1) 일반 자료형
        1-1) 부울   ( bool )
        1-2) 정수   ( int )
        1-3) 실수   ( float )
        1-4) 문자   ( str )
        1-5) 문자열 ( str )

    2) 고수준의 자료형

        2-1) 리스트   ( list )
        2-2) 튜플     ( tuple )
        2-3) 딕셔너리 ( dict )
        2-4) 집합     ( set )

'''


# 1-1) 부울 ( bool ) : 참,거짓을 판별하는 논리 자료형
print(True)
print(False)
print(type(True))    # type() : () 안의 자료형을 알려준다.
print("True")        # 다른 데이터
print(type("True"))
print()


# 1-2) 정수 ( int )
print(7)
print(-7)
print(type(7))
print()


# 1-3) 실수 ( float )
print(0.0)
print(-0.7)
print(0.7)
print(type(0.0))
print()


# 1-4) 문자, 문자열 ( str )
print('#')
print("#")
print(type('#'))
print(type("#"))
print()

print('Python')
print("Python")
print(type('Python'))
print(type("Python"))
print()


#@) 문자열을 만드는 4가지 방법
print('string data')       # ''
print("string data")       # ""
print('''string data''')   # ''' '''
print("""string data""")   # """ """
print()

# ''  "" 은 한줄의 문자열만 작성 가능하다.
# print('이름 :
# 나이:
# 생일:')
#
# print("이름 :
# 나이:
# 생일:
# ")

# ''' '''  """ """은 여러줄의 문자열 작성이 가능하다.
print('''이름 : 
나이 :
생일 :
''')

print(""" 이름 :
나이 : 
생일 : 
""")

# 이스케이프 문자
# \n : new line 한줄을 건너 뛴다.
print("testData1\n")
print("testData2")

# \t : tab 만큼 건너 뛴다.
print("testData3\ttestData4")
print()


# 문자열 연산
print("Language" + ": Python")      # 문자열 더하기 => 문자열 이어붙이기
pythonGrade = 100
print("grade : " + str(pythonGrade)) # 문자열로 형변환하여 이어붙인다.
print()

print("=" * 50)                 # 문자열 곱하기 => 문자열 반복하기
print()


# 문자열 인덱싱 : 문자열의 특정 문자의 위치에 접근한다.
personalID = "000101-1234567"
print(personalID)
print(personalID[0])    # 0부터 시작
print(personalID[3])
print(personalID[-1])   # - 는 -1부터 시작 ( -0이 없기때문에 )
print(personalID[-3])
print()


# 문자열 슬라이싱 : 문자열을 특정한 범위로 자른다.
personalID = "000101-1234567"
print(personalID)       # 000101-1234567
print(personalID[:2])   # 00
print(personalID[2:4])  # 01
print(personalID[7:])   # 1234567
print(personalID[:-1])  # 000101-123456
print()


# 문자열 관련 함수
'''
    split 
    replace
    index
    upper
    lower
    strip
    lstrip
    rstrip
'''




