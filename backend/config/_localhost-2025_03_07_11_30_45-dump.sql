/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.6.2-MariaDB, for osx10.19 (x86_64)
--
-- Host: 127.0.0.1    Database: cogip
-- ------------------------------------------------------
-- Server version	11.6.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `companies`
--

DROP TABLE IF EXISTS `companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `companies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `type_id` int(11) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `tva` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `update_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `type_id` (`type_id`),
  CONSTRAINT `companies_ibfk_1` FOREIGN KEY (`type_id`) REFERENCES `types` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companies`
--

LOCK TABLES `companies` WRITE;
/*!40000 ALTER TABLE `companies` DISABLE KEYS */;
INSERT INTO `companies` VALUES
(1,'Raviga',1,'United States','US456 654 321','2020-09-25 00:00:00','2025-01-30 12:31:50'),
(2,'Dunder Mifflin',2,'United States','US676 787 767','2020-09-25 00:00:00','2025-01-30 12:31:50'),
(3,'Pierre Cailloux',1,'France','FR 676 676 676','2020-09-25 00:00:00','2025-01-30 12:31:50'),
(4,'Belgalol',1,'Belgium','BE0987 876 787','2020-09-25 00:00:00','2025-01-30 12:31:50'),
(5,'Jouet Jean-Michel',2,'France','FR 787 776 998','2020-09-25 00:00:00','2025-02-07 12:24:05'),
(6,'Pied Piper',2,'France','FR 787 776 876','2020-09-25 00:00:00','2025-02-07 11:47:37');
/*!40000 ALTER TABLE `companies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacts`
--

DROP TABLE IF EXISTS `contacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contacts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `company_id` int(11) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `update_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `contacts_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `companies` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts`
--

LOCK TABLES `contacts` WRITE;
/*!40000 ALTER TABLE `contacts` DISABLE KEYS */;
INSERT INTO `contacts` VALUES
(1,'Peter Gregory',1,'peter.gregory@raviga.com','555-4567','2020-09-25 00:00:00','2025-01-30 12:31:50'),
(2,'Cameron How',2,'cam.how@mutiny.net','555-8765','2020-09-25 00:00:00','2025-01-30 12:31:50'),
(3,'Gavin Belson',3,'gavin@hooli.com','555-6354','2020-09-25 00:00:00','2025-01-30 12:31:50'),
(4,'Jian Yang',4,'jian.yan@phoque.off','555-8765','2020-09-25 00:00:00','2025-01-30 12:31:50'),
(8,'test45',6,'testGH@gmail.com','123456','2025-02-04 12:30:01','2025-02-04 12:30:01'),
(10,'feferfe',6,'zeffze@zezf.com','ffzef','2025-02-04 20:32:07','2025-02-04 20:32:08'),
(11,'ezfzefz',6,'azazazaz@zdd.com','azazaz','2025-02-05 14:32:11','2025-02-05 14:32:11'),
(12,'zzefzef',6,'zddzed@zdzef.com','zzedz','2025-02-05 14:32:27','2025-02-05 14:32:24'),
(13,'zefzef',6,'zef@rf.com','zezefze','2025-02-05 14:32:38','2025-02-05 14:32:39'),
(14,'zedzed',6,'zefze@zfzef.com','zdzedzd','2025-02-05 14:32:48','2025-02-05 14:32:48'),
(15,'zfzef',6,'zezedze@zef.com','zefzef','2025-02-05 14:32:57','2025-02-05 14:32:57');
/*!40000 ALTER TABLE `contacts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoices`
--

DROP TABLE IF EXISTS `invoices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `invoices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ref` varchar(50) DEFAULT NULL,
  `id_company` int(11) NOT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `update_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `date_due` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_company` (`id_company`),
  CONSTRAINT `invoices_ibfk_1` FOREIGN KEY (`id_company`) REFERENCES `companies` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoices`
--

LOCK TABLES `invoices` WRITE;
/*!40000 ALTER TABLE `invoices` DISABLE KEYS */;
INSERT INTO `invoices` VALUES
(1,'F20220915-001',1,'2020-09-25 00:00:00','2025-02-06 10:35:48','2025-02-20'),
(2,'F20220915-002',6,'2020-09-25 00:00:00','2025-02-06 10:36:34','2025-02-20'),
(3,'F20220915-003',6,'2020-09-25 00:00:00','2025-02-06 10:36:34','2025-02-20'),
(4,'F20220915-004',6,'2020-09-25 00:00:00','2025-02-06 10:36:34','2025-02-20'),
(32,'F20250326-032',1,'2025-02-07 11:50:57','2025-02-07 11:50:57','2025-03-26'),
(33,'F20250323-033',2,'2025-02-07 11:51:07','2025-02-07 11:51:07','2025-03-23'),
(34,'F20250327-034',3,'2025-02-07 11:51:16','2025-02-07 11:51:16','2025-03-27'),
(35,'F20250329-035',3,'2025-02-07 11:51:22','2025-02-07 11:51:22','2025-03-29'),
(36,'F20250329-036',2,'2025-02-07 11:51:29','2025-02-07 11:51:29','2025-03-29'),
(37,'F20250329-037',1,'2025-02-07 11:51:33','2025-02-07 11:51:33','2025-03-29'),
(38,'F20250213-038',6,'2025-02-09 14:10:53','2025-02-09 14:10:53','2025-02-13'),
(39,'F20250312-039',6,'2025-02-09 14:12:49','2025-02-09 14:12:49','2025-03-12'),
(40,'F20250314-040',6,'2025-02-09 18:15:37','2025-02-09 18:15:37','2025-03-14'),
(44,'F20250315-044',6,'2025-02-09 18:19:50','2025-02-09 18:19:50','2025-03-15'),
(45,'9639818b-70eb-49d8-abe6-adf8da01327a',6,'2025-02-09 18:21:21','2025-02-09 18:21:21','2025-03-15'),
(47,'F20250315-64a0',6,'2025-02-09 18:30:55','2025-02-09 18:30:55','2025-03-15'),
(48,'F20250316-3cc1',6,'2025-02-09 18:38:01','2025-02-09 18:38:01','2025-03-16'),
(49,'F20250220-8d950209',6,'2025-02-09 19:15:05','2025-02-09 19:15:05','2025-02-20'),
(50,'F20250222-050',6,'2025-02-09 20:51:56','2025-02-09 20:51:56','2025-02-22'),
(51,'F20250224-3aa21ad1-2bd4-41e9-bb6a-35d7653d',6,'2025-02-09 20:53:52','2025-02-09 20:53:52','2025-02-24'),
(52,'F20250225-052',6,'2025-02-09 21:00:46','2025-02-09 21:00:46','2025-02-25'),
(53,'F20250225-22eab3ca-22c7-4f6b-9b2f-e9d3f078',6,'2025-02-09 21:04:14','2025-02-09 21:04:14','2025-02-25'),
(54,'F2025-02-25-054',6,'2025-02-09 21:07:07','2025-02-09 21:07:07','2025-02-25'),
(55,'F20250225-055',6,'2025-02-10 07:19:59','2025-02-10 07:19:59','2025-02-25'),
(57,'F20250225-057',6,'2025-02-10 07:22:54','2025-02-10 07:22:54','2025-02-25'),
(58,'F20250225-058',6,'2025-02-10 11:19:23','2025-02-10 11:19:23','2025-02-25'),
(61,'F20250225-618376c7-6a90-46f4-b76a-58c59234',6,'2025-02-10 11:41:02','2025-02-10 11:41:02','2025-02-25'),
(62,'F20250225-d7a',6,'2025-02-10 11:44:33','2025-02-10 11:44:33','2025-02-25'),
(63,'F20250225-063',6,'2025-02-10 11:45:28','2025-02-10 11:45:28','2025-02-25'),
(64,'F20250225-064',6,'2025-02-10 11:45:59','2025-02-10 11:45:59','2025-02-25'),
(65,'F20250225-39a9eb46-b60b-47bf-b8fe-ee025905',6,'2025-02-10 11:46:19','2025-02-10 11:46:19','2025-02-25'),
(66,'F20250226-066',6,'2025-02-10 13:35:30','2025-02-10 13:35:30','2025-02-26'),
(67,'F20250226-310545d2-b264-4a21-a331-dd34b638',6,'2025-02-10 13:38:22','2025-02-10 13:38:22','2025-02-26'),
(68,'F20250226-fcf',6,'2025-02-10 13:39:11','2025-02-10 13:39:11','2025-02-26');
/*!40000 ALTER TABLE `invoices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permissions`
--

DROP TABLE IF EXISTS `permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `update_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permissions`
--

LOCK TABLES `permissions` WRITE;
/*!40000 ALTER TABLE `permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `update_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES
(1,'membre','2025-01-31 14:00:33','2025-01-31 14:00:34'),
(2,'admin','2025-01-31 14:00:42','2025-01-31 14:00:43');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles_permission`
--

DROP TABLE IF EXISTS `roles_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roles_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `permission_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `permission_id` (`permission_id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `roles_permission_ibfk_1` FOREIGN KEY (`permission_id`) REFERENCES `permissions` (`id`),
  CONSTRAINT `roles_permission_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles_permission`
--

LOCK TABLES `roles_permission` WRITE;
/*!40000 ALTER TABLE `roles_permission` DISABLE KEYS */;
/*!40000 ALTER TABLE `roles_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `types`
--

DROP TABLE IF EXISTS `types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `update_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `types`
--

LOCK TABLES `types` WRITE;
/*!40000 ALTER TABLE `types` DISABLE KEYS */;
INSERT INTO `types` VALUES
(1,'Supplier','2025-01-30 12:31:50','2025-01-30 12:31:50'),
(2,'Client','2025-01-30 12:31:50','2025-01-30 12:31:50');
/*!40000 ALTER TABLE `types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `role_id` int(11) DEFAULT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `update_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES
(7,'Mohab',1,'Le G','mg@gmail.com','12345','2025-01-31 14:10:47','2025-02-07 11:53:03'),
(9,'Max',1,'Le A','ma@gmai.com','12345','2025-01-31 14:44:24','2025-02-07 11:53:03'),
(10,'Vespid',1,'Vespid','vespid2@gmail.com','12345','2025-01-31 14:46:17','2025-01-31 14:46:17'),
(11,'Vespid',1,'Vespid','vespid3@gmail.com','12345','2025-01-31 14:53:50','2025-01-31 14:53:50'),
(13,'Vespid',1,'Vespid','vespid4@gmail.com','12345','2025-01-31 16:31:46','2025-01-31 16:31:46'),
(14,'Jean-Christian',2,'Bernard','jcb@gmail.com','12345','2025-02-07 11:43:27','2025-02-07 11:43:28'),
(15,'Muriel',2,'Bernard','mb@gmail.com','12345','2025-02-07 11:44:04','2025-02-07 11:44:04');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-03-07 11:30:45
