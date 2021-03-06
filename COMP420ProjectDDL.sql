use COMP420Project;
DROP database COMP420Project;
create database COMP420Project;
use COMP420Project;

create table CUSTOMER(
CUST_ID int auto_increment,
CUST_FNAME VARCHAR(15),
CUST_LNAME VARCHAR(15),
CUST_ALIAS varchar(15),
steam_alias varchar(15),
epic_alias varchar(15), 
uplay_alias varchar(15), 
gog_alias varchar(15), 
ea_alias varchar(15),
CUST_EMAIL varchar(50),
pass varchar(50),
DATE_ADDED DATE,
primary key (CUST_ID)
);

create table PUBLISHER(
PUBLISHER_ID int auto_increment,
P_COMPANY_NAME VARCHAR(100),
P_REP_PHONE VARCHAR(12),
P_REP_EMAIL VARCHAR(50),
P_CMPY_WEBSITE VARCHAR(50),
COUNTER int,
PRIMARY KEY (PUBLISHER_ID)
);

CREATE TABLE DEVELOPER(
DEVELOPER_ID int auto_increment,
D_COMPANY_NAME VARCHAR(100),
D_REP_PHONE VARCHAR(120),
D_REP_EMAIL VARCHAR(50),
D_CMPY_WEBSITE VARCHAR(50),
COUNTER int,
PRIMARY KEY (DEVELOPER_ID)
);

CREATE TABLE GAME(
GAME_ID int auto_increment,
PUBLISHER_ID int not null,
DEVELOPER_ID int not null,
G_TITLE VARCHAR(100) not null,
G_ESRB VARCHAR(3),
G_PRICE FLOAT not null,
G_DISCOUNT FLOAT not null,
G_RELEASE_DATE DATE not null,
G_MAX_SPEC VARCHAR(1000) not null,
G_MIN_SPEC VARCHAR(1000) not null,
G_AVG_RATING FLOAT,
DATE_ADDED DATE,
COUNTER int,
PRIMARY KEY (GAME_ID),
FOREIGN KEY (PUBLISHER_ID) references PUBLISHER (PUBLISHER_ID),
FOREIGN KEY (DEVELOPER_ID) references DEVELOPER (DEVELOPER_ID)
);

CREATE TABLE GAME_PLATFORM(
GP_ID INT auto_increment,
GAME_ID INT,
PLAT_NAME ENUM ('STEAM','UPLAY','GOG','EA','EPIC'),  
PLAT_website varchar(100),
PRIMARY KEY(GP_ID),
FOREIGN KEY (GAME_ID) REFERENCES GAME (GAME_ID)
);

CREATE TABLE Tag(
TAG_CODE int auto_increment,
TAG_NAME VARCHAR(15),
PRIMARY KEY (TAG_CODE)
);

CREATE TABLE GAME_DLC(
DLC_ID int auto_increment,
GAME_ID int,
DEVELOPER_ID int,
DLC_TITLE VARCHAR(30),
DLC_PRICE FLOAT,
DLC_DISCOUNT FLOAT,
DLC_RELEASE_DATE DATE,
DATE_ADDED DATE,
COUNTER int,
PRIMARY KEY (DLC_ID),
FOREIGN KEY (GAME_ID) REFERENCES GAME (GAME_ID),
FOREIGN KEY (DEVELOPER_ID) REFERENCES DEVELOPER (DEVELOPER_ID)
);

CREATE TABLE GAME_TAG(
TAG_CODE int,
GAME_ID int,
PRIMARY KEY (TAG_CODE, GAME_ID),
FOREIGN KEY (TAG_CODE) REFERENCES TAG (TAG_CODE),
FOREIGN KEY (GAME_ID) REFERENCES GAME (GAME_ID)
);

CREATE TABLE GAME_LIBRARY_ENTRY(
CUST_ID int,
GAME_ID int,
PLAT_NAME ENUM ('STEAM','UPLAY','GOG','EA','EPIC'),  
EXE_PATH varchar(1000),
DATE_ADDED DATE,
PRIMARY KEY (CUST_ID, GAME_ID),
FOREIGN KEY (CUST_ID) REFERENCES CUSTOMER (CUST_ID),
FOREIGN KEY (GAME_ID) REFERENCES GAME (GAME_ID)
);

CREATE TABLE DLC_LIBRARY_ENTRY(
CUST_ID int,
DLC_ID int,
PRIMARY KEY (CUST_ID, DLC_ID),
FOREIGN KEY (CUST_ID) REFERENCES CUSTOMER (CUST_ID),
FOREIGN KEY (DLC_ID) REFERENCES GAME_DLC (DLC_ID)
);

CREATE TABLE REVIEW(
CUST_ID int,
GAME_ID int,
R_RATING INT,
R_COMMENT VARCHAR(250),
PRIMARY KEY (CUST_ID, GAME_ID),
FOREIGN KEY (CUST_ID) REFERENCES CUSTOMER (CUST_ID),
FOREIGN KEY (GAME_ID) REFERENCES GAME (GAME_ID)
);

CREATE TABLE CUSTOMER_COLLECTION(
COLLECTION_ID int,
CUST_ID int,
C_NAME VARCHAR(10),
PRIMARY KEY (COLLECTION_ID),
FOREIGN KEY (CUST_ID) REFERENCES CUSTOMER (CUST_ID)
);

CREATE TABLE COLLECTION_ENTRY(
GAME_ID int,
COLLECTION_ID int,
PRIMARY KEY (GAME_ID, COLLECTION_ID),
FOREIGN KEY (GAME_ID) REFERENCES GAME (GAME_ID),
FOREIGN KEY (COLLECTION_ID) REFERENCES CUSTOMER_COLLECTION (COLLECTION_ID)
);

CREATE TABLE MESSAGE(
MESSAGE_ID int auto_increment,
M_CREATE_DATE DATETIME,
M_CONTENT VARCHAR(250),
M_IMAGE_PATH VARCHAR(250),
M_CREATED_BY int,
PRIMARY KEY (MESSAGE_ID),
FOREIGN KEY (M_CREATED_BY) REFERENCES CUSTOMER (CUST_ID)
);

CREATE TABLE RECIPIENT(
MESSAGE_ID int,
CUST_ID int,
R_READ int, 
PRIMARY KEY(MESSAGE_ID, CUST_ID),
FOREIGN KEY (CUST_ID) REFERENCES CUSTOMER (CUST_ID),
FOREIGN KEY (MESSAGE_ID) REFERENCES MESSAGE (MESSAGE_ID)
);

CREATE TABLE FRIEND(
CUST_ID int,
FRIEND_ID int,
F_SHARE_SETTING bool,
F_REAL_NAME bool,
PRIMARY KEY(CUST_ID, FRIEND_ID),
FOREIGN KEY (CUST_ID) REFERENCES CUSTOMER (CUST_ID),
FOREIGN KEY (FRIEND_ID) REFERENCES CUSTOMER (CUST_ID)
);