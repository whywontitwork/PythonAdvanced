### 모듈을 사용하는 다양한 방법 ###
'''

    1) import 모듈명
    2) import 모듈명 as 별명
    3) from 모듈명 import 모듈의 변수, 모듈의함수, 모듈의 클래스
    4) from 모듈명 import *

'''

#1) import 모듈명
#     > 모듈명.변수 , 모듈명.함수  , 모듈명.클래스
import myModule
print(myModule.iVar)
print(myModule.fVar)
print(myModule.strVar)
print()

myModule.func1()
myModule.func2()
print()

myModule.cls1()
myModule.cls2()
print("\n\n")

#2) import 모듈명 as 별명
#     > 별명.변수 , 별명.함수 , 별명.클래스

import myModule as md
print(md.iVar)
print(md.fVar)
print(md.strVar)
print()

md.func1()
md.func2()
print()

md.cls1()
md.cls2()
print()

