from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QTextDocument
from crud_laporan import simpan, read_all, hapus

class LaporanKaryawanWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("form_laporan.ui", self)
        self.setWindowTitle("Laporan Karyawan")

        # Hubungkan tombol ke fungsi
        self.btnhitung.clicked.connect(self.hitung_total)
        self.btnhapus.clicked.connect(self.hapus_data)
        self.btnprint.clicked.connect(self.cetak_laporan)

        # Setup tabel laporan
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels([
            "No", "ID", "Nama Karyawan", "Tanggal", "Total Penghasilan"
        ])
        self.tableWidget.verticalHeader().setVisible(False)

        # Auto resize kolom agar tampil rapi
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)

        # Load data awal dari database
        self.load_data()

    # Fungsi untuk menghitung total penghasilan dan simpan ke database
    def hitung_total(self):
        nama = self.namaKaryawanLE.text()
        tanggal = self.TanggalLaporanEdit.date().toString("yyyy-MM-dd")

        if not nama:
            QtWidgets.QMessageBox.warning(self, "Validasi", "Nama karyawan tidak boleh kosong.")
            return

        simpan(nama, tanggal)
        QtWidgets.QMessageBox.information(self, "Sukses", "Data laporan berhasil dihitung dan disimpan.")
        self.load_data()
        self.bersih()

    # Fungsi untuk memuat semua data laporan ke tabel
    def load_data(self):
        data = read_all()
        self.tableWidget.setRowCount(0)

        for index, row_data in enumerate(data, start=1):
            id_laporan, nama, tanggal, total = row_data
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)

            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(index)))         # No
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(id_laporan)))    # ID
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(nama))               # Nama Karyawan
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(tanggal)))       # Tanggal
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{total:.2f}"))     # Total Penghasilan

    # Fungsi untuk menghapus data laporan terpilih
    def hapus_data(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            id_item = self.tableWidget.item(selected_row, 1)  # Ambil kolom ID
            if id_item:
                id_laporan = int(id_item.text())
                hapus(id_laporan)
                self.load_data()
                self.bersih()

    # Fungsi untuk membersihkan form input
    def bersih(self):
        self.TanggalLaporanEdit.setDate(QDate.currentDate())
        self.TotalDS.setValue(0.0)
        self.namaKaryawanLE.clear()

    # Fungsi untuk mencetak laporan ke printer
    def cetak_laporan(self):
        printer = QPrinter()
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            doc = QTextDocument()

            # HTML untuk header dan table
            html = """
                <style>
                    table { border-collapse: collapse; width: 100%; font-family: Segoe UI; font-size: 10pt; }
                    th, td { border: 1px solid black; padding: 6px; text-align: center; }
                    th { background-color: #f0f0f0; }
                    h2 { text-align: center; }
                </style>
                <h2>Laporan Karyawan</h2>
                <table>
                    <tr>
                        <th>No</th>
                        <th>ID</th>
                        <th>Nama Karyawan</th>
                        <th>Tanggal</th>
                        <th>Total</th>
                    </tr>
            """

            # Loop isi tabel dari data di tableWidget
            for row in range(self.tableWidget.rowCount()):
                html += "<tr>"
                for col in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, col)
                    html += f"<td>{item.text() if item else ''}</td>"
                html += "</tr>"

            html += "</table>"

            # Set dan cetak dokumen
            doc.setHtml(html)
            doc.print_(printer)
