# Census Data Standardization and Analysis Pipeline

## Overview

This project focuses on cleaning, processing, and analyzing census data to ensure uniformity, accuracy, and accessibility. 

## Key functionalities

* **1. Data Acquisition :** Collect census data from structured files , read additional files (e.g., district lists for new states) and integrate them.
* **2. Data Cleaning :**  Renaming columns, standardizing State/UT names, and handling missing data.
* **3. Missing Data Handling :** Detect missing data percentages, Impute missing values using logical relationships (e.g., `Population = Male + Female)`.
* **4. State/UT Formation Handling :** Accounting for Telangana (2014) and Ladakh (2019) by processing district-specific changes.
* **5. Data Storage :** Saving processed data to MongoDB
* **6. Database Connection :** Fetching data from the mongoDB and uploading to a relational database using python code.
* **7. Querying and Visualization :** Executing queries and displaying results using Streamlit for user-friendly dashboards.
  
## Tasks covered 

* **Task 1:** Renaming columns for consistency.
* **Task 2:** Standardizing State/UT names.
* **Task 3:** Handling new State/UT formations (Telangana, Ladakh).
* **Task 4:** Processing missing data with logical computations.
* **Task 5:** Saving the cleaned data to MongoDB.
* **Task 6:** Uploading data to relational databases

## Technologies Used

## Python

* **Role :**  Python serves as the backbone of the project, orchestrating all the tasks from data cleaning to visualization.
* **How It’s Used:**
  * Reading census data from files (CSV, TXT, etc.).
  * Automating data cleaning tasks, such as renaming columns, formatting State/UT names, and processing missing data.
  * Implementing conditional logic for specific tasks, such as splitting states based on historical changes.
  * Establishing connections with databases (MongoDB and relational databases).
  * Writing queries for analysis and running them programmatically.
 
## Pandas

* **Role :** Pandas is used for data manipulation and processing.
* **How It’s Used:**
  * `Data Cleaning`: Renaming columns, standardizing data formats, and handling missing values.
  * `Analysis`: Performing aggregations (e.g., total population, literacy rates) and deriving insights like household distributions and age groups.
  * `Validation`: Verifying calculations like the total population by summing subsets (e.g., male + female).
  * `Exporting Data`: Preparing the cleaned and processed data for storage in MongoDB or a relational database.

## SQL

* **Role :** SQL is used for structured data storage, querying, and analysis.
* **How It’s Used:**
  * 






