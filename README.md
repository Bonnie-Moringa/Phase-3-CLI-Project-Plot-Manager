# Plot_Manager
### Project By Boniface Mburu
### Date 28 May 2025

## Introduction
This project is a command-line interface (CLI) tool built for managing data in a land-selling company. It uses SQLite as the backend database and offers features to add consultants, projects, and customers, as well as view existing projects and customers along with their associated information.

## Key Features
Database Management: Set up and manage a SQLite database (real_estate.db) to store information related to consultants, projects, and customers.

Consultant Management: Add new consultants by entering their name, contact number, email, and phone number.

Project Management: Create new project entries, assign them a status (sold or not sold), and link them to specific consultants.

Customer Management: Register customers who have purchased or reserved projects, connecting them with both the consultant and the relevant project.

View Operations: Access and display all projects along with their assigned consultants, and view a complete list of customers with their related consultants and projects.


## Project Structure
phase-3-project/ 
├── Pipfile 
├── Pipfile.lock 
├── README.md 
└── lib 
├── models │ 
├── __init__.py │ 
└── model_1.py 
├── cli.py 
├── config.py 
├── debug.py 
└── helpers.py 
├── db # Database directory (will be created)

## Installation and Usage
Installation: Clone the repository, install dependencies using Pipenv, and initialize the database.
Usage: Utilize the CLI commands provided (addagent, addproperty, addclient, viewproperties, viewclients) to manage agents, properties, and clients efficiently from the command line.

## Commands to run the project
Run pyhton lib/cli.py in the terminal
Choose one option from the ones provided

## Purpose
This tool offers an easy-to-use interface for managing real estate operations, allowing users to efficiently handle consultant details, project listings, customer registrations, and data access within a SQLite database. It's ideal for real estate professionals or agencies seeking a simple digital solution for organizing their workflows.

## Technologies used
-Python
-Sqlite
