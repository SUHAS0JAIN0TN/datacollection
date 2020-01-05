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
-- Table structure for table `quotebuilder`
--

DROP TABLE IF EXISTS `quotebuilder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quotebuilder` (
  `QuoteBuilderNumber` varchar(75) NOT NULL,
  `ActionLog` text,
  `ActionNotes` text,
  `AddlTextSelect` text,
  `Address1` text,
  `Address2` text,
  `Affiliates1` text,
  `Affiliates2` text,
  `AffiliatesSummaryInfo1` text,
  `AffiliatesSummaryInfo2` text,
  `AllDEAQty` text,
  `AllDEASchedule` text,
  `AllDEAYN` text,
  `AMPMReceived` text,
  `AnalysisQty` text,
  `AnalysisTypes` text,
  `AssocProj` text,
  `AssocProj1` text,
  `ATFSampleQty` text,
  `AuthorDate` text,
  `AuthorName` text,
  `Authors` text,
  `BlockTextChoices` text,
  `City` text,
  `Comments` text,
  `CompanyName` text,
  `CompletePayTerms` text,
  `ContactName` text,
  `ContactNumber` text,
  `Country` text,
  `Created` text,
  `CustomCharge` text,
  `CustomDescription` text,
  `CustomReturnCharge` text,
  `DateDue` text,
  `DateReceived` text,
  `DiscountNotes` text,
  `EditAuthors` text,
  `EditDates` text,
  `EditDateName` text,
  `Edited` text,
  `EditProjStatus` text,
  `EMail` text,
  `EmbeddedObjects` blob,
  `EnterDateDue` text,
  `EnterQuoteNumber` text,
  `ExcelQuoteFilePath` text,
  `FamilyID` varchar(35) DEFAULT NULL,
  `FamilyName` text,
  `Favorited` text,
  `Fax` text,
  `Finalize` text,
  `FinalizedDate` text,
  `FinalPayTerms` text,
  `HazSampleQty` text,
  `HiddenServices` text,
  `HiddenServices_Quotes` text,
  `Inactive` text,
  `InhouseQuote` text,
  `InvAddress1` text,
  `InvAddress2` text,
  `InvCity` text,
  `InvCompanyName` text,
  `InvContactName` text,
  `InvCountry` text,
  `InvEMail` text,
  `InvFamilyID` text,
  `InvFamilyName` text,
  `InvFax` text,
  `InvLocationID` text,
  `InvPersonID` text,
  `InvPhone` text,
  `InvState` text,
  `InvZip` text,
  `ISO` text,
  `LastAccessed` text,
  `LastModified` text,
  `LocationID` text,
  `MethodServices` text,
  `MethodServiceType` text,
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
  `Notes_Text_Loc_Archive` text,
  `Notes_Text_Loc_Historical` text,
  `PaymentTerms` text,
  `PersonID` varchar(35) DEFAULT NULL,
  `PrepayTerms` text,
  `PriceQuoteNotes` text,
  `ProjCGMP` text,
  `ProjID` varchar(35) DEFAULT NULL,
  `ProjISO` text,
  `ProjPriority` text,
  `ProtocolPerson` text,
  `PartlyHiddenServices` text,
  `PartlyHiddenServices_Quotes` text,
  `PrefObjRepID` text,
  `ProjNum_Digits` text,
  `QuoteCompanyName` text,
  `QuoteDate` text,
  `ReturnReason` text,
  `RptLocationID` text,
  `RptPersonID` text,
  `SalesPerson` text,
  `SampleQty` text,
  `SamplesATFYN` text,
  `SamplesDEA` text,
  `SamplesHaz` text,
  `SamplesHazYN` text,
  `SampleTypes` text,
  `SampReturn` text,
  `State` text,
  `TurnaroundText` text,
  `TURNAROUNDTEXTQUOTE` text,
  `TurnaroundTextQuote100` text,
  `TurnaroundTextQuote50` text,
  `TurnaroundTextQuoteStd` text,
  `UniversalID` text,
  `ValidateNow` text,
  `Zip` text,
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
