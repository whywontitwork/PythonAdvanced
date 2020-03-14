# index 함수를 구현해보세요.
def my_index(datas , value):

    for i,j in enumerate(datas):

        if j == value:

            return i

datas = ["Adele","Maroon5","Sia","Bruno Mars","Psy","]

print(datas.index("Psy"))

res = my_index(datas , "Psy")
print(res)

res = my_index2(datas , "Psy")
print(res)