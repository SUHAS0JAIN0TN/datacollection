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
-- Table structure for table `invoice_billingn1`
--

DROP TABLE IF EXISTS `invoice_billingn1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoice_billingn1` (
  `ProjectNumber` varchar(30) DEFAULT NULL,
  `ProjID` varchar(30) DEFAULT NULL,
  `AcctNotes` text,
  `Address1` varchar(100) DEFAULT NULL,
  `Address2` varchar(100) DEFAULT NULL,
  `AuthorDate` varchar(50) DEFAULT NULL,
  `AuthorName` varchar(50) DEFAULT NULL,
  `Authors` varchar(50) DEFAULT NULL,
  `BilledYN` varchar(30) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  `companyname` varchar(100) DEFAULT NULL,
  `ContactName` varchar(50) DEFAULT NULL,
  `ContactNumber` varchar(60) DEFAULT NULL,
  `Country` varchar(30) DEFAULT NULL,
  `DateDue` varchar(30) DEFAULT NULL,
  `DateReceived` varchar(30) DEFAULT NULL,
  `DocID` varchar(30) DEFAULT NULL,
  `EMail` varchar(100) DEFAULT NULL,
  `EmbeddedObjects` blob,
  `FamilyID` varchar(30) DEFAULT NULL,
  `FamilyName` varchar(125) DEFAULT NULL,
  `Fax` varchar(50) DEFAULT NULL,
  `HasMissedOpportunity` varchar(10) DEFAULT NULL,
  `InvAmt` varchar(30) DEFAULT NULL,
  `InvCity` varchar(50) DEFAULT NULL,
  `InvCompanyName` varchar(100) DEFAULT NULL,
  `InvCountry` varchar(30) DEFAULT NULL,
  `InvDate` varchar(30) DEFAULT NULL,
  `InvDisc` varchar(30) DEFAULT NULL,
  `InvFamilyID` varchar(30) DEFAULT NULL,
  `InvDesc` text,
  `InvFamilyName` varchar(100) DEFAULT NULL,
  `InvLocationID` varchar(30) DEFAULT NULL,
  `InvoiceDate` varchar(30) DEFAULT NULL,
  `InvPersonID` varchar(30) DEFAULT NULL,
  `InvQty` varchar(30) DEFAULT NULL,
  `InvRate` varchar(30) DEFAULT NULL,
  `InvState` varchar(30) DEFAULT NULL,
  `InvTotal` varchar(30) DEFAULT NULL,
  `LocationID` varchar(30) DEFAULT NULL,
  `MissCategory` varchar(100) DEFAULT NULL,
  `MissDescription` text,
  `MissEstimate` varchar(30) DEFAULT NULL,
  `MissLineItems` text,
  `Note1_Desc` varchar(30) DEFAULT NULL,
  `Note1_Name` varchar(30) DEFAULT NULL,
  `Note2_Desc` varchar(30) DEFAULT NULL,
  `Note2_Name` varchar(30) DEFAULT NULL,
  `Note3_Desc` varchar(30) DEFAULT NULL,
  `Note3_Name` varchar(30) DEFAULT NULL,
  `Note4_Desc` varchar(30) DEFAULT NULL,
  `Note4_Name` varchar(30) DEFAULT NULL,
  `Note5_Desc` varchar(30) DEFAULT NULL,
  `Note5_Name` varchar(30) DEFAULT NULL,
  `Note6_Desc` varchar(30) DEFAULT NULL,
  `Note6_Name` varchar(30) DEFAULT NULL,
  `NoteID` varchar(30) DEFAULT NULL,
  `Notes_Text_Loc_1` text,
  `Notes_Text_Loc_2` text,
  `Notes_Text_Loc_3` text,
  `Notes_Text_Loc_4` text,
  `Notes_Text_Loc_5` text,
  `Notes_Text_Loc_6` text,
  `Notes_Text_Loc_Archive` text,
  `Notes_Text_Loc_Historical` text,
  `Notes_Text_Org_1` text,
  `Notes_Text_Org_2` text,
  `Notes_Text_Org_3` text,
  `Notes_Text_Org_4` text,
  `Notes_Text_Org_5` text,
  `Notes_Text_Org_6` text,
  `Notes_Text_Org_Archive` text,
  `Notes_Text_Org_Historical` text,
  `PersonID` varchar(30) DEFAULT NULL,
  `PONumber` varchar(150) DEFAULT NULL,
  `PrelimDataSentDate` varchar(30) DEFAULT NULL,
  `PROJASSGN` varchar(30) DEFAULT NULL,
  `ProjDirector` varchar(30) DEFAULT NULL,
  `ProjStatus` varchar(50) DEFAULT NULL,
  `Quote` varchar(75) DEFAULT NULL,
  `RptShipSentDate` varchar(30) DEFAULT NULL,
  `SAMPCOUNT` varchar(30) DEFAULT NULL,
  `SampleTypes` text,
  `State` varchar(30) DEFAULT NULL,
  `UniversalID` varchar(50) DEFAULT NULL,
  KEY `idx_billingsheet_ProjID` (`ProjID`),
  KEY `idx_billingsheet_PersonID` (`PersonID`)
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

-- Dump completed on 2019-12-28 15:24:01
