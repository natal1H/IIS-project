-- Inserting into 'facility' table
INSERT INTO canteen_facility (id_facility, address, name, deadline, max_ordered_meals)
    VALUES (1, 'Božetěchova 1, Brno-Královo Pole', 'Menza Starý pivovar', '18:00:00', 5);
INSERT INTO canteen_facility (id_facility, address, name, deadline, max_ordered_meals)
    VALUES (2, 'Purkyňova 93, Brno-Královo Pole', 'Menza Purkyňova', '17:00:00', 5);

-- Inserting into 'menu' table
INSERT INTO canteen_menu (id_menu, type, date, max_items)
    VALUES (1, 'd', '2019-10-16', 10);
INSERT INTO canteen_menu (id_menu, type, date, max_items)
    VALUES (2, 'd', '2019-10-17', 10);
INSERT INTO canteen_menu (id_menu, type, max_items)
    VALUES (3, 's', 10);
INSERT INTO canteen_menu (id_menu, type, max_items)
    VALUES (4, 's', 10);

-- Inserting into 'item' table
INSERT INTO canteen_item (id_item, diet_type, name, description, price)
    VALUES (1, 'n', 'Párok v rožku', 'Proste párok v rožku', 1.5);
INSERT INTO canteen_item (id_item, diet_type, name, description, price)
    VALUES (2, 'n', 'Bageta', 'Proste bageta', 2.5);

-- Inserting into 'person' table
INSERT INTO canteen_person (id_person, firstname, surname, address, telephone)
    VALUES (1, 'Jozef', 'Mrkvička', 'Purkyňova 93, 612 00 Brno', '0987654321');
INSERT INTO canteen_person (id_person, firstname, surname, address, telephone)
    VALUES (2, 'Ján', 'Mrkvička', 'Purkyňova 93, 612 00 Brno', '0987654322');
INSERT INTO canteen_person (id_person, firstname, surname, address, telephone)
    VALUES (3, 'Jana', 'Mrkvová', 'Purkyňova 93, 612 00 Brno', '0987654323');
INSERT INTO canteen_person (id_person, firstname, surname, address, telephone)
    VALUES (4, 'Anna', 'Mrkvová', 'Purkyňova 93, 612 00 Brno', '0987654324');

-- Inserting into 'food_order' table
INSERT INTO canteen_food_order (id_food_order, status, payment_form, person_id, facility_id, date_created, date_approved, date_delivered, date_paid, approved_by_id, delivered_by_id)
   VALUES (1, 'o', 'd', 1, 1, '2019-10-16 15:26', null, null, null, null, null);


-- Inserting into 'registered' table
INSERT INTO canteen_registered (person_id, email, login, password)
    VALUES (1, 'jozef.mrkvicka@mail.com', 'mrkva1', '123456');
INSERT INTO canteen_registered (person_id, email, login, password)
    VALUES (2, 'jan.mrkvicka@mail.com', 'mrkva2', '123456');
INSERT INTO canteen_registered (person_id, email, login, password)
    VALUES (3, 'jana.mrkvova@mail.com', 'mrkva3', '123456');
INSERT INTO canteen_registered (person_id, email, login, password)
    VALUES (4, 'anna.mrkvova@mail.com', 'mrkva4', '123456');

-- Inserting into 'employee' table
INSERT INTO canteen_employee (registered_id, role)
    VALUES ('jozef.mrkvicka@mail.com', 'a');
INSERT INTO canteen_employee (registered_id, role)
    VALUES ('jan.mrkvicka@mail.com', 'o');
INSERT INTO canteen_employee (registered_id, role)
    VALUES ('jana.mrkvova@mail.com', 'd');


-- Inserting into 'facility_menus' table
INSERT INTO canteen_facility_menus (id_facility_id, id_menu_id)
    VALUES (1, 1);
INSERT INTO canteen_facility_menus (id_facility_id, id_menu_id)
    VALUES (1, 2);
INSERT INTO canteen_facility_menus (id_facility_id, id_menu_id)
    VALUES (1, 3);
INSERT INTO canteen_facility_menus (id_facility_id, id_menu_id)
    VALUES (2, 4);

-- Inserting into 'menu_items' table
INSERT INTO canteen_menu_items (id_menu_id, id_item_id)
    VALUES (3, 1);

-- Inserting into 'food_order_item' table
INSERT INTO canteen_food_order_item (id_food_order_id, id_item_id)
    VALUES (1, 2);