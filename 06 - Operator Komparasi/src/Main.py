# Operator Komparasi
# >,<,>=,<=,==,!=,is,is not

a = 4
b = 5
# Lebih Dari
hasil = a > 3
print(a,'>',3,'=',hasil)

# Kurang Dari
hasil = a < 3
print(a,'<',3,'=',hasil)

# Lebih Dari Samadengan
hasil = a >= 3
print(a,'>=',3,'=',hasil)

# Kurang Dari Samadengan
hasil = a <= 3
print(a,'<=',3,'=',hasil)

# Samadengan
hasil = a == 3
print(a,'==',3,'=',hasil)

# Tidak Samadengan
hasil = a != 3
print(a,'!=',3,'=',hasil)

# is digunakan untuk membandinghkan memory
x = 5
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is y
print(x,'is',y,'=',hasil)

# is not
x = 5
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is not y
print(x,'is',y,'=',hasil)