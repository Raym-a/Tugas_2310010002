
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox
from crud_bukutamu import simpan, read_all, hapus

class BukuTamuWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("form_bukutamu.ui", self)
        self.setWindowTitle("Buku Tamu")
        self.selected_id = None  # Menyimpan ID tamu yang sedang dipilih

        # Setup tabel untuk menampilkan data buku tamu
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Nama", "Tanggal", "Saran"])
        self.tableWidget.verticalHeader().setVisible(False)

        # Auto resize kolom agar tabel terlihat rapi
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)

        # Load data dari database saat form dibuka
        self.load_data()

        # Hubungkan tombol ke fungsi
        self.btnsimpan.clicked.connect(self.simpan_data)
        self.btnhapus.clicked.connect(self.hapus_data)
        self.btnbersih.clicked.connect(self.bersih)
        self.tableWidget.itemSelectionChanged.connect(self.pilih_baris)

    # Fungsi untuk load semua data dari database ke tabel
    def load_data(self):
        self.tableWidget.setRowCount(0)  # Bersihkan isi tabel dulu
        for row_data in read_all():  # Ambil data dari database
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for col, data in enumerate(row_data):
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(data)))

    # Fungsi untuk menyimpan data baru ke database
    def simpan_data(self):
        nama = self.namaPengunjungLE.text()
        tanggal = self.TanggalKunjunganEdit.date().toString("yyyy-MM-dd")
        saran = self.SaranLE.text()

        if nama and saran:
            simpan(nama, tanggal, saran)  # Simpan ke database
            self.load_data()  # Refresh tabel
            self.bersih()     # Kosongkan form input
        else:
            QMessageBox.warning(self, "Input Kosong", "Nama dan Saran tidak boleh kosong.")

    # Fungsi untuk menghapus data berdasarkan ID yang dipilih
    def hapus_data(self):
        if self.selected_id:
            hapus(self.selected_id)  # Hapus dari database
            self.load_data()        # Refresh tabel
            self.bersih()           # Kosongkan form input

    # Fungsi saat memilih baris di tabel → menampilkan datanya di form
    def pilih_baris(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            id_item = self.tableWidget.item(selected_row, 0)
            if id_item:
                self.selected_id = int(id_item.text())
                self.namaPengunjungLE.setText(self.tableWidget.item(selected_row, 1).text())
                tanggal = self.tableWidget.item(selected_row, 2).text()
                self.TanggalKunjunganEdit.setDate(QDate.fromString(tanggal, "yyyy-MM-dd"))
                self.SaranLE.setText(self.tableWidget.item(selected_row, 3).text())

    # Fungsi untuk membersihkan form input
    def bersih(self):
        self.namaPengunjungLE.clear()
        self.TanggalKunjunganEdit.setDate(QDate.currentDate())
        self.SaranLE.clear()
        self.selected_id = None
