# Data Yang Diinputkan pasti String
data = input("Masukan Data : ")
print("data = ",data," - type : ",type(data))

# Jika ingin mengambil data int / float
data_float = float(input("Masukan Angka : "))
data_int = int(input("Masukan Angka : "))

# Jika Boolean
data_bool = bool(int(input("Masukan Nilai Boolean : ")))
print("data = ",data_bool," - type : ",type(data_bool))