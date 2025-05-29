import os
import pandas as pd
import csv
from tabulate import tabulate

keranjang_belanja = []

def TampilanSelamatDatang():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#======================================================#")
    print("#                                                      #")
    print("#                 SELAMAT DATANG DI                    #")
    print("#                 TOKO SAHABAT TANI                    #")
    print("#                                                      #")
    print("#     Nikmati pengalaman belanja yang mudah dan        #")
    print("#              terpercaya bersama kami!                #")
    print("#                                                      #")
    print("#======================================================#")
    print("#                                                      #")
    print("#       Tekan [ENTER] untuk memulai belanja!           #")
    print("#                                                      #")
    print("#======================================================#")
    input("")

def MenuUtama():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#======================================================#")
    print("#                 MENU TOKO SAHABAT TANI               #")
    print("#======================================================#")
    print("# 1. Login                                             #")
    print("# 2. Register                                          #")
    print("# 3. Logout                                            #")
    print("#======================================================#")
    
    pilihan = input("Pilih menu (1-3): ")
    if pilihan == "1":
        Login()
    elif pilihan == "2":
        Register()
    elif pilihan == "3":
        TampilanAkhir()  
        exit()
    else:
        print("Pilihan tidak valid.")
        input("Tekan Enter... ")
        MenuUtama()

def Login():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#======================================================#")
    print("#                     LOGIN PAGE                       #")
    print("#======================================================#")
    print("#            MASUKKAN USERNAME & PASSWORD              #")
    print("#======================================================#")

    if not os.path.isfile("Users.csv"):
        print("Belum ada akun yang terdaftar. Silakan register terlebih dahulu.")
        input("Tekan Enter untuk kembali ke menu utama...")
        MenuUtama()

    print("Pilih jenis akun:")
    print("1. Admin")
    print("2. Pembeli")
    print("3. Kembali ke Menu Utama")
    pilihan = input("Masukkan pilihan (1/2/3): ").strip()

    if pilihan == "1":
        jenis_akun = "Admin"
    elif pilihan == "2":
        jenis_akun = "Pembeli"
    elif pilihan == "3":
        MenuUtama()
        return
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        input("Tekan Enter untuk melanjutkan...")
        return Login()

    print("\nMasukkan data login Anda:")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if jenis_akun == "Admin":
        if username == "rizqi" and password == "rizqi":
            print(f"\nSelamat Datang, {username} ({jenis_akun})!")
            input("\nTekan Enter untuk melanjutkan... ")
            TampilanMenuAdmin()
            return
        else:
            print("\nHanya admin yang dapat login.")
            input("Tekan Enter untuk mencoba lagi... ")
            Login()
            return

    with open("Users.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 3 and row[0] == username and row[1] == password and row[2] == jenis_akun:
                print(f"\nSelamat Datang, {username} ({jenis_akun})!")
                input("\nTekan Enter untuk melanjutkan... ")
                TampilanMenuPembeli()
                return
            
    print("\nUsername, Password, atau jenis akun salah.")
    input("Tekan Enter untuk mencoba lagi... ")
    Login()
  
def Register():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#======================================================#")
    print("#                   REGISTER PAGE                      #")
    print("#======================================================#")
    print("#            MASUKKAN USERNAME & PASSWORD              #")
    print("#======================================================#")

    print("1. Daftar Akun Baru")
    print("2. Kembali ke Menu Utama")

    pilihan = input("Masukkan pilihan (1/2): ").strip()

    if pilihan == "2":
        MenuUtama()  
        return
    elif pilihan == "1":
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()

        if not username or not password:
            print("Username dan password tidak boleh kosong.")
            input("Tekan Enter untuk mencoba lagi... ")
            Register()  

        jenis_akun = "Pembeli"  
        cek_file = os.path.isfile("Users.csv")
        with open("Users.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if not cek_file:
                writer.writerow(["Username", "Password", "JenisAkun"])
            writer.writerow([username, password, jenis_akun])

        print("Akun berhasil didaftarkan.")
        input("Tekan Enter untuk kembali ke menu utama... ")
        MenuUtama()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        input("Tekan Enter untuk melanjutkan... ")
        Register()
    
def TampilanMenuAdmin():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#======================================================#")
    print("#                 DASHBOARD ADMIN                      #")
    print("#======================================================#")
    print("# 1. Tambah Produk                                     #")
    print("# 2. Lihat Produk                                      #")
    print("# 3. Update Stok Produk                                #")  
    print("# 4. Hapus Produk                                      #")
    print("# 5. Logout                                            #")
    print("#======================================================#")

    pilihan = input("Pilih menu (1-5): ")
    if pilihan == "1":
        TambahkanProduk()
    elif pilihan == "2":
        LihatProduk()
    elif pilihan == "3":  
        UpdateStokProduk()
    elif pilihan == "4":
        HapusProduk()
    elif pilihan == "5":
        print("Logout berhasil.")
        input("Tekan Enter untuk kembali ke menu utama... ")
        MenuUtama()
    else:
        print("Pilihan tidak valid.")
        input("Tekan Enter... ")
        TampilanMenuAdmin()

def TambahkanProduk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Tambah Produk ===")
    try:
        NamaProduk = input("Nama Produk: ").capitalize()
        Kategori = input("Kategori: ").capitalize()
        HargaPerUnit = float(input("Harga per unit (Rp): "))
        Stok = int(input("Jumlah Stok: "))
        cek_file = os.path.isfile("DaftarProduk.csv")
        with open("DaftarProduk.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if not cek_file:
                writer.writerow(["NamaProduk", "Kategori", "HargaPerUnit", "Stok"])
            writer.writerow([NamaProduk, Kategori, HargaPerUnit, Stok])
        print("Produk berhasil ditambahkan.")
    except ValueError:
        print("Input harga dan stok harus berupa angka.")
    input("Tekan Enter untuk melanjutkan... ")
    TampilanMenuAdmin()
    
def UpdateStokProduk():
    while True:  
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== Update Stok Produk ===")
        
        if os.path.isfile("DaftarProduk.csv"):
            data = pd.read_csv("DaftarProduk.csv")
            
            if data.empty:
                print("Tidak ada produk yang tersedia.")
            else:
                data['Stok'] = data['Stok'].fillna(0).apply(lambda x: int(x) if str(x).isdigit() else 0)

                print(tabulate(data, headers="keys", tablefmt="grid"))
                
                try:
                    index_update = int(input("Masukkan indeks produk yang ingin diupdate stoknya: "))
                    
                    if 0 <= index_update < len(data):
                        produk = data.iloc[index_update]
                        print(f"\nProduk yang dipilih: {produk['NamaProduk']}")
                        print(f"Stok saat ini: {produk['Stok']}")
                        
                        jenis_update = input("Pilih jenis update (tambah/kurang): ").strip().lower()
                        if jenis_update not in ['tambah', 'kurang']:
                            print("Pilihan tidak valid. Gunakan 'tambah' atau 'kurang'.")
                            continue 
                        
                        jumlah_update = int(input("Masukkan jumlah stok yang ingin diupdate: "))
                        if jumlah_update < 0:
                            print("Jumlah update tidak boleh negatif.")
                            continue  
                        
                        if jenis_update == 'tambah':
                            data.at[index_update, 'Stok'] += jumlah_update
                            print(f"Stok {produk['NamaProduk']} berhasil ditambahkan sebanyak {jumlah_update}")
                        else:
                            if jumlah_update > produk['Stok']:
                                print("Jumlah pengurangan melebihi stok yang tersedia.")
                                continue  
                            data.at[index_update, 'Stok'] -= jumlah_update
                            print(f"Stok {produk['NamaProduk']} berhasil dikurangi sebanyak {jumlah_update}")
                        
                        data.to_csv("DaftarProduk.csv", index=False)
                        print("Stok produk berhasil diperbarui.")
                    else:
                        print("Indeks tidak valid.")
                
                except ValueError:
                    print("Masukkan angka yang valid.")
            
            lanjutkan = input("\nApakah Anda ingin mengupdate stok produk lain? (y/n): ").strip().lower()
            if lanjutkan != 'y':
                break  
        else:
            print("File produk tidak ditemukan.")
            break  
    
    input("Tekan Enter untuk kembali ke menu... ")
    TampilanMenuAdmin()  

def LihatProduk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Daftar Produk ===")
    if os.path.isfile("DaftarProduk.csv"):
        data = pd.read_csv("DaftarProduk.csv")
        if data.empty:
            print("Tidak ada produk yang tersedia.")
        else:
            print(tabulate(data, headers="keys", tablefmt="grid"))
    else:
        print("File produk tidak ditemukan.")
    input("Tekan Enter untuk kembali ke menu... ")
    TampilanMenuAdmin()

def HapusProduk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Hapus Produk ===")
    
    if os.path.isfile("DaftarProduk.csv"):
        data = pd.read_csv("DaftarProduk.csv")
        
        if data.empty:
            print("Tidak ada produk yang bisa dihapus.")
        else:
            print(tabulate(data, headers="keys", tablefmt="grid"))
            
            try:
                index_hapus = int(input("Masukkan indeks produk yang ingin dihapus: "))
                if 0 <= index_hapus < len(data):
                    data_list = data.to_dict('records')
                    data_list.pop(index_hapus)
                    data = pd.DataFrame(data_list)
                    data.to_csv("DaftarProduk.csv", index=False)
                    print("Produk berhasil dihapus.")
                else:
                    print("Indeks tidak valid.")
            except ValueError:
                print("Masukkan angka yang valid.")
    else:
        print("File produk tidak ditemukan.")
    
    input("Tekan Enter untuk kembali ke menu... ")
    TampilanMenuAdmin()

def TampilanMenuPembeli():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("#======================================================#")
        print("#                 DASHBOARD PEMBELI                    #")
        print("#======================================================#")
        print("# 1. Lihat Produk                                      #")
        print("# 2. Tambah Ke Keranjang                               #")
        print("# 3. Checkout                                          #")
        print("# 4. Riwayat Pembelian                                 #")
        print("# 5. Logout                                            #")
        print("#======================================================#")

        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            LihatProdukPembeli()
        elif pilihan == "2":
            TambahKeranjang()
        elif pilihan == "3":
            Checkout()
        elif pilihan == "4":
            RiwayatPembelian()
        elif pilihan == "5":
            print("Logout berhasil.")
            input("Tekan Enter untuk kembali ke menu utama... ")
            MenuUtama()  
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter... ")
        
def LihatProdukPembeli():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Daftar Produk ===")
    if os.path.isfile("DaftarProduk.csv"):
        data = pd.read_csv("DaftarProduk.csv")
        if data.empty:
            print("Tidak ada produk yang tersedia.")
        else:
            print(tabulate(data, headers="keys", tablefmt="grid"))
    else:
        print("File produk tidak ditemukan.")
    input("Tekan Enter untuk kembali ke menu... ")
    TampilanMenuPembeli()

def TambahKeranjang():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Tambahkan ke Keranjang ===")
    
    if not os.path.isfile("DaftarProduk.csv"):
        print("File produk tidak ditemukan.")
        input("Tekan Enter untuk kembali ke menu...")
        TampilanMenuPembeli()
        return

    data = pd.read_csv("DaftarProduk.csv")
    
    data["HargaPerUnit"] = pd.to_numeric(data["HargaPerUnit"], errors="coerce")
    data["Stok"] = pd.to_numeric(data["Stok"], errors="coerce")
    
    if data.empty:
        print("Tidak ada produk yang tersedia.")
        input("Tekan Enter untuk kembali ke menu...")
        TampilanMenuPembeli()
        return

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(tabulate(data, headers="keys", tablefmt="grid"))

        try:
            index_pilih = int(input("Masukkan indeks produk yang ingin ditambahkan ke keranjang: "))
            
            if 0 <= index_pilih < len(data):
                produk = data.iloc[index_pilih]
                
                if produk['Stok'] <= 0:
                    print("Produk habis. Tidak dapat menambahkan produk ini ke keranjang.")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                
                jumlah = int(input(f"Masukkan jumlah (stok tersedia: {produk['Stok']}): "))
                
                if 0 < jumlah <= produk['Stok']:
                    keranjang_belanja.append({
                        "NamaProduk": produk["NamaProduk"],
                        "Jumlah": jumlah,
                        "HargaPerUnit": produk["HargaPerUnit"],
                        "TotalHarga": produk["HargaPerUnit"] * jumlah  
                    })
                    
                    data.at[index_pilih, 'Stok'] -= jumlah
                    data.to_csv("DaftarProduk.csv", index=False)
                    
                    print("Produk berhasil ditambahkan ke keranjang.")
                    
                else:
                    print("Jumlah tidak valid. Harus lebih dari 0 dan tidak melebihi stok tersedia.")
            else:
                print("Indeks tidak valid.")
        
        except ValueError:
            print("Masukkan angka yang valid.")
        
        lanjutkan = input("Apakah Anda ingin menambahkan produk lain ke keranjang? (y/n): ").strip().lower()
        if lanjutkan != 'y':
            break

    input("Tekan Enter untuk kembali ke menu...")
    TampilanMenuPembeli()

def Checkout():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Checkout ===")
    
    if keranjang_belanja:
        total_bayar = sum(item["TotalHarga"] for item in keranjang_belanja)
        print(tabulate(keranjang_belanja, headers="keys", tablefmt="grid"))
        print(f"Total yang harus dibayar: Rp {total_bayar:,}")
        
        alamat = input("Masukkan alamat pengiriman: ").strip()
        if not alamat:
            print("Alamat tidak boleh kosong.")
            input("Tekan Enter untuk kembali... ")
            return Checkout()

        print("\nPilih metode pembayaran:")
        print("1. Transfer Bank")
        print("2. Cash On Delivery (COD)")
        metode_pembayaran = input("Masukkan pilihan (1/2): ").strip()
        
        if metode_pembayaran == "1":
            metode_pembayaran = "Transfer Bank"
        elif metode_pembayaran == "2":
            metode_pembayaran = "Cash On Delivery (COD)"
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali...")
            return Checkout()

        konfirmasi = input("Konfirmasi pembelian? (y/n): ").strip().lower()
        if konfirmasi == "y":
            cek_file = os.path.isfile("RiwayatPembelian.csv")
            with open("RiwayatPembelian.csv", "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                if not cek_file or os.stat("RiwayatPembelian.csv").st_size == 0:
                    writer.writerow(["NamaProduk", "Jumlah", "HargaPerUnit", "TotalHarga", "Alamat", "MetodePembayaran", "Status"])
                for item in keranjang_belanja:
                    writer.writerow([
                        item["NamaProduk"], 
                        item["Jumlah"], 
                        item["HargaPerUnit"], 
                        item["TotalHarga"], 
                        alamat, 
                        metode_pembayaran, 
                        "Berhasil"
                    ])
            print("Pembelian berhasil.")
            keranjang_belanja.clear() 
        else:
            print("Checkout dibatalkan.")
    else:
        print("Keranjang belanja kosong.")
    
    input("Tekan Enter untuk kembali ke menu... ")
    TampilanMenuPembeli()

def RiwayatPembelian():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Riwayat Pembelian ===")
    
    if os.path.isfile("RiwayatPembelian.csv"):
        data = pd.read_csv("RiwayatPembelian.csv")  
        if data.empty:
            print("Belum ada riwayat pembelian.")
        else:

            print(tabulate(data, headers='keys', tablefmt='grid', showindex=False))
    else:
        print("Belum ada riwayat pembelian.")
    
    input("\nTekan Enter untuk kembali ke menu pembeli... ")
    TampilanMenuPembeli()

def TampilanAkhir():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#======================================================#")
    print("#                                                      #")
    print("#        TERIMA KASIH TELAH BERBELANJA DI TOKO         #")
    print("#                   SAHABAT TANI                       #")
    print("#                                                      #")
    print("#======================================================#")
    print("#          Kami Menantikan Kunjungan Anda              #")
    print("#                                                      #")
    print("#                 SEMOGA HARI ANDA                     #")
    print("#                    MENYENANGKAN                      #")
    print("#======================================================#")

    input("Tekan Enter untuk keluar...")
    
TampilanSelamatDatang()
MenuUtama()
