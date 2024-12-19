# Census Data Standardization and Analysis Pipeline

## Overview

This project focuses on cleaning, processing, and analyzing census data to ensure uniformity, accuracy, and accessibility. 

## Key functionalities

* **1. Data Cleaning :**  Renaming columns, standardizing State/UT names, and handling missing data.
* **2. Missing Data Handling :** Detect missing data percentages, Impute missing values using logical relationships (e.g., `Population = Male + Female)`.
* **3. State/UT Formation Handling :** Accounting for Telangana (2014) and Ladakh (2019) by processing district-specific changes.
* **4. Data Storage :** Saving processed data to MongoDB
* **5. Database Connection :** Fetching data from the mongoDB and uploading to a relational database using python code.
* **6. Querying and Visualization :** Executing queries and displaying results using Streamlit for user-friendly dashboards.
  
## Tasks covered 

* **Task 1:** Renaming columns for consistency.
* **Task 2:** Standardizing State/UT names.
* **Task 3:** Handling new State/UT formations (Telangana, Ladakh).
* **Task 4:** Processing missing data with logical computations.
* **Task 5:** Saving the cleaned data to MongoDB.
* **Task 6:** Uploading data to relational databases

## Technologies Used

* **Python**
* **Pandas**
* **SQL**
* **MongoDB**
* **Streamlit**


