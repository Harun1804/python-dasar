a = 10
b = 3

# Operasi Tambah
hasil = a + b
print(a,"+",b,"=",hasil)

# Operasi Pengurangan
hasil = a - b
print(a,"-",b,"=",hasil)

# Operasi Perkalian
hasil = a * b
print(a,"*",b,"=",hasil)

# Operasi Pembagian
hasil = a / b
print(a,"/",b,"=",hasil)

# Operasi Exkponen (pangkat)
hasil = a ** b
print(a,"^",b,"=",hasil)

# Operasi modulus (sisa bagi)
hasil = a % b
print(a,"%",b,"=",hasil)

# Operasi floor division (Pembagian dan pembulatan kebawah)
hasil = a // b
print(a,"//",b,"=",hasil)

# Prioritas Operasi, operational precendence
x = 3
y = 2
z = 4

# ()
# exponen
# perkalian / Pembagian / modulus / floor division
# Pertambahan / Pengurangan

hasil = x ** y * z + x / y - y % z // x
print(x,"**",y,"*" ,z ,"+" ,x,"/" ,y, "-" ,y ,"%" ,z ,"//" ,x,"=",hasil)


