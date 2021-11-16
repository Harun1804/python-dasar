# Operator Logika
# not, or, and, xor

# Not
# kebalikan, jika benar maka salah
# jika salah maka benar
a = True
c = not a
print("data a = ",a)
print("data c = ",c)

# Or (Jika salah satu true, maka hasilnya true)
# salah satu benar maka benar
a = True
b = False
c = a or b
print(a,'or',b,'=',c)

# And (Jika keduanya true, maka hasilnya true)
a = True
b = True
c = a and b
print(a,'and',b,'=',c)

# Xor (Akan true jika salah satu true, sisanya false)
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)