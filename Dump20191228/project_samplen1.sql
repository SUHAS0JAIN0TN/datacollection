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
-- Table structure for table `samplen1`
--

DROP TABLE IF EXISTS `samplen1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `samplen1` (
  `SampLogNum` varchar(35) DEFAULT NULL,
  `ProjectNumber` varchar(35) DEFAULT NULL,
  `DocID` varchar(35) DEFAULT NULL,
  `FamilyID` varchar(100) DEFAULT NULL,
  `LocationID` varchar(35) DEFAULT NULL,
  `ProjID` varchar(35) DEFAULT NULL,
  `SampID` varchar(176) DEFAULT NULL,
  `ActionLog` text,
  `AuthorDate` varchar(35) DEFAULT NULL,
  `AuthorName` varchar(35) DEFAULT NULL,
  `CompanyName` varchar(100) DEFAULT NULL,
  `DangerousGoods` varchar(15) DEFAULT NULL,
  `DateDue` varchar(35) DEFAULT NULL,
  `DateReceived` varchar(35) DEFAULT NULL,
  `DEASchedule` varchar(35) DEFAULT NULL,
  `FamilyName` varchar(150) DEFAULT NULL,
  `GHS00` varchar(15) DEFAULT NULL,
  `GHS01` varchar(15) DEFAULT NULL,
  `GHS02` varchar(15) DEFAULT NULL,
  `GHS03` varchar(15) DEFAULT NULL,
  `GHS04` varchar(15) DEFAULT NULL,
  `GHS05` varchar(15) DEFAULT NULL,
  `GHS06` varchar(15) DEFAULT NULL,
  `GHS07` varchar(15) DEFAULT NULL,
  `GHS08` varchar(15) DEFAULT NULL,
  `GHS09` varchar(15) DEFAULT NULL,
  `NoticeSent` varchar(15) DEFAULT NULL,
  `ProjStatus` varchar(35) DEFAULT NULL,
  `SampAnlReq` varchar(35) DEFAULT NULL,
  `SampBSL` varchar(15) DEFAULT NULL,
  `SampClass` varchar(15) DEFAULT NULL,
  `SampClassATF` varchar(15) DEFAULT NULL,
  `SampClassDEA` varchar(15) DEFAULT NULL,
  `SampHazards` varchar(15) DEFAULT NULL,
  `SampHazFlame` varchar(15) DEFAULT NULL,
  `SampHazHealth` varchar(15) DEFAULT NULL,
  `SampHazPPE` varchar(15) DEFAULT NULL,
  `SampHazReact` varchar(15) DEFAULT NULL,
  `SampOneWordList` varchar(15) DEFAULT NULL,
  `SampPhraseList` varchar(15) DEFAULT NULL,
  `SampQty` varchar(15) DEFAULT NULL,
  `SampStorg` varchar(35) DEFAULT NULL,
  `SampTwoWordList` varchar(35) DEFAULT NULL,
  `SampType` text,
  `SignalWord` varchar(35) DEFAULT NULL,
  `SmplSrchWrdCnt` varchar(35) DEFAULT NULL,
  `UniversalID` varchar(35) DEFAULT NULL,
  KEY `idx_sample_ProjectNumber` (`ProjectNumber`),
  KEY `idx_sample_ProjID` (`ProjID`),
  KEY `FamilyID` (`FamilyID`) /*!80000 INVISIBLE */,
  KEY `DocID` (`DocID`) /*!80000 INVISIBLE */,
  KEY `LocationID` (`LocationID`) /*!80000 INVISIBLE */,
  KEY `SampID` (`SampID`) /*!80000 INVISIBLE */
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
