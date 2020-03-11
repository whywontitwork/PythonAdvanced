### 다중 오류,예외처리 ###

datas = [2, 'f' , 0]

try:
    res = 4 / datas[0]   #datas[0]부터 3까지 바꿔가면서 해보세요.
    print(res)
except TypeError:
    print("에러코드 ( 숫자와 문자를 연산할 수 없습니다. )")
except ZeroDivisionError:
    print("에러코드 ( 0으로 나눌 수 없습니다. )")
except IndexError:
    print("에러코드 ( 리스트의 범위를 확인해 주세요. )")
except:
    print("에러코드")