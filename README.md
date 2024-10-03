# Aplikasi Penyalin Semua File dari Subfolder ke Satu Folder

Aplikasi Python ini bertujuan untuk menyalin semua file dari sebuah folder sumber, termasuk subfoldernya, ke satu folder tujuan baru. File asli di lokasi sumber tidak diubah, dan semua file hanya disalin ke folder tujuan.

## Fitur Utama
- **Penyalinan file tanpa mengubah file asli:** Semua file disalin dari folder sumber dan subfolder ke satu folder tujuan tanpa mengubah atau memindahkan file aslinya.
- **Pembuatan nama file unik:** Jika ada file dengan nama yang sama di folder tujuan, aplikasi akan menambahkan angka di akhir nama file untuk menghindari penimpaan.
- **Mendukung semua jenis file:** Aplikasi dapat menyalin semua jenis file, terlepas dari ekstensi file tersebut.
- **Mode Debug:** Menyediakan informasi tambahan selama proses penyalinan file jika mode debug diaktifkan.

## Persyaratan
- **Python 3.x**
- Modul standar Python:
  - `os`
  - `shutil`

## Instalasi
1. Pastikan Anda telah menginstal **Python 3.x** di sistem Anda.
2. Clone repositori ini ke direktori lokal Anda:
   ```bash
   git clone https://github.com/darksidepriv/cobine-file-subfolder
