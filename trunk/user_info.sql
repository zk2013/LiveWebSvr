/*
Navicat MySQL Data Transfer

Source Server         : 52live
Source Server Version : 50717
Source Host           : 127.0.0.1:3306
Source Database       : livedb

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2017-06-01 12:21:16
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for user_info
-- ----------------------------
DROP TABLE IF EXISTS `user_info`;
CREATE TABLE `user_info` (
  `UID` varchar(20) NOT NULL,
  `USERNUM` text,
  `HEAD` text,
  `HEAD_640` text,
  `NICKNAME` text,
  `SIGN` text,
  `PHONE` text,
  `EMAIL` text,
  `TOKEN` text,
  `MONEY` int(11) NOT NULL,
  `THIRD` int(11) NOT NULL,
  `VIPLEVEL` int(11) NOT NULL,
  `LASTMODNICKNAME` int(11) NOT NULL,
  `SEX` int(11) NOT NULL,
  `FANS` int(11) NOT NULL,
  `FOLLOW` int(11) NOT NULL,
  `ADDRESS` text,
  `SECURITY` text,
  `IMTOKEN` text,
  `IMTIME` text,
  `IS_MANAGER` int(11) NOT NULL,
  `ANCHOR` int(11) NOT NULL,
  `BIRTHDAY` text,
  `HOMETOWN` text,
  `USER_TAG` int(11) NOT NULL,
  `RZ` int(11) NOT NULL,
  `SHOW_AUTHOR_TYPE_TAG` int(11) NOT NULL,
  `BEFORE_NOBLE_EXP` int(11) NOT NULL,
  `NOBLE_EXP` int(11) NOT NULL,
  `AFTER_NOBLE_EXP` int(11) NOT NULL,
  `GAMEB` int(11) NOT NULL,
  `MEDAL_ID` text,
  `LAST_LOGIN_TIME` text,
  `UPDATE_TIME` int(11) NOT NULL,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_info
-- ----------------------------
INSERT INTO `user_info` VALUES ('2327163', '2327163', null, null, 'zk2813', '黄河之水天上来 奔流到海不复回', '13437265183', '378925748@qq.com', 'jbzPCTMdgujEMtAvZepIxNms9p0vm9WrYaBuMi9MWGMYGy4UmpGfWy5A+7z8lfJYN3uFXrKF8FZecE2Hm6e3/riuKl04mpol6xdjLw3Z3T4=', '0', '0', '1', '0', '1', '0', '10', '湖北省 武汉市', '9f93dad3d2fa08b507f9eb73fa84d83c', '01619d33c46caa7792532994a7a07fb0fbb1328c', '1496288126', '0', '0', '1983-07-13', null, '0', '0', '0', '0', '2', '30', '0', null, '2017-06-01 11:33:24', '0');
