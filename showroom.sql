-- phpMyAdmin SQL Dump
-- version 3.2.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 19, 2018 at 04:39 PM
-- Server version: 5.1.41
-- PHP Version: 5.3.1

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `showroom`
--

-- --------------------------------------------------------

--
-- Table structure for table `sales`
--

CREATE TABLE IF NOT EXISTS `sales` (
  `invoiceNumber` int(6) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `modelName` varchar(50) NOT NULL,
  `onRoadPrice` double NOT NULL,
  `consumerName` varchar(50) NOT NULL,
  `address` varchar(200) NOT NULL,
  `paymentMode` varchar(30) NOT NULL,
  `mobileNumber` bigint(10) NOT NULL,
  `paid` int(6) NOT NULL,
  PRIMARY KEY (`invoiceNumber`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `sales`
--

INSERT INTO `sales` (`invoiceNumber`, `date`, `modelName`, `onRoadPrice`, `consumerName`, `address`, `paymentMode`, `mobileNumber`, `paid`) VALUES
(1, '2018-02-18', 'Avenger Cruise', 98790, 'Razak Mohamed', 'Ponnammapet,Salem', 'EMI', 9677520692, 38000),
(2, '2018-02-17', 'Avenger Cruise', 98790, 'Mohamed', 'Ponnammapet,Salem', 'DownPayment', 9677520692, 100000),
(3, '2018-02-18', 'Avenger Street', 78908, 'Mohamed', 'Salem', 'DownPayment', 9677520692, 80000),
(4, '2018-01-26', 'Avenger Street', 78908, 'Razak', 'SAlem', 'EMI', 9597334782, 80000),
(5, '2018-02-19', 'Avenger Street', 78908, 'Gokul', 'Salem', 'DownPayment', 987654567, 80000);

-- --------------------------------------------------------

--
-- Table structure for table `vehicle`
--

CREATE TABLE IF NOT EXISTS `vehicle` (
  `modelName` varchar(50) NOT NULL,
  `type` varchar(20) NOT NULL,
  `modelYear` int(4) NOT NULL,
  `engineCapacity` int(4) NOT NULL,
  `averageMilage` int(2) NOT NULL,
  `quantity` int(4) NOT NULL,
  `warrenty` int(2) NOT NULL,
  `onRoadPrice` double NOT NULL,
  PRIMARY KEY (`modelName`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vehicle`
--

INSERT INTO `vehicle` (`modelName`, `type`, `modelYear`, `engineCapacity`, `averageMilage`, `quantity`, `warrenty`, `onRoadPrice`) VALUES
('Avenger Cruise', 'Gear', 2016, 220, 45, 19, 5, 98790),
('Avenger Street', 'Gear', 2017, 150, 40, 7, 5, 78908);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
