# 논리 연산자

'''
논리 and : 좌우변이 모두 참일 때만 참
           그렇지 않을 경우 모두 거짓

논리 or  : 좌우변중 하나라도 참일 경우 참
           좌우변이 모두 거짓일 때 거짓

논리 not : 참 -> 거짓  , 거짓 -> 참 변환

'''

data1 = 100
data2 = 99

# True and True = True
print(data1 == 100 and data2 == 99)

#True and False = False
print(data1 == 100 and data2 != 99)

#False and True = False
print(data1 != 100 and data2 == 99)

#False and False = False
print(data1 != 100 and data2 != 99)
print()



# True or True = True
print(data1 == 100 or data2 == 99)

#True or False = True
print(data1 == 100 or data2 != 99)

#False or True = True
print(data1 != 100 or data2 == 99)

#False or False = False
print(data1 != 100 or data2 != 99)
print()

print( data1 == 100 )    # True
print(not(data1 == 100)) # True -> False

print( data1 != 100)      # False
print( not(data1 != 100)) # False -> True
