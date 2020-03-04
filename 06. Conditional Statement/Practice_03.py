year = int(input("# year ? : "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("%d년은 '윤년'입니다." % year)

else:
    print("%d년은 '평년'입니다." % year)




