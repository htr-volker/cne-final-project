CREATE DATABASE IF NOT EXISTS "helpqueue";

USE "helpqueue";

DROP TABLE IF EXISTS "tickets";

CREATE TABLE "tickets" (
  "id" int(11) NOT NULL AUTO_INCREMENT,
  "title" varchar(50) NOT NULL,
  "author" varchar(50) NOT NULL,
  "description" varchar(500) NOT NULL,
  "time_created" datetime NOT NULL,
  "open" tinyint(1) NOT NULL,
  PRIMARY KEY ("id")
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
