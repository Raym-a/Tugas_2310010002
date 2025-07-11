from koneksi import get_connection

# Fungsi untuk menyimpan data karyawan baru ke tabel pendaftaran_karyawan
def simpan(nama_karyawan, no_hp, tanggal_daftar):
    conn = get_connection()                 # Membuka koneksi ke database
    cur = conn.cursor()                      # Buat cursor untuk menjalankan perintah SQL
    sql = """
        INSERT INTO pendaftaran_karyawan (nama_karyawan, no_hp, tanggal_daftar)
        VALUES (%s, %s, %s)
    """
    cur.execute(sql, (nama_karyawan, no_hp, tanggal_daftar))   # Jalankan perintah SQL dengan data
    conn.commit()                         # Simpan perubahan ke database
    conn.close()                          # Tutup koneksi

# Fungsi untuk mengedit data karyawan berdasarkan id_karyawan
def edit(id_karyawan, nama_karyawan, no_hp, tanggal_daftar):
    conn = get_connection()
    cur = conn.cursor()
    sql = """
        UPDATE pendaftaran_karyawan
        SET nama_karyawan=%s, no_hp=%s, tanggal_daftar=%s
        WHERE id_karyawan=%s
    """
    cur.execute(sql, (nama_karyawan, no_hp, tanggal_daftar, id_karyawan))  # Jalankan update
    conn.commit()          # Simpan perubahan
    conn.close()          # Tutup koneksi

# Fungsi untuk menghapus data karyawan berdasarkan id_karyawan
def hapus(id_karyawan):
    conn = get_connection()
    cur = conn.cursor()
    sql = "DELETE FROM pendaftaran_karyawan WHERE id_karyawan=%s"
    cur.execute(sql, (id_karyawan,))   # Jalankan delete
    conn.commit()
    conn.close()

# Fungsi untuk membaca semua data karyawan
def read_all():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM pendaftaran_karyawan")  # Ambil semua data pada Tabel di database
    data = cur.fetchall()               # Ambil hasil query sebagai list of tuples
    print("Data dari database:", data)  # Tampilkan data di console (debug)
    conn.close()
    return data

# Fungsi untuk membaca hanya kolom nama_karyawan dari tabel (untuk combo box)
def read_nama_karyawan():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nama_karyawan FROM pendaftaran_karyawan")
    hasil = [row[0] for row in cursor.fetchall()]  # Ambil hasil dan simpan hanya nama
    conn.close()
    return hasil
