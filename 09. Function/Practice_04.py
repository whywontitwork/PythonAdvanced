#문자열의 단어의 개수를 반환하는 함수를 구현해보세요.
print(len("abcdefgh"))


def get_count_string(param):
    cnt = 0
    for i in param:
        cnt += 1
    return cnt

print(get_count_string("abcdefgh"))