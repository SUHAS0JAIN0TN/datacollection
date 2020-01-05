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
-- Table structure for table `locationsn1`
--

DROP TABLE IF EXISTS `locationsn1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locationsn1` (
  `CompanyID` varchar(25) NOT NULL,
  `FamilyID` varchar(100) DEFAULT NULL,
  `PersonID` varchar(50) DEFAULT NULL,
  `ParentID` varchar(50) DEFAULT NULL,
  `PrevFamilyID` varchar(50) DEFAULT NULL,
  `AbbBillingNotes` text,
  `AgreementDate` text,
  `avg_invoice` varchar(50) DEFAULT NULL,
  `BillingNotes` text,
  `City` varchar(50) DEFAULT NULL,
  `coFEIN` varchar(15) DEFAULT NULL,
  `CompanyAcctExec` varchar(15) DEFAULT NULL,
  `CompanyAcctTeam` varchar(15) DEFAULT NULL,
  `CompanyClass` text,
  `CompanyCounty` text,
  `CompanyCredit` varchar(10) DEFAULT NULL,
  `CompanyDiscount` varchar(5) DEFAULT NULL,
  `CompanyEmpl` varchar(5) DEFAULT NULL,
  `CompanyIndustry` varchar(50) DEFAULT NULL,
  `CompanyInsAgree` varchar(5) DEFAULT NULL,
  `CompanyLat` text,
  `CompanyLong` text,
  `CompanyMPhone` varchar(50) DEFAULT NULL,
  `CompanyName` varchar(100) DEFAULT NULL,
  `CompanyNameCheck` text,
  `CompanyNumber` text,
  `CompanySales` varchar(20) DEFAULT NULL,
  `CompanySearch` text,
  `CompanySIC` text,
  `CompanyTerritory` text,
  `CompanyType` varchar(25) DEFAULT NULL,
  `CompanyURL` varchar(100) DEFAULT NULL,
  `CompanyYears` varchar(5) DEFAULT NULL,
  `count_invoice` varchar(10) DEFAULT NULL,
  `count_quotes` varchar(10) DEFAULT NULL,
  `Country` varchar(25) DEFAULT NULL,
  `Created` varchar(25) DEFAULT NULL,
  `DUNS` varchar(25) DEFAULT NULL,
  `FamilyJoinDate` text,
  `FamilyName` text,
  `FamilyNotes` text,
  `first_invoice` text,
  `gap_invoice` varchar(15) DEFAULT NULL,
  `IndustryCode` varchar(15) DEFAULT NULL,
  `last_invoice` text,
  `LastAccessed` text,
  `LastModified` text,
  `lineitems` text,
  `LitigationSampleText` text,
  `LitigationSampleTypes` text,
  `Location` varchar(50) DEFAULT NULL,
  `MailAddress1` text,
  `MailAddress2` varchar(25) DEFAULT NULL,
  `MailCity` varchar(25) DEFAULT NULL,
  `MailCountry` varchar(25) DEFAULT NULL,
  `MailState` varchar(15) DEFAULT NULL,
  `MailZip` varchar(15) DEFAULT NULL,
  `Office800PhoneNumber` varchar(50) DEFAULT NULL,
  `OfficeAddress1` text,
  `OfficeAddress2` text,
  `OfficeFAXPhoneNumber` varchar(25) DEFAULT NULL,
  `OfficePhoneNumber` varchar(100) DEFAULT NULL,
  `OtherNames` text,
  `OtherNamesMPhone` varchar(75) DEFAULT NULL,
  `PaymentTerms` varchar(25) DEFAULT NULL,
  `PrefObjRepID` text,
  `PrelimDataRvw` varchar(5) DEFAULT NULL,
  `PrevFamilyJoinDate` text,
  `ReferralSource` varchar(35) DEFAULT NULL,
  `ReferredBy` varchar(50) DEFAULT NULL,
  `Rel` varchar(5) DEFAULT NULL,
  `SendHardCopyRpt` varchar(5) DEFAULT NULL,
  `State` varchar(35) DEFAULT NULL,
  `SurchargeDesc` text,
  `SurchargePrice` text,
  `Type` varchar(15) DEFAULT NULL,
  `UniversalID` varchar(50) DEFAULT NULL,
  `UserNameList` text,
  `Zip` varchar(50) DEFAULT NULL,
  `Note1_Desc` text,
  `Note1_Name` text,
  `Note2_Desc` text,
  `Note2_Name` text,
  `Note3_Desc` text,
  `Note3_Name` text,
  `Note4_Desc` text,
  `Note4_Name` text,
  `Note5_Desc` text,
  `Note5_Name` text,
  `Note6_Desc` text,
  `Note6_Name` text,
  PRIMARY KEY (`CompanyID`),
  KEY `PersonID_idx` (`PersonID`)
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
