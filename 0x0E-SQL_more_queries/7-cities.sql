-- Creates the database hbtn_0d_usa with the table cities.
USE `hbtn_0d_usa`;

CREATE TABLE IF NOT EXISTS `cities` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `state_id` INT NOT NULL,
    `name` VARCHAR(256) NOT NULL,
    FOREIGN KEY (`state_id`) REFERENCES `states`(`id`)
);