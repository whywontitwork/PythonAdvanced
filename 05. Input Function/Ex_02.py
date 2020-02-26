### input함수와 형 변환 ###

'''
    input함수에 저장된 기본 데이터 타입은 문자열(★)
    필요에 따라 input함수로 받은 후에 형변환을 해야 된다.
'''


# pythonGrade = input("# python grade: ")
# javaGrade = input("# java grade: ")
# cGrade = input("# C grade:")
#
# print("총점 : " + pythonGrade + javaGrade + cGrade)


pythonGrade = int(input("# python grade: "))
javaGrade = int(input("# java grade: "))
cGrade = int(input("# C grade:"))

print("총점 : %d" % (pythonGrade + javaGrade + cGrade))
