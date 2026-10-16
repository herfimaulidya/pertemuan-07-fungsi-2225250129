
# Pertemuan 07 — Fungsi Python

**Nama:** Herfi Maulidya  
**NIM:** 2225250129  
**Kelas:** 3A  
**Mata Kuliah:** Algoritma dan Pemrograman  
**Dosen Pengampu:** Dr. Aan Hendrayana, S.Si., M.Pd.

## 1. Tujuan

Praktikum ini bertujuan untuk memahami penggunaan fungsi, parameter, return value, dan scope variabel dalam Python. Praktikum juga melatih modularisasi program, pengujian fungsi, serta penggunaan Git dan GitHub untuk mendokumentasikan perkembangan pekerjaan.

## 2. Struktur Proyek

```text
pertemuan-07-fungsi-2225250129/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_salam.py
│   ├── 02_luas_persegi_panjang.py
│   ├── 03_jumlah_n.py
│   ├── 04_statistik_sederhana.py
│   └── 05_scope.py
└── praktik/
    └── utilitas_matematika.py
```

## 3. Cara Menjalankan Program

Pastikan Python sudah terpasang dan terminal berada di folder utama proyek.

Jalankan latihan menggunakan perintah berikut:

```powershell
py latihan/01_salam.py
py latihan/02_luas_persegi_panjang.py
py latihan/03_jumlah_n.py
py latihan/04_statistik_sederhana.py
py latihan/05_scope.py
```

Untuk menjalankan program utilitas matematika:

```powershell
py praktik/utilitas_matematika.py
```

Pilih operasi melalui menu yang ditampilkan, kemudian masukkan nilai sesuai permintaan program.

## 4. Struktur Fungsi

### A. Fungsi Salam

File: `latihan/01_salam.py`

Fungsi `salam(nama, kelas)` menerima nama dan kelas melalui parameter, kemudian menampilkan salam sesuai nilai yang diberikan.

### B. Luas Persegi Panjang

File: `latihan/02_luas_persegi_panjang.py`

Fungsi `luas_persegi_panjang(panjang, lebar)` menghitung luas dengan mengalikan panjang dan lebar. Nilai luas dikembalikan menggunakan `return`.

### C. Jumlah Bilangan 1 sampai n

File: `latihan/03_jumlah_n.py`

Fungsi `jumlah_n(n)` menggunakan perulangan `for` dan variabel akumulator untuk menghitung jumlah bilangan dari 1 sampai n. Hasil dikembalikan menggunakan `return`.

### D. Statistik Sederhana

File: `latihan/04_statistik_sederhana.py`

Fungsi `statistik_sederhana(data)` mengolah sekumpulan data dan mengembalikan tiga nilai, yaitu minimum, maksimum, dan rata-rata.

### E. Scope Variabel

File: `latihan/05_scope.py`

Program menunjukkan perbedaan variabel global dan lokal. Parameter `x` di dalam fungsi menerima nilai 20, sedangkan variabel global `x` tetap bernilai 10. Nilai `y` dikembalikan melalui `return`.

### F. Utilitas Matematika Modular

File: `praktik/utilitas_matematika.py`

Program terdiri atas fungsi-fungsi berikut:

- `luas_persegi_panjang(p, l)`: menghitung luas persegi panjang.
- `luas_segitiga(a, t)`: menghitung luas segitiga.
- `jumlah_n(n)`: menghitung jumlah bilangan dari 1 sampai n.
- `faktorial(n)`: menghitung faktorial menggunakan perulangan.
- `tampilkan_menu()`: menampilkan pilihan operasi matematika.

Program utama menggunakan seleksi untuk menjalankan operasi sesuai pilihan pengguna. Input n untuk operasi jumlah dan faktorial divalidasi agar berupa bilangan bulat nonnegatif.

## 5. Hasil Pengujian

### A. Latihan 02 — Luas Persegi Panjang

| Input | Hasil yang Diharapkan | Hasil Aktual |
|---|---:|---:|
| panjang = 8, lebar = 5 | 40 | 40 |
| panjang = 2.5, lebar = 4 | 10.0 | 10.0 |
| panjang = 0, lebar = 7 | 0 | 0 |

Status: Berhasil.

### B. Latihan 03 — Jumlah Bilangan

| n | Hasil Perulangan | Hasil Rumus | Status |
|---:|---:|---:|---|
| 1 | 1 | 1 | Berhasil |
| 5 | 15 | 15 | Berhasil |
| 10 | 55 | 55 | Berhasil |
| 100 | 5050 | 5050 | Berhasil |

Rumus pembanding:

S = n(n + 1) / 2

### C. Latihan 04 — Statistik Sederhana

Data pengujian: `[70, 80, 65, 90, 75]`

| Statistik | Hasil yang Diharapkan | Hasil Aktual |
|---|---:|---:|
| Minimum | 65 | 65 |
| Maksimum | 90 | 90 |
| Rata-rata | 76.0 | 76.0 |

Status: Berhasil.

### D. Latihan 05 — Scope Variabel

| Variabel | Hasil yang Diharapkan | Hasil Aktual |
|---|---:|---:|
| x di dalam fungsi | 20 | 20 |
| y di dalam fungsi | 25 | 25 |
| x di luar fungsi | 10 | 10 |
| hasil | 25 | 25 |

Status: Berhasil.

### E. Praktik — Utilitas Matematika

| Operasi | Input | Hasil yang Diharapkan | Hasil Aktual |
|---|---|---:|---:|
| Luas persegi panjang | p = 8, l = 5 | 40 | 40.0 |
| Luas segitiga | a = 10, t = 6 | 30.0 | 30.0 |
| Jumlah 1 sampai n | n = 10 | 55 | 55 |
| Faktorial | n = 5 | 120 | 120 |
| Faktorial | n = 0 | 1 | 1 |

Status: Berhasil.

## 6. Refleksi

Melalui praktikum ini, saya memahami bahwa fungsi membantu membagi program menjadi bagian-bagian yang memiliki tugas jelas dan dapat digunakan kembali. Parameter memungkinkan fungsi menerima input yang berbeda, sedangkan `return` mengembalikan hasil agar dapat digunakan oleh bagian program lain.

Saya juga mempelajari bahwa variabel lokal hanya dapat digunakan dalam ruang lingkupnya, sehingga tidak semua variabel di dalam fungsi dapat diakses dari luar fungsi. Modularisasi membuat program lebih mudah dibaca, diuji, dan diperbaiki.

## 7. Sumber dan Bantuan

- Bahan Ajar Algoritma dan Pemrograman — Pertemuan 07: Fungsi, Parameter, Return Value, dan Scope dalam Python di VS Code dan Pengumpulan melalui GitHub.
- Python Software Foundation. Dokumentasi Python 3: Defining Functions.
- Visual Studio Code Documentation: Python in Visual Studio Code.
- GitHub Docs: Adding locally hosted code to GitHub.

Bantuan AI digunakan untuk membantu memahami konsep, menyusun kode, dan menyusun dokumentasi. Saya bertanggung jawab memeriksa, menjalankan, menguji, dan memahami program yang dikumpulkan.
