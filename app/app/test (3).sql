-- Adminer 4.7.7 PostgreSQL dump

\connect "test";

DROP TABLE IF EXISTS "admin";
DROP SEQUENCE IF EXISTS admin_id_seq;
CREATE SEQUENCE admin_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 5 CACHE 1;

CREATE TABLE "public"."admin" (
    "id" integer DEFAULT nextval('admin_id_seq') NOT NULL,
    "firstname" character varying(120),
    "lastname" character varying(120),
    "email" character varying(120) NOT NULL,
    "password" character varying(80) NOT NULL,
    CONSTRAINT "admin_email_key" UNIQUE ("email"),
    CONSTRAINT "admin_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "aircraft";
DROP SEQUENCE IF EXISTS aircraft_id_seq;
CREATE SEQUENCE aircraft_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 30 CACHE 1;

CREATE TABLE "public"."aircraft" (
    "id" integer DEFAULT nextval('aircraft_id_seq') NOT NULL,
    "tail_number" character varying(20),
    "model_id" integer,
    CONSTRAINT "aircraft_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "aircraft_model_id_fkey" FOREIGN KEY (model_id) REFERENCES aircraft_model(id) NOT DEFERRABLE
) WITH (oids = false);


DROP TABLE IF EXISTS "aircraft_model";
DROP SEQUENCE IF EXISTS aircraft_model_id_seq;
CREATE SEQUENCE aircraft_model_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 246 CACHE 1;

CREATE TABLE "public"."aircraft_model" (
    "id" integer DEFAULT nextval('aircraft_model_id_seq') NOT NULL,
    "number_of_col" integer,
    "number_of_row" integer,
    "model_name" character varying(120),
    "model_code" character varying(120),
    CONSTRAINT "aircraft_model_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "airport";
DROP SEQUENCE IF EXISTS airport_id_seq;
CREATE SEQUENCE airport_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 7698 CACHE 1;

CREATE TABLE "public"."airport" (
    "id" integer DEFAULT nextval('airport_id_seq') NOT NULL,
    "name" character varying(200) NOT NULL,
    "city_id" integer,
    "code" character varying(80) NOT NULL,
    CONSTRAINT "airport_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "airport_city_id_fkey" FOREIGN KEY (city_id) REFERENCES city(id) NOT DEFERRABLE
) WITH (oids = false);


DROP TABLE IF EXISTS "arrival_airport";
DROP SEQUENCE IF EXISTS arrival_airport_id_seq;
CREATE SEQUENCE arrival_airport_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 2451 CACHE 1;

CREATE TABLE "public"."arrival_airport" (
    "id" integer DEFAULT nextval('arrival_airport_id_seq') NOT NULL,
    "airport_id" integer,
    CONSTRAINT "arrival_airport_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "arrival_airport_airport_id_fkey" FOREIGN KEY (airport_id) REFERENCES airport(id) NOT DEFERRABLE
) WITH (oids = false);


DROP TABLE IF EXISTS "booking";
DROP SEQUENCE IF EXISTS booking_id_seq;
CREATE SEQUENCE booking_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1399 CACHE 1;

CREATE TABLE "public"."booking" (
    "id" integer DEFAULT nextval('booking_id_seq') NOT NULL,
    "client_id" integer,
    "booking_code" integer,
    CONSTRAINT "booking_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "booking_client_id_fkey" FOREIGN KEY (client_id) REFERENCES client(id) NOT DEFERRABLE
) WITH (oids = false);


DROP TABLE IF EXISTS "cabin_crew";
CREATE TABLE "public"."cabin_crew" (
    "flight_id" integer,
    "cabin_member_id" integer,
    CONSTRAINT "cabin_crew_cabin_member_id_fkey" FOREIGN KEY (cabin_member_id) REFERENCES cabin_member(id) NOT DEFERRABLE,
    CONSTRAINT "cabin_crew_flight_id_fkey" FOREIGN KEY (flight_id) REFERENCES flight(id) NOT DEFERRABLE
) WITH (oids = false);


DROP TABLE IF EXISTS "cabin_member";
DROP SEQUENCE IF EXISTS cabin_member_id_seq;
CREATE SEQUENCE cabin_member_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 2000 CACHE 1;

CREATE TABLE "public"."cabin_member" (
    "id" integer DEFAULT nextval('cabin_member_id_seq') NOT NULL,
    "firstname" character varying(120),
    "lastname" character varying(120),
    "email" character varying(120) NOT NULL,
    "password" character varying(80) NOT NULL,
    "salary" integer,
    CONSTRAINT "cabin_member_email_key" UNIQUE ("email"),
    CONSTRAINT "cabin_member_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "check";
DROP SEQUENCE IF EXISTS check_id_seq;
CREATE SEQUENCE check_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 330 CACHE 1;

CREATE TABLE "public"."check" (
    "id" integer DEFAULT nextval('check_id_seq') NOT NULL,
    "date" timestamp,
    "is_checked" boolean,
    "aircraft_id" integer,
    "technician_id" integer,
    CONSTRAINT "check_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "check_aircraft_id_fkey" FOREIGN KEY (aircraft_id) REFERENCES aircraft(id) NOT DEFERRABLE,
    CONSTRAINT "check_technician_id_fkey" FOREIGN KEY (technician_id) REFERENCES technician(id) NOT DEFERRABLE
) WITH (oids = false);


DROP TABLE IF EXISTS "city";
DROP SEQUENCE IF EXISTS city_id_seq;
CREATE SEQUENCE city_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 7698 CACHE 1;

CREATE TABLE "public"."city" (
    "id" integer DEFAULT nextval('city_id_seq') NOT NULL,
    "name" character varying(200) NOT NULL,
    "country_id" integer,
    CONSTRAINT "city_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "city_country_id_fkey" FOREIGN KEY (country_id) REFERENCES country(id) NOT DEFERRABLE
) WITH (oids = false);


DROP TABLE IF EXISTS "client";
DROP SEQUENCE IF EXISTS client_id_seq;
CREATE SEQUENCE client_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1000 CACHE 1;

CREATE TABLE "public"."client" (
    "id" integer DEFAULT nextval('client_id_seq') NOT NULL,
    "phone_number" character varying(80),
    "email" character varying(120) NOT NULL,
    "password" character varying(80) NOT NULL,
    "firstname" character varying(120),
    "lastname" character varying(120),
    CONSTRAINT "client_email_key" UNIQUE ("email"),
    CONSTRAINT "client_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "country";
DROP SEQUENCE IF EXISTS country_id_seq;
CREATE SEQUENCE country_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 256 CACHE 1;

CREATE TABLE "public"."country" (
    "id" integer DEFAULT nextval('country_id_seq') NOT NULL,
    "name" character varying(200) NOT NULL,
    CONSTRAINT "country_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "departure_airport";
DROP SEQUENCE IF EXISTS departure_airport_id_seq;
CREATE SEQUENCE departure_airport_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 2451 CACHE 1;

CREATE TABLE "public"."departure_airport" (
    "id" integer DEFAULT nextval('departure_airport_id_seq') NOT NULL,
    "airport_id" integer,
    CONSTRAINT "departure_airport_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "departure_airport_airport_id_fkey" FOREIGN KEY (airport_id) REFERENCES airport(id) NOT DEFERRABLE
) WITH (oids = false);


DROP TABLE IF EXISTS "flight";
DROP SEQUENCE IF EXISTS flight_id_seq;
CREATE SEQUENCE flight_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 137 CACHE 1;

CREATE TABLE "public"."flight" (
    "id" integer DEFAULT nextval('flight_id_seq') NOT NULL,
    "route_id" integer,
    "aircraft_id" integer,
    "actual_departure_date_time" timestamp,
    "actual_arrival_date_time" timestamp,
    "estimated_departure_date_time" timestamp,
    "estimated_arrival_date_time" timestamp,
    CONSTRAINT "flight_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "flight_aircraft_id_fkey" FOREIGN KEY (aircraft_id) REFERENCES aircraft(id) NOT DEFERRABLE,
    CONSTRAINT "flight_route_id_fkey" FOREIGN KEY (route_id) REFERENCES route(id) NOT DEFERRABLE
) WITH (oids = false);

INSERT INTO "flight" ("id", "route_id", "aircraft_id", "actual_departure_date_time", "actual_arrival_date_time", "estimated_departure_date_time", "estimated_arrival_date_time") VALUES
(1,	30,	25,	'2020-02-20 06:59:10.877559',	'2020-02-20 19:41:10.877559',	'2020-02-20 06:59:10.877559',	'2020-02-20 14:22:10.877559'),
(2,	1217,	7,	NULL,	NULL,	'2020-08-26 04:59:11.019847',	'2020-08-26 16:07:11.019847'),
(3,	1614,	12,	NULL,	NULL,	'2020-09-20 23:59:11.208861',	'2020-09-21 03:31:11.208861'),
(4,	686,	3,	'2020-04-23 15:22:11.347343',	'2020-04-24 02:47:11.347343',	'2020-04-23 08:59:11.347343',	'2020-04-23 14:01:11.347343'),
(5,	632,	22,	'2020-03-01 22:59:11.610337',	'2020-03-02 11:36:11.610337',	'2020-03-01 22:59:11.610337',	'2020-03-02 08:40:11.610337'),
(6,	1186,	9,	'2020-03-12 00:59:11.844092',	'2020-03-12 10:14:11.844092',	'2020-03-12 00:59:11.844092',	'2020-03-12 04:49:11.844092'),
(7,	542,	28,	NULL,	NULL,	'2020-12-01 02:59:11.995745',	'2020-12-01 14:30:11.995745'),
(8,	183,	23,	NULL,	NULL,	'2020-08-09 23:59:12.311444',	'2020-08-10 08:21:12.311444'),
(9,	572,	17,	NULL,	NULL,	'2020-09-18 07:59:12.538408',	'2020-09-18 14:41:12.538408'),
(10,	1926,	24,	'2020-04-26 22:59:12.678475',	'2020-04-27 12:23:12.678475',	'2020-04-26 22:59:12.678475',	'2020-04-27 10:00:12.678475'),
(11,	818,	30,	'2020-05-08 01:38:12.87387',	'2020-05-08 08:22:12.87387',	'2020-05-07 23:59:12.87387',	'2020-05-08 05:04:12.87387'),
(12,	1613,	15,	'2020-02-15 08:59:13.087772',	'2020-02-15 19:56:13.087772',	'2020-02-15 08:59:13.087772',	'2020-02-15 16:40:13.087772'),
(13,	2268,	24,	NULL,	NULL,	'2021-01-27 23:59:13.393681',	'2021-01-28 07:34:13.393681'),
(14,	185,	18,	NULL,	NULL,	'2020-09-06 04:59:13.551921',	'2020-09-06 05:55:13.551921'),
(15,	1135,	14,	'2020-02-02 23:24:13.803857',	'2020-02-03 05:34:13.803857',	'2020-02-02 20:59:13.803857',	'2020-02-03 00:44:13.803857'),
(16,	246,	15,	'2020-07-14 12:59:13.979342',	'2020-07-14 18:18:13.979342',	'2020-07-14 12:59:13.979342',	'2020-07-14 16:15:13.979342'),
(17,	963,	5,	NULL,	NULL,	'2020-10-01 01:59:14.26678',	'2020-10-01 09:28:14.26678'),
(18,	953,	29,	'2020-04-15 21:59:14.519983',	'2020-04-16 04:00:14.519983',	'2020-04-15 21:59:14.519983',	'2020-04-15 22:55:14.519983'),
(19,	1659,	9,	'2020-05-28 16:33:14.70222',	'2020-05-28 20:40:14.70222',	'2020-05-28 13:59:14.70222',	'2020-05-28 15:32:14.70222'),
(20,	760,	13,	NULL,	NULL,	'2021-01-07 00:59:14.812146',	'2021-01-07 09:38:14.812146'),
(21,	817,	30,	NULL,	NULL,	'2020-07-31 23:59:15.053448',	'2020-08-01 09:06:15.053448'),
(22,	1561,	29,	NULL,	NULL,	'2020-09-25 17:59:15.31978',	'2020-09-26 02:42:15.31978'),
(23,	1006,	20,	'2020-07-09 13:59:15.522619',	'2020-07-09 22:49:15.522619',	'2020-07-09 13:59:15.522619',	'2020-07-09 21:28:15.522619'),
(24,	1035,	6,	'2020-02-26 23:59:15.661947',	'2020-02-27 05:06:15.661947',	'2020-02-26 23:59:15.661947',	'2020-02-27 02:22:15.661947'),
(25,	2355,	21,	NULL,	NULL,	'2020-12-25 21:59:15.921136',	'2020-12-26 08:22:15.921136'),
(26,	1384,	22,	NULL,	NULL,	'2020-12-13 21:59:16.246185',	'2020-12-14 05:23:16.246185'),
(27,	1090,	19,	'2020-05-28 19:59:17.00322',	'2020-05-29 05:03:17.00322',	'2020-05-28 19:59:17.00322',	'2020-05-29 02:22:17.00322'),
(28,	1946,	26,	'2020-06-15 23:59:17.301224',	'2020-06-16 08:50:17.301224',	'2020-06-15 23:59:17.301224',	'2020-06-16 03:54:17.301224'),
(29,	444,	16,	'2020-01-31 10:59:17.435226',	'2020-02-01 00:42:17.435226',	'2020-01-31 10:59:17.435226',	'2020-01-31 18:19:17.435226'),
(30,	2297,	15,	'2020-07-17 22:59:17.780214',	'2020-07-18 12:31:17.780214',	'2020-07-17 22:59:17.780214',	'2020-07-18 08:09:17.780214'),
(31,	1356,	10,	'2020-03-05 22:59:18.10042',	'2020-03-06 09:06:18.10042',	'2020-03-05 22:59:18.10042',	'2020-03-06 04:18:18.10042'),
(32,	2244,	2,	'2020-05-03 07:59:18.329281',	'2020-05-03 17:34:18.329281',	'2020-05-03 07:59:18.329281',	'2020-05-03 16:13:18.329281'),
(33,	1134,	1,	NULL,	NULL,	'2020-11-11 10:59:18.649067',	'2020-11-11 11:52:18.649067'),
(34,	2063,	8,	'2020-06-11 00:59:18.928261',	'2020-06-11 08:25:18.928261',	'2020-06-11 00:59:18.928261',	'2020-06-11 07:44:18.928261'),
(35,	148,	4,	'2020-01-30 08:59:19.085686',	'2020-01-30 20:51:19.085686',	'2020-01-30 08:59:19.085686',	'2020-01-30 14:45:19.085686'),
(36,	2144,	11,	'2020-04-22 02:59:19.253729',	'2020-04-22 15:35:19.253729',	'2020-04-22 02:59:19.253729',	'2020-04-22 10:08:19.253729'),
(37,	663,	25,	'2020-06-22 20:33:19.49958',	'2020-06-23 10:29:19.49958',	'2020-06-22 18:59:19.49958',	'2020-06-23 07:21:19.49958'),
(38,	861,	2,	NULL,	NULL,	'2021-01-12 03:59:19.713589',	'2021-01-12 12:28:19.713589'),
(39,	525,	3,	NULL,	NULL,	'2020-11-29 00:59:20.22783',	'2020-11-29 04:18:20.22783'),
(40,	697,	28,	NULL,	NULL,	'2021-01-25 20:59:20.535267',	'2021-01-25 22:55:20.535267'),
(41,	792,	16,	NULL,	NULL,	'2020-08-09 12:59:21.004841',	'2020-08-09 15:53:21.004841'),
(42,	1239,	14,	'2020-03-07 08:59:21.366171',	'2020-03-08 02:07:21.366171',	'2020-03-07 08:59:21.366171',	'2020-03-07 20:52:21.366171'),
(43,	323,	17,	NULL,	NULL,	'2020-11-29 09:59:21.57117',	'2020-11-29 12:19:21.57117'),
(44,	1482,	23,	NULL,	NULL,	'2020-09-07 01:59:21.757249',	'2020-09-07 10:23:21.757249'),
(45,	1727,	27,	'2020-02-08 09:59:22.083862',	'2020-02-08 14:51:22.083862',	'2020-02-08 09:59:22.083862',	'2020-02-08 13:19:22.083862'),
(46,	616,	8,	NULL,	NULL,	'2020-10-08 01:59:22.235474',	'2020-10-08 13:53:22.235474'),
(47,	2210,	4,	NULL,	NULL,	'2020-07-30 04:59:22.349879',	'2020-07-30 09:59:22.349879'),
(48,	549,	14,	'2020-07-03 07:59:22.474553',	'2020-07-03 11:58:22.474553',	'2020-07-03 07:59:22.474553',	'2020-07-03 08:53:22.474553'),
(49,	1179,	11,	'2020-05-05 07:59:22.625261',	'2020-05-05 14:32:22.625261',	'2020-05-05 07:59:22.625261',	'2020-05-05 09:47:22.625261'),
(50,	1217,	14,	NULL,	NULL,	'2020-08-26 10:59:22.884614',	'2020-08-26 14:05:22.884614'),
(51,	1604,	9,	'2020-06-06 09:59:23.071274',	'2020-06-06 15:13:23.071274',	'2020-06-06 09:59:23.071274',	'2020-06-06 11:02:23.071274'),
(52,	257,	27,	NULL,	NULL,	'2020-07-31 03:59:23.258261',	'2020-07-31 08:47:23.258261'),
(53,	1657,	14,	NULL,	NULL,	'2020-12-19 07:59:23.455727',	'2020-12-19 18:55:23.455727'),
(54,	415,	11,	NULL,	NULL,	'2020-08-17 13:59:23.589146',	'2020-08-17 19:35:23.589146'),
(55,	2476,	26,	NULL,	NULL,	'2020-08-20 04:59:23.901919',	'2020-08-20 11:08:23.901919'),
(56,	1222,	25,	'2020-07-19 09:59:24.070532',	'2020-07-19 21:00:24.070532',	'2020-07-19 09:59:24.070532',	'2020-07-19 14:51:24.070532'),
(57,	1419,	10,	'2020-04-30 11:59:24.333179',	'2020-04-30 22:37:24.333179',	'2020-04-30 11:59:24.333179',	'2020-04-30 21:47:24.333179'),
(58,	2402,	19,	NULL,	NULL,	'2020-07-30 04:59:24.505516',	'2020-07-30 14:05:24.505516'),
(59,	189,	18,	NULL,	NULL,	'2020-11-30 08:59:24.875229',	'2020-11-30 18:42:24.875229'),
(60,	1633,	4,	NULL,	NULL,	'2020-08-31 12:59:25.382953',	'2020-09-01 01:04:25.382953'),
(61,	1531,	15,	NULL,	NULL,	'2020-08-13 05:59:25.515804',	'2020-08-13 17:02:25.515804'),
(62,	1441,	5,	NULL,	NULL,	'2020-12-07 13:59:25.848336',	'2020-12-07 16:21:25.848336'),
(63,	1314,	16,	NULL,	NULL,	'2020-09-01 00:59:26.258193',	'2020-09-01 11:07:26.258193'),
(64,	1409,	27,	NULL,	NULL,	'2020-08-24 12:59:26.570989',	'2020-08-24 17:34:26.570989'),
(65,	2400,	6,	'2020-04-24 07:59:26.707483',	'2020-04-24 18:15:26.707483',	'2020-04-24 07:59:26.707483',	'2020-04-24 16:57:26.707483'),
(66,	1339,	1,	NULL,	NULL,	'2020-11-26 01:59:27.071378',	'2020-11-26 09:50:27.071378'),
(67,	953,	10,	'2020-06-22 09:09:27.456807',	'2020-06-22 18:02:27.456807',	'2020-06-22 07:59:27.456807',	'2020-06-22 15:42:27.456807'),
(68,	1350,	9,	NULL,	NULL,	'2020-08-30 06:59:27.663791',	'2020-08-30 12:15:27.663791'),
(69,	2329,	25,	NULL,	NULL,	'2020-11-06 05:59:27.844453',	'2020-11-06 10:51:27.844453'),
(70,	889,	30,	NULL,	NULL,	'2020-11-29 02:59:27.957988',	'2020-11-29 05:17:27.957988'),
(71,	992,	6,	NULL,	NULL,	'2020-08-18 05:59:28.335249',	'2020-08-18 08:15:28.335249'),
(72,	2408,	20,	NULL,	NULL,	'2020-10-12 15:59:28.74419',	'2020-10-12 22:36:28.74419'),
(73,	1489,	29,	NULL,	NULL,	'2020-09-28 12:59:28.905267',	'2020-09-28 20:00:28.905267'),
(74,	1030,	26,	NULL,	NULL,	'2020-11-10 14:59:29.059487',	'2020-11-10 16:25:29.059487'),
(75,	2131,	9,	NULL,	NULL,	'2020-09-07 00:59:29.331702',	'2020-09-07 04:17:29.331702'),
(76,	536,	17,	NULL,	NULL,	'2020-12-04 01:59:29.457463',	'2020-12-04 09:23:29.457463'),
(77,	2080,	4,	NULL,	NULL,	'2020-12-07 20:59:29.64352',	'2020-12-08 09:19:29.64352'),
(78,	2105,	16,	NULL,	NULL,	'2020-09-17 08:59:29.968085',	'2020-09-17 19:26:29.968085'),
(79,	742,	15,	NULL,	NULL,	'2020-10-14 02:59:30.630104',	'2020-10-14 15:10:30.630104'),
(80,	2384,	11,	NULL,	NULL,	'2020-10-02 13:59:31.229223',	'2020-10-02 18:56:31.229223'),
(81,	1970,	10,	NULL,	NULL,	'2020-10-03 16:59:31.579094',	'2020-10-04 03:17:31.579094'),
(82,	1640,	23,	NULL,	NULL,	'2020-09-15 05:59:31.780228',	'2020-09-15 12:05:31.780228'),
(83,	822,	27,	NULL,	NULL,	'2020-09-10 19:59:32.139514',	'2020-09-11 04:26:32.139514'),
(84,	1982,	23,	NULL,	NULL,	'2020-10-05 03:59:32.405187',	'2020-10-05 12:44:32.405187'),
(85,	1754,	12,	NULL,	NULL,	'2020-10-26 14:59:32.665029',	'2020-10-26 22:42:32.665029'),
(86,	2096,	11,	NULL,	NULL,	'2020-10-25 21:59:32.77063',	'2020-10-26 03:24:32.77063'),
(87,	688,	19,	NULL,	NULL,	'2020-09-09 12:59:33.061971',	'2020-09-09 14:14:33.061971'),
(88,	2205,	26,	NULL,	NULL,	'2020-12-30 08:59:33.494887',	'2020-12-30 09:51:33.494887'),
(89,	1115,	16,	NULL,	NULL,	'2020-10-15 06:59:33.876643',	'2020-10-15 09:58:33.876643'),
(90,	361,	6,	NULL,	NULL,	'2020-09-02 00:59:34.410839',	'2020-09-02 04:00:34.410839'),
(91,	216,	25,	NULL,	NULL,	'2020-12-27 03:59:34.885433',	'2020-12-27 06:58:34.885433'),
(92,	914,	7,	NULL,	NULL,	'2020-12-12 21:59:35.059159',	'2020-12-13 03:42:35.059159'),
(93,	1921,	27,	NULL,	NULL,	'2020-09-25 15:59:35.277465',	'2020-09-25 22:31:35.277465'),
(94,	1874,	17,	NULL,	NULL,	'2020-12-08 17:59:35.459868',	'2020-12-08 21:51:35.459868'),
(95,	711,	6,	NULL,	NULL,	'2020-09-21 15:59:35.656381',	'2020-09-21 21:37:35.656381'),
(96,	885,	10,	NULL,	NULL,	'2020-11-29 04:59:36.198981',	'2020-11-29 16:36:36.198981'),
(97,	1272,	20,	NULL,	NULL,	'2020-11-25 20:59:36.449717',	'2020-11-26 06:39:36.449717'),
(98,	2015,	9,	NULL,	NULL,	'2020-12-12 09:59:36.637521',	'2020-12-12 20:05:36.637521'),
(99,	976,	19,	NULL,	NULL,	'2020-09-22 20:59:36.862878',	'2020-09-23 01:49:36.862878'),
(100,	2146,	6,	NULL,	NULL,	'2021-01-13 00:59:37.254659',	'2021-01-13 07:00:37.254659'),
(101,	2007,	12,	NULL,	NULL,	'2020-11-17 21:59:37.587758',	'2020-11-18 04:43:37.587758'),
(102,	313,	5,	NULL,	NULL,	'2021-01-15 14:59:37.71966',	'2021-01-16 03:02:37.71966'),
(103,	2107,	27,	NULL,	NULL,	'2020-11-24 22:59:38.042381',	'2020-11-25 09:53:38.042381'),
(104,	1210,	20,	NULL,	NULL,	'2020-12-25 13:59:38.283051',	'2020-12-26 01:43:38.283051'),
(105,	2083,	21,	NULL,	NULL,	'2020-12-28 09:59:38.511354',	'2020-12-28 13:07:38.511354'),
(106,	1405,	3,	NULL,	NULL,	'2021-01-20 10:59:38.76212',	'2021-01-20 23:19:38.76212'),
(107,	1464,	11,	NULL,	NULL,	'2020-11-18 02:59:39.09247',	'2020-11-18 06:53:39.09247'),
(108,	215,	30,	NULL,	NULL,	'2020-11-30 06:59:39.356458',	'2020-11-30 17:42:39.356458'),
(109,	1533,	19,	NULL,	NULL,	'2020-10-21 01:59:39.921968',	'2020-10-21 12:18:39.921968'),
(110,	2076,	8,	NULL,	NULL,	'2020-11-13 12:59:40.476111',	'2020-11-13 22:52:40.476111'),
(111,	1824,	16,	NULL,	NULL,	'2020-10-30 04:59:40.699354',	'2020-10-30 10:14:40.699354'),
(112,	730,	23,	NULL,	NULL,	'2020-10-26 01:59:41.110906',	'2020-10-26 06:57:41.110906'),
(113,	430,	29,	NULL,	NULL,	'2020-10-20 14:59:41.573453',	'2020-10-21 01:14:41.573453'),
(114,	814,	23,	NULL,	NULL,	'2020-11-01 16:59:41.839736',	'2020-11-01 21:39:41.839736'),
(115,	1863,	15,	NULL,	NULL,	'2020-10-28 08:59:42.329325',	'2020-10-28 17:12:42.329325'),
(116,	244,	6,	NULL,	NULL,	'2021-01-27 21:59:43.029',	'2021-01-28 09:56:43.029'),
(117,	367,	21,	NULL,	NULL,	'2021-01-21 21:59:43.60914',	'2021-01-22 04:53:43.60914'),
(118,	161,	11,	NULL,	NULL,	'2020-12-10 04:59:43.980605',	'2020-12-10 10:58:43.980605'),
(119,	1576,	23,	NULL,	NULL,	'2021-01-02 03:59:44.29278',	'2021-01-02 06:33:44.29278'),
(120,	1851,	19,	NULL,	NULL,	'2020-12-14 22:59:44.79791',	'2020-12-15 04:36:44.79791'),
(121,	105,	15,	NULL,	NULL,	'2020-11-09 12:59:45.091183',	'2020-11-09 21:59:45.091183'),
(122,	1366,	4,	NULL,	NULL,	'2020-12-10 22:59:45.355432',	'2020-12-11 06:04:45.355432'),
(123,	654,	7,	NULL,	NULL,	'2021-01-08 13:59:45.704114',	'2021-01-08 20:12:45.704114'),
(124,	628,	29,	NULL,	NULL,	'2020-12-08 02:59:45.954972',	'2020-12-08 08:51:45.954972'),
(125,	1456,	30,	NULL,	NULL,	'2020-12-26 07:59:46.122201',	'2020-12-26 11:21:46.122201'),
(126,	324,	16,	NULL,	NULL,	'2020-11-09 16:59:46.537312',	'2020-11-10 02:34:46.537312'),
(127,	945,	27,	NULL,	NULL,	'2020-12-16 09:59:46.906195',	'2020-12-16 14:13:46.906195'),
(128,	1047,	25,	NULL,	NULL,	'2020-12-30 00:59:47.109214',	'2020-12-30 09:40:47.109214'),
(129,	2150,	11,	NULL,	NULL,	'2020-12-28 10:59:47.444575',	'2020-12-28 17:41:47.444575'),
(130,	176,	8,	NULL,	NULL,	'2020-12-24 09:59:47.665085',	'2020-12-24 17:21:47.665085'),
(131,	1427,	16,	NULL,	NULL,	'2020-12-27 20:59:47.878935',	'2020-12-28 02:47:47.878935'),
(132,	668,	15,	NULL,	NULL,	'2020-11-24 22:59:48.246993',	'2020-11-25 00:11:48.246993'),
(133,	1621,	19,	NULL,	NULL,	'2021-01-26 02:59:48.795691',	'2021-01-26 04:00:48.795691'),
(134,	894,	17,	NULL,	NULL,	'2020-12-25 19:59:49.106297',	'2020-12-26 08:18:49.106297'),
(135,	1484,	18,	NULL,	NULL,	'2020-12-11 00:59:49.321546',	'2020-12-11 11:41:49.321546'),
(136,	1413,	12,	NULL,	NULL,	'2020-12-13 13:59:49.638483',	'2020-12-13 23:53:49.638483'),
(137,	665,	1,	NULL,	NULL,	'2020-12-10 16:59:49.807658',	'2020-12-10 21:57:49.807658');

DROP TABLE IF EXISTS "pilot";
DROP SEQUENCE IF EXISTS pilot_id_seq;
CREATE SEQUENCE pilot_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1000 CACHE 1;

CREATE TABLE "public"."pilot" (
    "id" integer DEFAULT nextval('pilot_id_seq') NOT NULL,
    "firstname" character varying(120),
    "lastname" character varying(120),
    "email" character varying(120) NOT NULL,
    "password" character varying(80) NOT NULL,
    "experience" integer,
    "salary" integer,
    CONSTRAINT "pilot_email_key" UNIQUE ("email"),
    CONSTRAINT "pilot_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "pilot_speciality";
CREATE TABLE "public"."pilot_speciality" (
    "pilot_id" integer,
    "aircraft_model_id" integer,
    CONSTRAINT "pilot_speciality_aircraft_model_id_fkey" FOREIGN KEY (aircraft_model_id) REFERENCES aircraft_model(id) NOT DEFERRABLE,
    CONSTRAINT "pilot_speciality_pilot_id_fkey" FOREIGN KEY (pilot_id) REFERENCES pilot(id) NOT DEFERRABLE
) WITH (oids = false);


DROP TABLE IF EXISTS "pilots_table";
CREATE TABLE "public"."pilots_table" (
    "flight_id" integer,
    "pilot_id" integer,
    CONSTRAINT "pilots_table_flight_id_fkey" FOREIGN KEY (flight_id) REFERENCES flight(id) NOT DEFERRABLE,
    CONSTRAINT "pilots_table_pilot_id_fkey" FOREIGN KEY (pilot_id) REFERENCES pilot(id) NOT DEFERRABLE
) WITH (oids = false);


DROP TABLE IF EXISTS "route";
DROP SEQUENCE IF EXISTS route_id_seq;
CREATE SEQUENCE route_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 2484 CACHE 1;

CREATE TABLE "public"."route" (
    "id" integer DEFAULT nextval('route_id_seq') NOT NULL,
    "departure_airport_id" integer,
    "arrival_airport_id" integer,
    CONSTRAINT "route_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "route_arrival_airport_id_fkey" FOREIGN KEY (arrival_airport_id) REFERENCES arrival_airport(id) NOT DEFERRABLE,
    CONSTRAINT "route_departure_airport_id_fkey" FOREIGN KEY (departure_airport_id) REFERENCES departure_airport(id) NOT DEFERRABLE
) WITH (oids = false);


DROP TABLE IF EXISTS "technician";
DROP SEQUENCE IF EXISTS technician_id_seq;
CREATE SEQUENCE technician_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1000 CACHE 1;

CREATE TABLE "public"."technician" (
    "id" integer DEFAULT nextval('technician_id_seq') NOT NULL,
    "firstname" character varying(120),
    "lastname" character varying(120),
    "email" character varying(120),
    "password" character varying(80) NOT NULL,
    "salary" integer,
    "model_id" integer,
    CONSTRAINT "technician_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "technician_model_id_fkey" FOREIGN KEY (model_id) REFERENCES aircraft_model(id) NOT DEFERRABLE
) WITH (oids = false);


DROP TABLE IF EXISTS "technician_speciality";
CREATE TABLE "public"."technician_speciality" (
    "technician_id" integer,
    "aircraft_model_id" integer,
    CONSTRAINT "technician_speciality_aircraft_model_id_fkey" FOREIGN KEY (aircraft_model_id) REFERENCES aircraft_model(id) NOT DEFERRABLE,
    CONSTRAINT "technician_speciality_technician_id_fkey" FOREIGN KEY (technician_id) REFERENCES technician(id) NOT DEFERRABLE
) WITH (oids = false);


DROP TABLE IF EXISTS "ticket";
DROP SEQUENCE IF EXISTS ticket_id_seq;
CREATE SEQUENCE ticket_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 35618 CACHE 1;

CREATE TABLE "public"."ticket" (
    "id" integer DEFAULT nextval('ticket_id_seq') NOT NULL,
    "price" integer,
    "last_price" integer,
    "is_avaliable" boolean,
    "is_checked_in" boolean,
    "booking_id" integer,
    "flight_id" integer,
    "seat_no" character varying(20),
    CONSTRAINT "ticket_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "ticket_booking_id_fkey" FOREIGN KEY (booking_id) REFERENCES booking(id) NOT DEFERRABLE,
    CONSTRAINT "ticket_flight_id_fkey" FOREIGN KEY (flight_id) REFERENCES flight(id) NOT DEFERRABLE
) WITH (oids = false);


-- 2020-07-27 16:38:50.224032+00
