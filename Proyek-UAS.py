# ============================================================
# PROGRAM: Personal Monthly Spending Awareness System
# DESKRIPSI:
# Program ini membantu pengguna mencatat, memantau,
# dan mengevaluasi pengeluaran selama satu bulan.
# ============================================================


# -------------------------------
# Variabel untuk menyimpan anggaran bulanan
# Dibuat di luar fungsi agar bisa diakses oleh semua fitur
# Nilai awal 0 menandakan anggaran belum diset
# -------------------------------
monthly_budget = 0


# -------------------------------
# List untuk menyimpan seluruh data pengeluaran
# Setiap pengeluaran disimpan sebagai dictionary
# agar data rapi dan mudah diolah
# -------------------------------
expenses = []


# -------------------------------
# Fungsi line()
# Fungsi ini hanya mencetak garis pemisah
# Tujuannya memperindah tampilan dan
# memisahkan antar bagian output
# -------------------------------
def line():
    print("=" * 70)  # mencetak karakter "=" sebanyak 70 kali


# -------------------------------
# Fungsi show_menu()
# Menampilkan menu utama program
# Dipanggil berulang kali selama program berjalan
# -------------------------------
def show_menu():
    line()  # memanggil fungsi line untuk membuat header lebih jelas
    print("Personal Monthly Spending Awareness System")
    print("Sistem pemantauan pengeluaran bulanan pribadi")
    line()
    print("1. Set anggaran bulanan")
    print("2. Catat pengeluaran")
    print("3. Lihat rekap pengeluaran")
    print("4. Cek status keuangan")
    print("5. Evaluasi dan saran")
    print("6. Keluar")
    line()


# -------------------------------
# Fungsi after_action()
# Digunakan setelah sebuah fitur selesai
# Memberi kontrol ke user apakah ingin lanjut atau keluar
# -------------------------------
def after_action():
    print("\nLangkah selanjutnya:")
    print("1. Kembali ke menu utama")
    print("2. Keluar dari program")
    return input("Pilihan (1/2): ")  # nilai dikembalikan ke pemanggil fungsi


# ============================================================
# FITUR 1: SET ANGGARAN BULANAN
# ============================================================
def set_budget():
    global monthly_budget  # memberi tahu Python bahwa variabel global akan diubah

    line()  # garis pembuka agar tampilan rapi
    print("Set anggaran bulanan")
    line()

    # Penjelasan agar user paham konteks fitur
    print("Pada menu ini kamu menentukan batas maksimal")
    print("pengeluaran selama satu bulan.")
    print("Anggaran ini akan menjadi acuan evaluasi.\n")

    # Input anggaran dari user dan diubah ke integer
    monthly_budget = int(input("Masukkan anggaran bulanan (Rp): "))

    line()

    # Respon interaktif berdasarkan besar anggaran
    if monthly_budget < 500_000:
        print("Anggaran tergolong kecil.")
        print("Program akan cepat memberi peringatan.")
    elif monthly_budget <= 1_000_000:
        print("Anggaran cukup realistis.")
        print("Masih aman selama pengeluaran terkontrol.")
    else:
        print("Anggaran cukup besar.")
        print("Pastikan pengeluaran tetap masuk akal.")

    # Konfirmasi nilai yang tersimpan
    print(f"\nAnggaran bulanan disimpan: Rp{monthly_budget}")
    print("Sistem siap memantau pengeluaran bulan ini.")


# ============================================================
# FITUR 2: CATAT PENGELUARAN
# ============================================================
def add_expense():
    # Dictionary kategori agar pilihan konsisten
    categories = {
        "1": "Makanan",
        "2": "Transportasi",
        "3": "Pendidikan",
        "4": "Hiburan",
        "5": "Kesehatan",
        "6": "Lainnya"
    }

    # Contoh pengeluaran untuk membantu user memahami kategori
    examples = {
        "Makanan": "contoh: makan siang, jajan, belanja dapur",
        "Transportasi": "contoh: bensin, ojek online, tiket bus",
        "Pendidikan": "contoh: buku, alat tulis, kuota belajar",
        "Hiburan": "contoh: nonton film, langganan streaming",
        "Kesehatan": "contoh: obat, vitamin, biaya dokter",
        "Lainnya": "contoh: donasi, hadiah, kebutuhan mendadak"
    }

    # Loop agar user bisa mencatat lebih dari satu pengeluaran
    while True:
        line()
        print("Catat pengeluaran bulanan")
        line()

        print("Gunakan menu ini untuk mencatat setiap pengeluaran")
        print("yang terjadi selama satu bulan.\n")

        # Menampilkan kategori
        print("Daftar kategori pengeluaran:")
        for key, value in categories.items():
            print(f"{key}. {value}")

        # Input pilihan kategori
        cat_choice = input("\nPilih kategori (1-6): ")

        # Validasi input kategori
        if cat_choice not in categories:
            print("Pilihan kategori tidak valid.")
            continue  # kembali ke awal loop

        # Menentukan kategori yang dipilih
        category = categories[cat_choice]

        line()
        print(f"Kategori dipilih: {category}")
        print(examples[category])  # menampilkan contoh sesuai kategori
        line()

        # Input detail pengeluaran
        name = input("Nama pengeluaran: ")
        amount = int(input("Jumlah pengeluaran (Rp): "))

        # Menyimpan data ke dalam dictionary
        expense = {
            "name": name,
            "category": category,
            "amount": amount
        }

        # Menambahkan dictionary ke list expenses
        expenses.append(expense)

        line()
        print("Pengeluaran berhasil dicatat.")
        print(f"Nama     : {name}")
        print(f"Kategori : {category}")
        print(f"Jumlah   : Rp{amount}")

        # Menanyakan apakah user ingin menambah data lagi
        again = input("\nIngin menambah pengeluaran lain? (y/n): ")
        if again.lower() != "y":
            break  # keluar dari loop


# ============================================================
# FITUR 3: REKAP PENGELUARAN
# ============================================================
def show_expenses():
    line()
    print("Rekap pengeluaran bulanan")
    line()

    # Jika belum ada pengeluaran
    if not expenses:
        print("Belum ada pengeluaran yang tercatat.")
        return

    total = 0  # variabel untuk menyimpan total pengeluaran

    # Loop untuk menampilkan semua pengeluaran
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['name']} | {exp['category']} | Rp{exp['amount']}")
        total += exp["amount"]  # menjumlahkan seluruh pengeluaran

    line()
    print(f"Total pengeluaran sementara: Rp{total}")


# ============================================================
# FITUR 4: STATUS KEUANGAN
# ============================================================
def financial_status():
    line()
    print("Status keuangan bulanan")
    line()

    # Validasi apakah anggaran sudah diset
    if monthly_budget == 0:
        print("Anggaran belum ditentukan.")
        return

    # Menghitung total pengeluaran menggunakan sum()
    total = sum(exp["amount"] for exp in expenses)

    # Menghitung persentase penggunaan anggaran
    # Rumus: (total_pengeluaran / anggaran) * 100
    percent = (total / monthly_budget) * 100

    print(f"Anggaran        : Rp{monthly_budget}")
    print(f"Total digunakan : Rp{total}")
    print(f"Pemakaian       : {percent:.2f}%")
    line()

    # Menentukan status berdasarkan persentase
    if percent < 70:
        print("Status keuangan aman.")
    elif percent <= 100:
        print("Status keuangan waspada.")
    else:
        print("Status keuangan kritis. Pengeluaran melebihi anggaran.")


# ============================================================
# FITUR 5: EVALUASI DAN SARAN
# ============================================================
def evaluation_and_advice():
    line()
    print("Evaluasi dan saran keuangan")
    line()

    # Validasi awal
    if monthly_budget == 0:
        print("Anggaran belum diset.")
        return

    # Menghitung total pengeluaran
    total = sum(exp["amount"] for exp in expenses)

    print(f"Anggaran bulanan : Rp{monthly_budget}")
    print(f"Total pengeluaran: Rp{total}")
    line()

    # Memberikan saran berdasarkan kondisi keuangan
    if total < monthly_budget * 0.7:
        print("Pengelolaan keuangan tergolong baik.")
    elif total <= monthly_budget:
        print("Pengeluaran mendekati batas anggaran.")
    else:
        print("Pengeluaran melebihi anggaran. Perlu evaluasi serius.")


# ============================================================
# PROGRAM UTAMA
# ============================================================
while True:
    show_menu()  # memanggil fungsi menu utama
    choice = input("Pilih menu (1-6): ")

    if choice == "1":
        set_budget()          # memanggil fitur set anggaran
        if after_action() == "2":
            break

    elif choice == "2":
        add_expense()         # memanggil fitur catat pengeluaran
        if after_action() == "2":
            break

    elif choice == "3":
        show_expenses()       # memanggil fitur rekap
        if after_action() == "2":
            break

    elif choice == "4":
        financial_status()    # memanggil fitur status keuangan
        if after_action() == "2":
            break

    elif choice == "5":
        evaluation_and_advice()  # memanggil fitur evaluasi
        if after_action() == "2":
            break

    elif choice == "6":
        line()
        print("Program selesai.")
        print("Terima kasih sudah menggunakan sistem ini.")
        line()
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
