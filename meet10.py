# belajar perbandingan lanjutan, ELIF

#nama = input("masukan nama")

#if nama=="azzam":  #kondisi 1
 #   print("mahasiswa")  #aksi true 1
#elif nama=="ilham": #kondisi 2
 #   print("mahasiswa")  #aksi true 2
#elif nama=="yanto": #kondisi 3
 #   print("pekerja")    #aksi true 3
#else:
 #   print("bukan mahasiswa")    #aksi False
#print("perogram selesai")

def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

# Meminta input operasi dari pengguna
operasi = input("Pilih operasi (penjumlahan/pengurangan): ")

# Meminta input angka dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Memilih operasi yang diminta pengguna
if operasi == "penjumlahan":
    hasil = penjumlahan(angka1, angka2)
    print("Hasil penjumlahan:", hasil)
elif operasi == "pengurangan":
    hasil = pengurangan(angka1, angka2)
    print("Hasil pengurangan:", hasil)
else:
    print("Operasi tidak valid. Silakan pilih 'penjumlahan' atau 'pengurangan'.")
