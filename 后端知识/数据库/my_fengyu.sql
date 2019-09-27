-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: my_fengyu
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
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add daohang',7,'add_daohang'),(20,'Can change daohang',7,'change_daohang'),(21,'Can delete daohang',7,'delete_daohang'),(22,'Can add fabu',8,'add_fabu'),(23,'Can change fabu',8,'change_fabu'),(24,'Can delete fabu',8,'delete_fabu'),(25,'Can add biaoqian',9,'add_biaoqian'),(26,'Can change biaoqian',9,'change_biaoqian'),(27,'Can delete biaoqian',9,'delete_biaoqian'),(28,'Can add lunbo',10,'add_lunbo'),(29,'Can change lunbo',10,'change_lunbo'),(30,'Can delete lunbo',10,'delete_lunbo');
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
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$XmllFDMJy2nU$oMk7o7E3g6lQiD/qifP6wsyNJ5bNZyR1aGMEP4eIBpE=','2018-11-24 07:12:48.995522',1,'sj','','','123@qq.com',1,1,'2018-11-24 07:12:32.012607');
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
-- Table structure for table `booktest_biaoqian`
--

DROP TABLE IF EXISTS `booktest_biaoqian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `booktest_biaoqian` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `btitle` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booktest_biaoqian`
--

LOCK TABLES `booktest_biaoqian` WRITE;
/*!40000 ALTER TABLE `booktest_biaoqian` DISABLE KEYS */;
INSERT INTO `booktest_biaoqian` VALUES (1,'java'),(2,'tomcat负载均衡'),(3,'panel'),(4,'JQuery'),(5,'JQuery选择器'),(6,'Linux'),(7,'spring'),(8,'chrome');
/*!40000 ALTER TABLE `booktest_biaoqian` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booktest_daohang`
--

LOCK TABLES `booktest_daohang` WRITE;
/*!40000 ALTER TABLE `booktest_daohang` DISABLE KEYS */;
INSERT INTO `booktest_daohang` VALUES (1,'首页'),(2,'关于'),(3,'成长'),(4,'学习'),(5,'说说'),(6,'娱乐'),(7,'留言');
/*!40000 ALTER TABLE `booktest_daohang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booktest_fabu`
--

DROP TABLE IF EXISTS `booktest_fabu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `booktest_fabu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ftitle` varchar(100) NOT NULL,
  `fneirong` varchar(500) NOT NULL,
  `fname` varchar(20) NOT NULL,
  `fyuedu` int(11) NOT NULL,
  `fpinglun` int(11) NOT NULL,
  `fdate` date NOT NULL,
  `ftupian` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booktest_fabu`
--

LOCK TABLES `booktest_fabu` WRITE;
/*!40000 ALTER TABLE `booktest_fabu` DISABLE KEYS */;
INSERT INTO `booktest_fabu` VALUES (1,'wfyvv.com','个人网站正在建设中...','admin',666,18,'2018-11-24','booktest/shenma.jpg'),(2,'使用 Nginx 实现 tomcat、glassfish 等 web 服务器负载均衡','1.web服务器负载均衡简介web服务器负载均衡是指将多台可用单节点服务器组合成web服务器集群，然后通过负载均衡器将客户端请求均匀的转发到不同的单节点web服务器上，从而增加整个web服务器集群的吞吐量。','admin',1003,23,'2018-10-24','booktest/shenma_Gxj3f36.jpg'),(3,'32位的UUID生成方法总结','在学习过程中，我们常常会用到ID，那么有哪些常用的 ID 生成方式，你知道吗？通过 java.util.UUID（终态类）生成','admin',527,74,'2018-09-24','booktest/shenma_4mIhCKZ.jpg');
/*!40000 ALTER TABLE `booktest_fabu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booktest_fabu_fbq`
--

DROP TABLE IF EXISTS `booktest_fabu_fbq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `booktest_fabu_fbq` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fabu_id` int(11) NOT NULL,
  `biaoqian_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `booktest_fabu_fbq_fabu_id_biaoqian_id_dd70e6e5_uniq` (`fabu_id`,`biaoqian_id`),
  KEY `booktest_fabu_fbq_biaoqian_id_3886bb8c_fk_booktest_biaoqian_id` (`biaoqian_id`),
  CONSTRAINT `booktest_fabu_fbq_biaoqian_id_3886bb8c_fk_booktest_biaoqian_id` FOREIGN KEY (`biaoqian_id`) REFERENCES `booktest_biaoqian` (`id`),
  CONSTRAINT `booktest_fabu_fbq_fabu_id_d88f95a0_fk_booktest_fabu_id` FOREIGN KEY (`fabu_id`) REFERENCES `booktest_fabu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booktest_fabu_fbq`
--

LOCK TABLES `booktest_fabu_fbq` WRITE;
/*!40000 ALTER TABLE `booktest_fabu_fbq` DISABLE KEYS */;
INSERT INTO `booktest_fabu_fbq` VALUES (1,1,1),(2,1,3),(3,1,6),(4,2,2),(5,2,4),(6,3,3),(7,3,4);
/*!40000 ALTER TABLE `booktest_fabu_fbq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booktest_lunbo`
--

DROP TABLE IF EXISTS `booktest_lunbo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `booktest_lunbo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lname` varchar(20) NOT NULL,
  `limage` varchar(100) NOT NULL,
  `lurl` varchar(512) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booktest_lunbo`
--

LOCK TABLES `booktest_lunbo` WRITE;
/*!40000 ALTER TABLE `booktest_lunbo` DISABLE KEYS */;
INSERT INTO `booktest_lunbo` VALUES (1,'小狗狗','booktest/mm.jpg','http://www.baidu.com',0),(2,'船','booktest/chuan.jpg','http://www.baidu.com',0),(3,'桥','booktest/qiao.jpg','http://www.baidu.com',1);
/*!40000 ALTER TABLE `booktest_lunbo` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-11-24 07:13:34.522814','1','首页',1,'[{\"added\": {}}]',7,1),(2,'2018-11-24 07:13:40.959529','2','关于',1,'[{\"added\": {}}]',7,1),(3,'2018-11-24 07:13:48.040489','3','成长',1,'[{\"added\": {}}]',7,1),(4,'2018-11-24 07:13:54.070234','4','学习',1,'[{\"added\": {}}]',7,1),(5,'2018-11-24 07:14:02.025836','5','说说',1,'[{\"added\": {}}]',7,1),(6,'2018-11-24 07:14:05.676825','6','娱乐',1,'[{\"added\": {}}]',7,1),(7,'2018-11-24 07:14:09.939949','7','留言',1,'[{\"added\": {}}]',7,1),(8,'2018-11-24 07:21:08.655955','1','小狗狗',1,'[{\"added\": {}}]',10,1),(9,'2018-11-24 07:21:23.268844','2','船',1,'[{\"added\": {}}]',10,1),(10,'2018-11-24 07:21:34.694970','3','桥',1,'[{\"added\": {}}]',10,1),(11,'2018-11-24 07:46:34.160254','1','java',1,'[{\"added\": {}}]',9,1),(12,'2018-11-24 07:46:45.115132','2','tomcat负载均衡',1,'[{\"added\": {}}]',9,1),(13,'2018-11-24 07:47:23.132322','3','panel',1,'[{\"added\": {}}]',9,1),(14,'2018-11-24 07:51:29.060963','4','JQuery',1,'[{\"added\": {}}]',9,1),(15,'2018-11-24 07:51:50.745259','5','JQuery选择器',1,'[{\"added\": {}}]',9,1),(16,'2018-11-24 07:57:53.631072','6','Linux',1,'[{\"added\": {}}]',9,1),(17,'2018-11-24 08:03:26.740715','1','wfyvv.com',1,'[{\"added\": {}}]',8,1),(18,'2018-11-24 08:05:07.529634','2','使用 Nginx 实现 tomcat、glassfish 等 web 服务器负载均衡',1,'[{\"added\": {}}]',8,1),(19,'2018-11-24 08:06:06.343805','3','32位的UUID生成方法总结',1,'[{\"added\": {}}]',8,1),(20,'2018-11-24 08:53:50.768380','7','spring',1,'[{\"added\": {}}]',9,1),(21,'2018-11-24 08:54:02.875179','8','chrome',1,'[{\"added\": {}}]',9,1),(22,'2018-11-25 10:58:02.825169','1','小狗狗',2,'[{\"changed\": {\"fields\": [\"limage\"]}}]',10,1),(23,'2018-11-25 12:22:20.441002','3','桥',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',10,1);
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
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(9,'booktest','biaoqian'),(7,'booktest','daohang'),(8,'booktest','fabu'),(10,'booktest','lunbo'),(5,'contenttypes','contenttype'),(6,'sessions','session');
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
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-11-24 07:11:19.031626'),(2,'auth','0001_initial','2018-11-24 07:11:28.959425'),(3,'admin','0001_initial','2018-11-24 07:11:31.036266'),(4,'admin','0002_logentry_remove_auto_add','2018-11-24 07:11:31.162289'),(5,'contenttypes','0002_remove_content_type_name','2018-11-24 07:11:32.368858'),(6,'auth','0002_alter_permission_name_max_length','2018-11-24 07:11:33.188744'),(7,'auth','0003_alter_user_email_max_length','2018-11-24 07:11:34.091954'),(8,'auth','0004_alter_user_username_opts','2018-11-24 07:11:34.141275'),(9,'auth','0005_alter_user_last_login_null','2018-11-24 07:11:34.729961'),(10,'auth','0006_require_contenttypes_0002','2018-11-24 07:11:34.780129'),(11,'auth','0007_alter_validators_add_error_messages','2018-11-24 07:11:34.838914'),(12,'auth','0008_alter_user_username_max_length','2018-11-24 07:11:35.784116'),(13,'booktest','0001_initial','2018-11-24 07:11:39.292587'),(14,'sessions','0001_initial','2018-11-24 07:11:39.869750'),(15,'booktest','0002_lunbo_is_active','2018-11-25 12:21:34.130833');
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
INSERT INTO `django_session` VALUES ('94yzus0lan5po8rtl9i1uh8ta9mnunz9','MWUyODE0MGIzOWZhMWQ1MDcwY2FlOGNhMzRiMjJjYWI3M2M2YmQ2ZTp7Il9hdXRoX3VzZXJfaGFzaCI6ImE3YTY3ZGYzMDRhNjE2Nzk3YTFmMDU4Njg4MDI1ZmU3NDZkMTU4NTgiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2018-12-08 07:12:49.047355');
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

-- Dump completed on 2018-12-16 19:48:26
