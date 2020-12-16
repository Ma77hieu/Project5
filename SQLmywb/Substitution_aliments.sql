-- MySQL Script generated by MySQL Workbench
-- Tue Dec 15 15:46:37 2020
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema substitution_aliments
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `substitution_aliments` ;
-- -----------------------------------------------------
-- Schema substitution_aliments
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `substitution_aliments` DEFAULT CHARACTER SET utf8 ;
USE `substitution_aliments` ;

-- -----------------------------------------------------
-- Table `substitution_aliments`.`categories`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `substitution_aliments`.`categories` ;

CREATE TABLE IF NOT EXISTS `substitution_aliments`.`categories` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name`VARCHAR(255) NULL,
  -- INDEX ind_cat_name (`name`),
  PRIMARY KEY (`id`))
  
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `substitution_aliments`.`aliments`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `substitution_aliments`.`aliments` ;

CREATE TABLE IF NOT EXISTS `substitution_aliments`.`aliments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(500) NULL,
  `nutrition_grade` CHAR(1) NULL,
  `stores` VARCHAR(255) NULL,
  `url` VARCHAR(255) NULL,
  `categories_id` VARCHAR(255) NULL,
  PRIMARY KEY (`id`)
  -- INDEX `fk_aliments_categories_idx` (`categories_id` ASC) VISIBLE,
  -- CONSTRAINT `fk_aliments_categories`
  --   FOREIGN KEY (`categories_id`)
  --   REFERENCES `substitution_aliments`.`categories` (`name`)
  --   ON DELETE NO ACTION
  --   ON UPDATE NO ACTION
  )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `substitution_aliments`.`substituts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `substitution_aliments`.`substituts` ;

CREATE TABLE IF NOT EXISTS `substitution_aliments`.`substituts` (
  `aliments_id` INT NOT NULL,
  `substitut_id` INT NOT NULL,
  PRIMARY KEY (`aliments_id`, `substitut_id`),
  INDEX `fk_aliments_has_aliments_aliments2_idx` (`substitut_id` ASC) VISIBLE,
  INDEX `fk_aliments_has_aliments_aliments1_idx` (`aliments_id` ASC) VISIBLE,
  CONSTRAINT `fk_aliments_has_aliments_aliments1`
    FOREIGN KEY (`aliments_id`)
    REFERENCES `substitution_aliments`.`aliments` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_aliments_has_aliments_aliments2`
    FOREIGN KEY (`substitut_id`)
    REFERENCES `substitution_aliments`.`aliments` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
