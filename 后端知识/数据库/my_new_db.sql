-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: my_new_db
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
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
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add user',2,'add_user'),(5,'Can change user',2,'change_user'),(6,'Can delete user',2,'delete_user'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add permission',4,'add_permission'),(11,'Can change permission',4,'change_permission'),(12,'Can delete permission',4,'delete_permission'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add lei',7,'add_lei'),(20,'Can change lei',7,'change_lei'),(21,'Can delete lei',7,'delete_lei'),(22,'Can add wenzhang',8,'add_wenzhang'),(23,'Can change wenzhang',8,'change_wenzhang'),(24,'Can delete wenzhang',8,'delete_wenzhang'),(25,'Can add mingpian',9,'add_mingpian'),(26,'Can change mingpian',9,'change_mingpian'),(27,'Can delete mingpian',9,'delete_mingpian'),(28,'Can add daohang',10,'add_daohang'),(29,'Can change daohang',10,'change_daohang'),(30,'Can delete daohang',10,'delete_daohang');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$ufolC2IUPScx$hpi1vwTkcoul0kw5xLlxlhCWWGiDhtQ3W5IEBF2v9PY=','2018-11-23 02:33:08.904495',1,'sj','','','123@qq.com',1,1,'2018-11-23 02:31:37.399560');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
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
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
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
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booktest_daohang`
--

DROP TABLE IF EXISTS `booktest_daohang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `booktest_daohang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dtitle` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booktest_daohang`
--

LOCK TABLES `booktest_daohang` WRITE;
/*!40000 ALTER TABLE `booktest_daohang` DISABLE KEYS */;
INSERT INTO `booktest_daohang` VALUES (1,'文章'),(2,'个人博客'),(3,'说说'),(4,'说说'),(5,'心情日志'),(6,'个人博客');
/*!40000 ALTER TABLE `booktest_daohang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booktest_lei`
--

DROP TABLE IF EXISTS `booktest_lei`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `booktest_lei` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lname` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booktest_lei`
--

LOCK TABLES `booktest_lei` WRITE;
/*!40000 ALTER TABLE `booktest_lei` DISABLE KEYS */;
INSERT INTO `booktest_lei` VALUES (1,'慢生活'),(2,'爱情美文'),(3,'博客模板'),(4,'女生博客模板'),(5,'马大哈风格');
/*!40000 ALTER TABLE `booktest_lei` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booktest_mingpian`
--

DROP TABLE IF EXISTS `booktest_mingpian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `booktest_mingpian` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mtitle` varchar(25) NOT NULL,
  `mdianhua` varchar(100) NOT NULL,
  `memail` varchar(100) NOT NULL,
  `mwangm` varchar(100) NOT NULL,
  `mzhiye` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booktest_mingpian`
--

LOCK TABLES `booktest_mingpian` WRITE;
/*!40000 ALTER TABLE `booktest_mingpian` DISABLE KEYS */;
INSERT INTO `booktest_mingpian` VALUES (1,'个人信息','电话：18883397160','Email：long_mu_fang@163.com','网名：新疆马蹄打了贝贝 | 含雪红梅','职业：Web前端设计师、网页设计');
/*!40000 ALTER TABLE `booktest_mingpian` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booktest_wenzhang`
--

DROP TABLE IF EXISTS `booktest_wenzhang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `booktest_wenzhang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wtitle` varchar(50) NOT NULL,
  `wneirong` varchar(300) NOT NULL,
  `wdate` date NOT NULL,
  `wpinglun` int(11) NOT NULL,
  `wdianzan` int(11) NOT NULL,
  `wenlei_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `booktest_wenzhang_wenlei_id_c3baf7b3_fk_booktest_lei_id` (`wenlei_id`),
  CONSTRAINT `booktest_wenzhang_wenlei_id_c3baf7b3_fk_booktest_lei_id` FOREIGN KEY (`wenlei_id`) REFERENCES `booktest_lei` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booktest_wenzhang`
--

LOCK TABLES `booktest_wenzhang` WRITE;
/*!40000 ALTER TABLE `booktest_wenzhang` DISABLE KEYS */;
INSERT INTO `booktest_wenzhang` VALUES (1,'好嗨哦','分活动卡时间发货发呆回家咖啡屋发的哈舒服就看看付额外负担和看风景而无法还是打款回复可见的实付额外','2018-08-23',24,33,5),(2,'明天会更好','噶啥告诉对方的是个觉得是个会卡死规定和高考时感受控股是','2018-09-12',22,10,3),(3,'真好','发的哈UI飞越安慰if多喝水附近可好玩我奥尔芬芳fhuadsifyuiwafy 飞花舞花覅一','2018-10-17',83,31,3),(4,'今天天气很好','发大水发hi和挖坟电脑服务ahff ewhaf adfdd fheiafkd分Hi好覅四 分慰安妇','2018-11-11',26,37,5);
/*!40000 ALTER TABLE `booktest_wenzhang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-11-23 02:38:23.990258','1','网站首页',1,'[{\"added\": {}}]',10,1),(2,'2018-11-23 02:38:33.056400','2','个人博客',1,'[{\"added\": {}}]',10,1),(3,'2018-11-23 02:38:39.505633','3','相册',1,'[{\"added\": {}}]',10,1),(4,'2018-11-23 02:38:44.573256','4','说说',1,'[{\"added\": {}}]',10,1),(5,'2018-11-23 02:38:51.210444','5','心情日志',1,'[{\"added\": {}}]',10,1),(6,'2018-11-23 02:38:56.353156','6','文章',1,'[{\"added\": {}}]',10,1),(7,'2018-11-23 02:51:01.803503','1','文章',2,'[{\"changed\": {\"fields\": [\"dtitle\"]}}]',10,1),(8,'2018-11-23 02:51:15.925740','6','个人博客',2,'[{\"changed\": {\"fields\": [\"dtitle\"]}}]',10,1),(9,'2018-11-23 02:51:23.282683','3','说说',2,'[{\"changed\": {\"fields\": [\"dtitle\"]}}]',10,1),(10,'2018-11-23 03:05:27.981580','1','我的名片',1,'[{\"added\": {}}]',9,1),(11,'2018-11-23 03:07:05.337329','1','个人信息',2,'[{\"changed\": {\"fields\": [\"mtitle\"]}}]',9,1),(12,'2018-11-23 03:10:06.798411','1','个人信息',2,'[]',9,1),(13,'2018-11-23 03:13:48.088537','1','个人信息',2,'[]',9,1),(14,'2018-11-23 03:14:50.060576','1','个人信息',2,'[]',9,1),(15,'2018-11-23 03:30:16.764267','1','网名：新疆马蹄打了贝贝 | 含雪红梅',2,'[{\"changed\": {\"fields\": [\"mwangm\"]}}]',9,1),(16,'2018-11-23 03:31:05.229004','1','慢生活',1,'[{\"added\": {}}]',7,1),(17,'2018-11-23 03:31:16.495423','2','爱情美文',1,'[{\"added\": {}}]',7,1),(18,'2018-11-23 03:31:33.009707','3','博客模板',1,'[{\"added\": {}}]',7,1),(19,'2018-11-23 03:31:40.036382','4','女生博客模板',1,'[{\"added\": {}}]',7,1),(20,'2018-11-23 03:31:59.408444','5','马大哈风格',1,'[{\"added\": {}}]',7,1),(21,'2018-11-23 03:34:18.728442','1','好嗨哦',1,'[{\"added\": {}}]',8,1),(22,'2018-11-23 03:34:58.676227','2','明天会更好',1,'[{\"added\": {}}]',8,1),(23,'2018-11-23 03:35:39.811743','3','真好',1,'[{\"added\": {}}]',8,1),(24,'2018-11-23 03:36:51.411637','4','今天天气很好',1,'[{\"added\": {}}]',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(4,'auth','permission'),(2,'auth','user'),(10,'booktest','daohang'),(7,'booktest','lei'),(9,'booktest','mingpian'),(8,'booktest','wenzhang'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-11-23 02:30:54.633229'),(2,'auth','0001_initial','2018-11-23 02:31:04.133363'),(3,'admin','0001_initial','2018-11-23 02:31:06.190876'),(4,'admin','0002_logentry_remove_auto_add','2018-11-23 02:31:06.352062'),(5,'contenttypes','0002_remove_content_type_name','2018-11-23 02:31:07.666400'),(6,'auth','0002_alter_permission_name_max_length','2018-11-23 02:31:08.511666'),(7,'auth','0003_alter_user_email_max_length','2018-11-23 02:31:09.406733'),(8,'auth','0004_alter_user_username_opts','2018-11-23 02:31:09.465806'),(9,'auth','0005_alter_user_last_login_null','2018-11-23 02:31:10.068905'),(10,'auth','0006_require_contenttypes_0002','2018-11-23 02:31:10.119101'),(11,'auth','0007_alter_validators_add_error_messages','2018-11-23 02:31:10.184124'),(12,'auth','0008_alter_user_username_max_length','2018-11-23 02:31:11.014177'),(13,'booktest','0001_initial','2018-11-23 02:31:13.355887'),(14,'sessions','0001_initial','2018-11-23 02:31:13.984728'),(15,'booktest','0002_auto_20181123_1100','2018-11-23 03:00:58.219075');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('ddf09f5nfp9yw3cm5rvzabe2fqtjfki0','OTYzOWJhMWYyMGU3MzdmNzY5YWM4ZTc5YTgxZDE1NzcyMDViMjNmZjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2hhc2giOiI3YzQ5NWYxMDMzYjU5M2RkYjdiNjk2Njg5ZDY3MWJlNDA1YmVmZDVhIn0=','2018-12-07 02:33:08.954794');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-16 19:49:37
