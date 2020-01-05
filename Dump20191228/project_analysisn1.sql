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
-- Table structure for table `analysisn1`
--

DROP TABLE IF EXISTS `analysisn1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analysisn1` (
  `analysisProjNumber` varchar(35) DEFAULT NULL,
  `DocID` varchar(75) DEFAULT NULL,
  `FamilyID` varchar(75) DEFAULT NULL,
  `NoteID` varchar(50) DEFAULT NULL,
  `ProjID` varchar(75) DEFAULT NULL,
  `LocationID` varchar(30) DEFAULT NULL,
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
  `AMPMReceived` varchar(10) DEFAULT NULL,
  `AnalysisAssign` varchar(30) DEFAULT NULL,
  `AnalysisATFChrgSt` varchar(30) DEFAULT NULL,
  `AnalysisCarrierUsed` varchar(10) DEFAULT NULL,
  `AnalysiscGMPChrg` varchar(10) DEFAULT NULL,
  `AnalysiscGMPChrgSt` varchar(10) DEFAULT NULL,
  `AnalysisDEAChrgSt` varchar(15) DEFAULT NULL,
  `AnalysisDept` varchar(50) DEFAULT NULL,
  `AnalysisDisc` varchar(30) DEFAULT NULL,
  `AnalysisDiscSt` varchar(15) DEFAULT NULL,
  `AnalysisDiscStat` varchar(10) DEFAULT NULL,
  `AnalysisHazChrg` varchar(10) DEFAULT NULL,
  `AnalysisHazChrgSt` varchar(10) DEFAULT NULL,
  `AnalysisInstr` text,
  `AnalysisISOChrg` varchar(15) DEFAULT NULL,
  `AnalysisISOChrgSt` varchar(15) DEFAULT NULL,
  `AnalysisNum` varchar(10) DEFAULT NULL,
  `AnalysisPrc` varchar(10) DEFAULT NULL,
  `AnalysisPrcEnt` varchar(10) DEFAULT NULL,
  `AnalysisPrcEntSt` varchar(10) DEFAULT NULL,
  `AnalysisPrcSt` varchar(10) DEFAULT NULL,
  `AnalysisPrioChrg` varchar(10) DEFAULT NULL,
  `AnalysisPriority` varchar(10) DEFAULT NULL,
  `AnalysisPrioSt` varchar(10) DEFAULT NULL,
  `AnalysisQty` varchar(10) DEFAULT NULL,
  `AnalysisQtyLab` varchar(10) DEFAULT NULL,
  `AnalysisSamples` text,
  `AnalysisSampleTypes` text,
  `AnalysisSrvc` varchar(100) DEFAULT NULL,
  `AnalysisTotal` varchar(10) DEFAULT NULL,
  `AnalysisTotalwAddl` varchar(10) DEFAULT NULL,
  `AnalysisType` varchar(100) DEFAULT NULL,
  `AnlPVQty` varchar(10) DEFAULT NULL,
  `AnlRunQty` varchar(10) DEFAULT NULL,
  `AuthorDate` varchar(30) DEFAULT NULL,
  `AuthorName` varchar(50) DEFAULT NULL,
  `BillingCopyLab` varchar(30) DEFAULT NULL,
  `BillingNotesText` text,
  `cGMPChange` varchar(10) DEFAULT NULL,
  `cGMPEnterPrc` varchar(10) DEFAULT NULL,
  `CompanyName` varchar(100) DEFAULT NULL,
  `ComplexProject` varchar(30) DEFAULT NULL,
  `DateDue` varchar(30) DEFAULT NULL,
  `DateReceived` varchar(30) DEFAULT NULL,
  `DiscType` varchar(10) DEFAULT NULL,
  `EditAuthors` varchar(100) DEFAULT NULL,
  `EditDates` varchar(50) DEFAULT NULL,
  `EditProjStatus` varchar(50) DEFAULT NULL,
  `EmbeddedObjects` blob,
  `EnterDateDue` varchar(30) DEFAULT NULL,
  `FamilyName` varchar(150) DEFAULT NULL,
  `HazQty` varchar(10) DEFAULT NULL,
  `InProjectTask` varchar(10) DEFAULT NULL,
  `IsHighDEA` varchar(10) DEFAULT NULL,
  `ISO` varchar(10) DEFAULT NULL,
  `IsHighATF` varchar(10) DEFAULT NULL,
  `ISOEnterPrc` varchar(10) DEFAULT NULL,
  `LineItems` varchar(10) DEFAULT NULL,
  `MethodServices` varchar(10) DEFAULT NULL,
  `MethodServiceType` varchar(30) DEFAULT NULL,
  `Options` varchar(30) DEFAULT NULL,
  `OutSrcLocation` varchar(50) DEFAULT NULL,
  `OutSrcMethod` varchar(30) DEFAULT NULL,
  `OutSrcPONum` varchar(30) DEFAULT NULL,
  `OutSrcTracking` varchar(30) DEFAULT NULL,
  `OverridecGMP` varchar(10) DEFAULT NULL,
  `OverrideISO` varchar(10) DEFAULT NULL,
  `OverridePrc` varchar(30) DEFAULT NULL,
  `PrelimDataCopyTo` varchar(100) DEFAULT NULL,
  `PrelimDataSentBy` varchar(50) DEFAULT NULL,
  `PrelimDataSentDate` varchar(30) DEFAULT NULL,
  `PrelimDataSentMethod` varchar(30) DEFAULT NULL,
  `PrelimDataSentTime` varchar(30) DEFAULT NULL,
  `PrelimDataSentTo` varchar(50) DEFAULT NULL,
  `ProjCanceled` varchar(10) DEFAULT NULL,
  `ProjCancelStat` varchar(10) DEFAULT NULL,
  `ProjCGMP` varchar(10) DEFAULT NULL,
  `ProjDirector` varchar(100) DEFAULT NULL,
  `ProjISO` varchar(10) DEFAULT NULL,
  `ProjQADataRvw` varchar(10) DEFAULT NULL,
  `ProjQARev` varchar(30) DEFAULT NULL,
  `ProjReptWrtr` varchar(30) DEFAULT NULL,
  `ProjStat` varchar(30) DEFAULT NULL,
  `ProjStatus` varchar(50) DEFAULT NULL,
  `ProjTechRev` varchar(30) DEFAULT NULL,
  `ReptWrtrAssign` varchar(30) DEFAULT NULL,
  `Revisions` varchar(30) DEFAULT NULL,
  `SubAnalysisTotal` varchar(10) DEFAULT NULL,
  `TechRevAssign` varchar(50) DEFAULT NULL,
  `TotalBeforeDisco` varchar(10) DEFAULT NULL,
  `trackLookup` varchar(50) DEFAULT NULL,
  `TrackSelection` varchar(30) DEFAULT NULL,
  `UniversalID` varchar(35) DEFAULT NULL,
  `TurnaroundTextQuote100` text,
  `TurnaroundTextQuote50` text,
  `TurnaroundTextQuoteStd` text,
  KEY `analysisProjNumber` (`analysisProjNumber`)
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
