

CREATE TABLE product (
    id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    company VARCHAR(50),
    cost INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    PRIMARY KEY (id)
);

CREATE TABLE customer (
    id INT NOT NULL,
    name VARCHAR(60) NOT NULL,
    password VARCHAR(20) NOT NULL,
    age INT,
    phone_no VARCHAR(12),
    address VARCHAR(200),
    gender VARCHAR(10),
    PRIMARY KEY (id)
);

-- Sample data for the product table
INSERT INTO product (id, name, company, cost, quantity) VALUES (1, 'Lipstick', 'CosmeticsCo', 150, 50);
INSERT INTO product (id, name, company, cost, quantity) VALUES (2, 'Foundation', 'BeautyCorp', 300, 30);
INSERT INTO product (id, name, company, cost, quantity) VALUES (3, 'Mascara', 'GlamourInc', 200, 20);
INSERT INTO product (id, name, company, cost, quantity) VALUES (4, 'Blush', 'MakeupWorld', 250, 40);
INSERT INTO product (id, name, company, cost, quantity) VALUES (5, 'Eyeliner', 'EyeBeauty', 100, 60);

-- Sample data for the customer table
INSERT INTO customer (id, name, age, password, phone_no, address, gender) VALUES (1, 'Vani Goyal', 25, '123', '555-0000', '500 Park St, Cosmopolis', 'Female');
INSERT INTO customer (id, name, age, password, phone_no, address, gender) VALUES (2, 'Alice Smith', 28, 'alice123', '555-1234', '123 Maple St, Springfield', 'Female');
INSERT INTO customer (id, name, age, password, phone_no, address, gender) VALUES (3, 'Bob Johnson', 35, 'bob123', '555-5678', '456 Oak St, Metropolis', 'Male');
INSERT INTO customer (id, name, age, password, phone_no, address, gender) VALUES (4, 'Carol White', 22, 'carol123', '555-8765', '789 Pine St, Gotham', 'Female');
INSERT INTO customer (id, name, age, password, phone_no, address, gender) VALUES (5, 'Dave Black', 40, 'dave123', '555-4321', '101 Birch St, Star City', 'Male');
INSERT INTO customer (id, name, age, password, phone_no, address, gender) VALUES (6, 'Eve Green', 30, 'eve123', '555-6789', '202 Cedar St, Central City', 'Female');

