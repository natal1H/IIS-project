CREATE TABLE facility(
    id_facility serial PRIMARY KEY,
    address VARCHAR (150) NOT NULL,
    name VARCHAR (50) UNIQUE NOT NULL,
    deadline TIME NOT NULL,
    max_ordered_meals SMALLINT DEFAULT 1
);

CREATE TABLE menu(
    id_menu serial PRIMARY KEY,
    type SMALLINT NOT NULL,
    date DATE,
    max_items SMALLINT DEFAULT 10
);

CREATE TABLE item(
    id_item serial PRIMARY KEY,
    diet_type VARCHAR (50),
    name VARCHAR (50) NOT NULL,
    description VARCHAR (150),
    price REAL NOT NULL,
    image VARCHAR (50)
);

CREATE TABLE food_order(
    id_food_order serial PRIMARY KEY,
    status VARCHAR (50),
    payment_form VARCHAR (50),
    date_created TIMESTAMP DEFAULT current_timestamp,
    date_paid TIMESTAMP,
    date_approved TIMESTAMP,
    date_delivered TIMESTAMP
);

CREATE TABLE person(
    id_person serial PRIMARY KEY,
    firstname VARCHAR (50) NOT NULL,
    surname VARCHAR (50) NOT NULL,
    address VARCHAR (150) NOT NULL,
    telephone VARCHAR (15) NOT NULL
);

CREATE TABLE registered(
    id_person INTEGER REFERENCES person(id_person),
    profile_info VARCHAR (200),
    image VARCHAR (50),
    email VARCHAR (50) UNIQUE NOT NULL,
    login VARCHAR (20) UNIQUE NOT NULL,
    password VARCHAR (50) NOT NULL,
    PRIMARY KEY (id_person)
);

CREATE TABLE employee(
    login VARCHAR (20) REFERENCES registered(login),
    role VARCHAR (50) NOT NULL,
    PRIMARY KEY (login)
);

CREATE TABLE rel_person_food_order(
    id_person INTEGER REFERENCES person(id_person),
    id_food_order INTEGER REFERENCES food_order(id_food_order),
    PRIMARY KEY (id_person, id_food_order)
);

CREATE TABLE rel_facility_menu(
    id_facility INTEGER REFERENCES facility(id_facility),
    id_menu INTEGER REFERENCES menu(id_menu),
    PRIMARY KEY (id_facility, id_menu)
);

CREATE TABLE rel_menu_item(
    id_menu INTEGER REFERENCES menu(id_menu),
    id_item INTEGER REFERENCES item(id_item),
    PRIMARY KEY (id_menu, id_item)
);

CREATE TABLE rel_food_order_facility(
    id_food_order INTEGER REFERENCES food_order(id_food_order),
    id_facility INTEGER REFERENCES facility(id_facility),
    PRIMARY KEY (id_food_order, id_facility)
);

CREATE TABLE rel_food_order_delivery(
    id_food_order INTEGER REFERENCES food_order(id_food_order),
    login VARCHAR (20) REFERENCES employee(login),
    PRIMARY KEY (id_food_order, login)
);

CREATE TABLE rel_food_order_approval(
    id_food_order INTEGER REFERENCES food_order(id_food_order),
    login VARCHAR (20) REFERENCES employee(login),
    PRIMARY KEY (id_food_order, login)
);
