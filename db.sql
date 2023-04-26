/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - answer_verifier
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`answer_verifier` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `answer_verifier`;

/*Table structure for table `answer` */

DROP TABLE IF EXISTS `answer`;

CREATE TABLE `answer` (
  `answer_id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) DEFAULT NULL,
  `answer` varchar(100) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `mark` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`answer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `answer` */

insert  into `answer`(`answer_id`,`question_id`,`answer`,`user_id`,`mark`) values 
(10,2,'qwerty',1,'10.0'),
(9,1,'os is an operating system',1,'1.0000000000000002'),
(11,3,'Hypertext markup language',1,'10.000000000000002'),
(12,4,'4',1,'0.0'),
(13,4,'6',2,'0.0'),
(21,10,'static/uploadsc6f28dbd-16fb-4742-8745-707baa567086asdf.jpg',1,'6.324555320336759'),
(20,9,'static/uploadsca5eef9c-1454-40ee-9a3d-e558869275a2asd.jpg',1,'10.0'),
(19,8,'static/uploadsf2728169-1826-437a-97de-5d77b6be92abss1.jpg',1,'10.0');

/*Table structure for table `exam` */

DROP TABLE IF EXISTS `exam`;

CREATE TABLE `exam` (
  `exam_id` int(11) NOT NULL AUTO_INCREMENT,
  `exam` varchar(100) DEFAULT NULL,
  `detail` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`exam_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `exam` */

insert  into `exam`(`exam_id`,`exam`,`detail`) values 
(1,'third semester','third semester regular/reapperance examination april 2023'),
(2,'annual','assdfghhjj');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'appu','appu','student'),
(5,'amal','amal','student'),
(4,'achu','achu','teacher');

/*Table structure for table `mark` */

DROP TABLE IF EXISTS `mark`;

CREATE TABLE `mark` (
  `mark_id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) DEFAULT NULL,
  `mark` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`mark_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `mark` */

/*Table structure for table `participate` */

DROP TABLE IF EXISTS `participate`;

CREATE TABLE `participate` (
  `participate_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `exam_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`participate_id`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

/*Data for the table `participate` */

insert  into `participate`(`participate_id`,`student_id`,`exam_id`) values 
(1,1,1),
(2,1,1),
(3,1,1),
(4,1,1),
(5,1,1),
(6,1,1),
(7,1,1),
(8,1,1),
(9,1,1),
(10,1,1),
(11,1,2),
(12,1,1),
(13,1,2),
(14,1,2),
(15,1,1),
(16,1,2),
(17,1,2),
(18,1,2),
(19,2,2),
(20,2,1),
(21,2,2),
(22,1,2),
(23,1,2),
(24,1,2),
(25,1,1),
(26,1,2),
(27,1,2),
(28,1,1),
(29,1,2),
(30,1,1);

/*Table structure for table `question` */

DROP TABLE IF EXISTS `question`;

CREATE TABLE `question` (
  `question_id` int(11) NOT NULL AUTO_INCREMENT,
  `exam_id` int(11) DEFAULT NULL,
  `question` varchar(100) DEFAULT NULL,
  `answer` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`question_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `question` */

insert  into `question`(`question_id`,`exam_id`,`question`,`answer`) values 
(1,1,'explan os?','os is an operating system'),
(2,1,'what are the fuctions of os?','qwerty'),
(3,2,'What is the full form of html','Hypertext markup language'),
(4,1,'colors in rainbow','7'),
(5,1,'rainbow','7'),
(6,2,'How many colors are there in a rainbow','7'),
(7,1,'RAINBOW','seven'),
(8,1,'Capital of india','Delhi'),
(9,1,'Capital of korea','Seoul'),
(10,1,'Who is the prime minister of India','The prime minister of india is Narendra modi. ');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`student_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values 
(1,2,'appu','kuttan','pala','7896541231','appu@gmail.com'),
(2,5,'amal','k','pala','7410236589','amal@gmail.com');

/*Table structure for table `teacher` */

DROP TABLE IF EXISTS `teacher`;

CREATE TABLE `teacher` (
  `teacher_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `subject` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`teacher_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `teacher` */

insert  into `teacher`(`teacher_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`,`subject`) values 
(1,4,'achu','k','palakkadu','7410236589','a@gmail.com','english');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
