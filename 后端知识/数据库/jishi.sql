-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: jishi
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
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add 分类',7,'add_tag'),(20,'Can change 分类',7,'change_tag'),(21,'Can delete 分类',7,'delete_tag'),(22,'Can add 文章',8,'add_article'),(23,'Can change 文章',8,'change_article'),(24,'Can delete 文章',8,'delete_article');
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
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$TYe2HohUCqHC$grjCZXCiS0um5NmaZ0C4JG7/4/0/rgtcJJ7KnMfMY0M=','2018-12-13 05:56:05.140662',1,'sj','','','12@qq.com',1,1,'2018-12-13 05:55:24.582265');
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
-- Table structure for table `booktest_article`
--

DROP TABLE IF EXISTS `booktest_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `booktest_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `content` longtext NOT NULL,
  `top` tinyint(1) NOT NULL,
  `read_num` int(11) NOT NULL,
  `index` int(11) NOT NULL,
  `pub_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `booktest_article_tag_id_0f64566c_fk_booktest_tag_id` (`tag_id`),
  CONSTRAINT `booktest_article_tag_id_0f64566c_fk_booktest_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `booktest_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booktest_article`
--

LOCK TABLES `booktest_article` WRITE;
/*!40000 ALTER TABLE `booktest_article` DISABLE KEYS */;
INSERT INTO `booktest_article` VALUES (1,'你们是练体操的吧，高难度','<p>唉呀妈呀 太好玩了&nbsp; 哈哈哈反倒是咖啡姐我方面拉人费方面的刷卡福尔沃方面的斯拉夫任务分解穷三代啊</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<img alt=\"\" src=\"/static/media/upload/2018/12/13/hashiqi.jpg\" style=\"height:300px; width:535px\" /></p>',0,432,0,'2018-12-13 06:00:55.863355','2018-12-13 06:00:55.863391',0,7),(2,'谁说偶长的是狼尾巴','<p>非农大家看法和史蒂夫的方法hi我取法而偶尔我去热分开飞机了我发看到手机费戊二醛皮肤束带结发豆奶粉额外hiUFO有圈附近的sf</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>&nbsp; &nbsp;<img alt=\"\" src=\"/static/media/upload/2018/12/13/shuju.jpg\" style=\"height:224px; width:224px\" /></p>',0,354,1,'2018-12-13 06:01:38.868832','2018-12-13 06:01:38.868873',0,4),(3,'喜庆的画面','<p>发货覅略微哈发几款是打发点时空裂缝让我法额哦覅然而和饭卡里说的风味哦发斯蒂芬让我分手费华为飞洒法但是否能卡萨丁范围奥拉夫sdf</p>\r\n\r\n<p>&nbsp;&nbsp;<img alt=\"\" src=\"/static/media/upload/2018/12/13/lvtong.jpg\" style=\"height:375px; width:500px\" /></p>',0,634,2,'2018-12-13 06:02:22.568164','2018-12-13 06:02:22.568201',0,6),(4,'待你长发及腰给我做身衣服可好','<p>放电脑撒可发货快完啦会发生的奶粉 发货时if惹火我秋天和世界咖啡你们都是农村第三方欧委会如何减肥但是那份看会电视卡复合物方女士对符合为反</p>\r\n\r\n<p><img alt=\"\" src=\"/static/media/upload/2018/12/13/timg.jpeg\" style=\"height:654px; width:656px\" /></p>',0,432,3,'2018-12-13 06:23:51.271894','2018-12-13 06:23:51.271929',0,11);
/*!40000 ALTER TABLE `booktest_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booktest_tag`
--

DROP TABLE IF EXISTS `booktest_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `booktest_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booktest_tag`
--

LOCK TABLES `booktest_tag` WRITE;
/*!40000 ALTER TABLE `booktest_tag` DISABLE KEYS */;
INSERT INTO `booktest_tag` VALUES (1,'爆笑男女',0,'2018-12-13 05:57:48.276433','2018-12-13 05:57:48.276483'),(2,'古代',0,'2018-12-13 05:57:56.881227','2018-12-13 05:57:56.881286'),(3,'鱼人',0,'2018-12-13 05:58:00.965143','2018-12-13 05:58:00.965182'),(4,'太搞笑',0,'2018-12-13 05:58:07.871592','2018-12-13 05:58:07.871626'),(5,'好搞笑',0,'2018-12-13 05:58:12.077440','2018-12-13 05:58:12.077473'),(6,'恐怖',0,'2018-12-13 05:58:14.881669','2018-12-13 05:58:14.881742'),(7,'事件',0,'2018-12-13 05:58:20.246682','2018-12-13 05:58:20.246715'),(8,'你猜我猜',0,'2018-12-13 05:58:27.227730','2018-12-13 05:58:27.227764'),(9,'家庭',0,'2018-12-13 05:58:37.044403','2018-12-13 05:58:37.044444'),(10,'幽默',0,'2018-12-13 05:58:40.491142','2018-12-13 05:58:40.491186'),(11,'儿童',0,'2018-12-13 05:58:45.325818','2018-12-13 05:58:45.325850');
/*!40000 ALTER TABLE `booktest_tag` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-12-13 05:57:48.277216','1','爆笑男女',1,'[{\"added\": {}}]',7,1),(2,'2018-12-13 05:57:56.882218','2','古代',1,'[{\"added\": {}}]',7,1),(3,'2018-12-13 05:58:00.965792','3','鱼人',1,'[{\"added\": {}}]',7,1),(4,'2018-12-13 05:58:07.872098','4','太搞笑',1,'[{\"added\": {}}]',7,1),(5,'2018-12-13 05:58:12.078029','5','好搞笑',1,'[{\"added\": {}}]',7,1),(6,'2018-12-13 05:58:14.882738','6','恐怖',1,'[{\"added\": {}}]',7,1),(7,'2018-12-13 05:58:20.247172','7','事件',1,'[{\"added\": {}}]',7,1),(8,'2018-12-13 05:58:27.228218','8','你猜我猜',1,'[{\"added\": {}}]',7,1),(9,'2018-12-13 05:58:37.044849','9','家庭',1,'[{\"added\": {}}]',7,1),(10,'2018-12-13 05:58:40.492671','10','幽默',1,'[{\"added\": {}}]',7,1),(11,'2018-12-13 05:58:45.326365','11','儿童',1,'[{\"added\": {}}]',7,1),(12,'2018-12-13 06:00:55.863982','1','你们是练体操的吧，高难度',1,'[{\"added\": {}}]',8,1),(13,'2018-12-13 06:01:38.869520','2','谁说偶长的是狼尾巴',1,'[{\"added\": {}}]',8,1),(14,'2018-12-13 06:02:22.568798','3','喜庆的画面',1,'[{\"added\": {}}]',8,1),(15,'2018-12-13 06:23:51.272483','4','待你长发及腰给我做身衣服可好',1,'[{\"added\": {}}]',8,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(8,'booktest','article'),(7,'booktest','tag'),(5,'contenttypes','contenttype'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-12-13 05:54:40.598366'),(2,'auth','0001_initial','2018-12-13 05:54:49.409304'),(3,'admin','0001_initial','2018-12-13 05:54:51.388345'),(4,'admin','0002_logentry_remove_auto_add','2018-12-13 05:54:51.522820'),(5,'contenttypes','0002_remove_content_type_name','2018-12-13 05:54:52.636299'),(6,'auth','0002_alter_permission_name_max_length','2018-12-13 05:54:53.415871'),(7,'auth','0003_alter_user_email_max_length','2018-12-13 05:54:54.186565'),(8,'auth','0004_alter_user_username_opts','2018-12-13 05:54:54.235186'),(9,'auth','0005_alter_user_last_login_null','2018-12-13 05:54:54.780684'),(10,'auth','0006_require_contenttypes_0002','2018-12-13 05:54:54.823144'),(11,'auth','0007_alter_validators_add_error_messages','2018-12-13 05:54:54.881814'),(12,'auth','0008_alter_user_username_max_length','2018-12-13 05:54:55.686274'),(13,'booktest','0001_initial','2018-12-13 05:54:57.621307'),(14,'sessions','0001_initial','2018-12-13 05:54:58.140125');
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
INSERT INTO `django_session` VALUES ('ucx7trcma8tx3ys9d4f62y87qcr4poy9','MWMyZmNjN2ExYzdkNmRkOTYyMDNjMDIwMTE4YjI2NTBiYmJjZmExMjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2hhc2giOiI3MjQwMTVlNDdjMDM0NzgyMTBmZjQwYTRkMThmZjk1NzEwNmUxNGFiIn0=','2018-12-27 05:56:05.200863');
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

-- Dump completed on 2018-12-16 19:46:39
