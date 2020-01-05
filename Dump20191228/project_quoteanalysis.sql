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
-- Table structure for table `quoteanalysis`
--

DROP TABLE IF EXISTS `quoteanalysis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quoteanalysis` (
  `QuoteNumber` varchar(75) DEFAULT NULL,
  `AACAmt0` text,
  `AACAmt1` text,
  `AACAmt2` text,
  `AACAmt3` text,
  `AACAmt4` text,
  `AACAmt5` text,
  `AACAmt6` text,
  `AACDesc0` text,
  `AACDesc1` text,
  `AACDesc2` text,
  `AACDesc3` text,
  `AACDesc4` text,
  `AACDesc5` text,
  `AACDesc6` text,
  `AACQty0` text,
  `AACQty1` text,
  `AACQty2` text,
  `AACQty3` text,
  `AACQty4` text,
  `AACQty5` text,
  `AACQty6` text,
  `AACTot0` text,
  `AACTot1` text,
  `AACTot2` text,
  `AACTot3` text,
  `AACTot4` text,
  `AACTot5` text,
  `AACTot6` text,
  `ActionLog` text,
  `ActionNotes` text,
  `AMPMReceived` text,
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
  `AnalysisSrvc` text,
  `AnalysisStandardRun` text,
  `AnalysisTotal` text,
  `AnalysisTotalwAddl` text,
  `AnalysisType` text,
  `AnlPVQty` text,
  `ATFQty` text,
  `ATFYN` text,
  `AuthorDate` text,
  `AuthorName` text,
  `Authors` text,
  `BillingNotesText` text,
  `cGMPChange` text,
  `cGMPEnterPrc` text,
  `Comment` text,
  `CompanyName` text,
  `Created` text,
  `CustomDesc` text,
  `CustomMSDesc` text,
  `CustomUnitName` text,
  `CustomUnitQty` text,
  `DateDue` text,
  `DateReceived` text,
  `DEAQty` text,
  `DEAYN` text,
  `DiscType` text,
  `DocID` text,
  `EditAuthors` text,
  `EditDates` text,
  `EditDateName` text,
  `EditProjStatus` text,
  `EmbeddedObjects` blob,
  `EnterDateDue` text,
  `FamilyID` text,
  `FamilyID_1` text,
  `FamilyName` text,
  `FamilyName_1` text,
  `Finalize` text,
  `FinalizedDate` text,
  `HasATFSamples` text,
  `HasDEASamples` text,
  `HiddenServices_Quotes` text,
  `InProjectTask` text,
  `InvFamilyID` text,
  `InvFamilyName` text,
  `IsHighATF` text,
  `IsHighDEA` text,
  `ISO` text,
  `ISOEnterPrc` text,
  `LastAccessed` text,
  `LastModified` text,
  `lineDescription` text,
  `LineItems` text,
  `LocationID` text,
  `MethodServices` text,
  `NoteID` text,
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
  `Notes_Text_Loc_1` text,
  `Notes_Text_Loc_2` text,
  `Notes_Text_Loc_3` text,
  `Notes_Text_Loc_4` text,
  `Notes_Text_Loc_5` text,
  `Notes_Text_Loc_6` text,
  `Notes_Text_Org_Archive` text,
  `Notes_Text_Org_Historical` text,
  `OverridecGMP` text,
  `OverrideISO` text,
  `OverridePrc` text,
  `PriceAgentRun` text,
  `ProjCGMP` text,
  `ProjID` varchar(35) DEFAULT NULL,
  `ProjISO` text,
  `PartlyHiddenServices` text,
  `PartlyHiddenServices_Quotes` text,
  `PrefObjRepID` text,
  `ProjNum_Digits` text,
  `RunQty` text,
  `SampQty` text,
  `SubAnalysisTotal` text,
  `TotalBeforeDisco` text,
  `TurnaroundText` text,
  `TurnaroundTextQuote100` text,
  `TurnaroundTextQuote50` text,
  `TurnaroundTextQuoteStd` text,
  `UseCustomDesc` text,
  `UseCustomUnits` text,
  `UniversalID` varchar(35) DEFAULT NULL,
  `ValidateEvent` text,
  `ValidateNow` text,
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

-- Dump completed on 2019-12-28 15:24:04
