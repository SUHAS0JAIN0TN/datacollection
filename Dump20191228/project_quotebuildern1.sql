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
-- Table structure for table `quotebuildern1`
--

DROP TABLE IF EXISTS `quotebuildern1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quotebuildern1` (
  `QuoteBuilderNumber` varchar(15) NOT NULL,
  `ActionLog` text,
  `AddlTextSelect` text,
  `Address1` varchar(100) DEFAULT NULL,
  `Address2` varchar(100) DEFAULT NULL,
  `AllDEAQty` varchar(15) DEFAULT NULL,
  `AllDEASchedule` varchar(15) DEFAULT NULL,
  `AllDEAYN` varchar(15) DEFAULT NULL,
  `AMPMReceived` varchar(15) DEFAULT NULL,
  `AnalysisQty` varchar(15) DEFAULT NULL,
  `AnalysisTypes` varchar(75) DEFAULT NULL,
  `AssocProj` varchar(15) DEFAULT NULL,
  `AssocProj1` varchar(35) DEFAULT NULL,
  `ATFSampleQty` varchar(15) DEFAULT NULL,
  `AuthorDate` varchar(35) DEFAULT NULL,
  `AuthorName` varchar(35) DEFAULT NULL,
  `City` varchar(35) DEFAULT NULL,
  `Comments` text,
  `CompanyName` varchar(105) DEFAULT NULL,
  `CompletePayTerms` text,
  `ContactName` varchar(50) DEFAULT NULL,
  `ContactNumber` varchar(35) DEFAULT NULL,
  `Country` varchar(35) DEFAULT NULL,
  `CustomCharge` varchar(35) DEFAULT NULL,
  `CustomDescription` text,
  `CustomReturnCharge` varchar(35) DEFAULT NULL,
  `DateDue` varchar(35) DEFAULT NULL,
  `DateReceived` varchar(35) DEFAULT NULL,
  `DiscountNotes` text,
  `EMail` varchar(105) DEFAULT NULL,
  `EnterDateDue` varchar(35) DEFAULT NULL,
  `ExcelQuoteFilePath` text,
  `FamilyID` varchar(35) DEFAULT NULL,
  `FamilyName` varchar(135) DEFAULT NULL,
  `Fax` varchar(35) DEFAULT NULL,
  `FinalizedDate` varchar(35) DEFAULT NULL,
  `FinalPayTerms` varchar(35) DEFAULT NULL,
  `HazSampleQty` varchar(15) DEFAULT NULL,
  `Inactive` varchar(15) DEFAULT NULL,
  `InhouseQuote` varchar(15) DEFAULT NULL,
  `InvAddress1` varchar(35) DEFAULT NULL,
  `InvAddress2` varchar(35) DEFAULT NULL,
  `InvCity` varchar(35) DEFAULT NULL,
  `InvCompanyName` varchar(105) DEFAULT NULL,
  `InvContactName` varchar(35) DEFAULT NULL,
  `InvCountry` varchar(35) DEFAULT NULL,
  `InvEMail` varchar(55) DEFAULT NULL,
  `InvFamilyID` varchar(35) DEFAULT NULL,
  `InvFamilyName` varchar(35) DEFAULT NULL,
  `InvFax` varchar(35) DEFAULT NULL,
  `InvLocationID` varchar(35) DEFAULT NULL,
  `InvPersonID` varchar(35) DEFAULT NULL,
  `InvPhone` varchar(35) DEFAULT NULL,
  `InvState` varchar(35) DEFAULT NULL,
  `InvZip` varchar(35) DEFAULT NULL,
  `ISO` varchar(15) DEFAULT NULL,
  `LocationID` varchar(15) DEFAULT NULL,
  `MethodServices` varchar(15) DEFAULT NULL,
  `MethodServiceType` varchar(35) DEFAULT NULL,
  `NoteID` varchar(35) DEFAULT NULL,
  `PaymentTerms` varchar(35) DEFAULT NULL,
  `PersonID` varchar(35) DEFAULT NULL,
  `PrepayTerms` varchar(35) DEFAULT NULL,
  `PriceQuoteNotes` text,
  `ProjCGMP` varchar(15) DEFAULT NULL,
  `ProjID` varchar(35) DEFAULT NULL,
  `ProjISO` varchar(15) DEFAULT NULL,
  `ProjPriority` varchar(15) DEFAULT NULL,
  `ProtocolPerson` varchar(35) DEFAULT NULL,
  `QuoteCompanyName` varchar(105) DEFAULT NULL,
  `QuoteDate` varchar(35) DEFAULT NULL,
  `ReturnReason` varchar(35) DEFAULT NULL,
  `RptLocationID` varchar(35) DEFAULT NULL,
  `RptPersonID` varchar(35) DEFAULT NULL,
  `SalesPerson` varchar(50) DEFAULT NULL,
  `SampleQty` varchar(15) DEFAULT NULL,
  `SamplesATFYN` varchar(15) DEFAULT NULL,
  `SamplesDEA` varchar(5) DEFAULT NULL,
  `SamplesHaz` varchar(15) DEFAULT NULL,
  `SamplesHazYN` varchar(15) DEFAULT NULL,
  `SampleTypes` varchar(105) DEFAULT NULL,
  `SampReturn` varchar(15) DEFAULT NULL,
  `State` varchar(35) DEFAULT NULL,
  `UniversalID` varchar(35) DEFAULT NULL,
  `Zip` varchar(35) DEFAULT NULL,
  PRIMARY KEY (`QuoteBuilderNumber`),
  KEY `idx_quotebuilder_ProjID` (`ProjID`),
  KEY `idx_quotebuilder_PersonID` (`PersonID`)
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

-- Dump completed on 2019-12-28 15:24:02
