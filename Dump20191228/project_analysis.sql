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
-- Table structure for table `analysis`
--

DROP TABLE IF EXISTS `analysis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analysis` (
  `analysisProjNumber` varchar(75) DEFAULT NULL,
  `DocID` varchar(75) DEFAULT NULL,
  `FamilyID` varchar(75) DEFAULT NULL,
  `NoteID` varchar(50) DEFAULT NULL,
  `ProjID` varchar(75) DEFAULT NULL,
  `AACAmt0` varchar(50) DEFAULT NULL,
  `AACAmt1` varchar(50) DEFAULT NULL,
  `AACAmt2` varchar(50) DEFAULT NULL,
  `AACAmt3` varchar(50) DEFAULT NULL,
  `AACAmt4` varchar(50) DEFAULT NULL,
  `AACAmt5` varchar(50) DEFAULT NULL,
  `AACAmt6` varchar(50) DEFAULT NULL,
  `AACDesc0` varchar(75) DEFAULT NULL,
  `AACDesc1` varchar(75) DEFAULT NULL,
  `AACDesc2` varchar(75) DEFAULT NULL,
  `AACDesc3` varchar(75) DEFAULT NULL,
  `AACDesc4` varchar(75) DEFAULT NULL,
  `AACDesc5` varchar(75) DEFAULT NULL,
  `AACDesc6` varchar(75) DEFAULT NULL,
  `AACQty0` varchar(50) DEFAULT NULL,
  `AACQty1` varchar(50) DEFAULT NULL,
  `AACQty2` varchar(50) DEFAULT NULL,
  `AACQty3` varchar(50) DEFAULT NULL,
  `AACQty4` varchar(50) DEFAULT NULL,
  `AACQty5` varchar(50) DEFAULT NULL,
  `AACQty6` varchar(50) DEFAULT NULL,
  `AACTot0` varchar(50) DEFAULT NULL,
  `AACTot1` varchar(50) DEFAULT NULL,
  `AACTot2` varchar(50) DEFAULT NULL,
  `AACTot3` varchar(50) DEFAULT NULL,
  `AACTot4` varchar(50) DEFAULT NULL,
  `AACTot5` varchar(50) DEFAULT NULL,
  `AACTot6` varchar(50) DEFAULT NULL,
  `ActionLog` text,
  `ActionNotes` text,
  `AMPMReceived` varchar(50) DEFAULT NULL,
  `AnalysisAssign` text,
  `AnalysisATFChrgSt` text,
  `AnalysisCarrierUsed` text,
  `AnalysiscGMPChrg` text,
  `AnalysiscGMPChrgSt` text,
  `AnalysisDEAChrgSt` text,
  `AnalysisDept` text,
  `AnalysisDisc` text,
  `AnalysisDiscSt` text,
  `AnalysisDiscStat` text,
  `AnalysisHazChrg` text,
  `AnalysisHazChrgSt` text,
  `AnalysisInstr` text,
  `AnalysisISOChrg` text,
  `AnalysisISOChrgSt` text,
  `AnalysisNum` text,
  `AnalysisPrc` text,
  `AnalysisPrcEnt` text,
  `AnalysisPrcEntSt` text,
  `AnalysisPrcSt` text,
  `AnalysisPrioChrg` text,
  `AnalysisPriority` text,
  `AnalysisPrioSt` text,
  `AnalysisQty` text,
  `AnalysisQtyLab` text,
  `AnalysisSamples` text,
  `AnalysisSampleTypes` text,
  `AnalysisSrvc` text,
  `AnalysisStandardRun` text,
  `AnalysisTotal` text,
  `AnalysisTotalwAddl` text,
  `AnalysisType` text,
  `AnlPVQty` text,
  `AnlRunQty` text,
  `AuthorDate` text,
  `AuthorName` text,
  `Authors` text,
  `BillingCopyLab` text,
  `BillingNotes` text,
  `BillingNotesText` text,
  `cGMPChange` text,
  `cGMPEnterPrc` text,
  `CompanyName` text,
  `ComplexProject` text,
  `Created` text,
  `DateDue` text,
  `DateReceived` text,
  `DiscType` text,
  `EditAuthors` text,
  `EditDates` text,
  `EditProjStatus` text,
  `EmbeddedObjects` blob,
  `EnterDateDue` text,
  `FamilyName` text,
  `HazQty` text,
  `HoldData` text,
  `InProjectTask` text,
  `InvFamilyID` text,
  `InvFamilyName` text,
  `IsHighDEA` text,
  `ISO` text,
  `IsHighATF` text,
  `ISOEnterPrc` text,
  `LastAccessed` text,
  `LastModified` text,
  `LineItems` text,
  `LocationID` text,
  `MethodServices` text,
  `MethodServiceType` text,
  `Options` text,
  `OutSrcLocation` text,
  `OutSrcMethod` text,
  `OutSrcPONum` text,
  `OutSrcTracking` text,
  `OverridecGMP` text,
  `OverrideISO` text,
  `OverridePrc` text,
  `PrelimDataCopyTo` text,
  `PrelimDataSentBy` text,
  `PrelimDataSentDate` text,
  `PrelimDataSentMethod` text,
  `PrelimDataSentTime` text,
  `PrelimDataSentTo` text,
  `ProjCanceled` text,
  `ProjCancelStat` text,
  `ProjCGMP` text,
  `ProjDirector` text,
  `ProjEvent` text,
  `ProjISO` text,
  `ProjQADataRvw` text,
  `ProjQARev` text,
  `ProjReptWrtr` text,
  `ProjStat` text,
  `ProjStatus` text,
  `ProjTechRev` text,
  `ReptWrtrAssign` text,
  `Revisions` text,
  `SubAnalysisTotal` text,
  `TechRevAssign` text,
  `TotalBeforeDisco` text,
  `trackLookup` text,
  `TrackSelection` text,
  `UniversalID` text,
  `UpdatedBy` text,
  `ValidateEvent` text,
  `ValidateNow` text,
  `TurnaroundTextQuote100` text,
  `TurnaroundTextQuote50` text,
  `TurnaroundTextQuoteStd` text,
  KEY `idx_analysis_ProjID` (`ProjID`)
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

-- Dump completed on 2019-12-28 15:24:04
