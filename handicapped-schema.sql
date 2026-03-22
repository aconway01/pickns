-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: aconway01.mysql.pythonanywhere-services.com    Database: aconway01$handicapped
-- ------------------------------------------------------
-- Server version	5.7.44-rds.20250508-log

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `equibasecard`
--

DROP TABLE IF EXISTS `equibasecard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equibasecard` (
  `equibasecard_id` int(11) NOT NULL AUTO_INCREMENT,
  `carddate` date DEFAULT NULL,
  `Track_Id` varchar(255) DEFAULT NULL,
  `Track_Name` varchar(255) DEFAULT NULL,
  `Area_Id` varchar(255) DEFAULT NULL,
  `EquibaseState` varchar(255) DEFAULT NULL,
  `Track_Stage` varchar(255) DEFAULT NULL,
  `is_bullring` varchar(1) DEFAULT NULL,
  `xml_flag` varchar(1) DEFAULT NULL,
  `isfeat` varchar(1) DEFAULT NULL,
  `frank` varchar(255) DEFAULT NULL,
  `Race_Number` varchar(255) DEFAULT NULL,
  `EquibaseText` text,
  `EquibaseDescription` varchar(255) DEFAULT NULL,
  `Wager_Text` text,
  `Total_Purse` decimal(14,2) DEFAULT NULL,
  `Post_Time` datetime DEFAULT NULL,
  `Race_Time` datetime DEFAULT NULL,
  `Day_Eve` varchar(255) DEFAULT NULL,
  `race_type_desc` varchar(255) DEFAULT NULL,
  `max_claim_price` decimal(14,2) DEFAULT NULL,
  `distance_unit` varchar(255) DEFAULT NULL,
  `distance_id` varchar(255) DEFAULT NULL,
  `distance_in_furlong` decimal(7,2) DEFAULT NULL,
  `course_type` varchar(255) DEFAULT NULL,
  `pub_val` varchar(255) DEFAULT NULL,
  `distance_display` decimal(7,2) DEFAULT NULL,
  `surface_display` varchar(255) DEFAULT NULL,
  `race_breed_type` varchar(255) DEFAULT NULL,
  `race_Type` varchar(255) DEFAULT NULL,
  `age_restriction` varchar(255) DEFAULT NULL,
  `class_rating` varchar(255) DEFAULT NULL,
  `distance_unit_desc` varchar(255) DEFAULT NULL,
  `Prog_No` varchar(255) DEFAULT NULL,
  `Reg_No` varchar(255) DEFAULT NULL,
  `Horse_Name` varchar(255) DEFAULT NULL,
  `ct` varchar(255) DEFAULT NULL,
  `Win_Per` varchar(255) DEFAULT NULL,
  `ML_Odds` varchar(255) DEFAULT NULL,
  `Scratch_Indicator` varchar(255) DEFAULT NULL,
  `post_pos` varchar(255) DEFAULT NULL,
  `breed_type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`equibasecard_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1314478 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `equibasecarddaily`
--

DROP TABLE IF EXISTS `equibasecarddaily`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equibasecarddaily` (
  `equibasecard_id` int(11) NOT NULL AUTO_INCREMENT,
  `carddate` date DEFAULT NULL,
  `Track_Id` varchar(255) DEFAULT NULL,
  `Track_Name` varchar(255) DEFAULT NULL,
  `Area_Id` varchar(255) DEFAULT NULL,
  `EquibaseState` varchar(255) DEFAULT NULL,
  `Track_Stage` varchar(255) DEFAULT NULL,
  `is_bullring` varchar(1) DEFAULT NULL,
  `xml_flag` varchar(1) DEFAULT NULL,
  `isfeat` varchar(1) DEFAULT NULL,
  `frank` varchar(255) DEFAULT NULL,
  `Race_Number` varchar(255) DEFAULT NULL,
  `EquibaseText` text,
  `EquibaseDescription` varchar(255) DEFAULT NULL,
  `Wager_Text` text,
  `Total_Purse` decimal(14,2) DEFAULT NULL,
  `Post_Time` datetime DEFAULT NULL,
  `Race_Time` datetime DEFAULT NULL,
  `Day_Eve` varchar(255) DEFAULT NULL,
  `race_type_desc` varchar(255) DEFAULT NULL,
  `max_claim_price` decimal(14,2) DEFAULT NULL,
  `distance_unit` varchar(255) DEFAULT NULL,
  `distance_id` varchar(255) DEFAULT NULL,
  `distance_in_furlong` decimal(7,2) DEFAULT NULL,
  `course_type` varchar(255) DEFAULT NULL,
  `pub_val` varchar(255) DEFAULT NULL,
  `distance_display` decimal(7,2) DEFAULT NULL,
  `surface_display` varchar(255) DEFAULT NULL,
  `race_breed_type` varchar(255) DEFAULT NULL,
  `race_Type` varchar(255) DEFAULT NULL,
  `age_restriction` varchar(255) DEFAULT NULL,
  `class_rating` varchar(255) DEFAULT NULL,
  `distance_unit_desc` varchar(255) DEFAULT NULL,
  `Prog_No` varchar(255) DEFAULT NULL,
  `Reg_No` varchar(255) DEFAULT NULL,
  `Horse_Name` varchar(255) DEFAULT NULL,
  `ct` varchar(255) DEFAULT NULL,
  `Win_Per` varchar(255) DEFAULT NULL,
  `ML_Odds` varchar(255) DEFAULT NULL,
  `Scratch_Indicator` varchar(255) DEFAULT NULL,
  `post_pos` varchar(255) DEFAULT NULL,
  `breed_type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`equibasecard_id`)
) ENGINE=InnoDB AUTO_INCREMENT=735294 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `equibasejockeys`
--

DROP TABLE IF EXISTS `equibasejockeys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equibasejockeys` (
  `equibasejockeys_id` int(11) NOT NULL AUTO_INCREMENT,
  `raceyear` varchar(10) DEFAULT NULL,
  `jockeyname` varchar(255) DEFAULT NULL,
  `winpercentage` decimal(6,2) DEFAULT NULL,
  `equibaseidentity` varchar(255) DEFAULT NULL,
  `earnings` decimal(14,2) DEFAULT NULL,
  `equibaserank` varchar(255) DEFAULT NULL,
  `place` decimal(8,2) DEFAULT NULL,
  `equibasestarts` decimal(8,2) DEFAULT NULL,
  `perstart` decimal(14,2) DEFAULT NULL,
  `topthreepercent` decimal(8,2) DEFAULT NULL,
  `equibaseshow` decimal(8,2) DEFAULT NULL,
  `win` decimal(8,2) DEFAULT NULL,
  `topthree` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`equibasejockeys_id`)
) ENGINE=InnoDB AUTO_INCREMENT=132420 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `equibaseowners`
--

DROP TABLE IF EXISTS `equibaseowners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equibaseowners` (
  `equibaseowners_id` int(11) NOT NULL AUTO_INCREMENT,
  `raceyear` varchar(10) DEFAULT NULL,
  `ownername` varchar(255) DEFAULT NULL,
  `winpercentage` decimal(6,2) DEFAULT NULL,
  `equibaseidentity` varchar(255) DEFAULT NULL,
  `earnings` decimal(14,2) DEFAULT NULL,
  `equibaserank` varchar(255) DEFAULT NULL,
  `place` decimal(8,2) DEFAULT NULL,
  `equibasestarts` decimal(8,2) DEFAULT NULL,
  `perstart` decimal(14,2) DEFAULT NULL,
  `topthreepercent` decimal(8,2) DEFAULT NULL,
  `equibaseshow` decimal(8,2) DEFAULT NULL,
  `win` decimal(8,2) DEFAULT NULL,
  `topthree` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`equibaseowners_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1895630 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `equibaserunnerinfo`
--

DROP TABLE IF EXISTS `equibaserunnerinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equibaserunnerinfo` (
  `equibaserunnerinfo_id` int(11) NOT NULL AUTO_INCREMENT,
  `trackid` varchar(255) DEFAULT NULL,
  `areaid` varchar(255) DEFAULT NULL,
  `racedate` date DEFAULT NULL,
  `raceyear` varchar(3) DEFAULT NULL,
  `racemonth` varchar(3) DEFAULT NULL,
  `raceday` varchar(3) DEFAULT NULL,
  `racenumber` varchar(255) DEFAULT NULL,
  `horsename` varchar(255) DEFAULT NULL,
  `horserefno` varchar(255) DEFAULT NULL,
  `jockeyname` varchar(255) DEFAULT NULL,
  `jockeyid` varchar(255) DEFAULT NULL,
  `trainername` varchar(255) DEFAULT NULL,
  `trainerid` varchar(255) DEFAULT NULL,
  `ownername` varchar(255) DEFAULT NULL,
  `ownerid` varchar(255) DEFAULT NULL,
  `sirename` varchar(255) DEFAULT NULL,
  `damname` varchar(255) DEFAULT NULL,
  `damsirename` varchar(255) DEFAULT NULL,
  `breeder` varchar(255) DEFAULT NULL,
  `pp` varchar(3) DEFAULT NULL,
  `age` varchar(3) DEFAULT NULL,
  `sex` varchar(2) DEFAULT NULL,
  `med` varchar(3) DEFAULT NULL,
  `jockeyweight` varchar(4) DEFAULT NULL,
  `mlodds` varchar(255) DEFAULT NULL,
  `claim` decimal(14,2) DEFAULT NULL,
  PRIMARY KEY (`equibaserunnerinfo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=746972 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `equibaserunnerinfodaily`
--

DROP TABLE IF EXISTS `equibaserunnerinfodaily`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equibaserunnerinfodaily` (
  `equibaserunnerinfo_id` int(11) NOT NULL AUTO_INCREMENT,
  `trackid` varchar(255) DEFAULT NULL,
  `areaid` varchar(255) DEFAULT NULL,
  `racedate` date DEFAULT NULL,
  `raceyear` varchar(3) DEFAULT NULL,
  `racemonth` varchar(3) DEFAULT NULL,
  `raceday` varchar(3) DEFAULT NULL,
  `racenumber` varchar(255) DEFAULT NULL,
  `horsename` varchar(255) DEFAULT NULL,
  `horserefno` varchar(255) DEFAULT NULL,
  `jockeyname` varchar(255) DEFAULT NULL,
  `jockeyid` varchar(255) DEFAULT NULL,
  `trainername` varchar(255) DEFAULT NULL,
  `trainerid` varchar(255) DEFAULT NULL,
  `ownername` varchar(255) DEFAULT NULL,
  `ownerid` varchar(255) DEFAULT NULL,
  `sirename` varchar(255) DEFAULT NULL,
  `damname` varchar(255) DEFAULT NULL,
  `damsirename` varchar(255) DEFAULT NULL,
  `breeder` varchar(255) DEFAULT NULL,
  `pp` varchar(3) DEFAULT NULL,
  `age` varchar(3) DEFAULT NULL,
  `sex` varchar(2) DEFAULT NULL,
  `med` varchar(3) DEFAULT NULL,
  `jockeyweight` varchar(4) DEFAULT NULL,
  `mlodds` varchar(255) DEFAULT NULL,
  `claim` decimal(14,2) DEFAULT NULL,
  PRIMARY KEY (`equibaserunnerinfo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=638102 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `equibasethoroughbredhorses`
--

DROP TABLE IF EXISTS `equibasethoroughbredhorses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equibasethoroughbredhorses` (
  `equibasethoroughbredhorses_id` int(11) NOT NULL AUTO_INCREMENT,
  `raceyear` varchar(10) DEFAULT NULL,
  `horsename` varchar(255) DEFAULT NULL,
  `winpercentage` decimal(6,2) DEFAULT NULL,
  `referencenumber` varchar(255) DEFAULT NULL,
  `earnings` decimal(14,2) DEFAULT NULL,
  `equibaserank` varchar(255) DEFAULT NULL,
  `place` decimal(8,2) DEFAULT NULL,
  `sirereference` varchar(255) DEFAULT NULL,
  `equibasestarts` decimal(8,2) DEFAULT NULL,
  `sirename` varchar(255) DEFAULT NULL,
  `speedfigure` varchar(255) DEFAULT NULL,
  `perstart` decimal(14,2) DEFAULT NULL,
  `topthreepercent` decimal(8,2) DEFAULT NULL,
  `equibaseshow` decimal(8,2) DEFAULT NULL,
  `win` decimal(8,2) DEFAULT NULL,
  `topthree` decimal(8,2) DEFAULT NULL,
  `registry` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`equibasethoroughbredhorses_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3905379 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `equibasetrainers`
--

DROP TABLE IF EXISTS `equibasetrainers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equibasetrainers` (
  `equibasetrainers_id` int(11) NOT NULL AUTO_INCREMENT,
  `raceyear` varchar(10) DEFAULT NULL,
  `trainername` varchar(255) DEFAULT NULL,
  `wpsperstarter` decimal(10,5) DEFAULT NULL,
  `earningsperstarter` decimal(10,5) DEFAULT NULL,
  `winpercentage` decimal(6,2) DEFAULT NULL,
  `equibaseidentity` varchar(255) DEFAULT NULL,
  `starters` decimal(8,2) DEFAULT NULL,
  `earnings` decimal(14,2) DEFAULT NULL,
  `equibaserank` varchar(255) DEFAULT NULL,
  `place` decimal(8,2) DEFAULT NULL,
  `equibasestarts` decimal(8,2) DEFAULT NULL,
  `perstart` decimal(14,2) DEFAULT NULL,
  `topthreepercent` decimal(8,2) DEFAULT NULL,
  `equibaseshow` decimal(8,2) DEFAULT NULL,
  `win` decimal(8,2) DEFAULT NULL,
  `startsperstarter` decimal(10,5) DEFAULT NULL,
  `topthree` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`equibasetrainers_id`)
) ENGINE=InnoDB AUTO_INCREMENT=401738 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `registration_registrationprofile`
--

DROP TABLE IF EXISTS `registration_registrationprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registration_registrationprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `activation_key` varchar(64) NOT NULL,
  `user_id` int(11) NOT NULL,
  `activated` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `registration_registr_user_id_5fcbf725_fk_auth_user` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `registration_supervisedregistrationprofile`
--

DROP TABLE IF EXISTS `registration_supervisedregistrationprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registration_supervisedregistrationprofile` (
  `registrationprofile_ptr_id` int(11) NOT NULL,
  PRIMARY KEY (`registrationprofile_ptr_id`),
  CONSTRAINT `registration_supervi_registrationprofile__0a59f3b2_fk_registrat` FOREIGN KEY (`registrationprofile_ptr_id`) REFERENCES `registration_registrationprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-22 11:27:31
