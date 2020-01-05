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
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locations` (
  `CompanyID` varchar(50) NOT NULL,
  `FamilyID` varchar(100) DEFAULT NULL,
  `PersonID` varchar(50) DEFAULT NULL,
  `ParentID` varchar(50) DEFAULT NULL,
  `PrevFamilyID` varchar(50) DEFAULT NULL,
  `AbbBillingNotes` text,
  `Affiliates1` text,
  `Affiliates2` text,
  `AffiliatesSummaryInfo1` text,
  `AffiliatesSummaryInfo2` text,
  `AgreementDate` text,
  `AuthorDate` text,
  `AuthorName` text,
  `Authors` text,
  `avg_invoice` text,
  `BillingNotes` text,
  `City` text,
  `coFEIN` text,
  `Comment` text,
  `CompanyAcctExec` text,
  `CompanyAcctTeam` text,
  `CompanyClass` text,
  `CompanyCounty` text,
  `CompanyCredit` text,
  `CompanyDiscount` text,
  `CompanyEmpl` text,
  `CompanyIndustry` text,
  `CompanyInsAgree` text,
  `CompanyLat` text,
  `CompanyLong` text,
  `CompanyMPhone` text,
  `CompanyName` text,
  `CompanyNameCheck` text,
  `CompanyNumber` text,
  `CompanySales` text,
  `CompanySearch` text,
  `CompanySIC` text,
  `CompanyTerritory` text,
  `CompanyType` text,
  `CompanyURL` text,
  `CompanyYears` text,
  `count_invoice` text,
  `count_quotes` text,
  `Country` text,
  `Created` text,
  `DUNS` text,
  `EditAuthors` text,
  `EditCount` text,
  `EditDateName` text,
  `EditDates` text,
  `Edited` text,
  `EditNames` text,
  `Edits` text,
  `FamilyJoinDate` text,
  `FamilyName` text,
  `FamilyNotes` text,
  `first_invoice` text,
  `gap_invoice` text,
  `HasFamilyDefinition` text,
  `HistoricalNotes` text,
  `IndustryCode` text,
  `last_invoice` text,
  `LastAccessed` text,
  `LastModified` text,
  `lineitems` text,
  `LitigationSampleText` text,
  `LitigationSampleTypes` text,
  `Location` text,
  `MailAddress1` text,
  `MailAddress2` text,
  `MailCity` text,
  `MailCountry` text,
  `MailState` text,
  `MailZip` text,
  `Note1_Desc` text,
  `Office800PhoneNumber` text,
  `OfficeAddress1` text,
  `OfficeAddress2` text,
  `OfficeFAXPhoneNumber` text,
  `OfficePhoneNumber` text,
  `OtherNames` text,
  `OtherNamesMPhone` text,
  `PaymentTerms` text,
  `PrefObjRepID` text,
  `PrelimDataRvw` text,
  `PrevFamilyJoinDate` text,
  `ReferralSource` text,
  `ReferredBy` text,
  `Rel` text,
  `SendHardCopyRpt` text,
  `State` text,
  `SurchargeDesc` text,
  `SurchargePrice` text,
  `Type` text,
  `UniversalID` varchar(50) DEFAULT NULL,
  `UserNameList` text,
  `Zip` varchar(50) DEFAULT NULL,
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
  PRIMARY KEY (`CompanyID`)
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
