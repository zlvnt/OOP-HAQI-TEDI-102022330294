CREATE DATABASE Zelvin_102022330294_A;

USE Zelvin_102022330294_A;
 CREATE TABLE showroomdaspro_costumers_0294(
    customer_id int(10) NOT NULL,
    customer_name VARCHAR(50) NOT NULL,
    customer_zip_code_prefix int(10) NOT NULL,
    customer_state VARCHAR(20) NOT NULL,
    primary key(customer_id)
 );

 CREATE TABLE showroomdaspro_salesperson_0294(
    salesperson_id int(10) NOT NULL,
    salesperson_name VARCHAR(50) NOT NULL,
    salesperson_city VARCHAR(20) NOT NULL,
    salesperson_zip_code_prefix INT(10) NOT NULL,
    salesperson_state VARCHAR(20) NOT NULL,
    primary key(salesperson_id)
 );

 CREATE TABLE showroomdaspro_cars_0294(
    car_id int(10) NOT NULL,
    car_brand VARCHAR(20) NOT NULL,
    car_model varchar(20) NOT NULL,
    description VARCHAR(50) NOT NULL,
    price INT(20) NOT NULL,
    primary key(car_id)
 );

 CREATE TABLE showroomdaspro_payments_0294(
    payment_id int(10) NOT NULL,
    payment_type VARCHAR(20) NOT NULL,
    primary key(payment_id)
 );

 CREATE TABLE showroomdaspro_order_0294(
    order_id INT(10) NOT NULL,
    customer_id int(10) NOT NULL,
    salesperson_id int(10) NOT NULL,
    payment_id int(10) NOT NULL,
    order_status VARCHAR(15) NOT NULL,
    order_purchase_time TIME,
    order_purhcase_date DATE,
    order_delivery_date DATE,
    total_payment int(20) NOT NULL,
    primary key(order_id),
    foreign key(customer_id)
        references showroomdaspro_costumers_0294(customer_id),
    foreign key(salesperson_id)
        references showroomdaspro_salesperson_0294(salesperson_id),
    foreign key(payment_id)
        references showroomdaspro_payments_0294(payment_id)
 );

 CREATE TABLE showroomdaspro_order_cars_0294(
    order_item_id INT(10) NOT NULL,
    order_id INT(10) NOT NULL,
    car_id INT(10) NOT NULL,
    quantity INT(20) NOT NULL,
    primary key(order_item_id),
    foreign key(order_id)
        references showroomdaspro_order_0294(order_id),
    foreign key(car_id)
        references showroomdaspro_cars_0294(car_id)
 );
    
ALTER TABLE nama_baris CHANGE nama_atribut_sebelum nama_atribut_sesudah varchar(50);    #gantikolom

ALTER TABLE old_table_name RENAME new_table_name; #gantinamaTABLE

ALTER TABLE namatabel MODIFY namakolom tipedatabaru; #gantitypekolom
