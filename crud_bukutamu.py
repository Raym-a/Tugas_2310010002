from koneksi import get_connection

# CREATE: fungsi untuk menyimpan data buku tamu ke database
def simpan(nama_pengunjung, tanggal_kunjungan, saran):
    conn = get_connection()           # Buka koneksi ke database
    cur = conn.cursor()               # Buat cursor untuk menjalankan perintah SQL
    sql = """
        INSERT INTO buku_tamu (nama_pengunjung, tanggal_kunjungan, saran)
        VALUES (%s, %s, %s)
    """
    cur.execute(sql, (nama_pengunjung, tanggal_kunjungan, saran))  # Jalankan perintah INSERT
    conn.commit()                     # Simpan perubahan ke database
    conn.close()                      # Tutup koneksi database

# READ: fungsi untuk membaca semua data dari tabel buku_tamu
def read_all():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM buku_tamu")  # Jalankan query SELECT
    hasil = cur.fetchall()            # Ambil semua hasil query
    conn.close()                      # Tutup koneksi database
    return hasil                       # Kembalikan hasil ke pemanggil fungsi

# DELETE: fungsi untuk menghapus data dari tabel buku_tamu berdasarkan id_tamu
def hapus(id_tamu):
    conn = get_connection()
    cur = conn.cursor()
    sql = "DELETE FROM buku_tamu WHERE id_tamu=%s"
    cur.execute(sql, (id_tamu,))      # Jalankan query DELETE dengan parameter id_tamu
    conn.commit()                     # Simpan perubahan
    conn.close()                      # Tutup koneksi database
