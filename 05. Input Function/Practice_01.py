'''

    8 bit     = 1 byte
    1024 byte = 1 kilo byte
    1024 kilo = 1 mega byte
    1024 mega = 1 giga byte
    1024 giga = 1 tera byte

'''

teraByte = int(input("# input tera byte: "))
gigaByte = teraByte * 1024
megaByte = gigaByte * 1024
kiloByte = megaByte * 1024
byte     = kiloByte * 1024
bit      = byte * 8

print("tera : %d" % teraByte)
print("giga : %d" % gigaByte)
print("mega : %d" % megaByte)
print("kilo : %d" % kiloByte)
print("byte : %d" % byte)
print("bit  : %d" % bit)