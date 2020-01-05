-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `contactsn1`
--

DROP TABLE IF EXISTS `contactsn1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contactsn1` (
  `PersonID` varchar(50) NOT NULL,
  `CompanyID` varchar(50) DEFAULT NULL,
  `FamilyID` varchar(25) DEFAULT NULL,
  `ActivityComments` text,
  `Assistant` varchar(50) DEFAULT NULL,
  `AssistantPhoneNumber` varchar(50) DEFAULT NULL,
  `CarPhoneNumber` varchar(30) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  `CompanyAcctStatus` varchar(50) DEFAULT NULL,
  `CompanyParent` varchar(100) DEFAULT NULL,
  `CompanyPhoneNumber` varchar(75) DEFAULT NULL,
  `Country` varchar(50) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  `Division` varchar(200) DEFAULT NULL,
  `DOB` varchar(50) DEFAULT NULL,
  `FamilyName` text,
  `HomeCellPhoneNumber` varchar(50) DEFAULT NULL,
  `Office800PhoneNumber` text,
  `FirstMPhone` varchar(50) DEFAULT NULL,
  `FirstName` varchar(50) DEFAULT NULL,
  `FullName` text,
  `HomeCarPhoneNumber` varchar(50) DEFAULT NULL,
  `HomeFAXPhoneNumber` varchar(50) DEFAULT NULL,
  `Interest` varchar(50) DEFAULT NULL,
  `JobTitle` varchar(150) DEFAULT NULL,
  `LabelName` varchar(50) DEFAULT NULL,
  `LastMPhone` varchar(50) DEFAULT NULL,
  `LastName` varchar(50) DEFAULT NULL,
  `MailAddress` text,
  `MailDomain` varchar(50) DEFAULT NULL,
  `MailingList` text,
  `MailName` text,
  `MailSystem` varchar(15) DEFAULT NULL,
  `Manager` varchar(50) DEFAULT NULL,
  `MiddleInitial` varchar(50) DEFAULT NULL,
  `NickName` varchar(50) DEFAULT NULL,
  `OfficeAddress1` text,
  `OfficeAddress2` varchar(100) DEFAULT NULL,
  `OfficeCity` varchar(50) DEFAULT NULL,
  `OfficeCountry` varchar(50) DEFAULT NULL,
  `OfficeFAXPhoneNumber` varchar(50) DEFAULT NULL,
  `OfficePhoneNumber` varchar(75) DEFAULT NULL,
  `OfficeState` varchar(50) DEFAULT NULL,
  `OfficeZip` varchar(25) DEFAULT NULL,
  `OMailAddress1` varchar(100) DEFAULT NULL,
  `OMailAddress2` varchar(50) DEFAULT NULL,
  `OMailCity` varchar(50) DEFAULT NULL,
  `OMailCountry` varchar(50) DEFAULT NULL,
  `OMailState` varchar(50) DEFAULT NULL,
  `OMailZip` varchar(25) DEFAULT NULL,
  `Owners` varchar(100) DEFAULT NULL,
  `PagerPhoneNumber` varchar(50) DEFAULT NULL,
  `Person800PhoneNumber` varchar(50) DEFAULT NULL,
  `PersonAddress1` varchar(100) DEFAULT NULL,
  `PersonAddress2` varchar(100) DEFAULT NULL,
  `PersonCity` varchar(50) DEFAULT NULL,
  `PersonCountry` varchar(50) DEFAULT NULL,
  `PersonFAXPhoneNumber` varchar(50) DEFAULT NULL,
  `PersonNameLFM` varchar(75) DEFAULT NULL,
  `PersonPhoneNumber` varchar(50) DEFAULT NULL,
  `PersonState` varchar(25) DEFAULT NULL,
  `PersonZip` varchar(50) DEFAULT NULL,
  `PhoneNumber` varchar(100) DEFAULT NULL,
  `PMailAddress1` varchar(50) DEFAULT NULL,
  `PMailAddress2` varchar(50) DEFAULT NULL,
  `PMailCity` varchar(50) DEFAULT NULL,
  `PMailCountry` varchar(50) DEFAULT NULL,
  `PMailState` varchar(50) DEFAULT NULL,
  `PrefObjRepID` text,
  `ReferralSource` varchar(100) DEFAULT NULL,
  `ReferredBy` varchar(100) DEFAULT NULL,
  `Rel` varchar(5) DEFAULT NULL,
  `Relationships` varchar(100) DEFAULT NULL,
  `Responsibility` varchar(25) DEFAULT NULL,
  `Salutation` varchar(50) DEFAULT NULL,
  `State` varchar(50) DEFAULT NULL,
  `Status` varchar(50) DEFAULT NULL,
  `StreetAddress` varchar(100) DEFAULT NULL,
  `Type` varchar(15) DEFAULT NULL,
  `UniversalID` varchar(50) DEFAULT NULL,
  `Zip` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`PersonID`),
  KEY `CompanyID_idx` (`CompanyID`),
  KEY `FamilyID_idx` (`FamilyID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-28 15:23:59
