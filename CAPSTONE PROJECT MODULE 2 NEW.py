# Capstone Project Module 2 Zafira Putri Suerman - Rental Mobil (RENT & GO)
from tabulate import tabulate
# pip install tabulate

kodeMobil = ["M001", "M002", "M003", "M004", "M005"]
merkMobil = ["Toyota", "Honda", "Suzuki", "Nissan", "Mitsubishi"]
tipeMobil = ["Avanza", "Civic", "Ertiga", "X-Trail", "Pajero"]
kategoriMobil = ["MPV", "Sedan", "Hatchback", "SUV", "SUV"]
tahunMobil = [2020, 2019, 2021, 2018, 2020]
hargaSewa = [300000, 250000, 200000, 400000, 450000]
statusMobil = ["Available", "Available", "Rented", "Maintenance", "Available"]

kategoriValid = ["MPV", "Sedan", "Hatchback", "SUV"]
statusValid = ["Available", "Rented", "Maintenance"]


# =========================================
# MENU UTAMA 
# =========================================

def menuUtama():
    while True:
        print("\n=======WELCOME TO RENTAL & GO =======")
        print("""
List Menu:
1. Read Data
2. Create Data
3. Update Data
4. Delete Data
5. Rental Menu
6. Statistik Data Mobil
7. Exit Program
""")

        pilih = input("Masukkan angka Menu yang ingin dijalankan: ")

        # opsi 1 - buka menu Read (liat data mobil)
        if pilih == "1":
            menuRead()

        # opsi 2 - buka menu Create (tambah data mobil)
        elif pilih == "2":
            menuCreate()    

        # opsi 3 - buka menu Update (ubah data mobil)
        elif pilih == "3":
            menuUpdate()

        # opsi 4 - buka menu Delete (hapus data mobil)
        elif pilih == "4":
            menuDelete()    

        # opsi 5 - buka menu Rental (sewa mobil)
        elif pilih == "5":
            menuRental()

        # opsi 6 - buka menu Statistik (lihat statistik data mobil)
        elif pilih == "6":
            tampilStatistik()

        # opsi 7 - keluar dari program
        elif pilih == "7":
            print("Terima kasih telah mengunjungi RENTAL & GO. Sampai jumpa lagi!")
            print("Semoga hari anda menyenangkan. Kami tunggu kedatangan anda kembali!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

# =================================================================================================
# FUNGSI BANTU - validasi input angka agar user tidak memasukkan huruf untuk data tahun dan harga
# =================================================================================================

def inputAngka(teks):
    while True:
        nilai = input(teks)
        if nilai.isdigit():
            return int(nilai)
        print("Input harus angka positif, coba lagi") 


# ===========================================================================
# FUNGSI cek status yang diketik user cocok atau tidak dengan daftar status 
# ===========================================================================

def cekStatus(teks):
    hasil = None
    for v in statusValid:
        if teks.strip().upper() == v.upper():
            hasil = v
    return hasil

# =======================================================================================
# FUNGSI mencari posisi index mobil berdasarkan kode, dipakai di hampir semua menu CRUD
# =======================================================================================

def cariIndex(kode):
    idx = -1
    for i in range(len(kodeMobil)):
        if kodeMobil[i] == kode:
            idx = i
    return idx


# ===============================================================================
# FUNGSI cek kategori yang diketik user cocok atau tidak dengan daftar kategori 
# ===============================================================================

def cekKategori(teks):
    hasil = None
    for v in kategoriValid:
        if teks.strip().upper() == v.upper():
            hasil = v
    return hasil


# ==========================================================================================================
# FITUR SORTING  untuk mengurutkan data mobil pakai sort manual, bisa berdasarkan harga, tahun, atau merk
# ==========================================================================================================

def urutkanData(mode):
    n = len(kodeMobil)
    for i in range(n):
        for j in range(0, n - i - 1):
            tukar = False
            if mode == "harga_murah":
                if hargaSewa[j] > hargaSewa[j + 1]:
                    tukar = True
            elif mode == "harga_mahal":
                if hargaSewa[j] < hargaSewa[j + 1]:
                    tukar = True
            elif mode == "tahun_baru":
                if tahunMobil[j] < tahunMobil[j + 1]:
                    tukar = True
            elif mode == "tahun_lama":
                if tahunMobil[j] > tahunMobil[j + 1]:
                    tukar = True
            elif mode == "merk_az":
                if merkMobil[j] > merkMobil[j + 1]:
                    tukar = True

            if tukar == True:
                kodeMobil[j], kodeMobil[j + 1] = kodeMobil[j + 1], kodeMobil[j]
                merkMobil[j], merkMobil[j + 1] = merkMobil[j + 1], merkMobil[j]
                tipeMobil[j], tipeMobil[j + 1] = tipeMobil[j + 1], tipeMobil[j]
                kategoriMobil[j], kategoriMobil[j + 1] = kategoriMobil[j + 1], kategoriMobil[j]
                tahunMobil[j], tahunMobil[j + 1] = tahunMobil[j + 1], tahunMobil[j]
                hargaSewa[j], hargaSewa[j + 1] = hargaSewa[j + 1], hargaSewa[j] 
                statusMobil[j], statusMobil[j + 1] = statusMobil[j + 1], statusMobil[j]


# =================================================================
# FUNGSI menampilkan data ke layar menggunakan tabulate biar rapi 
# =================================================================

def cetakTabel(baris):
    print(tabulate(tabular_data=baris,
                    headers=["Kode", "Merk", "Tipe", "Kategori", "Tahun", "Harga Sewa", "Status"], 
                    tablefmt="heavy_grid"))    


def cetakTabelSewa(baris):
    print(tabulate(tabular_data=baris,
                    headers=["Kode", "Merk", "Tipe", "Harga Sewa"], 
                    tablefmt="heavy_grid"))


def cetakSemua():
    gabung = list(zip(kodeMobil, merkMobil, tipeMobil, kategoriMobil, tahunMobil, hargaSewa, statusMobil))
    print()
    cetakTabel(gabung)


# ========================================================================================================================
# FITUR STATISTIK DATA MOBIL- menghitung jumlah total mobil dan breakdown per status (Available/Booked/Rented/Maintenance)
# ========================================================================================================================

def tampilStatistik():
    total = len(kodeMobil)
    jmlAvailable = 0
    jmlBooked = 0
    jmlRented = 0
    jmlMaintenance = 0

    for s in statusMobil:
        if s == "Available":
            jmlAvailable = jmlAvailable + 1
        elif s == "Booked":
            jmlBooked = jmlBooked + 1
        elif s == "Rented":
            jmlRented = jmlRented + 1
        elif s == "Maintenance":
            jmlMaintenance = jmlMaintenance + 1

    dataStatistik = [
        ["Total Mobil", total],
        ["Available", jmlAvailable],
        ["Booked", jmlBooked],
        ["Rented", jmlRented],
        ["Maintenance", jmlMaintenance],
    ]

    print("\n===== STATISTIK DATA MOBIL =====")
    print(tabulate(tabular_data=dataStatistik,
                    headers=["Keterangan", "Jumlah"],
                    tablefmt="heavy_grid"))


# ===================================================================================================
# MENU RENTAL - simulasi sewa & pengembalian mobil, sekaligus menghitung estimasi total biaya sewa
# ===================================================================================================

def menuRental():
    while True:
        print("\n===== RENTAL MENU =====")
        print("1. Sewa Mobil")
        print("2. Kembalikan Mobil")
        print("3. Kembali ke Menu Utama")
        pilih = input("Pilih menu: ")

        # fitur rental - sewa mobil yang Available, hitung total biaya, lalu status jadi Rented
        if pilih == "1":
            baris = []
            for i in range(len(kodeMobil)):
                if statusMobil[i] == "Available":
                    baris.append([kodeMobil[i], merkMobil[i], tipeMobil[i], hargaSewa[i]])

            if len(baris) == 0:
                print("Tidak ada mobil yang available sekarang. Silakan cek kembali nanti.")
                continue

            print("\nMobil yang tersedia untuk disewa:")
            cetakTabelSewa(baris)

            kode = input("\nMasukkan kode mobil yang ingin disewa: ").upper()
            idx = cariIndex(kode)

            if idx == -1:
                print("Kode mobil tidak ditemukan. Silakan coba lagi.")
                continue    

            if statusMobil[idx] != "Available":
                print(f"Mobil dengan kode {kode} tidak tersedia untuk disewa saat ini. Status: {statusMobil[idx]}")
                continue

            durasiSewa = inputAngka("Masukkan durasi sewa (hari): ")
            totalBiaya = durasiSewa * hargaSewa[idx]

            print(f"\nHarga per hari : {hargaSewa[idx]}")
            print(f"Durasi sewa : {durasiSewa} hari")
            print(f"Total biaya sewa : Rp{totalBiaya}")

            konfirmasi = input("Apakah Anda ingin melanjutkan penyewaan? (Y/N): ").upper()
            if konfirmasi == "Y":
                statusMobil[idx] = "Rented"
                print(f"\nMobil {merkMobil[idx]} {tipeMobil[idx]} berhasil disewa selama {durasiSewa} hari.")
            else:
                print("Penyewaan dibatalkan.")

        # fitur rental - mengembalikan mobil yang sedang dalam status Rented, lalu status kembali jadi Available
        elif pilih == "2":
            kode = input("Masukkan kode mobil yang ingin dikembalikan: ").upper()
            idx = cariIndex(kode)

            if idx == -1:
                print("Kode mobil tidak ditemukan. Silakan coba lagi.")
                continue

            if statusMobil[idx] != "Rented":
                print(f"Mobil dengan kode {kode} tidak sedang disewa. Status saat ini: {statusMobil[idx]}")
                continue

            konfirmasi = input(f"Apakah Anda yakin ingin mengembalikan mobil {merkMobil[idx]} {tipeMobil[idx]}? (Y/N): ").upper()
            if konfirmasi == "Y":
                statusMobil[idx] = "Available"
                print(f"\nMobil {merkMobil[idx]} {tipeMobil[idx]} berhasil dikembalikan.")
            else:
                print("Pengembalian dibatalkan.")

        elif pilih == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

# ========================================================================================================================
# MENU DELETE untuk menghapus data mobil, terdapat validasi tidak boleh hapus mobil yang statusnya sedang disewa 'Rented'
# ========================================================================================================================

def menuDelete():
    while True:
        print("\n===== MENU HAPUS DATA MOBIL =====")
        print("1. Hapus Data Mobil")
        print("2. Hapus Semua Mobil dalam Satu Kategori")
        print("3. Kembali ke Menu Utama")
        pilih = input("Pilih menu (1-3): ")

        # fitur delete - hapus 1 mobil berdasarkan kode, terdapat 2 kali konfirmasi agar user tidak salah klik
        if pilih == "1":
            if len(kodeMobil) == 0:
                print("Data mobil kosong. Tidak ada yang bisa dihapus.")
                continue

            kode = input("Masukkan kode mobil yang ingin dihapus: ").upper()
            idx = cariIndex(kode)

            if idx == -1:
                print("Kode mobil tidak ditemukan. Silakan coba lagi.")
                continue

            if statusMobil[idx] == "Rented":
                print("Mobil sedang disewa. Tidak bisa dihapus.")
                continue

            print("\nData mobil yang akan dihapus:")
            print(f"Kode        : {kodeMobil[idx]}")
            print(f"Merk        : {merkMobil[idx]}")
            print(f"Tipe        : {tipeMobil[idx]}")
            print(f"Kategori    : {kategoriMobil[idx]}")
            print(f"Tahun       : {tahunMobil[idx]}")
            print(f"Harga Sewa  : {hargaSewa[idx]}")
            print(f"Status      : {statusMobil[idx]}")

            hapus = input("Apakah Anda yakin ingin menghapus mobil ini? (Y/N): ").upper()
            if hapus != "Y":
                if hapus == "N":
                    print("Data mobil batal dihapus.")
                    continue

            hapusLagi = input("Konfirmasi lagi, apakah Anda benar-benar ingin menghapus mobil ini? (Y/N): ").upper()
            if hapusLagi == "Y":
                del kodeMobil[idx]
                del merkMobil[idx]
                del tipeMobil[idx]
                del kategoriMobil[idx]
                del tahunMobil[idx]
                del hargaSewa[idx]
                del statusMobil[idx]
                print(f"Data mobil dengan kode {kode} berhasil dihapus.")
            else:
                print("Data mobil batal dihapus.")

        # fitur delete (tambahan) - hapus banyak mobil sekaligus per kategori, yang status rented otomatis di-skip
        elif pilih == "2":
            if len(kodeMobil) == 0:
                print("Data mobil kosong. Tidak ada yang bisa dihapus.")
                continue

            kat = cekKategori(input("Masukkan kategori mobil yang ingin dihapus (MPV/SUV/City Car/Sedan/Hatchback): "))
            if kat == None:
                print("Kategori tidak dikenal. Silakan coba lagi.")
                continue

            idxHapus = []
            skipRented = 0
            for i in range(len(kodeMobil)):
                if kategoriMobil[i] == kat:
                    if statusMobil[i] == "Rented":
                        skipRented = skipRented +1
                    else:idxHapus.append(i)

            if len(idxHapus) == 0:
                print(f"Tidak ada mobil yang bisa dihapus dalam kategori {kat}.")
                continue

            if skipRented > 0:
                print(f"{skipRented} mobil dalam kategori ini sedang disewa dan tidak bisa dihapus.")

            hapus = input("Yakin hapus semua mobil dalam kategori ini? (Y/N): ").upper()
            if hapus != "Y":
                print("Data mobil batal dihapus.")
                continue

            hapusLagi = input("Konfirmasi lagi, apakah Anda benar-benar ingin menghapus semua mobil dalam kategori ini? (Y/N): ").upper()
            if hapusLagi == "Y":
                for i in sorted(idxHapus, reverse=True):
                    del kodeMobil[i]
                    del merkMobil[i]
                    del tipeMobil[i]
                    del kategoriMobil[i]
                    del tahunMobil[i]
                    del hargaSewa[i]
                    del statusMobil[i]
                print(f"Semua mobil dalam kategori {kat} berhasil dihapus.")
            else:
                print("Data mobil batal dihapus.")

        elif pilih == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")


# ================================================================================================================
# MENU CREATE - menambahkan data mobil baru ke collection, terdapat validasi kode unik dan preview sebelum simpan
# ================================================================================================================

def menuCreate():
    while True:
        print("\n===== MENU TAMBAH DATA MOBIL =====")
        print("1. Tambah Data Mobil")
        print("2. Kembali ke Menu Utama")
        pilih = input("Pilih menu (1-2): ")

        # fitur create - input data mobil satu-satu, dicek dulu sebelum masuk ke list
        if pilih == "1":
            kode = input("Masukkan kode mobil (contoh: M001): ").upper()

            if cariIndex(kode) != -1:
                print("Kode mobil sudah dipakai. Silakan gunakan kode lain.")
                continue

            merk = input("Masukkan merk mobil: ")
            tipe = input("Masukkan tipe mobil: ")

            while True:
                kat = cekKategori(input("Masukkan kategori mobil (MPV/SUV/City Car/Sedan/Hatchback): "))
                if kat != None:
                    break
                print("Kategori tidak dikenal. Silakan coba lagi.")

            tahun = inputAngka("Masukkan tahun mobil (contoh: 2020): ")
            harga = inputAngka("Masukkan harga sewa per hari (contoh: 300000): ")
            statusBaru = "Available"

            print("\nData yang mau disimpan:")
            print(f"Kode: {kode}")
            print(f"Merk: {merk}")
            print(f"Tipe: {tipe}")
            print(f"Kategori: {kat}")
            print(f"Tahun: {tahun}")
            print(f"Harga Sewa: {harga}")
            print(f"Status: {statusBaru}")

            simpan = input("Apakah Anda ingin menyimpan data ini? (Y/N): ").upper()
            if simpan == "Y":
                kodeMobil.append(kode)
                merkMobil.append(merk)
                tipeMobil.append(tipe)
                kategoriMobil.append(kat)
                tahunMobil.append(tahun)
                hargaSewa.append(harga)
                statusMobil.append(statusBaru)
                print("Data mobil berhasil disimpan.")
            else:
                print("Data mobil batal disimpan.")

        elif pilih == "2":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")


# ========================================================================================================================================
# MENU READ - menampilkan data mobil, bisa menggunakan macam-macam cara mencari mobil seperti kode, merk, harga, kategori, sampai sorting
# ========================================================================================================================================

def menuRead():
    while True:
        print("\n===== MENU LIHAT DATA MOBIL =====")
        print("1. Tampilkan Semua Data Mobil")
        print("2. Cari Data Mobil Berdasarkan Kode")
        print("3. Cari Data Mobil Berdasarkan Merk")
        print("4. Cari Data Mobil Berdasarkan Harga Sewa")
        print("5. Cari Data Mobil yang Available")
        print("6. Cari Data Mobil Berdasarkan Kategori")
        print("7. Urutkan Data Mobil")
        print("8. Cari Multi Filter (Merk + Status)")
        print("9. Kembali ke Menu Utama")
        pilih = input("Pilih menu (1-9): ")

        if len(kodeMobil) == 0 and pilih != "9":
            print("Data mobil kosong. Silakan tambah data mobil terlebih dahulu.")
            continue

        # fitur read - lihat semua data mobil
        if pilih == "1":
            cetakSemua()

        # fitur read - cari 1 mobil spesifik pakai kode (primary key)
        elif pilih == "2":
            kode = input("Masukkan kode mobil yang ingin dicari: ").upper()
            idx = cariIndex(kode)

            if idx == -1:
                print("Kode mobil tidak ditemukan.")
                continue
            print("\nData mobil yang ditemukan:")
            cetakTabel([[kodeMobil[idx], merkMobil[idx], tipeMobil[idx], kategoriMobil[idx], tahunMobil[idx], hargaSewa[idx], statusMobil[idx]]])

        # fitur read (tambahan) - mencari semua mobil dari 1 merk tertentu
        elif pilih == "3":
            merk = input("Masukkan merk mobil yang ingin dicari: ")
            baris = []
            for i in range(len(kodeMobil)):
                if merkMobil[i].upper() == merk.strip().upper():
                    baris.append([kodeMobil[i], merkMobil[i], tipeMobil[i], kategoriMobil[i], tahunMobil[i], hargaSewa[i], statusMobil[i]])

            if len(baris) == 0:
                print("Tidak ada mobil dengan merk tersebut.")
            else:
                print("\nData mobil yang ditemukan:")
                cetakTabel(baris)

        # fitur read (tambahan) - mencari mobil yang harga sewanya di antara harga min-max
        elif pilih == "4":
            hargaMin = inputAngka("Masukkan harga sewa minimum: ")
            hargaMax = inputAngka("Masukkan harga sewa maksimum: ")
            baris = []
            for i in range(len(kodeMobil)):
                if hargaSewa[i] >= hargaMin and hargaSewa[i] <= hargaMax:
                    baris.append([kodeMobil[i], merkMobil[i], tipeMobil[i], kategoriMobil[i], tahunMobil[i], hargaSewa[i], statusMobil[i]])

            if len(baris) == 0:
                print("Tidak ada mobil dalam rentang harga tersebut.")
            else:
                print("\nData mobil yang ditemukan:")
                cetakTabel(baris)

        # fitur read (tambahan) - langsung filter mobil yang statusnya Available saja
        elif pilih == "5":
            baris = []
            for i in range(len(kodeMobil)):
                if statusMobil[i] == "Available":
                    baris.append([kodeMobil[i], merkMobil[i], tipeMobil[i], kategoriMobil[i], tahunMobil[i], hargaSewa[i], statusMobil[i]])

            if len(baris) == 0:
                print("Tidak ada mobil yang tersedia saat ini.")
            else:
                print("\nData mobil yang tersedia:")
                cetakTabel(baris)

        # fitur read (tambahan) - mencari mobil berdasarkan kategori
        elif pilih == "6":
            kat = cekKategori(input("Masukkan kategori mobil yang ingin dicari (MPV/SUV/City Car/Sedan/Hatchback): "))
            if kat == None:
                print("Kategori tidak dikenal. Silakan coba lagi.")
                continue

            baris = []
            for i in range(len(kodeMobil)):
                if kategoriMobil[i] == kat:
                    baris.append([kodeMobil[i], merkMobil[i], tipeMobil[i], kategoriMobil[i], tahunMobil[i], hargaSewa[i], statusMobil[i]])

            if len(baris) == 0:
                print(f"Tidak ada mobil dalam kategori {kat}.")
            else:
                print(f"\nData mobil dalam kategori {kat}:")
                cetakTabel(baris)

        # fitur sorting (tambahan) - mengurutkan data mobil, terdapat 5 pilihan mode
        elif pilih == "7":
            print("\nUrutkan berdasarkan:")
            print("1. Harga Sewa Termurah")
            print("2. Harga Sewa Termahal")
            print("3. Tahun Terbaru")
            print("4. Tahun Terlama")
            print("5. Merk A-Z")
            mode = input("Masukkan pilihan (1-5): ")

            if mode == "1":
                urutkanData("harga_murah")
                print("Data mobil telah diurutkan berdasarkan harga sewa termurah.")
            elif mode == "2":
                urutkanData("harga_mahal")
                print("Data mobil telah diurutkan berdasarkan harga sewa termahal.")
            elif mode == "3":
                urutkanData("tahun_baru")
                print("Data mobil telah diurutkan berdasarkan tahun terbaru.")
            elif mode == "4":
                urutkanData("tahun_lama")
                print("Data mobil telah diurutkan berdasarkan tahun terlama.")
            elif mode == "5":
                urutkanData("merk_az")
                print("Data mobil telah diurutkan berdasarkan merk A-Z.")
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

        # fitur multi filter (tambahan) - cari mobil yang cocok (merk dan status sekaligus)
        elif pilih == "8":
            merk = input("Masukkan merk mobil yang ingin dicari: ")
            status = cekStatus(input("Masukkan status mobil (Available/Rented/Maintenance): "))

            if status == None:
                print("Status tidak dikenal. Silakan coba lagi.")
                continue

            baris = []
            for i in range(len(kodeMobil)):
                if merkMobil[i].upper() == merk.strip().upper() and statusMobil[i] == status:
                    baris.append([kodeMobil[i], merkMobil[i], tipeMobil[i], kategoriMobil[i], tahunMobil[i], hargaSewa[i], statusMobil[i]])

            if len(baris) == 0:
                print(f"Tidak ada mobil dengan merk {merk} dan status {status}.")
            else:
                print(f"\nData mobil dengan merk {merk} dan status {status}:")
                cetakTabel(baris)

        elif pilih == "9":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

# =====================================================================================================
# MENU UPDATE - mengubah data mobil yang sudah ada, user bisa pilih sendiri kolom mana yang mau diubah
# =====================================================================================================

def menuUpdate():
    while True:
        print("\n===== MENU UPDATE DATA MOBIL =====")
        print("1. Update Data Mobil")
        print("2. Kembali ke Menu Utama")
        pilih = input("Pilih menu (1-2): ")

        # fitur update - mencari mobil dulu pake kode, baru boleh ubah kolomnya
        if pilih == "1":
            if len(kodeMobil) == 0:
                print("Data mobil masih kosong.")
                continue

            kode = input("Masukkan kode mobil yang ingin diubah: ").upper()
            idx = cariIndex(kode)

            if idx == -1:
                print("Kode mobil tidak ditemukan. Silakan coba lagi.")
                continue

            print("\nData mobil saat ini:")
            print(f"Kode        : {kodeMobil[idx]}")
            print(f"Merk        : {merkMobil[idx]}")
            print(f"Tipe        : {tipeMobil[idx]}")
            print(f"Kategori    : {kategoriMobil[idx]}")
            print(f"Tahun       : {tahunMobil[idx]}")
            print(f"Harga Sewa  : {hargaSewa[idx]}")
            print(f"Status      : {statusMobil[idx]}")

            lanjut = input("\nLanjut update date ini? (Y/N): ").upper()
            if lanjut != "Y":
                continue

            while True:
                print("\nKolom yang bisa diubah: merk, tipe, kategori, tahun, harga, status")
                kolom = input("Masukkan nama kolom yang ingin diubah: ").lower()

                if kolom == "merk":
                    lama = merkMobil[idx]
                    baru = input("Masukkan merk baru: ")
                elif kolom == "tipe":
                    lama = tipeMobil[idx]
                    baru = input("Masukkan tipe baru: ")
                elif kolom == "kategori":
                    lama = kategoriMobil[idx]
                    while True:
                        baru = cekKategori(input("Masukkan kategori baru (MPV/SUV/City Car/Sedan/Hatchback: "))
                        if baru != None:
                            break
                        print("Kategori tidak dikenal. Silahkan coba lagi.")
                elif kolom == "tahun": 
                    lama = tahunMobil[idx]
                    baru = inputAngka("Masukkan tahun: ")
                elif kolom == "harga":
                    lama = hargaSewa[idx]
                    baru = inputAngka("Masukkan harga sewa: ")
                elif kolom == "status":
                    lama = statusMobil[idx]
                    while True:
                        baru = cekStatus(input("Masukkan status baru (Available/Booked/Rented/Maintenance): "))
                        if baru != None:
                            break
                        print("Status tidak dikenal. Silahkan coba lagi.")
                else:
                    print("Nama kolom tidak dikenal.")
                    lagi = input("Update kolom lain untuk mobil ini? (Y/N): ").upper()
                    if lagi != "Y":
                        break
                    continue

                print(f"\nData Lama : {lama}")
                print(f"\nData Baru : {baru}")
                konfirmasi = input(f"Apakah Anda yakin akan update {kolom}? (Y/N): ").upper()
                if konfirmasi == "Y":
                    if kolom == "merk":
                        merkMobil[idx] = baru
                    elif kolom == "tipe":
                        tipeMobil[idx] = baru
                    elif kolom == "kategori":
                        kategoriMobil[idx] = baru
                    elif kolom == "tahun":
                        tahunMobil[idx] = baru
                    elif kolom == "harga":
                        hargaSewa[idx] = baru
                    elif kolom == "status":
                        statusMobil[idx] = baru
                    print("Data berhasil diupdate!")
                else:
                    print("Update dibatalkan.")

                lagi = input("Update kolom lain untuk mobil ini? (Y/N): ").lower()
                if lagi != "Y":
                    break

        elif pilih == "2":
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")

menuUtama()
