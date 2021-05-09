use comp420project;


-- procedures

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

-- creates a record for a new game
delimiter //
create procedure new_game(in title varchar(30), pub varchar(30), dev varchar(30), esrb varchar(3), price float, discount float, release_date date, max_spec varchar(250), min_spec varchar(250))
BEGIN
DECLARE p,d char(9);
SELECT PUBLISHER_ID into p from publisher where pub = p_company_name;
Select developer_id into d from developer where dev = d_company_name;
insert into game values (p,d,title,esrb,price,discount,release_date, max_spec, min_spec, 0);
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
create procedure new_dlc(in game_id char(9), dev varchar(30),title varchar(30), price float, discount float, release_date date)
BEGIN
DECLARE d char(9);
Select developer_id into d from developer where dev = d_company_name;
insert into game_dlc values (game_id, d,title, price, discount, release_date);
END //
delimiter ;

-- adds a specified dlc, using dlc ID, to a specified user's library
delimiter // 
create procedure add_game(IN cus_id char(9), dlc_id char(9))
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

CREATE VIEW BasicGameList AS SELECT g_title, g_esrb, g_price, g_avg_rating from game;

create view BasicCustInfo as select cust_fname, cust_lname, cust_alias from customer;



-- testing 
INSERT INTO customer values(null,'Roger','Lorelli','kain525','roger.lorelli@yahoo.com');

select * from BasicCustInfo;

select * from customer;

insert into customer values(null,'Chris','Lorelli','cyclesurgeon','something@something.com');

call create_message(1, "dude, where's my car?",null);

call send_message(1,2);

select * from recipient;
select * from message;