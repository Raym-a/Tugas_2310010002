import sys
from PyQt5 import QtWidgets, uic
from view_karyawan import KaryawanWindow
from view_pemesanan import PemesananWindow
from view_laporan import LaporanKaryawanWindow
from view_bukutamu import BukuTamuWindow


class MenuUtama(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("mainmenu.ui", self)  # Load tampilan UI dari file mainmenu.ui
        self.setWindowTitle("Menu Utama Aplikasi Barbershop")

        # Membuat variabel di dalam class untuk menyimpan objek/jendela lain nanti.
        self.karyawan = None
        self.pemesanan_window = None
        self.laporan_window = None
        self.bukutamu_window = None

        # Hubungkan tombol di UI dengan fungsi
        self.btnPendaftaran.clicked.connect(self.buka_karyawan)
        self.btnPemesanan.clicked.connect(self.buka_pemesanan)
        self.btnLaporan.clicked.connect(self.buka_laporan)
        self.btnBukuTamu.clicked.connect(self.buka_bukutamu)

    # Fungsi membuka jendela Pendaftaran Karyawan
    def buka_karyawan(self):
        self.karyawan = KaryawanWindow()
        self.karyawan.show()

    # Fungsi membuka jendela Pemesanan
    def buka_pemesanan(self):
        self.pemesanan_window = PemesananWindow()
        self.pemesanan_window.show()

    # Fungsi membuka jendela Laporan Karyawan
    def buka_laporan(self):
        self.laporan_window = LaporanKaryawanWindow()
        self.laporan_window.show()

    # Fungsi membuka jendela Buku Tamu
    def buka_bukutamu(self):
        self.bukutamu_window = BukuTamuWindow()
        self.bukutamu_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MenuUtama()
    window.show()
    sys.exit(app.exec_())
