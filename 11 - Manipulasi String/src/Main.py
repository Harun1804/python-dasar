# Operasi dan manipulasi string

# 1. Menyambung string(concatenate)

namaPertama = "Harun "
namaTengah = "Ar - "
namaAkhir = "Rasyid"
namaLengkap = namaPertama + namaTengah + namaAkhir
print(namaLengkap)

# 2. Menghitung panjang string
panjang = len(namaLengkap)
print("panjang dari "+namaLengkap + " = "+ str(panjang))

# 3. Operator untuk string
# mengecek apakah ada komponen char atau string di string

d = "d"
status = d in namaLengkap
print(status)

# Mengulang String
print("wk"*10)

# indexing
print("index ke-0 : "+namaLengkap[0])
print("index ke-(-1) : "+namaLengkap[-1])
print("index ke-[0:3] : "+namaLengkap[0:3])
print("index ke-[0,2,4,6] : "+namaLengkap[0:10:2])

# Item Paling Kecil
print("Paling Kecil : "+min(namaLengkap))
# Item Paling Besar
print("Paling Besar : "+max(namaLengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah "+str(ascii_code))
data = 117
print("Char Untuk ASCII 117 adalah "+chr(data))

# 4. Operator dalam bentuk method
data = "otong surotong parotong"
jumlah = data.count("o")
print(jumlah) 

# merubah case dari string
## merubah semua ke upper case
salam = "bro!"
print("normal = " +salam)
salam = salam.upper()
print("Uppercase = " +salam)

## Merubah semua ke lower case
alay = "AkU KeCe AbIs"
print("normal = " +alay)
alay = alay.lower()
print("lower = "+alay)

# pengecekan dengan isX method
## pengecekan lower case
salam = "sist"
apakah_lower = salam.islower()
print(salam," is lower "+str(apakah_lower))
apakah_upper = salam.isupper()
print(salam," is upper "+str(apakah_lower))

# isalpha() <- untuk mengecek semuanya huruf
# isnum() <- untuk mengecek huruf dan angka
# isdecimal() <- untuk mengecek angka
# isspace() <- spasi, tab, newline \n
# istitle() <- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title =" + str(cek_judul))

# mengecekan komponen startswith() endswith() <-- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = "+str(cek_start))

cek_end = "Sangjangnim Oppa".endswith("Oppa")
print("end = "+str(cek_start))

# pengabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabung = ', '.join(pisah)
print(pisah)
print(gabung)

pecah = ",".split(gabung)
print(pecah)

## ALokasi Karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")
kiri = "kiri".ljust(10)
print("'"+kiri+"'")
tengah = "tengah".center(20,"-")
print("'"+tengah+"'")

## kebalikannya --> strip()
tengah = tengah.strip("-")
print("'"+tengah+"'")

