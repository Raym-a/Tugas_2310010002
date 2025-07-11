from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate
from crud_Karyawan import simpan, edit, hapus, read_all

class KaryawanWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("form_karyawan.ui", self)  # Load UI dari file form_karyawan.ui
        self.setWindowTitle("Pendaftaran Karyawan")
        self.selected_id = None              # Menyimpan ID karyawan yang sedang dipilih
        self.data_ids = []                   # List untuk menyimpan ID dari setiap baris tabel

        # Setup tabel
        self.tblkaryawan.setColumnCount(4)
        self.tblkaryawan.setHorizontalHeaderLabels(["No", "Nama", "Telepon", "Tanggal Daftar"])
        self.tblkaryawan.verticalHeader().setVisible(False)

        # Agar kolom otomatis menyesuaikan ukuran
        self.tblkaryawan.horizontalHeader().setStretchLastSection(True)
        self.tblkaryawan.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Hubungkan tombol dengan fungsi
        self.btnsimpan.clicked.connect(self.simpanData)
        self.btnedit.clicked.connect(self.ubahData)
        self.btnhapus.clicked.connect(self.hapusData)
        self.btnbersih.clicked.connect(self.clear_form)
        self.tblkaryawan.itemSelectionChanged.connect(self.select_row)

        # Muat data awal ke tabel
        self.load_data()

    # Fungsi untuk memuat data karyawan ke tabel
    def load_data(self):
        self.tblkaryawan.setRowCount(0)  # Kosongkan tabel dulu
        self.data_ids = []              # Kosongkan daftar ID

        for index, row_data in enumerate(read_all(), start=1):
            id_karyawan, nama, no_hp, tanggal = row_data
            row = self.tblkaryawan.rowCount()
            self.tblkaryawan.insertRow(row)

            # Isi kolom tabel
            self.tblkaryawan.setItem(row, 0, QtWidgets.QTableWidgetItem(str(index)))  # Nomor urut
            self.tblkaryawan.setItem(row, 1, QtWidgets.QTableWidgetItem(nama))
            self.tblkaryawan.setItem(row, 2, QtWidgets.QTableWidgetItem(no_hp))
            self.tblkaryawan.setItem(row, 3, QtWidgets.QTableWidgetItem(str(tanggal)))

            # Simpan ID karyawan di list agar mudah dipakai saat edit/hapus
            self.data_ids.append(id_karyawan)

    # Fungsi untuk menyimpan data baru
    def simpanData(self):
        nama = self.namaKaryawanLE.text()
        no_hp = self.noHpLE.text()
        tanggal = self.dateEdit.date().toString("yyyy-MM-dd")

        if nama and no_hp:
            simpan(nama, no_hp, tanggal)
            QtWidgets.QMessageBox.information(self, "Info", "Data berhasil disimpan")
            self.clear_form()
            self.load_data()
        else:
            QtWidgets.QMessageBox.warning(self, "Peringatan", "Semua field harus diisi.")

    # Fungsi yang dipanggil saat baris di tabel dipilih
    def select_row(self):
        selected_row = self.tblkaryawan.currentRow()
        if selected_row >= 0:
            try:
                # Ambil ID karyawan sesuai baris terpilih
                self.selected_id = self.data_ids[selected_row]
                self.namaKaryawanLE.setText(self.tblkaryawan.item(selected_row, 1).text())
                self.noHpLE.setText(self.tblkaryawan.item(selected_row, 2).text())
                tanggal_str = self.tblkaryawan.item(selected_row, 3).text()
                self.dateEdit.setDate(QDate.fromString(tanggal_str, "yyyy-MM-dd"))
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Error", f"Gagal memilih data:\n{str(e)}")

    # Fungsi untuk mengedit data yang sudah ada
    def ubahData(self):
        if self.selected_id:
            nama = self.namaKaryawanLE.text()
            no_hp = self.noHpLE.text()
            tanggal = self.dateEdit.date().toString("yyyy-MM-dd")

            if nama and no_hp:
                edit(self.selected_id, nama, no_hp, tanggal)
                QtWidgets.QMessageBox.information(self, "Info", "Data berhasil diubah")
                self.clear_form()
                self.load_data()
            else:
                QtWidgets.QMessageBox.warning(self, "Peringatan", "Field tidak boleh kosong.")
        else:
            QtWidgets.QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin diubah.")

    # Fungsi untuk menghapus data
    def hapusData(self):
        if self.selected_id:
            hapus(self.selected_id)
            QtWidgets.QMessageBox.information(self, "Info", "Data berhasil dihapus")
            self.clear_form()
            self.load_data()
        else:
            QtWidgets.QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus.")

    # Fungsi untuk membersihkan form input
    def clear_form(self):
        self.namaKaryawanLE.clear()
        self.noHpLE.clear()
        self.dateEdit.setDate(QDate.currentDate())
        self.selected_id = None
        self.tblkaryawan.clearSelection()
