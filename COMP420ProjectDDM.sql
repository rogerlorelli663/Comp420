use comp420project;


-- procedures
delimiter //
create procedure retrievegamelibrary(IN id char(9))
BEGIN
SELECT g_title from game
join game_library_entry using (game_id)
join customer using (cust_id)
where cust_id = id;
END //
delimiter ;

delimiter //
create procedure new_game(in title varchar(30), pub varchar(30), dev varchar(30), esrb varchar(3), price float, discount float, release_date date, max_spec varchar(250), min_spec varchar(250))
BEGIN
DECLARE p,d char(9);
SELECT PUBLISHER_ID into p from publisher where pub = p_company_name;
Select developer_id into d from developer where dev = d_company_name;
insert into game values (p,d,title,esrb,price,discount,release_date, max_spec, min_spec, 0);
END //
delimiter ;

delimiter // 
create procedure add_game(IN cus_id char(9), g_id char(9))
BEGIN  
insert into game_library_entry values (cus_id,g_id);
END //
delimiter ;


-- triggers
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

insert into customer values(null,'Chris','Lorelli','cyclesurgeon','something@something.com');