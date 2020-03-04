'''
	C점수와 Python 점수와 java점수를 입력받고,
	총점과 평균을 구하여
	총점과 평균을 화면에 출력하고
	평균이 90점 이상이면 1등급
	평균이 80점 이상이면 2등급
	평균이 70점 이상이면 3등급
	평균이 60점 이상이면 4등급
	그 이하는 모두        재시험을
	화면에 출력해 보세요.
'''


python = int(input("# python ? : "))
c = int(input("# c ? : "))
java = int(input("# java ? : "))

total = python + c + java
avg = total / 3

if avg >= 90.0:
    print("총점 : %d , 평균 : %.1f , 등급 : 1등급" % (total,avg))
elif avg >= 80.0:
    print("총점 : %d , 평균 : %.1f , 등급 : 2등급" % (total, avg))
elif avg >= 70.0:
    print("총점 : %d , 평균 : %.1f , 등급 : 3등급" % (total, avg))
elif avg >= 60.0:
    print("총점 : %d , 평균 : %.1f , 등급 : 4등급" % (total, avg))
else:
    print("총점 : %d , 평균 : %.1f , 등급 : 재시험" % (total, avg))