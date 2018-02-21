CREATE TABLE `water_monitor` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `location` varchar(256) NOT NULL,
  `start_time` varchar(256) NOT NULL,
  `end_time` varchar(256) NOT NULL,
  `duration` int(11) NOT NULL,
  `release_date` varchar(256) NOT NULL,
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;