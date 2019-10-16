-- Inserting into 'facility' table
INSERT INTO facility (id_facility, address, name, deadline, max_ordered_meals)
    VALUES (1, 'Božetěchova 1, Brno-Královo Pole', 'Menza Starý pivovar', '18:00:00', 5);

-- Inserting into 'menu' table
INSERT INTO menu (id_menu, type, date, max_items)
    VALUES (1, 0, '2019-10-16', 10);
INSERT INTO menu (id_menu, type, date, max_items)
    VALUES (2, 0, '2019-10-17', 10);
INSERT INTO menu (id_menu, type, max_items)
    VALUES (3, 1, 10);

-- Inserting into 'person' table
INSERT INTO person (id_person, firstname, surname, address, telephone)
    VALUES (1, 'Jozef', 'Mrkvička', 'Purkyňova 93, 612 00 Brno', '0987654321');
INSERT INTO person (id_person, firstname, surname, address, telephone)
    VALUES (2, 'Ján', 'Mrkvička', 'Purkyňova 93, 612 00 Brno', '0987654322');
INSERT INTO person (id_person, firstname, surname, address, telephone)
    VALUES (3, 'Jana', 'Mrkvová', 'Purkyňova 93, 612 00 Brno', '0987654323');
INSERT INTO person (id_person, firstname, surname, address, telephone)
    VALUES (4, 'Anna', 'Mrkvová', 'Purkyňova 93, 612 00 Brno', '0987654324');

-- Inserting into 'item' table
INSERT INTO item (id_item, diet_type, name, description, price)
    VALUES (1, 'normálne', 'Párok v rožku', 'Proste párok v rožku', 1.5);
INSERT INTO item (id_item, diet_type, name, description, price)
    VALUES (2, 'normálne', 'Bageta', 'Proste bageta', 2.5);

-- Inserting into 'food_order' table
INSERT INTO food_order (id_food_order, status, payment_form)
    VALUES (1, 'nezaplatené', 'karta');

-- Inserting into 'registered' table
INSERT INTO registered (id_person, email, login, password)
    VALUES (1, 'jozef.mrkvicka@mail.com', 'mrkva1', '123456');
INSERT INTO registered (id_person, email, login, password)
    VALUES (2, 'jan.mrkvicka@mail.com', 'mrkva2', '123456');
INSERT INTO registered (id_person, email, login, password)
    VALUES (3, 'jana.mrkvova@mail.com', 'mrkva3', '123456');
INSERT INTO registered (id_person, email, login, password)
    VALUES (4, 'anna.mrkvova@mail.com', 'mrkva4', '123456');

-- Inserting into 'employee' table
INSERT INTO employee (login, role)
    VALUES ('mrkva1', 0);
INSERT INTO employee (login, role)
    VALUES ('mrkva2', 1);
INSERT INTO employee (login, role)
    VALUES ('mrkva3', 2);

-- Inserting into 'rel_person_food_order' table
INSERT INTO rel_person_food_order (id_person, id_food_order)
    VALUES (1, 1);

-- Inserting into 'rel_facility_menu' table
INSERT INTO rel_facility_menu (id_facility, id_menu)
    VALUES (1, 1);
INSERT INTO rel_facility_menu (id_facility, id_menu)
    VALUES (1, 2);
INSERT INTO rel_facility_menu (id_facility, id_menu)
    VALUES (1, 3);

-- Inserting into 'rel_menu_item' table
INSERT INTO rel_menu_item (id_menu, id_item)
    VALUES (3, 1);

-- Inserting into 'rel_food_order_facility' table
INSERT INTO rel_food_order_facility (id_food_order, id_facility)
    VALUES (1, 1);

-- Inserting into 'rel_food_order_delivery' table
INSERT INTO rel_food_order_delivery (id_food_order, login)
    VALUES (1, 'mrkva3');

-- Inserting into 'rel_food_order_approval' table
