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

  ### Pipeline Diagram
  
```plaintext
+-----------------+      +------------------+      +-------------------+
|   Raw Data      | ---> | Data Cleaning    | ---> | Data Transformation|
+-----------------+      +------------------+      +-------------------+
                                 |
                                 v
                       +-------------------+
                       |  Data Validation  |
                       +-------------------+
                                 |
                                 v
                       +-------------------+
                       | Data Storage/DB   |
                       +-------------------+
                                 |
                                 v
                       +-------------------+
                       | Analysis /        |  
                       |  Visualization    |
                       +-------------------+

```

---

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
  * `Relational Database Storage`: Data from MongoDB collections is uploaded to SQL-based relational databases (e.g., MySQL).
  * `Querying`: Running the project-specific queries to extract insights like population distribution, literacy rates, and household conditions.
  * `Streamlit Integration`: SQL queries are executed in Python, and results are displayed via Streamlit.
 
## MongoDB

* **Role :** MongoDB acts as the initial data storage layer for unstructured or semi-structured data.
* **How It’s Used:**
 * `Storing Processed Data`: Processed census data is saved as a MongoDB collection named `census`.
 *  `Data Retrieval`: MongoDB serves as the source for transferring data to a relational database.

## Streamlit

* **Role :** Streamlit provides the user interface for interaction, data visualization, and displaying query results.
* * **How It’s Used:**
  * `Visualization`: Charts, tables, and graphs are displayed for insights like household size distribution or population breakdown.
  * `Query Execution`: Users select predefined queries, and the app fetches and displays the results dynamically.
  * `User Interaction`: Input options allow users to explore different aspects of the census data (e.g., filtering by district or state).
  * `Real-Time Results`: Displays query outputs and visualizations in an intuitive dashboard format.

This combination of technologies ensures the project efficiently handles the entire workflow—from data cleaning and analysis to visualization.

## Libraries to install
```bash
!python -m pip install pymongo --upgrade
!pip install pandas
!pip install mysql-connector-python
!pip install streamlit
!pip install sqlalchemy
```
## Data Cleaning, Modifying, and Processing

### Purpose 
The aim is to ensure the census data is accurate, uniform, and ready for analysis. This involves cleaning inconsistent values, standardizing formats, and handling missing data while adhering to business rules.

### Task 1 : Column Renaming for Consistency

 * Renamed columns to maintain uniformity across datasets.
 * Ensured column names adhere to character length limits (max 60 characters).
 * Updated column names:
  - `State name` → `State_UT`
  - `District name` → `District`
  - `Male_Literate` → `Literate_Male`
  - `Female_Literate` → `Literate_Female`
  - `Rural_Households` → `Households_Rural`
  - `Urban_Households` → `Households_Urban`
  - `Age_Group_0_29` → `Young_and_Adult`
  - `Age_Group_30_49` → `Middle_Aged`
  - `Age_Group_50` → `Senior_Citizen`
  - `Age not stated` → `Age_Not_Stated`

### Examples

| Original Column Name        | Updated Column Name     |
|-----------------------------|-------------------------|
| State name                  | State_UT                |
| District name               | District                |
| Male_Literate               | Literate_Male           |
| Female_Literate             | Literate_Female         |
| Rural_Households            | Households_Rural        |
| Urban_Households            | Households_Urban        |
| Age_Group_0_29              | Young_and_Adult         |
| Age_Group_30_49             | Middle_Aged             |
| Age_Group_50                | Senior_Citizen          |
| Age not stated              | Age_Not_Stated          |

### Code Example
```python
import pandas as pd

df=pd.read_csv("census_2011.csv")

# Task 1: Rename the Column names
change_column_name={
  'State name': 'State/UT',
  'District name': 'District',
  'Male_Literate': 'Literate_Male',
  'Female_Literate': 'Literate_Female',
  'Rural_Households': 'Households_Rural',
  'Urban_ Households': 'Households_Urban',
  'Age_Group_0_29': 'Young_and_Adult',
  'Age_Group_30_49': 'Middle_Aged',
  'Age_Group_50': 'Senior_Citizen',
  'Age not stated': 'Age_Not_Stated'
}
df.rename(columns=change_column_name,inplace=True)

```

### Task 2 : State/UT Name Standardization

* Converted all-uppercase State/UT names to title case, ensuring only the first letter of each word is capitalized.
* Replaced the `&` symbol with "and" for uniformity.
* Ensured the word "and" is always in lowercase, irrespective of its position in the name.

## Examples

| Original Name                | Standardized Name          |
|------------------------------|----------------------------|
| ANDAMAN & NICOBAR ISLANDS    | Andaman and Nicobar Islands|
| ARUNACHAL PRADESH            | Arunachal Pradesh          |
| BIHAR                        | Bihar                      |

### Code Example
```python
import pandas as pd
df=pd.read_csv("census_2011.csv")

# Task 2: Rename State/UT Names
def Capitalization(df):
    for i in range(len(df)):
        x = df.loc[i,'State/UT'].lower().split()
        for j in range(len(x)):
            if x[j] != 'and':
                x[j] = x[j].capitalize()
        df.loc[i,'State/UT'] = " ".join(x)

Capitalization(df)
```

## Task 3: New State/UT Formation

* Accounted for the formation of new states/UTs from parent states/UTs based on the census year.
* Updated State/UT names for the relevant districts as follows:
  - **Telangana Formation (2014)**: Renamed `Andhra Pradesh` to `Telangana` for districts listed in `Data/Telangana.txt`.
  - **Ladakh Formation (2019)**: Renamed `Jammu and Kashmir` to `Ladakh` for the districts `Leh` and `Kargil`.

### Examples

| Original State/UT Name      | District          | Updated State/UT Name  | 
|-----------------------------|-------------------|------------------------|
| Andhra Pradesh              | Hyderabad         | Telangana              |
| Jammu and Kashmir           | Leh               | Ladakh                 |
| Jammu and Kashmir           | Kargil            | Ladakh                 |

### Code Example
```python
import pandas as pd
df=pd.read_csv("census_2011.csv")

# Task 3: New State/UT formation
with open('Telangana.txt', 'r') as telangana:
    telangana_districts = telangana.read()
telangana_districts = telangana_districts.split("\n")

# setting the values as Telangana if the districts are in the telangana_districts list
def telangana(df):
    for i in range(len(df)):
        if df.loc[i,'District'] in telangana_districts:
            df.loc[i,'State/UT'] = "Telangana"

telangana(df)

# setting the values as Ladakh if the districts are in the ladakh list
def ladakh(df):
    ladakh = ['Leh', 'Kargil']
    for district in ladakh:
        for i in range(len(df)):
            if district in df.loc[i,'District']:
                df.loc[i,'State/UT'] = "Ladakh"

ladakh(df)
```
## Task 4: Find and Process Missing Data

* Identified and calculated the percentage of missing data for each column.
* Applied data-filling techniques using information from other cells to infer missing values.
* Updated formulas for filling missing data:
  - **Population** = `Male + Female`
  - **Literate** = `Literate_Male + Literate_Female`
  - **Population** = `Young_and_Adult + Middle_Aged + Senior_Citizen + Age_Not_Stated`
  - **Households** = `Households_Rural + Households_Urban`
* Compared the percentage of missing data before and after the data-filling process.

### Examples

| Column Name       | Missing Data (Before) | Missing Data (After) |
|-------------------|-----------------------|----------------------|
| Population        | 10%                   | 0%                   |
| Literate          | 5%                    | 0%                   |
| Households        | 8%                    | 0%                   |

## Task 5: Save Data to MongoDB

* Saved the processed data to MongoDB for persistent storage and analysis.
* The data is stored in a database named `census_db` with a collection named `census`.


### Code Example
```python
import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Load CSV file
df = pd.read_csv("cleandata.csv")

# MongoDB Connection URI
uri = "mongodb+srv://jayasenthur:1234@cluster0.78ilsyt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to MongoDB
client = MongoClient(uri, server_api=ServerApi('1'))

# Test MongoDB connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit()

# Define Database and Collection
db = client['census_db']
collection = db['census']

# Insert Data into MongoDB
try:
    if not df.empty:
        records = df.to_dict(orient='records')
        collection.insert_many(records)
        print(f"Inserted {len(records)} records into MongoDB.")
    else:
        print("No data to insert into MongoDB.")
except Exception as e:
    print(f"Error inserting data into MongoDB: {e}")
```
## Task 6: Database Connection and Data Upload

* Retrieved data from MongoDB and uploaded it to a relational database MySQL.
* Used the file name (without extension) as the table name in the relational database.
* Added primary and foreign key constraints wherever necessary.
```python
# Retrieve Data from MongoDB
try:
    print("\nRecords from MongoDB:")
    mongo_data = list(collection.find({}, {'_id': 0}))  # Exclude '_id' from MongoDB documents
    df = pd.DataFrame(mongo_data)  # Convert to DataFrame
    if '_id' in df.columns:
     df = df.drop(columns=['_id'])

    if df.empty:
        print("No data found in MongoDB.")
    
except Exception as e:
    print(f"Error fetching records from MongoDB: {e}")

    # Dictionary to renaming columns which length are more than 65
column_rename_map = {
    'Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car': 'Households_TV_Computer_Laptop_Telephone_mobile_phone_Scooter_Car',
    #----------------------------
    'Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households':'Type_of_latrine_facility_Night_soil_disposed_into_open_drain',
    #----------------------------
    'Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households':'Type_of_latrine_Flush_pour_connected_to_other_system_Households',
    #----------------------------
    'Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households':'Not_having_latrine_within_premises_Other_source_Open_Households',
    #----------------------------
    'Main_source_of_drinking_water_Handpump_Tubewell_Borewell_Households':'Source_of_drinking_water_Handpump_Tubewell_Borewell_Households',
    #----------------------------
    'Main_source_of_drinking_water_Other_sources_Spring_River_Canal_Tank_Pond_Lake_Other_sources__Households':'Drinking_water_Spring_River_Canal_Tank_Pond_Lake_Other_Household'
    
}

df = df.rename(columns=column_rename_map)

# MySQL Connection Setup
mysql_user = "root"
mysql_password = "root"  # Replace with your MySQL password
mysql_host = "localhost"
mysql_db = "census"  # Replace with your MySQL database name

# Create SQLAlchemy engine to interact with MySQL
engine = create_engine(f'mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}')

# Create the database if not exists
try:
    connection = mysql.connector.connect(user=mysql_user, password=mysql_password, host=mysql_host)
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {mysql_db};")
    connection.commit()
    cursor.close()
except Exception as e:
    print(f"Error creating database in MySQL: {e}")

# Upload the DataFrame to MySQL
if not df.empty:
    try:
        df.to_sql('census', con=engine, if_exists='replace', index=False)
        print("Data uploaded to MySQL database successfully.")
    except Exception as e:
        print(f"Error uploading data to MySQL: {e}")
else:
    print("No data to insert into MySQL.")
```
## Task 7 : Run Query on the database and show output on streamlit

* **1. What is the total population of each district?**
  ```sql
  SELECT district, SUM(population) AS total_population 
        FROM census
        GROUP BY district;
  ```
* **2. How many literate males and females are there in each district?**
```sql
SELECT 
    District,
    SUM(Male) AS Total_Male,
    SUM(Female) AS Total_Female,
    SUM(Literate_Male) AS Literate_Male,
    SUM(Literate_Female) AS Literate_Female
FROM 
    census
GROUP BY 
    District;
```
* **3. What is the percentage of workers (both male and female) in each district?**
```sql
SELECT 
    District,
    ROUND((SUM(Male_Workers + Female_Workers) / SUM(Population)) * 100, 2) AS Workers_Percentage
FROM 
    census
GROUP BY 
    District;
```
* **4. How many households have access to LPG or PNG as a cooking fuel in each district?**
```sql
SELECT 
    `District` AS District_Name,
    SUM(`LPG_or_PNG_Households`) AS Households_With_LPG_PNG
FROM 
    census
GROUP BY 
    `District`;
```
* **5. What is the religious composition (Hindus, Muslims, Christians, etc.) of each district?**
```sql
SELECT 
    District,
    SUM(Hindus) AS Hindus,
    SUM(Muslims) AS Muslims,
    SUM(Christians) AS Christians,
    SUM(Sikhs) AS Sikhs,
    SUM(Buddhists) AS Buddhists,
    SUM(Jains) AS Jains,
    SUM(Others_Religions) AS Other_Religions,
    SUM(Religion_Not_Stated) AS Religions_Not_Stated
FROM 
    census
GROUP BY 
    District
```
* **6. How many households have internet access in each district?**
```sql
SELECT District, SUM(Households_with_Internet) AS LPG_PNG_Households
FROM census
GROUP BY District;
```
* **7. What is the educational attainment distribution (below primary, primary, middle, secondary, etc.) in each district?**
```sql
SELECT 
    `District` AS District_Name,
    SUM(`Below_Primary_Education`) AS Below_Primary,
    SUM(`Primary_Education`) AS PrimaryEducation,
    SUM(`Middle_Education`) AS Middle,
    SUM(`Secondary_Education`) AS SecondaryEducation,
    SUM(`Higher_Education`) AS Higher,
    SUM(`Graduate_Education`) AS Graduate,
    SUM(`Other_Education`) AS Other
FROM 
    census
GROUP BY 
    `District`;
```

* **8. How many households have access to various modes of transportation (bicycle, car, radio, television, etc.) in each district?**
```sql
SELECT 
    `District` AS District_Name,
    SUM(`Households_with_Bicycle`) AS Bicycle,
    SUM(`Households_with_Car_Jeep_Van`) AS Car_Jeep_Van,
    SUM(`Households_with_Radio_Transistor`) AS Radio_Transistor,
    SUM(`Households_with_Television`) AS Television,
    SUM(`Households_with_Scooter_Motorcycle_Moped`) AS Scooter_Motorcycle_Moped
FROM 
    census
GROUP BY 
    `District`;
```

* **9. What is the condition of occupied census houses (dilapidated, with separate kitchen, with bathing facility, with latrine facility, etc.) in each district?**
```sql
SELECT 
    `District` AS District_Name,
    SUM(`Condition_of_occupied_census_houses_Dilapidated_Households`) AS Dilapidated_Houses,
    SUM(`Households_with_separate_kitchen_Cooking_inside_house`) AS Separate_Kitchen,
    SUM(`Having_bathing_facility_Total_Households`) AS Bathing_Facility,
    SUM(`Having_latrine_facility_within_the_premises_Total_Households`) AS Latrine_Facility
FROM 
    census
GROUP BY 
    `District`;
```

* **10. How is the household size distributed (1 person, 2 persons, 3-5 persons, etc.) in each district?**
```sql
SELECT 
    `District` AS District_Name,
    SUM(`Household_size_1_person_Households`) AS One_Person_Households,
    SUM(`Household_size_2_persons_Households`) AS Two_Person_Households,
    SUM(`Household_size_3_to_5_persons_Households`) AS Three_to_Five_Person_Households,
    SUM(`Household_size_6_8_persons_Households`) AS Six_to_Eight_Person_Households,
    SUM(`Household_size_9_persons_and_above_Households`) AS Nine_or_More_Person_Households
FROM 
    census
GROUP BY 
    `District`;
```

* **11. What is the total number of households in each state?**
```sql
SELECT 
    `State/UT` AS State,
    SUM(Households) AS Total_Households
FROM census
GROUP BY `State/UT`;
```

* **12.How many households have a latrine facility within the premises in each state?**
```sql
SELECT 
    `State/UT` AS State_Name,
    SUM(`Having_latrine_facility_within_the_premises_Total_Households`) AS Households_With_Latrine_Facility
FROM 
    census
GROUP BY 
    `State/UT`;
```

* **13. What is the average household size in each state?**
```sql
SELECT 
    `State/UT` AS State_Name,
    ROUND(AVG(`Households` / NULLIF(`Population`, 0)), 2) AS Average_Household_Size
FROM 
    census
GROUP BY 
    `State/UT`;
```

* **14. How many households are owned versus rented in each state?**
```sql
SELECT 
    `State/UT` AS State_Name,
    SUM(`Ownership_Owned_Households`) AS Owned_Households,
    SUM(`Ownership_Rented_Households`) AS Rented_Households
FROM 
    census
GROUP BY 
    `State/UT`;
```

* **15. What is the distribution of different types of latrine facilities (pit latrine, flush latrine, etc.) in each state?**
```sql
SELECT 
    `State/UT` AS State_Name,
    SUM(`Type_of_latrine_facility_Pit_latrine_Households`) AS Pit_Latrine_Households,
    SUM(`Type_of_latrine_Flush_pour_connected_to_other_system_Households`) AS Flush_Latrine_Households,
    SUM(`Type_of_latrine_facility_Other_latrine_Households`) AS Other_Latrine_Households,
    SUM(`Type_of_latrine_facility_Night_soil_disposed_into_open_drain`) AS Night_Soil_Disposal_Households
FROM 
    census
GROUP BY 
    `State/UT`;
```

* **16. How many households have access to drinking water sources near the premises in each state?**
```sql
SELECT 
    `State/UT` AS State_Name,
    SUM(`Location_of_drinking_water_source_Near_the_premises_Households`) AS Households_Near_Water_Source
FROM 
    census
GROUP BY 
    `State/UT`;
```

* **17. What is the average household income distribution in each state based on the power parity categories?**
```sql
SELECT 
    `State/UT` AS State_Name,
    AVG(`Power_Parity_Less_than_Rs_45000`) AS Avg_Less_Than_45000,
    AVG(`Power_Parity_Rs_45000_90000`) AS Avg_45000_to_90000,
    AVG(`Power_Parity_Rs_90000_150000`) AS Avg_90000_to_150000,
    AVG(`Power_Parity_Rs_150000_240000`) AS Avg_150000_to_240000,
    AVG(`Power_Parity_Rs_240000_330000`) AS Avg_240000_to_330000,
    AVG(`Power_Parity_Rs_330000_425000`) AS Avg_330000_to_425000,
    AVG(`Power_Parity_Rs_425000_545000`) AS Avg_425000_to_545000,
    AVG(`Power_Parity_Above_Rs_545000`) AS Avg_Above_545000
FROM 
    census
GROUP BY 
    `State/UT`;
```

* **18. What is the percentage of married couples with different household sizes in each state?**
```sql
SELECT 
    `State/UT` AS State_Name,
    ROUND(SUM(`Married_couples_1_Households`) * 100.0 / SUM(`Households`), 2) AS Percent_1_Couple,
    ROUND(SUM(`Married_couples_2_Households`) * 100.0 / SUM(`Households`), 2) AS Percent_2_Couples,
    ROUND(SUM(`Married_couples_3_Households`) * 100.0 / SUM(`Households`), 2) AS Percent_3_Couples,
    ROUND(SUM(`Married_couples_3_or_more_Households`) * 100.0 / SUM(`Households`), 2) AS Percent_3_or_More_Couples,
    ROUND(SUM(`Married_couples_None_Households`) * 100.0 / SUM(`Households`), 2) AS Percent_No_Couples
FROM 
    census
GROUP BY 
    `State/UT`;
```

* **19. How many households fall below the poverty line in each state based on the power parity categories?**
```sql
SELECT 
    `State/UT` AS State_Name,
    SUM(`Power_Parity_Less_than_Rs_45000`) AS Households_Below_Poverty_Line
FROM 
    census
GROUP BY 
    `State/UT`;
```

* **20. What is the overall literacy rate (percentage of literate population) in each state?**
```sql
SELECT 
    `State/UT` AS State_Name,
    (SUM(`Literate`) / SUM(`Population`) * 100) AS Literacy_Rate_Percentage
FROM 
    census
GROUP BY 
    `State/UT`;
```
