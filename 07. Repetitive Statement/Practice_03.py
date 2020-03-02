
answer = 77

while True:
    getAnswer = int(input("# 정답 : "))
    if getAnswer == answer:
        print("정답")
        break
    elif getAnswer > answer:
        print("다운")
    elif getAnswer < answer:
        print("업")
