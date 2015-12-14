-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema BloodDonationStorage
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema BloodDonationStorage
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `BloodDonationStorage` DEFAULT CHARACTER SET utf8 ;
USE `BloodDonationStorage` ;

-- -----------------------------------------------------
-- Table `BloodDonationStorage`.`Event`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BloodDonationStorage`.`Event` (
  `Id` INT AUTO_INCREMENT PRIMARY KEY,
  `DateOfEvent` DATE NOT NULL,
  `StartTime` TIME NOT NULL,
  `EndTime` TIME NOT NULL,
  `ZipCode` INT NOT NULL,
  `City` VARCHAR(45) NOT NULL,
  `Address` VARCHAR(45) NOT NULL,
  `AvailableBeds` INT NOT NULL,
  `PlannedDonorNumber` INT NOT NULL,
  `Successfull` INT NOT NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BloodDonationStorage`.`Donor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BloodDonationStorage`.`Donor` (
  `UniqueId` VARCHAR(8) NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Weight` INT NOT NULL,
  `Gender` ENUM('M', 'F') NOT NULL,
  `DateOfBirth` DATE NOT NULL,
  `LastDonationDate` DATE NOT NULL,
  `Wassick` ENUM('Y', 'N') NOT NULL,
  `BloodType` ENUM('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', '0+', '0-') NOT NULL,
  `ExpofId` DATE NOT NULL,
  `Emailaddress` VARCHAR(45) NOT NULL,
  `Mobilnumber` VARCHAR(45) NOT NULL,
  `HemoglobinLevel` INT NOT NULL,
  PRIMARY KEY (`UniqueId`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
