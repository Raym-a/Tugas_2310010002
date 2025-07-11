from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate, QTime
from crud_pemesanan import simpan, edit, hapus, read_all
from crud_Karyawan import read_nama_karyawan

class PemesananWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("form_pemesanan.ui", self)
        self.setWindowTitle("Form Pemesanan")
        self.selected_id = None
        self.data_ids = []  # List untuk menyimpan id_pemesanan, agar tidak tampil di tabel tapi tetap diketahui

        # Set kolom tabel
        self.tblpemesanan.setColumnCount(8)
        self.tblpemesanan.setHorizontalHeaderLabels([
            "No", "Nama Pelanggan", "Layanan", "Tanggal", "Jam", "Telepon", "Harga", "Barber"
        ])
        self.tblpemesanan.verticalHeader().setVisible(False)

        # Auto resize kolom tabel supaya tampil rapi
        header = self.tblpemesanan.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)

        # Inisialisasi daftar layanan dan harga
        self.layanan_harga = {
            "Potong Rambut": 25000,
            "Cukur Jenggot": 15000,
            "Cuci Rambut": 20000,
            "Paket Komplit": 50000
        }
        # Tambahkan daftar layanan ke combo box
        self.layananCB.addItems(self.layanan_harga.keys())
        # Set harga otomatis saat layanan berubah
        self.layananCB.currentTextChanged.connect(self.set_harga_otomatis)

        # Load nama karyawan/barber ke combo box
        self.load_nama_karyawan()

        # Hubungkan tombol dengan fungsi
        self.btnsimpan.clicked.connect(self.aksi_simpan)
        self.btnedit.clicked.connect(self.aksi_edit)
        self.btnhapus.clicked.connect(self.aksi_hapus)
        self.btnbersih.clicked.connect(self.clear_form)
        self.tblpemesanan.itemSelectionChanged.connect(self.select_row)

        # Load data awal ke tabel
        self.load_data()

    # Fungsi untuk otomatis set harga sesuai layanan yang dipilih
    def set_harga_otomatis(self, layanan):
        harga = self.layanan_harga.get(layanan, 0)
        self.hargaSB.setValue(harga)

    # Fungsi untuk load data pemesanan dari database ke tabel
    def load_data(self):
        self.tblpemesanan.setRowCount(0)  # Kosongkan tabel dulu
        self.data_ids.clear()  # Kosongkan list ID

        for index, row_data in enumerate(read_all(), start=1):
            id_pemesanan = row_data[0]
            self.data_ids.append(id_pemesanan)  # Simpan id ke list

            row = self.tblpemesanan.rowCount()
            self.tblpemesanan.insertRow(row)

            # Isi kolom tabel sesuai urutan
            self.tblpemesanan.setItem(row, 0, QtWidgets.QTableWidgetItem(str(index)))  # No
            self.tblpemesanan.setItem(row, 1, QtWidgets.QTableWidgetItem(str(row_data[1])))  # Nama
            self.tblpemesanan.setItem(row, 2, QtWidgets.QTableWidgetItem(str(row_data[2])))  # Layanan
            self.tblpemesanan.setItem(row, 3, QtWidgets.QTableWidgetItem(str(row_data[3])))  # Tanggal
            self.tblpemesanan.setItem(row, 4, QtWidgets.QTableWidgetItem(str(row_data[4])))  # Jam
            self.tblpemesanan.setItem(row, 5, QtWidgets.QTableWidgetItem(str(row_data[5])))  # Telepon
            self.tblpemesanan.setItem(row, 6, QtWidgets.QTableWidgetItem(str(row_data[6])))  # Harga
            self.tblpemesanan.setItem(row, 7, QtWidgets.QTableWidgetItem(str(row_data[7])))  # Barber

    # Fungsi untuk menyimpan data baru ke database
    def aksi_simpan(self):
        try:
            nama = self.namaPelangganLE.text()
            layanan = self.layananCB.currentText()
            tanggal = self.TanggalPesanLE.date().toString("yyyy-MM-dd")
            jam = self.JamPesanTE.time().toString("HH:mm:ss")
            no_hp = self.noHPLE.text()
            harga = self.hargaSB.value()
            karyawan = self.PilihBarberCB.currentText()

            if nama and no_hp:
                simpan(nama, layanan, tanggal, jam, no_hp, harga, karyawan)
                QtWidgets.QMessageBox.information(self, "Info", "Pemesanan berhasil disimpan.")
                self.clear_form()
                self.load_data()
            else:
                QtWidgets.QMessageBox.warning(self, "Peringatan", "Nama dan No HP wajib diisi.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "ERROR", f"Gagal menyimpan:\n{str(e)}")

    # Fungsi saat memilih baris di tabel → isi form dengan data yg dipilih
    def select_row(self):
        selected_row = self.tblpemesanan.currentRow()
        if selected_row >= 0 and selected_row < len(self.data_ids):
            self.selected_id = self.data_ids[selected_row]
            self.namaPelangganLE.setText(self.tblpemesanan.item(selected_row, 1).text())
            self.layananCB.setCurrentText(self.tblpemesanan.item(selected_row, 2).text())
            self.TanggalPesanLE.setDate(QDate.fromString(self.tblpemesanan.item(selected_row, 3).text(), "yyyy-MM-dd"))
            self.JamPesanTE.setTime(QTime.fromString(self.tblpemesanan.item(selected_row, 4).text(), "HH:mm:ss"))
            self.noHPLE.setText(self.tblpemesanan.item(selected_row, 5).text())
            self.hargaSB.setValue(float(self.tblpemesanan.item(selected_row, 6).text()))
            self.PilihBarberCB.setCurrentText(self.tblpemesanan.item(selected_row, 7).text())

    # Fungsi untuk edit/update data
    def aksi_edit(self):
        if self.selected_id:
            nama = self.namaPelangganLE.text()
            layanan = self.layananCB.currentText()
            tanggal = self.TanggalPesanLE.date().toString("yyyy-MM-dd")
            jam = self.JamPesanTE.time().toString("HH:mm:ss")
            no_hp = self.noHPLE.text()
            harga = self.hargaSB.value()
            karyawan = self.PilihBarberCB.currentText()

            if nama and no_hp:
                edit(self.selected_id, nama, layanan, tanggal, jam, no_hp, harga, karyawan)
                QtWidgets.QMessageBox.information(self, "Info", "Data berhasil diubah.")
                self.clear_form()
                self.load_data()
            else:
                QtWidgets.QMessageBox.warning(self, "Peringatan", "Nama dan No HP wajib diisi.")
        else:
            QtWidgets.QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin diubah.")

    # Fungsi untuk hapus data
    def aksi_hapus(self):
        if self.selected_id:
            hapus(self.selected_id)
            QtWidgets.QMessageBox.information(self, "Info", "Data berhasil dihapus.")
            self.clear_form()
            self.load_data()
        else:
            QtWidgets.QMessageBox.warning(self, "Peringatan", "Pilih data terlebih dahulu.")

    # Fungsi untuk membersihkan form input
    def clear_form(self):
        self.namaPelangganLE.clear()
        self.layananCB.setCurrentIndex(0)
        self.TanggalPesanLE.setDate(QDate.currentDate())
        self.JamPesanTE.setTime(QTime.currentTime())
        self.noHPLE.clear()
        self.hargaSB.setValue(0.0)
        self.PilihBarberCB.setCurrentIndex(0)
        self.selected_id = None
        self.tblpemesanan.clearSelection()

    # Fungsi untuk load nama karyawan/barber ke combo box
    def load_nama_karyawan(self):
        self.PilihBarberCB.clear()
        daftar_karyawan = read_nama_karyawan()
        self.PilihBarberCB.addItems(daftar_karyawan)

