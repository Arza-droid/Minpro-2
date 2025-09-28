nama_daerah = ["", "jawa", "sumatra", "kalimantan", "bali"]
jalan_tol = {"jawa":["", "Tanggerang-Merak", "Jakarta-Cikampek", "Cikampek-Palimanan"],
            "sumatra":["", "Palembang-Indralaya", "Indralaya-Muara Enim"],
            "kalimantan":["", "Balikpapan-Samarinda"],
            "bali":["", "I Gusti Ngurah Rai-Benoa-Nusa Dua"]
}
tarif_tol ={"jawa":{"golongan 1":"6000",
                    "golongan 2":"12000",
                    "golongan 3":"14000",
                    "golongan 4":"16000",
                    "golongan 5":"20000",
                    "golongan 6":"5000",
},
            "sumatra":{"golongan 1":"7000",
                    "golongan 2":"13000",
                    "golongan 3":"15000",
                    "golongan 4":"17000",
                    "golongan 5":"21000",
                    "golongan 6":"6000",
},
            "kalimantan":{"golongan 1":"8000",
                    "golongan 2":"14000",
                    "golongan 3":"16000",
                    "golongan 4":"18000",
                    "golongan 5":"22000",
                    "golongan 6":"7000",
},
            "bali":{"golongan 1":"9000",
                    "golongan 2":"15000",
                    "golongan 3":"17000",
                    "golongan 4":"19000",
                    "golongan 5":"23000",
                    "golongan 6":"8000",
},
}
username = {"admin":"admin1"}

def menu():
    print("== Pilih Role ==")
    print("1. Admin")
    print("2. User")
    print("3. Keluar")
    print("=================")

def menua():
    print("====== Admin ======")
    user= str(input("masukkan username: "))
    pw = str(input("masukkan password: "))
    print("==========================")
    try:
        if user in username and username [user] == pw :
            menub()
        else :
            print("tidak terdaftar")
    except BaseException:
        print("terjadi error")

def menub():
        while True:
            print("====== Menu Admin ======")
            print("1. Tampilkan Data")
            print("2. Tambah Data Jalan Tol")
            print("3. Ubah Tarif Tol")
            print("4. Hapus Data Jalan Tol")
            print("5. Keluar")
            print("==========================")
            a1 = int(input("pilih menu: "))
            try:
                if a1 == 1:
                    for daerah in nama_daerah[1:]:
                        print(f"== {daerah} ==")
                        print("== jalan tol ==")
                        for tol in jalan_tol[daerah]:
                            if tol:
                                print(f"{tol}")
                        print("== tarif tol ==")
                        for golongan, tarif in tarif_tol[daerah].items():
                            print(f"{golongan}:{tarif}")
                elif a1 == 2:
                    for daerah in nama_daerah[1:]:
                        print(f"== {daerah} ==")
                        print("== jalan tol ==")
                        for tol in jalan_tol[daerah]:
                            if tol:
                                print(f"{tol}")
                    a2 = str(input("masukkan nama daerah: "))
                    a3 = str(input("masukkan nama jalan tol baru: "))
                    jalan_tol[a2].append(a3)
                    print(jalan_tol[a2])
                elif a1 == 3:
                    daerah = str(input("masukkan nama daerah: "))
                    golongan = input("masukkan tarif golongan yang diubah(golongan 1-6): ")
                    tarif_baru = int(input("masukkan tarif baru: "))
                    tarif_tol[daerah][golongan] = tarif_baru
                    print(f"=={daerah}==")
                    print("==jalan tol==")
                    for tol in jalan_tol[daerah]:
                        if tol:
                            print(f"{tol}")
                    print("==tarif tol==")
                    for golongan, tarif in tarif_tol[daerah].items():
                        print(f"{golongan}: {tarif}")
                elif a1 == 4:
                    daerah = str(input("masukkan nama daerah: "))
                    print(f"daftar jalan tol{daerah}: ")
                    for tol in jalan_tol[daerah]:
                        if tol:
                            print(tol)
                    dihapus = str(input("masukkan nama jalan tol yang ingin dihapus: "))
                    if dihapus in jalan_tol[daerah]:
                        jalan_tol[daerah].remove(dihapus)
                    else:
                        print("jalan tol tidak ditemukan")
                    print(f"=={daerah}==")
                    print("==jalan tol==")
                    for tol in jalan_tol[daerah]:
                        if tol:
                            print(f"{tol}")
                elif a1 == 5:
                    break
                else:
                    print("tidak ada di menu")
            except BaseException:
                print("terjadi error")

def menuc():
        while True:
            print("====== Menu pengguna ======")
            print("1. Cek Tarif Tol")
            print("2. Keluar")
            print("============================")
            try:
                    b1 = int(input("pilih menu: "))
                    if b1 == 1:
                        for daerah in nama_daerah[1:]:
                                        print(f"{daerah}")
                        daerah = str(input("masukkan nama daerah: "))
                        if daerah in tarif_tol:
                            print("daftar golongan kendaraan:")
                            for golongan in tarif_tol[daerah]:
                                print(golongan)
                            golongan_kendaraan = input("masukkan golongan kendaraan(golongan 1-6):")
                            if golongan_kendaraan in tarif_tol[daerah]:
                                print("daftar jalan tol: ")
                                for tol in jalan_tol[daerah]:
                                    print(tol)
                                pilih_tol = str(input("masukkan jalan tol:"))
                                if pilih_tol in jalan_tol[daerah]:
                                    print(f"{daerah}")
                                    print(f"{golongan_kendaraan}")
                                    print(f"jalan tol:{pilih_tol}")
                                    print(f"tarif tol anda:{tarif_tol[daerah][golongan_kendaraan]}")
                                else:
                                    print("nama jalan tol tidak ada")
                            else:
                                print("golongan kendaraan tidak ada")
                        else:
                            print("nama daerah tidak ada")
                    elif b1 == 2:
                        print("terimakasih")
                        break
                    
            except BaseException:
                    print("terjadi error")


while True:
    menu()
    try:
            a = int(input("Pilih menu: "))
            if a == 1:
                menua()
            elif a == 2:
                menuc()
            elif a == 3:
                print("terimakasih")
                break
            else:
                print("Input tidak valid")
    except ValueError:
        print("tolong hanya masukkan angka pada menu")
    except KeyboardInterrupt:
        print("tolong jangan menekan ctrl+c")
