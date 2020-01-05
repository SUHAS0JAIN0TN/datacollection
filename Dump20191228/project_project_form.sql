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
-- Table structure for table `project_form`
--

DROP TABLE IF EXISTS `project_form`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_form` (
  `ProjectNumber` varchar(45) NOT NULL,
  `NoteID` varchar(45) DEFAULT NULL,
  `UniversalID` varchar(45) DEFAULT NULL,
  `AcctNotes` text,
  `ActionLog` text,
  `ActionNotes` text,
  `AddQuoteNotes` text,
  `Created` text,
  `LastAccessed` text,
  `LastModified` text,
  `Address1` text,
  `Address2` text,
  `AMPMReceived` text,
  `AnalysisComments` text,
  `AnalysisQty` text,
  `AnalysisTypes` text,
  `AuthorDate` text,
  `AuthorName` text,
  `Authors` text,
  `AutoEmailed` text,
  `City` text,
  `ClientWaitReason` text,
  `CompanyFirstProj` text,
  `CompanyName` text,
  `ComplexProject` text,
  `ContactName` text,
  `ContactNumber` text,
  `Country` text,
  `CustCriteria` text,
  `CustomCharge` text,
  `CustomDescription` text,
  `CustomReturnCharge` text,
  `CustType` text,
  `DangerousGoods` text,
  `DateDue` text,
  `DateReceived` text,
  `DateRcvd` varchar(10) DEFAULT NULL,
  `EditAuthors` text,
  `EditDates` text,
  `EditProjStatus` text,
  `EMail` text,
  `EnterDateDue` text,
  `EnterProjectNumber` text,
  `FamilyID` text,
  `FamilyName` text,
  `Fax` text,
  `FirstProjLookup` text,
  `HoldData` text,
  `HoldDataFollowup` text,
  `InDraftDate` text,
  `IndustryCode` text,
  `InProjectTask` text,
  `InvAddress1` text,
  `InvAddress2` text,
  `InvCity` text,
  `InvCompanyName` text,
  `InvContactName` text,
  `InvCountry` text,
  `InvEMail` text,
  `InvFamilyID` text,
  `POHardCopy` text,
  `PONumber` varchar(100) DEFAULT NULL,
  `InvFamilyName` text,
  `InvFax` text,
  `InvLocationID` text,
  `InvPersonID` text,
  `InvPhone` text,
  `InvState` text,
  `InvZip` text,
  `LocationID` text,
  `MethodServices` text,
  `MethodServiceType` text,
  `MSQuoteAllow` text,
  `NeedsHardCopyRpt` text,
  `OverrideCreditHold` text,
  `PersonID` varchar(100) DEFAULT NULL,
  `ProjCanceled` text,
  `ProjCGMP` varchar(5) DEFAULT NULL,
  `ProjDirector` text,
  `ProjEvent` text,
  `ProjID` varchar(35) DEFAULT NULL,
  `ProjISO` varchar(10) DEFAULT NULL,
  `ProjLitigation` text,
  `ProjPOFollowup` text,
  `ProjPriority` varchar(10) DEFAULT NULL,
  `ProjQADataRvw` text,
  `ProjQADiscrepancy` text,
  `ProjQARev` text,
  `ProjReptWrtr` text,
  `ProjSource` text,
  `ProjStatus` text,
  `ProjTechRev` text,
  `ProtocolPerson` text,
  `Quote` text,
  `ReportTracking` text,
  `ReturnReason` text,
  `ReturnShipFrom` text,
  `ReturnShipMethod` text,
  `ReturnShipSentDate` text,
  `ReturnTracking` text,
  `RptContactName` text,
  `RptDigBy` text,
  `RptDigSendDate` text,
  `RptDigSendTime` text,
  `RptDigSent` text,
  `RptDigTo` text,
  `RptHardCopySent` text,
  `RptLocationID` text,
  `RptPersonID` text,
  `RptShipFrom` text,
  `RptShipMethod` text,
  `RptShipSentDate` text,
  `RptShipSentTime` text,
  `SampDEAScheds` text,
  `SampleComments` text,
  `SampleQty` text,
  `SamplesDEA` text,
  `SamplesHaz` text,
  `SampleStorage` text,
  `SampleTypes` text,
  `SampReturn` text,
  `State` text,
  `TrackSelection` text,
  `ValidateNow` text,
  `Zip` text,
  `Affiliates1` text,
  `Affiliates2` text,
  `AffiliatesSummaryInfo1` text,
  `AffiliatesSummaryInfo2` text,
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
  `PartlyHiddenServices` text,
  `PartlyHiddenServices_Quotes` text,
  `PrefObjRepID` text,
  `ProjNum_Digits` text,
  PRIMARY KEY (`ProjectNumber`),
  UNIQUE KEY `projectNumber_UNIQUE` (`ProjectNumber`),
  KEY `idx_project_form_ProjID` (`ProjID`),
  KEY `idx_project_form_PONumber` (`PONumber`),
  KEY `idx_project_form_PersonID` (`PersonID`)
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

-- Dump completed on 2019-12-28 15:24:00
