-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema project
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `project` DEFAULT CHARACTER SET utf8 ;
USE `project` ;

-- -----------------------------------------------------
-- Table `project`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(20) NOT NULL,
  `created_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`categories` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`instruments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`instruments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `user_id` INT NOT NULL,
  `category_id` INT NOT NULL,
  `price` FLOAT(10,2) NOT NULL,
  `description` VARCHAR(500) NOT NULL,
  `discount` FLOAT(2,2) NOT NULL DEFAULT 0.00,
  `model` VARCHAR(100) NULL,
  `company_name` VARCHAR(150) NULL,
  `availablity` BLOB NOT NULL DEFAULT True,
  `picture_1` VARCHAR(100) NOT NULL,
  `picture_2` VARCHAR(100) NULL,
  `picture_3` VARCHAR(100) NULL,
  PRIMARY KEY (`id`),
  INDEX `user_id_idx` (`user_id` ASC) VISIBLE,
  INDEX `category_id_idx` (`category_id` ASC) VISIBLE,
  CONSTRAINT `user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `project`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `category_id`
    FOREIGN KEY (`category_id`)
    REFERENCES `project`.`categories` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`rentals`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`rentals` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `instrument_id` INT NOT NULL,
  `hired_date` DATETIME NOT NULL,
  `retured_date` DATETIME NOT NULL,
  `hired` BLOB NOT NULL DEFAULT True,
  `returned` BLOB NULL DEFAULT False,
  PRIMARY KEY (`id`),
  INDEX `id_user_idx` (`user_id` ASC) VISIBLE,
  INDEX `instrument_id_idx` (`instrument_id` ASC) VISIBLE,
  CONSTRAINT `id_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `project`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `instrument_id`
    FOREIGN KEY (`instrument_id`)
    REFERENCES `project`.`instruments` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`reviews`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`reviews` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comment` VARCHAR(200) NOT NULL,
  `star` INT NOT NULL DEFAULT 0,
  `user_id` INT NOT NULL,
  `instrument_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `user_idd_idx` (`user_id` ASC) VISIBLE,
  INDEX `id_instrument_idx` (`instrument_id` ASC) VISIBLE,
  CONSTRAINT `user_idd`
    FOREIGN KEY (`user_id`)
    REFERENCES `project`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `id_instrument`
    FOREIGN KEY (`instrument_id`)
    REFERENCES `project`.`instruments` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`kyc_status`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`kyc_status` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `country_identity_number` INT NULL,
  `date_of_birth` DATETIME NOT NULL,
  `other_names` VARCHAR(200) NOT NULL,
  `confirm_country_id` BLOB NULL DEFAULT False,
  `country` VARCHAR(50) NOT NULL,
  `city` VARCHAR(50) NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `id_usere_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `id_usere`
    FOREIGN KEY (`user_id`)
    REFERENCES `project`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
