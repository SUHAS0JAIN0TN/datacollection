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
-- Table structure for table `invoice_billingarch`
--

DROP TABLE IF EXISTS `invoice_billingarch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoice_billingarch` (
  `ProjectNumber` text,
  `ProjID` varchar(30) DEFAULT NULL,
  `AcctNotes` text,
  `Address1` text,
  `Address2` text,
  `AnalysisComments` text,
  `AuthorDate` text,
  `AuthorName` text,
  `Authors` text,
  `BilledYN` text,
  `BillingNotes` text,
  `City` text,
  `companyname` text,
  `ContactName` text,
  `ContactNumber` text,
  `Country` text,
  `Created` text,
  `DateDue` text,
  `DateReceived` text,
  `DocID` text,
  `EditAuthors` text,
  `EditDates` text,
  `EMail` text,
  `EmbeddedObjects` blob,
  `FamilyID` text,
  `FamilyName` text,
  `FamilyNotes` text,
  `Fax` text,
  `HasMissedOpportunity` text,
  `InvAmt` text,
  `InvCity` text,
  `InvCompanyName` text,
  `InvCountry` text,
  `InvDate` text,
  `InvDesc` text,
  `InvDisc` text,
  `InvFamilyID` text,
  `InvFamilyName` text,
  `InvLocationID` text,
  `InvoiceDate` text,
  `InvPersonID` text,
  `InvQty` text,
  `InvRate` text,
  `InvState` text,
  `InvTotal` text,
  `LastAccessed` text,
  `LastModified` text,
  `LocationID` text,
  `MissCategory` text,
  `MissDescription` text,
  `MissEstimate` text,
  `MissLineItems` text,
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
  `NoteID` text,
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
  `PONumber` text,
  `PrelimDataSentDate` text,
  `PROJASSGN` text,
  `ProjDirector` text,
  `ProjectComments` text,
  `ProjEvent` text,
  `ProjSource` text,
  `ProjStatus` text,
  `Quote` text,
  `RptShipSentDate` text,
  `SAMPCOUNT` text,
  `SampleComments` text,
  `SampleTypes` text,
  `SpecialTermsInvoice` text,
  `SpecialTermsReport` text,
  `State` text,
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

-- Dump completed on 2019-12-28 15:24:03
