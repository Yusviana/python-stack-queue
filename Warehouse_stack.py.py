#Percobaan 4 : Tumpukan Barang di Sebuah Gudang(Stack)

stack = []

def tambah_barang(stack, barang_baru):
    stack.append(barang_baru)
    print(f"{barang_baru} berhasil ditambahkan ke dalam stack.")

def hapus_barang_terakhir(stack):
    if len(stack) == 0 :
        print("Stack kosong,tidak ada barang yang dapat ditampilkan.")
    else:
        barang_teratas = stack[-1]
        print(f"Barang teratas di dalam stack adalah {barang_teratas}.")

def tampilkan_barang_teratas(stack):
    if len(stack)==0:
        print("Stack kosong,tidak ada barang yanng dapat ditampilkan.")
    else:
        barang_teratas=stack[-1]
        print(f"Barang teratas di dalam stack adalah {barang_teratas}.")
while True:
    print("\nGudang saat ini : ",stack)
    print("Menu:")
    print("1. Tambah Barang")
    print("2. Hapus Barang Terakhir")
    print("3.Tampilkan Barang teratas")
    print("4.Keluar")

    pilihan = input("Masukan pilihan Anda (1/2/3/4): ")

    if pilihan == "1":
        barang_baru = input("Masukan nama barang yang akan ditambahkan : ")
        tambah_barang(stack, barang_baru)
    elif pilihan == "2":
       hapus_barang_terakhir(stack)
    elif pilihan == "3":
        tampilkan_barang_teratas(stack)
    elif pilihan == "4":
        print("Terimakasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silahkan masukan pilihan yang benar.")