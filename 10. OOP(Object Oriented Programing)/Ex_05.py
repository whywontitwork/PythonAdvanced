### 클래스의 속성 ###

class propertyEx:
    publicVar   = "공개 속성 변수"    # 클래스 내부,외부에서 다 보입니다.
    # 변수명 앞에 __를 붙이면 비공개 속성 변수
    __privateVar = "비공개 속성 변수" # 클래스 외부에서는 보이지 않습니다.

    def publicMethod(self):           # 클래스 내부,외부에서 다 보입니다.
        print("공개 속성 메소드 :)")
    # 메소드명 앞에 __를 붙이면 비공개 속성 메소드
    def __privateMethod(self):        # 클래스 외부에서는 보이지 않습니다.
        print("비공개 속성 메소드 :)")
    def printVars(self):
        print("\n--- 변수 ---")
        print(self.publicVar)
        print(self.__privateVar)
        print("\n--- 메소드 ---")
        self.publicMethod()
        self.__privateMethod()


obj = propertyEx()
print(obj.publicVar)
#print(obj.__privateVar)   # 접근 불가

obj.publicMethod()
#obj.__privateMethod()     # 접근 불가
obj.printVars()