-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 19, 2021 at 07:40 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vvc`
--

-- --------------------------------------------------------

--
-- Table structure for table `report`
--

CREATE TABLE `report` (
  `runindex` int(11) NOT NULL COMMENT 'running index',
  `myusername` text COLLATE utf8_bin NOT NULL COMMENT 'name should be unique',
  `myfullname` text COLLATE utf8_bin DEFAULT NULL COMMENT 'Full name',
  `myoffice` text COLLATE utf8_bin DEFAULT NULL COMMENT 'occupation',
  `myorg` text COLLATE utf8_bin DEFAULT NULL COMMENT 'name of organization',
  `myphone` text COLLATE utf8_bin DEFAULT NULL COMMENT 'static phone number',
  `mymobile` text COLLATE utf8_bin DEFAULT NULL COMMENT 'mobile phone number',
  `myemail` text COLLATE utf8_bin DEFAULT NULL COMMENT 'email',
  `mywebsite` text COLLATE utf8_bin DEFAULT NULL COMMENT 'website address',
  `myaddress` text COLLATE utf8_bin DEFAULT NULL COMMENT 'physical address'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `report`
--

INSERT INTO `report` (`runindex`, `myusername`, `myfullname`, `myoffice`, `myorg`, `myphone`, `mymobile`, `myemail`, `mywebsite`, `myaddress`) VALUES
(1, 'username', 'User Full Name', 'User Job', 'User Organization', '012345678', '0501234567', 'usermail@myorg.co.il', 'www.myorg.co.il', 'My Street 1, MyCity, MyCountry');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `report`
--
ALTER TABLE `report`
  ADD PRIMARY KEY (`runindex`),
  ADD UNIQUE KEY `myname` (`myusername`) USING HASH;

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `report`
--
ALTER TABLE `report`
  MODIFY `runindex` int(11) NOT NULL AUTO_INCREMENT COMMENT 'running index', AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
