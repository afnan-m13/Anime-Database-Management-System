-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 11 مايو 2024 الساعة 19:11
-- إصدار الخادم: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `finalproject`
--

-- --------------------------------------------------------

--
-- بنية الجدول `affiliated`
--

CREATE TABLE `affiliated` (
  `CID` int(11) NOT NULL,
  `Acode` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `animation`
--

CREATE TABLE `animation` (
  `SID` int(11) NOT NULL,
  `astyle` varchar(30) DEFAULT NULL,
  `Notableworks` varchar(30) DEFAULT NULL,
  `Date_joined` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `animation`
--

INSERT INTO `animation` (`SID`, `astyle`, `Notableworks`, `Date_joined`) VALUES
(100, '3d Animation', 'empty', '0000-00-00');

-- --------------------------------------------------------

--
-- بنية الجدول `anime_projects`
--

CREATE TABLE `anime_projects` (
  `Atitle` varchar(50) DEFAULT NULL,
  `Agenres` varchar(50) DEFAULT NULL,
  `Adirector` varchar(30) DEFAULT NULL,
  `Adescripition` varchar(200) DEFAULT NULL,
  `WriterDesc` varchar(200) DEFAULT NULL,
  `ADID` int(11) DEFAULT NULL,
  `Acode` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `anime_projects`
--

INSERT INTO `anime_projects` (`Atitle`, `Agenres`, `Adirector`, `Adescripition`, `WriterDesc`, `ADID`, `Acode`) VALUES
('Hotarubi no Mori e', 'Drama, Supernatural', 'Takahiro Omori', 'A six-year-old girl, Hotaru, meets Gin a boy cursed to disappear if touched\r\nin a forest.  Despite the curse\r\nthey form a close friendship.', 'Yuki Midorikawa', 2, 1),
('avatar', 'drama', 'empty', 'empty', 'empty', 3, 2),
('Attack on Titan', 'Genres Action Drama Fantasy Mystery', 'Araki Tetsurou', 'Titans once terrifying consume humans\\\r\nfor pleasure.In the present a city without titans\\\r\nfor over 100 years is destroyed by a super titan causing\\\r\nteenage boy Eren to take revenge', 'Isayama Hajime born August 1986\\\r\na Japanese manga artist His first series Attack on Titan\\\r\n2009-2022\\\r\n became one of the best selling manga series with 140M copies', 1, 1111);

-- --------------------------------------------------------

--
-- بنية الجدول `atasks`
--

CREATE TABLE `atasks` (
  `Title` varchar(50) DEFAULT NULL,
  `s_date` date DEFAULT NULL,
  `e_date` date DEFAULT NULL,
  `Task_desc` varchar(200) DEFAULT NULL,
  `TID` int(11) NOT NULL,
  `Enumber` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `atasks`
--

INSERT INTO `atasks` (`Title`, `s_date`, `e_date`, `Task_desc`, `TID`, `Enumber`) VALUES
('uploading ', '0000-00-00', '0000-00-00', 'uploading episodes', 24, 4);

-- --------------------------------------------------------

--
-- بنية الجدول `contract`
--

CREATE TABLE `contract` (
  `Sdate` date DEFAULT NULL,
  `Edate` date DEFAULT NULL,
  `payment` varchar(30) DEFAULT NULL,
  `CID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `contract`
--

INSERT INTO `contract` (`Sdate`, `Edate`, `payment`, `CID`) VALUES
('0000-00-00', '0000-00-00', '200000sr', 10);

-- --------------------------------------------------------

--
-- بنية الجدول `department`
--

CREATE TABLE `department` (
  `Dname` varchar(30) DEFAULT NULL,
  `Dgenres` varchar(50) DEFAULT NULL,
  `Doffice` varchar(30) DEFAULT NULL,
  `DID` int(11) NOT NULL,
  `SID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `department`
--

INSERT INTO `department` (`Dname`, `Dgenres`, `Doffice`, `DID`, `SID`) VALUES
('one', 'action', '1', 1, 5),
('two', 'drama', '203', 2, 1),
('three', 'romance', '32', 3, 100),
('seven', 'horror', '300', 7, 88);

-- --------------------------------------------------------

--
-- بنية الجدول `episodes`
--

CREATE TABLE `episodes` (
  `Acode` int(11) NOT NULL,
  `ESummery` varchar(200) DEFAULT NULL,
  `Etitle` varchar(50) DEFAULT NULL,
  `AirDate` date DEFAULT NULL,
  `Enumber` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `episodes`
--

INSERT INTO `episodes` (`Acode`, `ESummery`, `Etitle`, `AirDate`, `Enumber`) VALUES
(1111, '............', 'fire', '0000-00-00', 4);

-- --------------------------------------------------------

--
-- بنية الجدول `production_helpers`
--

CREATE TABLE `production_helpers` (
  `SID` int(11) NOT NULL,
  `responisibility` varchar(30) DEFAULT NULL,
  `specific_roles` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `production_helpers`
--

INSERT INTO `production_helpers` (`SID`, `responisibility`, `specific_roles`) VALUES
(1, 'productor', 'none');

-- --------------------------------------------------------

--
-- بنية الجدول `review`
--

CREATE TABLE `review` (
  `V_ID` int(11) NOT NULL,
  `E_number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `stuffmembers`
--

CREATE TABLE `stuffmembers` (
  `S_job` varchar(30) DEFAULT NULL,
  `Fname` varchar(30) DEFAULT NULL,
  `Lname` varchar(30) DEFAULT NULL,
  `SID` int(11) NOT NULL,
  `De_DID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `stuffmembers`
--

INSERT INTO `stuffmembers` (`S_job`, `Fname`, `Lname`, `SID`, `De_DID`) VALUES
('1', 'haitham', 'moh', 0, 2),
('writer', 'mona', 'ali', 1, 3),
('WRITER', 'SAMI', 'AHMAD', 5, 1),
('voice actor', 'ayah', 'naif', 88, 3),
('animation', 'Afrah', 'mohammad', 100, 3),
('director', 'jana', 'mufti', 23211, 3);

-- --------------------------------------------------------

--
-- بنية الجدول `viewers`
--

CREATE TABLE `viewers` (
  `rate` varchar(10) DEFAULT NULL,
  `VID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `viewers`
--

INSERT INTO `viewers` (`rate`, `VID`) VALUES
('22223', 10);

-- --------------------------------------------------------

--
-- بنية الجدول `voiceactor`
--

CREATE TABLE `voiceactor` (
  `SID` int(11) NOT NULL,
  `roles` varchar(30) DEFAULT NULL,
  `Vdate` date DEFAULT NULL,
  `Vrange` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `voiceactor`
--

INSERT INTO `voiceactor` (`SID`, `roles`, `Vdate`, `Vrange`) VALUES
(88, 'nitusu voice', '0000-00-00', '5');

-- --------------------------------------------------------

--
-- بنية الجدول `work_on`
--

CREATE TABLE `work_on` (
  `TID` int(11) NOT NULL,
  `SID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `affiliated`
--
ALTER TABLE `affiliated`
  ADD PRIMARY KEY (`CID`,`Acode`),
  ADD KEY `Acode` (`Acode`);

--
-- Indexes for table `animation`
--
ALTER TABLE `animation`
  ADD PRIMARY KEY (`SID`);

--
-- Indexes for table `anime_projects`
--
ALTER TABLE `anime_projects`
  ADD PRIMARY KEY (`Acode`),
  ADD KEY `fk_aprojects_department` (`ADID`);

--
-- Indexes for table `atasks`
--
ALTER TABLE `atasks`
  ADD PRIMARY KEY (`TID`,`Enumber`),
  ADD KEY `Enumber` (`Enumber`);

--
-- Indexes for table `contract`
--
ALTER TABLE `contract`
  ADD PRIMARY KEY (`CID`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`DID`),
  ADD KEY `SID` (`SID`);

--
-- Indexes for table `episodes`
--
ALTER TABLE `episodes`
  ADD PRIMARY KEY (`Enumber`,`Acode`),
  ADD KEY `Acode` (`Acode`);

--
-- Indexes for table `production_helpers`
--
ALTER TABLE `production_helpers`
  ADD PRIMARY KEY (`SID`);

--
-- Indexes for table `review`
--
ALTER TABLE `review`
  ADD PRIMARY KEY (`V_ID`,`E_number`),
  ADD KEY `E_number` (`E_number`);

--
-- Indexes for table `stuffmembers`
--
ALTER TABLE `stuffmembers`
  ADD PRIMARY KEY (`SID`),
  ADD KEY `De_DID` (`De_DID`);

--
-- Indexes for table `viewers`
--
ALTER TABLE `viewers`
  ADD PRIMARY KEY (`VID`);

--
-- Indexes for table `voiceactor`
--
ALTER TABLE `voiceactor`
  ADD PRIMARY KEY (`SID`);

--
-- Indexes for table `work_on`
--
ALTER TABLE `work_on`
  ADD PRIMARY KEY (`TID`,`SID`),
  ADD KEY `SID` (`SID`);

--
-- قيود الجداول المُلقاة.
--

--
-- قيود الجداول `affiliated`
--
ALTER TABLE `affiliated`
  ADD CONSTRAINT `affiliated_ibfk_1` FOREIGN KEY (`CID`) REFERENCES `contract` (`CID`),
  ADD CONSTRAINT `affiliated_ibfk_2` FOREIGN KEY (`Acode`) REFERENCES `anime_projects` (`Acode`);

--
-- قيود الجداول `animation`
--
ALTER TABLE `animation`
  ADD CONSTRAINT `animation_ibfk_1` FOREIGN KEY (`SID`) REFERENCES `stuffmembers` (`SID`);

--
-- قيود الجداول `anime_projects`
--
ALTER TABLE `anime_projects`
  ADD CONSTRAINT `fk_aprojects_department` FOREIGN KEY (`ADID`) REFERENCES `department` (`DID`);

--
-- قيود الجداول `atasks`
--
ALTER TABLE `atasks`
  ADD CONSTRAINT `atasks_ibfk_1` FOREIGN KEY (`Enumber`) REFERENCES `episodes` (`Enumber`);

--
-- قيود الجداول `department`
--
ALTER TABLE `department`
  ADD CONSTRAINT `department_ibfk_1` FOREIGN KEY (`SID`) REFERENCES `stuffmembers` (`SID`);

--
-- قيود الجداول `episodes`
--
ALTER TABLE `episodes`
  ADD CONSTRAINT `episodes_ibfk_1` FOREIGN KEY (`Acode`) REFERENCES `anime_projects` (`Acode`);

--
-- قيود الجداول `production_helpers`
--
ALTER TABLE `production_helpers`
  ADD CONSTRAINT `production_helpers_ibfk_1` FOREIGN KEY (`SID`) REFERENCES `stuffmembers` (`SID`);

--
-- قيود الجداول `review`
--
ALTER TABLE `review`
  ADD CONSTRAINT `review_ibfk_1` FOREIGN KEY (`E_number`) REFERENCES `episodes` (`Enumber`),
  ADD CONSTRAINT `review_ibfk_2` FOREIGN KEY (`V_ID`) REFERENCES `viewers` (`VID`);

--
-- قيود الجداول `stuffmembers`
--
ALTER TABLE `stuffmembers`
  ADD CONSTRAINT `stuffmembers_ibfk_1` FOREIGN KEY (`De_DID`) REFERENCES `department` (`DID`);

--
-- قيود الجداول `voiceactor`
--
ALTER TABLE `voiceactor`
  ADD CONSTRAINT `voiceactor_ibfk_1` FOREIGN KEY (`SID`) REFERENCES `stuffmembers` (`SID`);

--
-- قيود الجداول `work_on`
--
ALTER TABLE `work_on`
  ADD CONSTRAINT `work_on_ibfk_1` FOREIGN KEY (`TID`) REFERENCES `atasks` (`TID`),
  ADD CONSTRAINT `work_on_ibfk_2` FOREIGN KEY (`SID`) REFERENCES `stuffmembers` (`SID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
