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
-- Table structure for table `sample`
--

DROP TABLE IF EXISTS `sample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sample` (
  `SampLogNum` varchar(100) DEFAULT NULL,
  `ProjectNumber` varchar(100) DEFAULT NULL,
  `ProjID` varchar(100) DEFAULT NULL,
  `ActionLog` text,
  `ActionLogHdg` text,
  `ActionNotes` text,
  `AuthorDate` text,
  `AuthorName` text,
  `Authors` text,
  `CompanyName` text,
  `Created` text,
  `DangerousGoods` text,
  `DateDue` text,
  `DateReceived` text,
  `DEASchedule` text,
  `DocID` text,
  `EditAuthors` text,
  `EditDateName` text,
  `EditDates` text,
  `Edited` text,
  `EditProjStatus` text,
  `EmbeddedObjects` blob,
  `FamilyID` text,
  `FamilyName` text,
  `GHS00` text,
  `GHS01` text,
  `GHS02` text,
  `GHS03` text,
  `GHS04` text,
  `GHS05` text,
  `GHS06` text,
  `GHS07` text,
  `GHS08` text,
  `GHS09` text,
  `LastAccessed` text,
  `LastModified` text,
  `LightSensitive` text,
  `LocationID` text,
  `NoticeSent` text,
  `PrefObjRepID` text,
  `ProjStatus` text,
  `SampAnlReq` text,
  `SampBSL` text,
  `SampClass` text,
  `SampClassATF` text,
  `SampClassDEA` text,
  `SampHazards` text,
  `SampHazFlame` text,
  `SampHazHealth` text,
  `SampHazPPE` text,
  `SampHazReact` text,
  `SampID` text,
  `SampOneWordList` text,
  `SampPhraseList` text,
  `SampQty` text,
  `SampStorg` text,
  `SampTwoWordList` text,
  `SampType` text,
  `SignalWord` text,
  `SmplSrchWrdCnt` text,
  `UniversalID` text,
  `UNnumber` text,
  KEY `idx_sample_ProjectNumber` (`ProjectNumber`),
  KEY `idx_sample_ProjID` (`ProjID`)
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

-- Dump completed on 2019-12-28 15:23:59
