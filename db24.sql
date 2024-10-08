-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: db24centromedico
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbclienti`
--

DROP TABLE IF EXISTS `tbclienti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbclienti` (
  `idcliente` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `cognome` varchar(45) NOT NULL,
  `usrmail` varchar(45) DEFAULT NULL,
  `pwd` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idcliente`),
  UNIQUE KEY `UQ_USR` (`usrmail`),
  KEY `IDX_COGNOME` (`cognome`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbclienti`
--

LOCK TABLES `tbclienti` WRITE;
/*!40000 ALTER TABLE `tbclienti` DISABLE KEYS */;
INSERT INTO `tbclienti` VALUES (38,'alfonso','domenici','alfonso.domenici@gmail.com','$pbkdf2-sha256$29000$835vLeX8nzNG6H2PUar1Xg$Uh0sWrD5GSBpqP2.UNjLUvY18wvNIY2Ay1hwlCnQgLk'),(39,'mario','rossi','rossi@gmail.com','$pbkdf2-sha256$29000$zZlzDmHs3fs/B.D831sLgQ$ro63DePje06QNsH3d9/s6ElHChcLJHRFlBMwJtEMGro'),(40,'mario','verdi','verdi@gmail.com','$pbkdf2-sha256$29000$jHGOsZZy7n3v/b93TonRmg$eOmULE6d.U/kkH6.RzSLo92hUkh7wXnBPCSy4/89fCc'),(41,'qwe','qwe','qwe','$pbkdf2-sha256$29000$.p9zLgUAIISQUiqFMAagdA$aBN8.xk/mBGjJMaPVSq6JTGLMX1HqdKr7VDpMjTFTJw');
/*!40000 ALTER TABLE `tbclienti` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbprenotazioni`
--

DROP TABLE IF EXISTS `tbprenotazioni`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbprenotazioni` (
  `idprenotazioni` int NOT NULL AUTO_INCREMENT,
  `idcliente` int NOT NULL,
  `idvisita` int NOT NULL,
  `data` datetime DEFAULT NULL,
  `pagato` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`idprenotazioni`),
  KEY `IDX_IDCLIENTE` (`idcliente`) /*!80000 INVISIBLE */,
  KEY `IDX_VISITA` (`idvisita`) /*!80000 INVISIBLE */,
  KEY `IDX_DATA` (`data`),
  CONSTRAINT `FK_IDCLIENTE` FOREIGN KEY (`idcliente`) REFERENCES `tbclienti` (`idcliente`),
  CONSTRAINT `FK_VISITE` FOREIGN KEY (`idvisita`) REFERENCES `tbvisite` (`idvisita`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbprenotazioni`
--

LOCK TABLES `tbprenotazioni` WRITE;
/*!40000 ALTER TABLE `tbprenotazioni` DISABLE KEYS */;
INSERT INTO `tbprenotazioni` VALUES (17,38,1,'2024-06-27 20:12:00',100.00),(18,38,1,'2024-06-26 16:18:00',80.00),(19,38,2,'2024-07-16 16:20:00',120.00),(20,39,2,'2024-07-01 08:00:00',40.00),(21,41,2,'2024-07-08 10:06:00',123.00);
/*!40000 ALTER TABLE `tbprenotazioni` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbvisite`
--

DROP TABLE IF EXISTS `tbvisite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbvisite` (
  `idvisita` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(45) NOT NULL,
  `costo` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`idvisita`),
  UNIQUE KEY `IDX_VISITA` (`tipo`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbvisite`
--

LOCK TABLES `tbvisite` WRITE;
/*!40000 ALTER TABLE `tbvisite` DISABLE KEYS */;
INSERT INTO `tbvisite` VALUES (1,'VISITA ODONTOIATRICA',120.00),(2,'VISITA OCULISTICA',100.00),(4,'visita dermatologica',90.00),(5,'Visita cardiaca',150.00),(6,'visita gomito tennista',150.00),(7,'visita endocrinologica',100.00),(8,'VISITA SPORTIVA',150.00);
/*!40000 ALTER TABLE `tbvisite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `v_prenotazioni`
--

DROP TABLE IF EXISTS `v_prenotazioni`;
/*!50001 DROP VIEW IF EXISTS `v_prenotazioni`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_prenotazioni` AS SELECT 
 1 AS `idcliente`,
 1 AS `nome`,
 1 AS `cognome`,
 1 AS `data`,
 1 AS `pagato`,
 1 AS `tipo`,
 1 AS `costo`,
 1 AS `saldo`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `v_prenotazioni`
--

/*!50001 DROP VIEW IF EXISTS `v_prenotazioni`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_prenotazioni` AS select `tbclienti`.`idcliente` AS `idcliente`,`tbclienti`.`nome` AS `nome`,`tbclienti`.`cognome` AS `cognome`,`tbprenotazioni`.`data` AS `data`,`tbprenotazioni`.`pagato` AS `pagato`,`tbvisite`.`tipo` AS `tipo`,`tbvisite`.`costo` AS `costo`,(`tbvisite`.`costo` - `tbprenotazioni`.`pagato`) AS `saldo` from ((`tbclienti` join `tbprenotazioni` on((`tbclienti`.`idcliente` = `tbprenotazioni`.`idcliente`))) join `tbvisite` on((`tbvisite`.`idvisita` = `tbprenotazioni`.`idvisita`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-23 15:57:40
