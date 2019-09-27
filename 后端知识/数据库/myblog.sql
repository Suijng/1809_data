-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: myblog
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
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add 文章',6,'add_article'),(17,'Can change 文章',6,'change_article'),(18,'Can delete 文章',6,'delete_article'),(19,'Can add 分类',7,'add_category'),(20,'Can change 分类',7,'change_category'),(21,'Can delete 分类',7,'delete_category'),(22,'Can add 轮播图',8,'add_banner'),(23,'Can change 轮播图',8,'change_banner'),(24,'Can delete 轮播图',8,'delete_banner'),(25,'Can add 友情链接',9,'add_friendlink'),(26,'Can change 友情链接',9,'change_friendlink'),(27,'Can delete 友情链接',9,'delete_friendlink'),(28,'Can add 评论',10,'add_comment'),(29,'Can change 评论',10,'change_comment'),(30,'Can delete 评论',10,'delete_comment'),(31,'Can add 标签',11,'add_tags'),(32,'Can change 标签',11,'change_tags'),(33,'Can delete 标签',11,'delete_tags'),(34,'Can add user',12,'add_bloguser'),(35,'Can change user',12,'change_bloguser'),(36,'Can delete user',12,'delete_bloguser'),(37,'Can add 邮箱验证码',13,'add_emailverifyrecord'),(38,'Can change 邮箱验证码',13,'change_emailverifyrecord'),(39,'Can delete 邮箱验证码',13,'delete_emailverifyrecord');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blogapp_article`
--

DROP TABLE IF EXISTS `blogapp_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blogapp_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `cover` varchar(100) NOT NULL,
  `read_num` int(11) NOT NULL,
  `top` tinyint(1) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `pub_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `category_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `content` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blogapp_article_category_id_61345280_fk_blogapp_category_id` (`category_id`),
  KEY `blogapp_article_user_id_1cbc21fc_fk_userapp_bloguser_id` (`user_id`),
  CONSTRAINT `blogapp_article_category_id_61345280_fk_blogapp_category_id` FOREIGN KEY (`category_id`) REFERENCES `blogapp_category` (`id`),
  CONSTRAINT `blogapp_article_user_id_1cbc21fc_fk_userapp_bloguser_id` FOREIGN KEY (`user_id`) REFERENCES `userapp_bloguser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogapp_article`
--

LOCK TABLES `blogapp_article` WRITE;
/*!40000 ALTER TABLE `blogapp_article` DISABLE KEYS */;
INSERT INTO `blogapp_article` VALUES (1,'马大哈','article/timg.jpeg',4,0,0,'2018-12-04 00:47:17.780869','2018-12-06 05:36:23.689744',2,1,'<p>付金额哦IT一欧去哟而且我IQ我怕入耳我去热温柔奶茶咖啡是导入后额外有人怀疑偶尔我也任何人 见客户管理和往日同业人发到你付款hi偶讨厌欺骗体育人愤怒的女明星呢法儿童和伊尔偶同意票的vncxnflrfuiewufhjk&nbsp; 法 发货的师傅骚一会昂回来福才能发你空间撒谎覅特务晴天一热衣服 你的声卡和覅恩我也提前费覅我要他气我</p>'),(2,'关于关于她姑姑','article/timg.gif',5,0,0,'2018-12-04 00:48:03.146464','2018-12-06 05:35:51.807671',3,1,'<p>发货客服也我同意 发生开了房间了;任务抛弃我如[请问你〔〕吧〔〕分那算快乐和覅恩我也日哦全网通 点卡收费不卡拉和覅额喔唷合肥京东方法答复客户如一日一日恢复和女伴夫妇可好看我依然我去而爱上发生法会封号法爱好日期同一户口本V型放大后双方的法打开时返回IE以偶为天翼田园是的发图TV台湾if还是得尽可能</p>'),(3,'哈哈哈密码','article/kemao.jpg',7,1,0,'2018-12-04 00:49:33.898468','2018-12-06 05:36:59.259007',5,1,'<p>1发哈U盘福诶我去人员服务器用途二批我 发我提一提哦哦IE富华大厦承诺才看见啦还是提前一批凸起物type你的卡vbmnxbcalshflkaytipwqt法爱福特一起为IP回复的时间不vkbds放到沙发客流为话题 程度上分为一天天法单开vhityqewir是的和方法一覅无法的肯定失败vjlsdafiewytpqytipru发货的安抚朋友投票啊法分为一片</p>'),(4,'搞笑我们是认真的','article/keai.jpeg',2,0,0,'2018-12-04 08:19:28.083865','2018-12-06 05:34:58.906426',2,1,'<p>附件是电话覅吴国太有钱 分泌物拉回去问一体哦亲统一而我要人聘请 成都市ankjfdsagfrityqiptywq9p 那附近看哈撒地方了一起陪同一起网页图片内存就打开时候覅为一体抛弃我一天&nbsp; 拿放大镜看撒化肥款卫衣图片企业提诶从你家看电视不尴尬软件而别人去网页踢皮球你打撒即可厉害日额问题一切问题一覅额啊哟的 才 按时发货IQ而为一日片尾曲</p>'),(5,'据统计','article/shuju.jpg',75,0,0,'2018-12-04 08:21:59.672993','2018-12-06 05:34:30.847283',4,1,'<p>1UI供热我当时看了没烦恼就会分我的手机离开&nbsp; &nbsp; &nbsp; &nbsp;发货单亚牛哦啊 才几点开一天排气筒 才类型女款包括和个体如恶意踢皮球丫头儿UR熊二吗&nbsp; 方可垃圾狗我一通脾气你内拉手 驸马路口见佛怕U盘企业提图一vkjbvzm分开来大神;认为群殴图片青云谱区日哦 你分开来大神客户服务我以突破千万你才看到就爱上风科技为液体&nbsp;</p>'),(6,'爬虫','article/tu.jpeg',6,0,0,'2018-12-05 01:41:19.860257','2018-12-06 05:34:02.187549',4,1,'<p>发京东卡十二五方法克拉hi偶然千万因特网IM的卡拉是不能出纳卡谁惹IP请问有人批完全同意 差带你飞科技安慰人和其他要求我配合回复你空间都是脑残东西覅而非问题以前我也特才能打开上来就放弃我朋友特务内存卡发光体欧曲儿一提我陪但是氛围和退役前问题U盘而因为怕反分hi一同我一定能吃饱vasd</p>'),(7,'数据分析','article/ji.jpg',14,0,0,'2018-12-05 01:47:40.418891','2018-12-06 05:40:25.963304',1,1,'<p>您付款的计划分类hi冷风 分码数的两人结为一体无其他业务放到方块刘天宇奶粉的快乐飞激情而我已uewyoifdfk是多拍 积分卡拉撒及体温与图片放得开了萨克hi图一体陪我发你看到啦hi舞台请饿哦发你的卡萨克&nbsp;</p>');
/*!40000 ALTER TABLE `blogapp_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blogapp_article_tags`
--

DROP TABLE IF EXISTS `blogapp_article_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blogapp_article_tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) NOT NULL,
  `tags_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `blogapp_article_tags_article_id_tags_id_539497b5_uniq` (`article_id`,`tags_id`),
  KEY `blogapp_article_tags_tags_id_b582257e_fk_blogapp_tags_id` (`tags_id`),
  CONSTRAINT `blogapp_article_tags_article_id_b9571347_fk_blogapp_article_id` FOREIGN KEY (`article_id`) REFERENCES `blogapp_article` (`id`),
  CONSTRAINT `blogapp_article_tags_tags_id_b582257e_fk_blogapp_tags_id` FOREIGN KEY (`tags_id`) REFERENCES `blogapp_tags` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogapp_article_tags`
--

LOCK TABLES `blogapp_article_tags` WRITE;
/*!40000 ALTER TABLE `blogapp_article_tags` DISABLE KEYS */;
INSERT INTO `blogapp_article_tags` VALUES (3,1,3),(4,1,5),(1,2,2),(2,2,4),(5,3,1),(6,3,2),(7,4,4),(8,4,5),(9,5,1),(10,5,2),(11,5,3),(12,6,2),(13,6,4),(14,6,6),(15,7,1),(16,7,3),(17,7,5);
/*!40000 ALTER TABLE `blogapp_article_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blogapp_banner`
--

DROP TABLE IF EXISTS `blogapp_banner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blogapp_banner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(20) NOT NULL,
  `img` varchar(100) NOT NULL,
  `position` int(11) NOT NULL,
  `url` varchar(512) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogapp_banner`
--

LOCK TABLES `blogapp_banner` WRITE;
/*!40000 ALTER TABLE `blogapp_banner` DISABLE KEYS */;
INSERT INTO `blogapp_banner` VALUES (1,'天','banner/tian.jpg',1,'https://www.baidu.com/',0,0,'2018-12-03 08:31:36.633843','2018-12-03 08:31:36.633883'),(2,'童年','banner/tong.jpg',2,'https://www.baidu.com/',0,0,'2018-12-03 08:31:55.068311','2018-12-03 08:49:09.418761'),(3,'小黄人','banner/huang.gif',0,'https://www.baidu.com/',1,0,'2018-12-03 08:33:43.717028','2018-12-03 08:48:57.175563');
/*!40000 ALTER TABLE `blogapp_banner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blogapp_category`
--

DROP TABLE IF EXISTS `blogapp_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blogapp_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogapp_category`
--

LOCK TABLES `blogapp_category` WRITE;
/*!40000 ALTER TABLE `blogapp_category` DISABLE KEYS */;
INSERT INTO `blogapp_category` VALUES (1,'AI事业',0,'2018-12-04 00:43:43.409010','2018-12-04 00:43:43.409045'),(2,'互联网发展',0,'2018-12-04 00:43:51.015320','2018-12-04 00:43:51.015375'),(3,'电子商务',0,'2018-12-04 00:44:03.317725','2018-12-04 00:44:03.317765'),(4,'人工智能',0,'2018-12-04 00:44:19.260169','2018-12-04 00:44:19.260210'),(5,'Python',0,'2018-12-04 00:44:43.614913','2018-12-04 00:44:43.614952');
/*!40000 ALTER TABLE `blogapp_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blogapp_comment`
--

DROP TABLE IF EXISTS `blogapp_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blogapp_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(200) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `article_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blogapp_comment_article_id_699be1c3_fk_blogapp_article_id` (`article_id`),
  KEY `blogapp_comment_user_id_136384d7_fk_userapp_bloguser_id` (`user_id`),
  CONSTRAINT `blogapp_comment_article_id_699be1c3_fk_blogapp_article_id` FOREIGN KEY (`article_id`) REFERENCES `blogapp_article` (`id`),
  CONSTRAINT `blogapp_comment_user_id_136384d7_fk_userapp_bloguser_id` FOREIGN KEY (`user_id`) REFERENCES `userapp_bloguser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogapp_comment`
--

LOCK TABLES `blogapp_comment` WRITE;
/*!40000 ALTER TABLE `blogapp_comment` DISABLE KEYS */;
INSERT INTO `blogapp_comment` VALUES (4,'好',0,'2018-12-04 02:03:52.742328','2018-12-04 02:04:23.723960',3,1),(5,'真好',0,'2018-12-04 02:05:20.868946','2018-12-04 02:05:20.868980',2,1),(6,'非常好',0,'2018-12-04 02:18:53.054331','2018-12-04 02:18:53.054367',2,1),(7,'你猜好不好',0,'2018-12-04 02:19:02.569842','2018-12-04 02:19:02.569880',2,1),(9,'分活动卡肌肤我唯一的奶粉的内存空间撒复合肥而后若非的 减肥的垃圾方略气人偶尔放电脑内存款大幅客户端一起发你的卡时间佛尔无肉ing话题去哟烦恼 房价大幅IQ欧烹饪法 放大时考虑及覅偶取肉脾气法度',0,'2018-12-04 09:51:12.271577','2018-12-04 09:51:12.271622',5,1),(10,'大傻子',0,'2018-12-05 08:06:33.892994','2018-12-05 08:06:33.893029',5,1),(11,'小花是猪',0,'2018-12-05 10:52:26.589226','2018-12-05 10:52:26.589258',5,1),(12,'你说什么',0,'2018-12-06 01:40:05.549221','2018-12-06 01:40:05.549253',2,1),(13,'数据时代 互联网 我们的世界到来了',0,'2018-12-06 02:14:15.238841','2018-12-06 02:14:15.238875',7,2);
/*!40000 ALTER TABLE `blogapp_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blogapp_friendlink`
--

DROP TABLE IF EXISTS `blogapp_friendlink`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blogapp_friendlink` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `url` varchar(512) NOT NULL,
  `position` int(11) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogapp_friendlink`
--

LOCK TABLES `blogapp_friendlink` WRITE;
/*!40000 ALTER TABLE `blogapp_friendlink` DISABLE KEYS */;
INSERT INTO `blogapp_friendlink` VALUES (1,'百度','https://www.baidu.com/',0,0,'2018-12-04 07:08:31.457346','2018-12-04 07:08:31.457383'),(2,'搜狗','https://123.sogou.com/',1,0,'2018-12-04 07:08:57.234190','2018-12-04 07:08:57.234248');
/*!40000 ALTER TABLE `blogapp_friendlink` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blogapp_tags`
--

DROP TABLE IF EXISTS `blogapp_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blogapp_tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogapp_tags`
--

LOCK TABLES `blogapp_tags` WRITE;
/*!40000 ALTER TABLE `blogapp_tags` DISABLE KEYS */;
INSERT INTO `blogapp_tags` VALUES (1,'网络博客',0,'2018-12-04 00:45:55.856374','2018-12-04 00:45:55.856491'),(2,'信息技术',0,'2018-12-04 00:46:01.500105','2018-12-04 00:46:01.500146'),(3,'数据时代',0,'2018-12-04 00:46:13.395432','2018-12-04 00:46:13.395471'),(4,'行业发展',0,'2018-12-04 00:46:26.700546','2018-12-04 00:46:26.700580'),(5,'专业',0,'2018-12-04 06:45:21.555887','2018-12-04 06:45:21.555925'),(6,'扒扒扒',0,'2018-12-05 01:41:09.919308','2018-12-05 01:41:09.919346'),(7,'飞得更高',0,'2018-12-05 01:53:31.178234','2018-12-05 01:53:31.178273');
/*!40000 ALTER TABLE `blogapp_tags` ENABLE KEYS */;
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
  KEY `django_admin_log_user_id_c564eba6_fk_userapp_bloguser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_userapp_bloguser_id` FOREIGN KEY (`user_id`) REFERENCES `userapp_bloguser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-12-03 08:31:36.634474','1','天',1,'[{\"added\": {}}]',8,1),(2,'2018-12-03 08:31:55.069014','2','童年',1,'[{\"added\": {}}]',8,1),(3,'2018-12-03 08:33:43.717635','3','小黄人',1,'[{\"added\": {}}]',8,1),(4,'2018-12-03 08:48:57.176737','3','小黄人',2,'[{\"changed\": {\"fields\": [\"position\", \"is_active\"]}}]',8,1),(5,'2018-12-03 08:49:09.419636','2','童年',2,'[{\"changed\": {\"fields\": [\"position\", \"is_active\"]}}]',8,1),(6,'2018-12-04 00:43:43.409518','1','AI事业',1,'[{\"added\": {}}]',7,1),(7,'2018-12-04 00:43:51.016117','2','互联网发展',1,'[{\"added\": {}}]',7,1),(8,'2018-12-04 00:44:03.319040','3','电子商务',1,'[{\"added\": {}}]',7,1),(9,'2018-12-04 00:44:19.260969','4','人工智能',1,'[{\"added\": {}}]',7,1),(10,'2018-12-04 00:44:43.615484','5','Python',1,'[{\"added\": {}}]',7,1),(11,'2018-12-04 00:45:55.858158','1','网络博客',1,'[{\"added\": {}}]',11,1),(12,'2018-12-04 00:46:01.501599','2','信息技术',1,'[{\"added\": {}}]',11,1),(13,'2018-12-04 00:46:13.395965','3','数据时代',1,'[{\"added\": {}}]',11,1),(14,'2018-12-04 00:46:26.701063','4','行业发展',1,'[{\"added\": {}}]',11,1),(15,'2018-12-04 00:47:17.781615','1','打开覅额阿瓦',1,'[{\"added\": {}}]',6,1),(16,'2018-12-04 00:48:03.147231','2','关于关于她姑姑',1,'[{\"added\": {}}]',6,1),(17,'2018-12-04 00:49:33.899276','3','哈哈哈密码',1,'[{\"added\": {}}]',6,1),(18,'2018-12-04 01:13:37.094044','3','哈哈哈密码',2,'[{\"changed\": {\"fields\": [\"read_num\"]}}]',6,1),(19,'2018-12-04 02:03:52.743127','4','sj',1,'[{\"added\": {}}]',10,1),(20,'2018-12-04 02:04:23.724938','4','sj',2,'[{\"changed\": {\"fields\": [\"content\", \"article\"]}}]',10,1),(21,'2018-12-04 02:05:20.869755','5','sj',1,'[{\"added\": {}}]',10,1),(22,'2018-12-04 02:18:53.054824','6','sj',1,'[{\"added\": {}}]',10,1),(23,'2018-12-04 02:19:02.570381','7','sj',1,'[{\"added\": {}}]',10,1),(24,'2018-12-04 06:42:53.446319','2','关于关于她姑姑',2,'[{\"changed\": {\"fields\": [\"category\"]}}]',6,1),(25,'2018-12-04 06:44:32.027493','2','关于关于她姑姑',2,'[]',6,1),(26,'2018-12-04 06:45:21.556411','5','专业',1,'[{\"added\": {}}]',11,1),(27,'2018-12-04 06:45:23.735277','1','打开覅额阿瓦',2,'[]',6,1),(28,'2018-12-04 06:45:31.058007','3','哈哈哈密码',2,'[]',6,1),(29,'2018-12-04 07:08:31.457941','1','百度',1,'[{\"added\": {}}]',9,1),(30,'2018-12-04 07:08:57.235114','2','搜狗',1,'[{\"added\": {}}]',9,1),(31,'2018-12-04 08:19:28.093741','4','搞笑我们是认真的',1,'[{\"added\": {}}]',6,1),(32,'2018-12-04 08:19:38.876932','3','哈哈哈密码',2,'[{\"changed\": {\"fields\": [\"read_num\"]}}]',6,1),(33,'2018-12-04 08:19:45.867433','4','搞笑我们是认真的',2,'[{\"changed\": {\"fields\": [\"read_num\"]}}]',6,1),(34,'2018-12-04 08:19:51.840898','2','关于关于她姑姑',2,'[{\"changed\": {\"fields\": [\"read_num\"]}}]',6,1),(35,'2018-12-04 08:19:57.675842','1','打开覅额阿瓦',2,'[{\"changed\": {\"fields\": [\"read_num\"]}}]',6,1),(36,'2018-12-04 08:21:59.760086','5','据统计',1,'[{\"added\": {}}]',6,1),(37,'2018-12-04 09:51:12.272300','9','sj',1,'[{\"added\": {}}]',10,1),(38,'2018-12-04 10:32:53.231605','3','哈哈哈密码',2,'[{\"changed\": {\"fields\": [\"cover\"]}}]',6,1),(39,'2018-12-04 10:34:04.650950','3','哈哈哈密码',2,'[{\"changed\": {\"fields\": [\"cover\"]}}]',6,1),(40,'2018-12-04 10:35:55.935526','3','哈哈哈密码',2,'[{\"changed\": {\"fields\": [\"cover\"]}}]',6,1),(41,'2018-12-04 10:37:01.618877','3','哈哈哈密码',2,'[{\"changed\": {\"fields\": [\"cover\"]}}]',6,1),(42,'2018-12-05 01:36:25.918908','1','马大哈',2,'[{\"changed\": {\"fields\": [\"title\"]}}]',6,1),(43,'2018-12-05 01:41:09.919900','6','扒扒扒',1,'[{\"added\": {}}]',11,1),(44,'2018-12-05 01:41:19.864992','6','爬虫',1,'[{\"added\": {}}]',6,1),(45,'2018-12-05 01:47:40.521967','7','数据分析',1,'[{\"added\": {}}]',6,1),(46,'2018-12-05 01:53:31.178772','7','飞得更高',1,'[{\"added\": {}}]',11,1),(47,'2018-12-06 05:33:41.764521','7','数据分析',2,'[{\"changed\": {\"fields\": [\"content\"]}}]',6,1),(48,'2018-12-06 05:34:02.192996','6','爬虫',2,'[{\"changed\": {\"fields\": [\"content\"]}}]',6,1),(49,'2018-12-06 05:34:30.850244','5','据统计',2,'[{\"changed\": {\"fields\": [\"content\"]}}]',6,1),(50,'2018-12-06 05:34:58.914313','4','搞笑我们是认真的',2,'[{\"changed\": {\"fields\": [\"content\"]}}]',6,1),(51,'2018-12-06 05:35:22.017700','3','哈哈哈密码',2,'[{\"changed\": {\"fields\": [\"content\"]}}]',6,1),(52,'2018-12-06 05:35:25.917104','3','哈哈哈密码',2,'[]',6,1),(53,'2018-12-06 05:35:51.813026','2','关于关于她姑姑',2,'[{\"changed\": {\"fields\": [\"content\"]}}]',6,1),(54,'2018-12-06 05:36:23.695090','1','马大哈',2,'[{\"changed\": {\"fields\": [\"content\"]}}]',6,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(6,'blogapp','article'),(8,'blogapp','banner'),(7,'blogapp','category'),(10,'blogapp','comment'),(9,'blogapp','friendlink'),(11,'blogapp','tags'),(4,'contenttypes','contenttype'),(5,'sessions','session'),(12,'userapp','bloguser'),(13,'userapp','emailverifyrecord');
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-12-03 08:10:28.733876'),(2,'contenttypes','0002_remove_content_type_name','2018-12-03 08:10:29.907507'),(3,'auth','0001_initial','2018-12-03 08:10:34.436812'),(4,'auth','0002_alter_permission_name_max_length','2018-12-03 08:10:35.312902'),(5,'auth','0003_alter_user_email_max_length','2018-12-03 08:10:35.360588'),(6,'auth','0004_alter_user_username_opts','2018-12-03 08:10:35.409749'),(7,'auth','0005_alter_user_last_login_null','2018-12-03 08:10:35.460350'),(8,'auth','0006_require_contenttypes_0002','2018-12-03 08:10:35.505932'),(9,'auth','0007_alter_validators_add_error_messages','2018-12-03 08:10:35.552367'),(10,'auth','0008_alter_user_username_max_length','2018-12-03 08:10:35.740359'),(11,'userapp','0001_initial','2018-12-03 08:10:40.994730'),(12,'admin','0001_initial','2018-12-03 08:10:42.943144'),(13,'admin','0002_logentry_remove_auto_add','2018-12-03 08:10:43.086225'),(14,'blogapp','0001_initial','2018-12-03 08:10:45.892615'),(15,'blogapp','0002_auto_20181203_1610','2018-12-03 08:10:49.939084'),(16,'sessions','0001_initial','2018-12-03 08:10:50.576429'),(17,'blogapp','0003_article_user','2018-12-04 06:05:07.981091'),(18,'blogapp','0004_auto_20181204_1443','2018-12-04 06:44:09.648675'),(19,'blogapp','0005_remove_article_content','2018-12-06 05:05:50.559656'),(20,'blogapp','0006_article_content','2018-12-06 05:32:49.806641');
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
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userapp_bloguser`
--

DROP TABLE IF EXISTS `userapp_bloguser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userapp_bloguser` (
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
  `nickname` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userapp_bloguser`
--

LOCK TABLES `userapp_bloguser` WRITE;
/*!40000 ALTER TABLE `userapp_bloguser` DISABLE KEYS */;
INSERT INTO `userapp_bloguser` VALUES (1,'pbkdf2_sha256$36000$x6OMnoGI4Cu7$gsybUkA0j8ruAk6JIjXF+QtAgEeN6Il9V8IPgCYtheA=','2018-12-06 05:06:33.234683',1,'sj','','','123@qq.com',1,1,'2018-12-03 08:25:09.834686',''),(2,'pbkdf2_sha256$36000$Rk7yY4EQESKF$FQUjwobl0SMP6k5r7syZjAOdkeD71iFnC3xnSLGscnI=','2018-12-06 02:12:45.030191',0,'sj1','','','123456@qq.com',0,1,'2018-12-06 02:12:37.232317',''),(3,'pbkdf2_sha256$36000$Q1iKJaIDthTq$l1adW1zksXj1gP6O/UOxUY1WC6Cp+/KuBcBluvHv+2Y=','2018-12-06 03:33:44.629926',0,'sj2','','','123@qq.com',0,1,'2018-12-06 03:33:40.750978',''),(4,'pbkdf2_sha256$36000$7UPc9nlQFoCp$7AXj0uQm2csXqH/hs12fFr1Y8PlLzjcovAsnKKEpd5U=',NULL,0,'yyh','','','123@qq.com',0,1,'2018-12-08 07:48:52.687942',''),(5,'pbkdf2_sha256$36000$PkOWAfeY26pX$tf4I/TD9ZXJUPX5wsaJLXYvmv7XTbszAR4gyDTFEnCg=',NULL,0,'yyh1','','','123@qq.com',0,1,'2018-12-08 07:49:32.434383',''),(6,'pbkdf2_sha256$36000$UuLHCdrtzRRP$B2a2vhmX2qnOvmJWqM13GzCXhCefCd5lVzAgejU0Zq4=','2018-12-08 07:50:04.914512',0,'yyh2','','','qwe@qq.com',0,1,'2018-12-08 07:49:56.794521','');
/*!40000 ALTER TABLE `userapp_bloguser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userapp_bloguser_groups`
--

DROP TABLE IF EXISTS `userapp_bloguser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userapp_bloguser_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bloguser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `userapp_bloguser_groups_bloguser_id_group_id_3b320c4e_uniq` (`bloguser_id`,`group_id`),
  KEY `userapp_bloguser_groups_group_id_6521ba89_fk_auth_group_id` (`group_id`),
  CONSTRAINT `userapp_bloguser_gro_bloguser_id_f42c4df1_fk_userapp_b` FOREIGN KEY (`bloguser_id`) REFERENCES `userapp_bloguser` (`id`),
  CONSTRAINT `userapp_bloguser_groups_group_id_6521ba89_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userapp_bloguser_groups`
--

LOCK TABLES `userapp_bloguser_groups` WRITE;
/*!40000 ALTER TABLE `userapp_bloguser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `userapp_bloguser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userapp_bloguser_user_permissions`
--

DROP TABLE IF EXISTS `userapp_bloguser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userapp_bloguser_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bloguser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `userapp_bloguser_user_pe_bloguser_id_permission_i_9d7c9e6e_uniq` (`bloguser_id`,`permission_id`),
  KEY `userapp_bloguser_use_permission_id_e95be918_fk_auth_perm` (`permission_id`),
  CONSTRAINT `userapp_bloguser_use_bloguser_id_77042bc2_fk_userapp_b` FOREIGN KEY (`bloguser_id`) REFERENCES `userapp_bloguser` (`id`),
  CONSTRAINT `userapp_bloguser_use_permission_id_e95be918_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userapp_bloguser_user_permissions`
--

LOCK TABLES `userapp_bloguser_user_permissions` WRITE;
/*!40000 ALTER TABLE `userapp_bloguser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `userapp_bloguser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userapp_emailverifyrecord`
--

DROP TABLE IF EXISTS `userapp_emailverifyrecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userapp_emailverifyrecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `send_type` varchar(30) NOT NULL,
  `send_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userapp_emailverifyrecord`
--

LOCK TABLES `userapp_emailverifyrecord` WRITE;
/*!40000 ALTER TABLE `userapp_emailverifyrecord` DISABLE KEYS */;
/*!40000 ALTER TABLE `userapp_emailverifyrecord` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-16 19:50:30
