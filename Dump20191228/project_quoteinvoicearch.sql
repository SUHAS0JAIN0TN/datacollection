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
-- Table structure for table `quoteinvoicearch`
--

DROP TABLE IF EXISTS `quoteinvoicearch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quoteinvoicearch` (
  `AllDEAQty` int(11) DEFAULT NULL,
  `AnalysisComments` varchar(500) DEFAULT NULL,
  `AnalysisQty` int(11) DEFAULT NULL,
  `AnalysisTypes` varchar(50) DEFAULT NULL,
  `ATFSampleQty` int(11) DEFAULT NULL,
  `AuthorDate` varchar(50) DEFAULT NULL,
  `AuthorName` varchar(50) DEFAULT NULL,
  `Authors` varchar(50) DEFAULT NULL,
  `BilledYN` varchar(50) DEFAULT NULL,
  `BillingNotes` varchar(500) DEFAULT NULL,
  `Comments` varchar(500) DEFAULT NULL,
  `ContactNumber` varchar(50) DEFAULT NULL,
  `Created` datetime DEFAULT NULL,
  `DateDue` datetime DEFAULT NULL,
  `DiscountNotes` varchar(500) DEFAULT NULL,
  `DocID` varchar(50) DEFAULT NULL,
  `EditAuthors` varchar(50) DEFAULT NULL,
  `EditDates` datetime DEFAULT NULL,
  `EMail` varchar(50) DEFAULT NULL,
  `EmbeddedObjects` blob,
  `FamilyID` varchar(50) DEFAULT NULL,
  `FamilyName` varchar(50) DEFAULT NULL,
  `Fax` varchar(50) DEFAULT NULL,
  `Finalize` varchar(50) DEFAULT NULL,
  `FinalizedDate` datetime DEFAULT NULL,
  `Form` varchar(100) DEFAULT NULL,
  `HazSampleQty` int(11) DEFAULT NULL,
  `InvAmt` int(11) DEFAULT NULL,
  `InvDate` datetime DEFAULT NULL,
  `InvDesc` varchar(100) DEFAULT NULL,
  `InvDisc` varchar(50) DEFAULT NULL,
  `InvFamilyID` varchar(50) DEFAULT NULL,
  `InvFamilyName` varchar(50) DEFAULT NULL,
  `InvLocationID` varchar(50) DEFAULT NULL,
  `InvoiceNum` varchar(50) DEFAULT NULL,
  `InvPersonID` varchar(50) DEFAULT NULL,
  `InvQty` int(11) DEFAULT NULL,
  `InvRate` varchar(50) DEFAULT NULL,
  `InvTotal` varchar(50) DEFAULT NULL,
  `LastAccessed` datetime DEFAULT NULL,
  `LastModified` datetime DEFAULT NULL,
  `LocationID` varchar(50) DEFAULT NULL,
  `NoteID` varchar(50) DEFAULT NULL,
  `PersonID` varchar(50) DEFAULT NULL,
  `PriceQuoteNotes` varchar(500) DEFAULT NULL,
  `ProjectComments` varchar(500) DEFAULT NULL,
  `ProjID` varchar(50) DEFAULT NULL,
  `QuoteAnalysisPriority` varchar(50) DEFAULT NULL,
  `QuoteAnlRuns` varchar(50) DEFAULT NULL,
  `QuoteAnlSamps` varchar(50) DEFAULT NULL,
  `QuoteCompanyName` varchar(50) DEFAULT NULL,
  `QuoteInvoiceNumber` varchar(50) NOT NULL,
  `RptLocationID` varchar(50) DEFAULT NULL,
  `RptPersonID` varchar(50) DEFAULT NULL,
  `SampCount` varchar(50) DEFAULT NULL,
  `SampleTypes` varchar(50) DEFAULT NULL,
  `UniversalID` varchar(50) DEFAULT NULL,
  `Affiliates1` varchar(50) DEFAULT NULL,
  `Affiliates2` varchar(50) DEFAULT NULL,
  `AffiliatesSummaryInfo1` varchar(50) DEFAULT NULL,
  `AffiliatesSummaryInfo2` varchar(50) DEFAULT NULL,
  `AppActivity` varchar(50) DEFAULT NULL,
  `AppAnalytics` varchar(50) DEFAULT NULL,
  `AppBidProc` varchar(50) DEFAULT NULL,
  `AppContact` varchar(50) DEFAULT NULL,
  `AppDEAReg` varchar(50) DEFAULT NULL,
  `AppDir` varchar(50) DEFAULT NULL,
  `AppDir2` varchar(50) DEFAULT NULL,
  `AppProjectWkfl` varchar(50) DEFAULT NULL,
  `AppSaleOpp` varchar(50) DEFAULT NULL,
  `AppSalesMkt` varchar(50) DEFAULT NULL,
  `AppServer` varchar(50) DEFAULT NULL,
  `AppServices` varchar(50) DEFAULT NULL,
  `AppSysPref` varchar(50) DEFAULT NULL,
  `AppTestMethods` varchar(50) DEFAULT NULL,
  `AppThisDB` varchar(50) DEFAULT NULL,
  `ColorCoding` varchar(50) DEFAULT NULL,
  `EditDateName` varchar(50) DEFAULT NULL,
  `Edited` varchar(50) DEFAULT NULL,
  `FormulaChecker` varchar(50) DEFAULT NULL,
  `HiddenServices` varchar(50) DEFAULT NULL,
  `HiddenServices_Quotes` varchar(50) DEFAULT NULL,
  `Note1_Desc` varchar(500) DEFAULT NULL,
  `Note1_Name` varchar(50) DEFAULT NULL,
  `Note2_Desc` varchar(500) DEFAULT NULL,
  `Note2_Name` varchar(50) DEFAULT NULL,
  `Note3_Desc` varchar(500) DEFAULT NULL,
  `Note3_Name` varchar(50) DEFAULT NULL,
  `Note4_Desc` varchar(500) DEFAULT NULL,
  `Note4_Name` varchar(50) DEFAULT NULL,
  `Note5_Desc` varchar(500) DEFAULT NULL,
  `Note5_Name` varchar(50) DEFAULT NULL,
  `Note6_Desc` varchar(500) DEFAULT NULL,
  `Note6_Name` varchar(50) DEFAULT NULL,
  `PartlyHiddenServices` varchar(50) DEFAULT NULL,
  `PartlyHiddenServices_Quotes` varchar(50) DEFAULT NULL,
  `PrefObjRepID` varchar(50) DEFAULT NULL,
  `ProjNum_Digits` varchar(50) DEFAULT NULL,
  `SystemName` varchar(50) DEFAULT NULL,
  `VersionChangeHistory` varchar(50) DEFAULT NULL,
  `WorkflowChangeHistory` varchar(50) DEFAULT NULL,
  `WorkflowRevisionNumber` varchar(50) DEFAULT NULL,
  `DIGIT_COUNT` varchar(50) DEFAULT NULL,
  `EditProjStatus` varchar(50) DEFAULT NULL,
  `LocationInfo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`QuoteInvoiceNumber`),
  KEY `idx_quoteinvoice_ProjID` (`ProjID`),
  KEY `idx_quoteinvoice_QuoteInvoiceNumber` (`QuoteInvoiceNumber`),
  KEY `idx_quoteinvoice_PersonID` (`PersonID`)
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
