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
-- Table structure for table `quoteanalysisn1`
--

DROP TABLE IF EXISTS `quoteanalysisn1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quoteanalysisn1` (
  `QuoteNumber` varchar(25) DEFAULT NULL,
  `ProjID` varchar(35) DEFAULT NULL,
  `ActionLog` text,
  `ActionNotes` text,
  `AMPMReceived` varchar(10) DEFAULT NULL,
  `AnalysisATFChrgSt` varchar(25) DEFAULT NULL,
  `AnalysisCarrierUsed` varchar(10) DEFAULT NULL,
  `AnalysiscGMPChrg` varchar(15) DEFAULT NULL,
  `AnalysiscGMPChrgSt` varchar(15) DEFAULT NULL,
  `AnalysisDEAChrgSt` varchar(25) DEFAULT NULL,
  `AnalysisDept` varchar(50) DEFAULT NULL,
  `AnalysisDisc` varchar(25) DEFAULT NULL,
  `AnalysisDiscSt` varchar(25) DEFAULT NULL,
  `AnalysisDiscStat` varchar(25) DEFAULT NULL,
  `AnalysisHazChrg` varchar(25) DEFAULT NULL,
  `AnalysisHazChrgSt` varchar(25) DEFAULT NULL,
  `AnalysisInstr` varchar(100) DEFAULT NULL,
  `AnalysisISOChrg` varchar(25) DEFAULT NULL,
  `AnalysisISOChrgSt` varchar(25) DEFAULT NULL,
  `AnalysisNum` varchar(25) DEFAULT NULL,
  `AnalysisPrc` varchar(15) DEFAULT NULL,
  `AnalysisPrcEnt` varchar(15) DEFAULT NULL,
  `AnalysisPrcEntSt` varchar(15) DEFAULT NULL,
  `AnalysisPrcSt` varchar(25) DEFAULT NULL,
  `AnalysisPrioChrg` varchar(25) DEFAULT NULL,
  `AnalysisPriority` varchar(15) DEFAULT NULL,
  `AnalysisPrioSt` varchar(25) DEFAULT NULL,
  `AnalysisQty` varchar(25) DEFAULT NULL,
  `AnalysisSrvc` varchar(100) DEFAULT NULL,
  `AnalysisStandardRun` varchar(15) DEFAULT NULL,
  `AnalysisTotal` varchar(25) DEFAULT NULL,
  `AnalysisTotalwAddl` varchar(25) DEFAULT NULL,
  `AnalysisType` varchar(100) DEFAULT NULL,
  `AnlPVQty` varchar(25) DEFAULT NULL,
  `ATFQty` varchar(25) DEFAULT NULL,
  `ATFYN` varchar(25) DEFAULT NULL,
  `AuthorDate` varchar(25) DEFAULT NULL,
  `AuthorName` varchar(50) DEFAULT NULL,
  `BillingNotesText` text,
  `cGMPChange` varchar(15) DEFAULT NULL,
  `cGMPEnterPrc` varchar(25) DEFAULT NULL,
  `Comment` text,
  `CompanyName` varchar(100) DEFAULT NULL,
  `CustomDesc` text,
  `CustomMSDesc` text,
  `CustomUnitName` varchar(25) DEFAULT NULL,
  `CustomUnitQty` varchar(25) DEFAULT NULL,
  `DateDue` varchar(25) DEFAULT NULL,
  `DateReceived` varchar(25) DEFAULT NULL,
  `DEAQty` varchar(25) DEFAULT NULL,
  `DEAYN` varchar(25) DEFAULT NULL,
  `DiscType` varchar(25) DEFAULT NULL,
  `DocID` varchar(25) DEFAULT NULL,
  `EnterDateDue` varchar(25) DEFAULT NULL,
  `FamilyID` varchar(25) DEFAULT NULL,
  `FamilyID_1` varchar(25) DEFAULT NULL,
  `FamilyName` varchar(125) DEFAULT NULL,
  `FamilyName_1` varchar(125) DEFAULT NULL,
  `Finalize` varchar(25) DEFAULT NULL,
  `FinalizedDate` varchar(25) DEFAULT NULL,
  `HasATFSamples` varchar(25) DEFAULT NULL,
  `HasDEASamples` varchar(25) DEFAULT NULL,
  `HiddenServices_Quotes` varchar(25) DEFAULT NULL,
  `InProjectTask` varchar(25) DEFAULT NULL,
  `InvFamilyID` varchar(25) DEFAULT NULL,
  `InvFamilyName` varchar(25) DEFAULT NULL,
  `IsHighATF` varchar(25) DEFAULT NULL,
  `IsHighDEA` varchar(25) DEFAULT NULL,
  `ISO` varchar(25) DEFAULT NULL,
  `ISOEnterPrc` varchar(25) DEFAULT NULL,
  `lineDescription` text,
  `LineItems` varchar(25) DEFAULT NULL,
  `LocationID` varchar(25) DEFAULT NULL,
  `MethodServices` varchar(25) DEFAULT NULL,
  `NoteID` varchar(25) DEFAULT NULL,
  `OverridecGMP` varchar(15) DEFAULT NULL,
  `OverrideISO` varchar(15) DEFAULT NULL,
  `OverridePrc` varchar(15) DEFAULT NULL,
  `ProjCGMP` varchar(5) DEFAULT NULL,
  `ProjISO` varchar(15) DEFAULT NULL,
  `PartlyHiddenServices` varchar(25) DEFAULT NULL,
  `PartlyHiddenServices_Quotes` varchar(25) DEFAULT NULL,
  `PrefObjRepID` varchar(25) DEFAULT NULL,
  `ProjNum_Digits` varchar(25) DEFAULT NULL,
  `RunQty` varchar(25) DEFAULT NULL,
  `SampQty` varchar(25) DEFAULT NULL,
  `SubAnalysisTotal` varchar(25) DEFAULT NULL,
  `TotalBeforeDisco` varchar(25) DEFAULT NULL,
  `TurnaroundText` varchar(125) DEFAULT NULL,
  `TurnaroundTextQuote100` varchar(125) DEFAULT NULL,
  `TurnaroundTextQuote50` text,
  `TurnaroundTextQuoteStd` text,
  `UseCustomDesc` text,
  `UseCustomUnits` varchar(25) DEFAULT NULL,
  `UniversalID` varchar(35) DEFAULT NULL,
  KEY `idx_quoteanalysis_ProjID` (`ProjID`),
  KEY `idx_quoteanalysis_QuoteNumber` (`QuoteNumber`)
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
