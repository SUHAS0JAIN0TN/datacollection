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
-- Table structure for table `project_formn1`
--

DROP TABLE IF EXISTS `project_formn1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_formn1` (
  `ProjectNumber` varchar(35) NOT NULL,
  `FamilyID` varchar(30) DEFAULT NULL,
  `LocationID` varchar(30) DEFAULT NULL,
  `PersonID` varchar(100) DEFAULT NULL,
  `UniversalID` varchar(45) DEFAULT NULL,
  `Address1` varchar(100) DEFAULT NULL,
  `Address2` varchar(100) DEFAULT NULL,
  `AMPMReceived` varchar(30) DEFAULT NULL,
  `AnalysisQty` varchar(30) DEFAULT NULL,
  `AnalysisTypes` varchar(100) DEFAULT NULL,
  `AuthorDate` varchar(30) DEFAULT NULL,
  `AuthorName` varchar(50) DEFAULT NULL,
  `AutoEmailed` varchar(30) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  `ClientWaitReason` varchar(30) DEFAULT NULL,
  `CompanyFirstProj` varchar(30) DEFAULT NULL,
  `CompanyName` varchar(100) DEFAULT NULL,
  `ComplexProject` varchar(30) DEFAULT NULL,
  `ContactName` varchar(50) DEFAULT NULL,
  `ContactNumber` varchar(50) DEFAULT NULL,
  `Country` varchar(30) DEFAULT NULL,
  `CustCriteria` varchar(30) DEFAULT NULL,
  `CustomCharge` varchar(30) DEFAULT NULL,
  `CustomDescription` text,
  `CustomReturnCharge` varchar(30) DEFAULT NULL,
  `CustType` varchar(30) DEFAULT NULL,
  `DangerousGoods` varchar(30) DEFAULT NULL,
  `DateDue` varchar(30) DEFAULT NULL,
  `DateReceived` varchar(30) DEFAULT NULL,
  `DateRcvd` varchar(15) DEFAULT NULL,
  `EMail` varchar(100) DEFAULT NULL,
  `EnterDateDue` varchar(30) DEFAULT NULL,
  `EnterProjectNumber` varchar(30) DEFAULT NULL,
  `FamilyName` varchar(150) DEFAULT NULL,
  `Fax` varchar(35) DEFAULT NULL,
  `FirstProjLookup` varchar(10) DEFAULT NULL,
  `HoldData` varchar(10) DEFAULT NULL,
  `HoldDataFollowup` varchar(30) DEFAULT NULL,
  `InDraftDate` varchar(50) DEFAULT NULL,
  `IndustryCode` varchar(30) DEFAULT NULL,
  `InProjectTask` varchar(30) DEFAULT NULL,
  `InvAddress1` varchar(100) DEFAULT NULL,
  `InvAddress2` varchar(30) DEFAULT NULL,
  `InvCity` varchar(30) DEFAULT NULL,
  `InvCompanyName` varchar(100) DEFAULT NULL,
  `InvContactName` varchar(30) DEFAULT NULL,
  `InvCountry` varchar(30) DEFAULT NULL,
  `InvEMail` varchar(100) DEFAULT NULL,
  `InvFamilyID` varchar(30) DEFAULT NULL,
  `InvFamilyName` varchar(70) DEFAULT NULL,
  `InvFax` varchar(30) DEFAULT NULL,
  `InvLocationID` varchar(30) DEFAULT NULL,
  `InvPersonID` varchar(30) DEFAULT NULL,
  `InvPhone` varchar(30) DEFAULT NULL,
  `InvState` varchar(30) DEFAULT NULL,
  `InvZip` varchar(30) DEFAULT NULL,
  `MethodServices` varchar(30) DEFAULT NULL,
  `MethodServiceType` varchar(30) DEFAULT NULL,
  `MSQuoteAllow` varchar(30) DEFAULT NULL,
  `NeedsHardCopyRpt` varchar(30) DEFAULT NULL,
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
  `OverrideCreditHold` text,
  `ProjCanceled` varchar(10) DEFAULT NULL,
  `ProjCGMP` varchar(5) DEFAULT NULL,
  `ProjDirector` varchar(30) DEFAULT NULL,
  `ProjEvent` varchar(30) DEFAULT NULL,
  `ProjID` varchar(35) DEFAULT NULL,
  `ProjISO` varchar(10) DEFAULT NULL,
  `ProjLitigation` varchar(30) DEFAULT NULL,
  `ProjPOFollowup` varchar(30) DEFAULT NULL,
  `ProjPriority` varchar(10) DEFAULT NULL,
  `ProjQADataRvw` varchar(10) DEFAULT NULL,
  `ProjQADiscrepancy` varchar(30) DEFAULT NULL,
  `ProjQARev` varchar(30) DEFAULT NULL,
  `ProjReptWrtr` varchar(30) DEFAULT NULL,
  `ProjSource` varchar(30) DEFAULT NULL,
  `ProjStatus` varchar(50) DEFAULT NULL,
  `ProjTechRev` varchar(30) DEFAULT NULL,
  `ProtocolPerson` varchar(30) DEFAULT NULL,
  `POHardCopy` varchar(30) DEFAULT NULL,
  `PONumber` varchar(100) DEFAULT NULL,
  `Quote` varchar(75) DEFAULT NULL,
  `ReportTracking` varchar(100) DEFAULT NULL,
  `ReturnReason` varchar(50) DEFAULT NULL,
  `ReturnShipFrom` varchar(50) DEFAULT NULL,
  `ReturnShipMethod` varchar(50) DEFAULT NULL,
  `ReturnShipSentDate` varchar(30) DEFAULT NULL,
  `ReturnTracking` varchar(100) DEFAULT NULL,
  `RptContactName` varchar(75) DEFAULT NULL,
  `RptDigBy` varchar(30) DEFAULT NULL,
  `RptDigSendDate` varchar(30) DEFAULT NULL,
  `RptDigSendTime` varchar(30) DEFAULT NULL,
  `RptDigSent` varchar(30) DEFAULT NULL,
  `RptDigTo` text,
  `RptHardCopySent` varchar(30) DEFAULT NULL,
  `RptLocationID` varchar(30) DEFAULT NULL,
  `RptPersonID` varchar(30) DEFAULT NULL,
  `RptShipFrom` varchar(50) DEFAULT NULL,
  `RptShipMethod` varchar(50) DEFAULT NULL,
  `RptShipSentDate` varchar(30) DEFAULT NULL,
  `RptShipSentTime` varchar(30) DEFAULT NULL,
  `SampDEAScheds` varchar(30) DEFAULT NULL,
  `SampleQty` varchar(10) DEFAULT NULL,
  `SamplesDEA` varchar(10) DEFAULT NULL,
  `SamplesHaz` varchar(10) DEFAULT NULL,
  `SampleStorage` varchar(30) DEFAULT NULL,
  `SampleTypes` text,
  `SampReturn` varchar(30) DEFAULT NULL,
  `State` varchar(30) DEFAULT NULL,
  `TrackSelection` varchar(30) DEFAULT NULL,
  `Zip` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`ProjectNumber`),
  UNIQUE KEY `projectNumber_UNIQUE` (`ProjectNumber`),
  KEY `idx_project_form_ProjID` (`ProjID`),
  KEY `idx_project_form_PONumber` (`PONumber`),
  KEY `idx_project_form_PersonID` (`PersonID`),
  KEY `CompanyName` (`CompanyName`)
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

-- Dump completed on 2019-12-28 15:24:05
