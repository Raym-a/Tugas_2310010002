from koneksi import get_connection

# Fungsi untuk menyimpan data laporan karyawan
def simpan(nama_karyawan, tanggal_laporan):
    conn = get_connection()           # Buka koneksi ke database
    cur = conn.cursor()               # Buat cursor untuk menjalankan query

    # Hitung total penghasilan karyawan dari tabel pemesanan
    sql_total = """
        SELECT SUM(harga) FROM pemesanan
        WHERE nama_karyawan = %s
    """
    cur.execute(sql_total, (nama_karyawan,))
    result = cur.fetchone()                       # Ambil hasil total
    total_penghasilan = result[0] if result[0] else 0.0  # Jika None, ganti jadi 0.0

    # Masukkan data ke tabel laporan_karyawan
    sql_insert = """
        INSERT INTO laporan_karyawan (nama_karyawan, tanggal_laporan, total_penghasilan)
        VALUES (%s, %s, %s)
    """
    cur.execute(sql_insert, (nama_karyawan, tanggal_laporan, total_penghasilan))

    conn.commit()     # Simpan perubahan ke database
    conn.close()      # Tutup koneksi

# Fungsi untuk membaca semua data dari tabel laporan_karyawan
def read_all():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM laporan_karyawan")
    hasil = cur.fetchall()    # Ambil semua data hasil query sebagai list of tuples
    conn.close()
    return hasil

# Fungsi untuk mengedit data laporan karyawan
def edit(id_laporan, nama_karyawan, tanggal_laporan, total_penghasilan):
    conn = get_connection()
    cur = conn.cursor()
    sql = """
        UPDATE laporan_karyawan
        SET nama_karyawan=%s,
            tanggal_laporan=%s,
            total_penghasilan=%s
        WHERE id_laporan=%s
    """
    cur.execute(sql, (nama_karyawan, tanggal_laporan, total_penghasilan, id_laporan))
    conn.commit()    # Simpan perubahan
    conn.close()

# Fungsi untuk menghapus data laporan karyawan berdasarkan id_laporan
def hapus(id_laporan):
    conn = get_connection()
    cur = conn.cursor()
    sql = "DELETE FROM laporan_karyawan WHERE id_laporan=%s"
    cur.execute(sql, (id_laporan,))
    conn.commit()
    conn.close()

# Fungsi khusus untuk menghitung total penghasilan karyawan pada tanggal tertentu
def hitung_total_penghasilan(nama_karyawan, tanggal):
    conn = get_connection()
    cur = conn.cursor()
    sql = """
        SELECT SUM(harga) FROM pemesanan
        WHERE nama_karyawan = %s AND tanggal_pesan = %s
    """
    cur.execute(sql, (nama_karyawan, tanggal))
    result = cur.fetchone()    # Ambil hasil query
    conn.close()
    return result[0] if result[0] else 0.0   # Jika None, ganti jadi 0.0
