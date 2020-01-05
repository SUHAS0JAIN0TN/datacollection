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
-- Table structure for table `contacts`
--

DROP TABLE IF EXISTS `contacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contacts` (
  `PersonID` varchar(50) NOT NULL,
  `CompanyID` varchar(50) DEFAULT NULL,
  `ActivityComments` text,
  `Assistant` text,
  `AssistantPhoneNumber` text,
  `AuthorDate` text,
  `AuthorName` text,
  `Authors` text,
  `CarPhoneNumber` text,
  `City` text,
  `Comment` text,
  `CompanyAcctExec` text,
  `CompanyAcctStatus` text,
  `CompanyAcctTeam` text,
  `CompanyIndustry` text,
  `CompanyName` text,
  `CompanyNumber` text,
  `CompanyParent` text,
  `CompanyPhoneNumber` text,
  `CompanyTerritory` text,
  `CompanyType` text,
  `Country` text,
  `Department` text,
  `Division` text,
  `DOB` text,
  `EditAuthors` text,
  `EditCount` text,
  `EditDateName` text,
  `EditDates` text,
  `Edited` text,
  `EditNames` text,
  `FamilyID` text,
  `FamilyName` text,
  `FirstMPhone` text,
  `FirstName` text,
  `FullName` text,
  `HomeCarPhoneNumber` text,
  `HomeCellPhoneNumber` text,
  `HomeFAXPhoneNumber` text,
  `IndustryCode` text,
  `Interest` text,
  `JobTitle` text,
  `LabelName` text,
  `LastAccessed` text,
  `LastModified` text,
  `LastMPhone` text,
  `LastName` text,
  `Location` text,
  `MailAddress` text,
  `MailDomain` text,
  `MailingList` text,
  `MailName` text,
  `MailSystem` text,
  `Manager` text,
  `MiddleInitial` text,
  `NickName` text,
  `Office800PhoneNumber` text,
  `OfficeAddress1` text,
  `OfficeAddress2` text,
  `OfficeCity` text,
  `OfficeCountry` text,
  `OfficeFAXPhoneNumber` text,
  `OfficePhoneNumber` text,
  `OfficeState` text,
  `OfficeZip` text,
  `OMailAddress1` text,
  `OMailAddress2` text,
  `OMailCity` text,
  `OMailCountry` text,
  `OMailState` text,
  `OMailZip` text,
  `Owners` text,
  `PagerPhoneNumber` text,
  `Person800PhoneNumber` text,
  `PersonAddress1` text,
  `PersonAddress2` text,
  `PersonCity` text,
  `PersonCountry` text,
  `PersonFAXPhoneNumber` text,
  `PersonNameLFM` text,
  `PersonPhoneNumber` text,
  `PersonState` text,
  `PersonZip` text,
  `PhoneNumber` text,
  `PMailAddress1` text,
  `PMailAddress2` text,
  `PMailCity` text,
  `PMailCountry` text,
  `PMailState` text,
  `PrefObjRepID` text,
  `ReferralSource` text,
  `ReferredBy` text,
  `Rel` text,
  `Relationships` text,
  `Responsibility` text,
  `Salutation` text,
  `State` text,
  `Status` text,
  `StreetAddress` text,
  `Type` text,
  `UniversalID` text,
  `UserNameList` text,
  `UserNamesList_1` text,
  `Zip` text,
  PRIMARY KEY (`PersonID`)
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
