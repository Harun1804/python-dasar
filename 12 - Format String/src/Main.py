# Format String

# contoh generic
nama = "lala"
format_str = f"hello {nama}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# Bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000
format_str = f"ribuan = {angka:,}"

# bilangan desimal
angka = 2005.5
format_str = f"desimal = {angka:.2f}"
print(format_str)

# bilangan leading zero
angka = 2005.5
format_str = f"desimal = {angka:09.2f}"
print(format_str)

# Menampilakn tanda + atau -
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus}"
format_plus = f"plus = {angka_plus:+d}"
print(format_minus)
print(format_plus)

# memformat persen
pesen = 0.045
format_persen = f"persen = {pesen:.2%}"
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5
format_str = f"harga total = Rp. {harga * jumlah}"
print(format_str)

# format angka lain (binary,oktal,hex)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexa = f"hex = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hexa)