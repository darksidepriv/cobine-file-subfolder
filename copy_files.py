import os
import shutil

def copy_all_files_to_new_folder(source_folder: str, destination_folder: str, debug: bool = False):
    # Memastikan folder tujuan ada, jika belum ada maka buat
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        if debug:
            print(f"Folder tujuan '{destination_folder}' dibuat.")

    # Iterasi melalui semua subfolder dan file
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            source_file_path = os.path.join(root, file)
            dest_file_path = os.path.join(destination_folder, file)
            
            # Jika file dengan nama yang sama sudah ada di folder tujuan, rename file
            if os.path.exists(dest_file_path):
                base_name, extension = os.path.splitext(file)
                counter = 1
                new_file_name = f"{base_name}_{counter}{extension}"
                new_dest_file_path = os.path.join(destination_folder, new_file_name)

                # Tambah angka sampai menemukan nama file yang belum ada
                while os.path.exists(new_dest_file_path):
                    counter += 1
                    new_file_name = f"{base_name}_{counter}{extension}"
                    new_dest_file_path = os.path.join(destination_folder, new_file_name)
                
                dest_file_path = new_dest_file_path

            # Copy file dari source ke destination
            shutil.copy2(source_file_path, dest_file_path)  # Menggunakan copy2 untuk menyalin file dan metadata
            
            if debug:
                print(f"File '{source_file_path}' berhasil disalin ke '{dest_file_path}'.")

def main():
    print("=== Aplikasi Penyalinan Semua File dari Subfolder ===")
    
    # Input dari pengguna
    source_folder = input("Masukkan folder sumber: ")
    if not os.path.exists(source_folder):
        print(f"Folder sumber '{source_folder}' tidak ditemukan.")
        return
    
    # Nama folder tujuan baru
    new_folder_name = input("Masukkan nama folder tujuan baru: ")
    destination_folder = os.path.join(os.getcwd(), new_folder_name)
    
    # Opsi debug
    debug_mode = input("Aktifkan mode debug? (y/n): ").lower() == 'y'
    
    # Panggil fungsi untuk menyalin semua file
    copy_all_files_to_new_folder(source_folder, destination_folder, debug=debug_mode)
    
    print(f"Proses selesai! Semua file dari folder '{source_folder}' telah disalin ke folder '{destination_folder}'.")

if __name__ == "__main__":
    main()
