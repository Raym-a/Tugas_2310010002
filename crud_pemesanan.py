from koneksi import get_connection

# Fungsi untuk menyimpan data pemesanan baru ke tabel pemesanan
def simpan(nama_pelanggan, layanan, tanggal_pesan, jam_pesan, no_hp, harga, nama_karyawan):
    conn = get_connection()  # Membuka koneksi ke database
    cursor = conn.cursor()   # Membuat cursor untuk menjalankan query
    sql = """
        INSERT INTO pemesanan (
            nama_pelanggan, layanan, tanggal_pesan, jam_pesan, no_hp, harga, nama_karyawan
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (nama_pelanggan, layanan, tanggal_pesan, jam_pesan, no_hp, harga, nama_karyawan))
    conn.commit()  # Simpan perubahan ke database
    conn.close()   # Tutup koneksi

# Fungsi untuk membaca semua data dari tabel pemesanan
def read_all():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT id_pemesanan, nama_pelanggan, layanan, tanggal_pesan, jam_pesan, no_hp, harga, nama_karyawan
        FROM pemesanan
    """)
    result = cur.fetchall()
    conn.close()
    return result

# Fungsi untuk mengedit / memperbarui data pemesanan
def edit(id_pemesanan, nama_pelanggan, layanan, tanggal_pesan, jam_pesan, no_hp, harga, nama_karyawan):
    conn = get_connection()
    cur = conn.cursor()
    sql = """
        UPDATE pemesanan
        SET nama_pelanggan=%s,
            layanan=%s,
            tanggal_pesan=%s,
            jam_pesan=%s,
            no_hp=%s,
            harga=%s,
            nama_karyawan=%s
        WHERE id_pemesanan=%s
    """
    cur.execute(sql, (nama_pelanggan, layanan, tanggal_pesan, jam_pesan, no_hp, harga, nama_karyawan, id_pemesanan))
    conn.commit()
    conn.close()

# Fungsi untuk menghapus data pemesanan berdasarkan ID
def hapus(id_pemesanan):
    conn = get_connection()
    cur = conn.cursor()
    sql = "DELETE FROM pemesanan WHERE id_pemesanan=%s"
    cur.execute(sql, (id_pemesanan,))
    conn.commit()
    conn.close()
