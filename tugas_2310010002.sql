-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 11, 2025 at 03:35 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tugas_2310010002`
--

-- --------------------------------------------------------

--
-- Table structure for table `buku_tamu`
--

CREATE TABLE `buku_tamu` (
  `id_tamu` int(11) NOT NULL,
  `nama_pengunjung` varchar(100) DEFAULT NULL,
  `tanggal_kunjungan` date DEFAULT curdate(),
  `saran` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `buku_tamu`
--

INSERT INTO `buku_tamu` (`id_tamu`, `nama_pengunjung`, `tanggal_kunjungan`, `saran`) VALUES
(3, 'Budiman', '2025-07-10', 'Jangan Berisk  dan juga terlalu panas '),
(4, 'Bebas', '2022-02-12', 'Kuang Bersih ');

-- --------------------------------------------------------

--
-- Table structure for table `laporan_karyawan`
--

CREATE TABLE `laporan_karyawan` (
  `id_laporan` int(11) NOT NULL,
  `nama_karyawan` varchar(100) DEFAULT NULL,
  `tanggal_laporan` date DEFAULT NULL,
  `total_penghasilan` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `laporan_karyawan`
--

INSERT INTO `laporan_karyawan` (`id_laporan`, `nama_karyawan`, `tanggal_laporan`, `total_penghasilan`) VALUES
(14, 'Ropani', '2000-01-01', 15000.00),
(15, 'Ray Mandanor', '2025-07-08', 35000.00),
(16, 'Ray Mandanor', '2025-01-01', 35000.00),
(18, 'Ray Mandanor', '2025-07-10', 65000.00),
(19, 'Ray Mandanor', '2025-07-10', 115000.00),
(20, 'Ray Mandanor', '2025-07-10', 65000.00),
(21, 'Mono', '2025-07-10', 50000.00);

-- --------------------------------------------------------

--
-- Table structure for table `pemesanan`
--

CREATE TABLE `pemesanan` (
  `id_pemesanan` int(11) NOT NULL,
  `nama_pelanggan` varchar(100) NOT NULL,
  `layanan` varchar(50) DEFAULT NULL,
  `tanggal_pesan` date NOT NULL,
  `jam_pesan` time NOT NULL,
  `no_hp` varchar(15) DEFAULT NULL,
  `harga` decimal(10,2) DEFAULT NULL,
  `nama_karyawan` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pemesanan`
--

INSERT INTO `pemesanan` (`id_pemesanan`, `nama_pelanggan`, `layanan`, `tanggal_pesan`, `jam_pesan`, `no_hp`, `harga`, `nama_karyawan`) VALUES
(1, 'Jidan', 'Cukur Jenggot', '2025-01-01', '12:00:00', '0093029302', 15000.00, 'Ropani'),
(7, 'Bodaman', 'Cukur Jenggot', '2025-01-01', '12:00:00', '232323', 15000.00, 'Ray Mandanor'),
(8, 'Munmun', 'Paket Komplit', '2025-07-08', '12:58:48', '323232', 50000.00, 'Ray Mandanor'),
(9, 'hjhjhj', 'Cukur Jenggot', '2025-07-09', '18:04:26', '78989789879', 15000.00, 'Ropani'),
(12, 'Yuo', 'Paket Komplit', '2025-07-10', '10:00:00', '3423432423423', 50000.00, 'Mono');

-- --------------------------------------------------------

--
-- Table structure for table `pendaftaran_karyawan`
--

CREATE TABLE `pendaftaran_karyawan` (
  `id_karyawan` int(11) NOT NULL,
  `nama_karyawan` varchar(100) NOT NULL,
  `no_hp` varchar(15) DEFAULT NULL,
  `tanggal_daftar` date DEFAULT curdate()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pendaftaran_karyawan`
--

INSERT INTO `pendaftaran_karyawan` (`id_karyawan`, `nama_karyawan`, `no_hp`, `tanggal_daftar`) VALUES
(11, 'Ray Mandanor', '0812948232', '2023-01-10'),
(17, 'Mantap', '232323', '2025-06-01'),
(19, 'Mono', '02930293283823', '2025-07-09'),
(20, 'Budiman', '92839283928392', '2025-05-12');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `buku_tamu`
--
ALTER TABLE `buku_tamu`
  ADD PRIMARY KEY (`id_tamu`);

--
-- Indexes for table `laporan_karyawan`
--
ALTER TABLE `laporan_karyawan`
  ADD PRIMARY KEY (`id_laporan`);

--
-- Indexes for table `pemesanan`
--
ALTER TABLE `pemesanan`
  ADD PRIMARY KEY (`id_pemesanan`);

--
-- Indexes for table `pendaftaran_karyawan`
--
ALTER TABLE `pendaftaran_karyawan`
  ADD PRIMARY KEY (`id_karyawan`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `buku_tamu`
--
ALTER TABLE `buku_tamu`
  MODIFY `id_tamu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `laporan_karyawan`
--
ALTER TABLE `laporan_karyawan`
  MODIFY `id_laporan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `pemesanan`
--
ALTER TABLE `pemesanan`
  MODIFY `id_pemesanan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `pendaftaran_karyawan`
--
ALTER TABLE `pendaftaran_karyawan`
  MODIFY `id_karyawan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
