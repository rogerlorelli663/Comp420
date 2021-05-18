-- use comp420project;


-- procedures

-- creates a new customer account
delimiter //
create procedure create_cust_account (in fname varchar(15), lname varchar(15), alias varchar(15), email varchar(50))
BEGIN
insert into customer values(null, fname, lname, alias, '', '', '', '', '',email);
END //
delimiter ;

-- link account to platform
delimiter //
create procedure link_account(in cust_id int, platform varchar(10), alias varchar(15))
BEGIN
declare l_sql_stmt varchar(1000);
Set l_sql_stmt = CONCAT('UPDATE customer SET ' + platform + ' = ' + alias + ' where customer.cust_id = ' + cust_id);
prepare stmt from @l_sql_stmt;
execute stmt;
DEALLOCATE PREPARE stmt;
END //
delimiter ;

-- create new publisher entry
delimiter //
create procedure create_publisher (in company_name varchar(100), rep_phone varchar(12), rep_email varchar(50), company_website varchar(50))
BEGIN
insert into publisher values(null, company_name, rep_phone, rep_email, company_website);
END //
delimiter ;

-- create new developer entry
delimiter //
create procedure create_developer (in company_name varchar(100), rep_phone varchar(12), rep_email varchar(50), company_website varchar(50))
BEGIN
insert into developer values(null, company_name, rep_phone, rep_email, company_website);
END //
delimiter ;

-- query to return all games in a player's library based on system customer ID
delimiter //
create procedure retrievegamelibrary(IN id char(9))
BEGIN
SELECT g_title from game
join game_library_entry using (game_id)
join customer using (cust_id)
where cust_id = id;
END //
delimiter ;

-- drop procedure retrievegamelibrary;

-- retrieve basic customer info by alias
delimiter //
create procedure get_customer(in alias varchar(15))
BEGIN
select * from BasicCustInfo where cust_alias = alias;
END //
delimiter ;

-- creates a record for a new game
delimiter //
create procedure new_game(in title varchar(100), pub varchar(100), dev varchar(100), esrb varchar(3), price float, discount float, release_date date, max_spec varchar(1000), min_spec varchar(1000))
BEGIN
DECLARE p,d int;
SELECT PUBLISHER_ID into p from publisher where pub = p_company_name;
Select developer_id into d from developer where dev = d_company_name;
insert into game values (null,p,d,title,esrb,price,discount,release_date, max_spec, min_spec, 0);
END //
delimiter ;

-- drop procedure new_game;

-- adds a specified game, using game ID, to a specified user's library
delimiter // 
create procedure add_game(IN cus_id char(9), g_id char(9))
BEGIN  
insert into game_library_entry values (cus_id,g_id);
END //
delimiter ;

-- creates a record for a new dlc
delimiter //
create procedure new_dlc(in game_id char(9), dev varchar(100),title varchar(100), price float, discount float, release_date date)
BEGIN
DECLARE d char(9);
Select developer_id into d from developer where dev = d_company_name;
insert into game_dlc values (game_id, d,title, price, discount, release_date);
END //
delimiter ;

-- adds a specified dlc, using dlc ID, to a specified user's library
delimiter // 
create procedure add_dlc(IN cus_id char(9), dlc_id char(9))
BEGIN  
insert into dlc_library_entry values (cus_id, dlc_id);
END //
delimiter ;

-- creates record for a message sent from user to friend, returns message id so that message can be forwarded to recipients
delimiter //
create procedure create_message(in cus_id int, message varchar(250), image_path varchar(250))
BEGIN
DECLARE date_now datetime;
Set date_now = now();
insert into message values(null, date_now, message, image_path, cus_id);
select message_id from message where m_create_date = date_now and m_created_by = cus_id;
END //
delimiter ;

-- drop procedure create_message;

-- send created message to recipients - must be called for each recipient
delimiter //
create procedure send_message(in message_id int, recipient_id int)
BEGIN
insert into recipient values (message_id, recipient_id);
END //
delimiter ;

-- retrieve unread messages
delimiter //
create procedure retrieve_messages(in recipient_id int)
BEGIN
select m_content, m_image_path, m_created_by, m_create_date from message
join recipient using (message_id) 
where recipient.cust_id = recipient_id and r_read = 0;
update recipient set r_read = 1 where cust_id = recipient_id and r_read = 0;
END //
delimiter ;

-- create new custom collection
delimiter //
create procedure create_collection(in cus_id int, name varchar(10))
BEGIN
insert into customer_collection values (null, cus_id, name);
END //
delimiter ;

-- add game to collection
delimiter //
create procedure collection_entry(in game_id int, collection_id int)
BEGIN
insert into collection_entry values (game_id, collection_id);
END //
delimiter ;

-- retrieves customer's collection by collection name
delimiter //
create procedure retrieve_collection(in cust_id int, collection_name varchar(10))
BEGIN
select g_title from game
join collection_entry using (game_id)
join customer_collection using (collection_id)
where c_name = collection_name and customer_collection.cust_id = cust_id;
END //
delimiter ; 

-- create new review
delimiter //
create procedure create_review(in cust_id int, game_id int, rating int, message varchar(250))
BEGIN
insert into review values(cust_id, game_id, rating, message);
END //
delimiter ;

-- add friend
delimiter //
create procedure add_friend(in cust_id int, friend_id int)
BEGIN
insert into friend values (cust_id, friend_id, '0','0');
END //
delimiter ;

-- update friend share settings  
delimiter //
create procedure update_friend_share(in cust_id int, friend_id int, setting char(1))
BEGIN
update friend Set f_share_setting = setting where friend.cust_id = cust_id and friend.friend_id = friend_id;
END //
delimiter ;

-- update friend real name setting
delimiter //
create procedure update_friend_rn(in cust_id int, friend_id int, real_name char(1))
BEGIN
update friend Set f_real_name = real_name where friend.cust_id = cust_id and friend.friend_id = friend_id;
END //
delimiter ;

-- retrieve list games friend owns
delimiter //
create procedure get_friend_game_list(in friend_id int)
BEGIN
select * from basicgamelistcollection
join game_library_entry using (game_id)
where cust_id = friend_id;
END //
delimiter ;

-- retrieve list of games that both cust and friend own
delimiter //
create procedure get_shared_game_list(in friend_id int, cust_id int)
BEGIN
select * from basicgamelistcollection p1
join game_library_entry using (game_id)
where cust_id = cust_id and
p1.game_id = (Select game_id from basicgamelistcollection 
join game_library_entry using (game_id)
where cust_id = friend_id);
END //
delimiter ;

-- triggers

-- updates the rating average of a game when a new review is written
delimiter //
create trigger rating_check
AFTER 
INSERT ON REVIEW
FOR EACH ROW
BEGIN 
DECLARE avg_rating float;
select avg(r_rating) into avg_rating from review where review.GAME_ID = new.GAME_ID;
update game Set g_avg_rating = avg_rating where game.game_id = new.GAME_ID;
END //
delimiter ; 

-- views

-- 

CREATE VIEW BasicGameListStore AS SELECT game_id, g_title, g_esrb, g_price, g_avg_rating from game;

CREATE VIEW BasicGameListCollection as select game_id, g_title from game;

-- removes personal information that other players do not need to be able to see
create view BasicCustInfo as select cust_id, cust_alias from customer; 

create view FriendInfo as select cust_alias, steam_alias, epic_alias, uplay_alias, gog_alias, ea_alias from customer;

create view TrueNameFriendInfo as select cust_fname, cust_lname, cust_alias, cust_email from customer;


create view GameTagList as SELECT game_id, g_title, GROUP_CONCAT(tag_name) as "tags" 
FROM game 
join game_tag using (game_id)
join tag using(tag_code)GROUP BY game_id;

