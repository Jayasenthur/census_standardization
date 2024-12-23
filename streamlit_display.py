import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt


# Connect to the database
db_user = "root"
db_password = "root"
db_host = "localhost"
db_name = "census"
db_port = "3306"

connection_string = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(connection_string)

# Streamlit interface
st.title("Census Data Analysis")

# Example queries
queries = {
    "Total population of each district": """
        SELECT district, SUM(population) AS total_population 
        FROM census
        GROUP BY district;
    """,
    "Literate males and females in each district": """
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
    """,
    "Percentage of workers (male and female) in each district": """
        SELECT 
    District,
    ROUND((SUM(Male_Workers + Female_Workers) / SUM(Population)) * 100, 2) AS Workers_Percentage
FROM 
    census
GROUP BY 
    District;
    """,
    "No. of households have access to LPG or PNG as a cooking fuel in each district" : """
SELECT 
    `District` AS District_Name,
    SUM(`LPG_or_PNG_Households`) AS Households_With_LPG_PNG
FROM 
    census
GROUP BY 
    `District`;
""",
    "Religious composition of each district": """
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
    District;
    """,
    "No. of Households with internet access in each district": """
    SELECT District, SUM(LPG_or_PNG_Households) AS LPG_PNG_Households
FROM census
GROUP BY District;
""",
" Educational attainment distribution in each district": """
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
""",
"No. of Households access to various mode of transport":"""
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
""",
"Condition of occupied cenus houses in each district":"""
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
""",
"Household size distribution (1 person, 2 persons, 3-5 persons, etc.) in each district":"""
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
""",
"Total number of households in each state" :"""
SELECT 
    `State/UT` AS State,
    SUM(Households) AS Total_Households
FROM census
GROUP BY `State/UT`;

""",
"No. of Households have a latrine facility within the premises in each state":"""
SELECT 
    `State/UT` AS State_Name,
    SUM(`Having_latrine_facility_within_the_premises_Total_Households`) AS Households_With_Latrine_Facility
FROM 
    census
GROUP BY 
    `State/UT`;
""",
"Average household size in each state ": """
SELECT 
    `State/UT` AS State_Name,
    ROUND(AVG(`Households` / NULLIF(`Population`, 0)), 2) AS Average_Household_Size
FROM 
    census
GROUP BY 
    `State/UT`;
    """,
    "No. of owned households versus rented households in each state":"""
    SELECT 
    `State/UT` AS State_Name,
    SUM(`Ownership_Owned_Households`) AS Owned_Households,
    SUM(`Ownership_Rented_Households`) AS Rented_Households
FROM 
    census
GROUP BY 
    `State/UT`;
""",
"Distribution of different types of latrine facilities in each state" :"""
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
""",

"No. of households have access to drinking water sources near the premises in each state" : """
SELECT 
    `State/UT` AS State_Name,
    SUM(`Location_of_drinking_water_source_Near_the_premises_Households`) AS Households_Near_Water_Source
FROM 
    census
GROUP BY 
    `State/UT`;
""",
"Average household income distribution in each state based on the power parity categories" : """
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
""",
"Percentage of married couples with different household sizes in each state":"""
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
""",
"No. of households fall below the poverty line in each state based on the power parity categories" :"""
SELECT 
    `State/UT` AS State_Name,
    SUM(`Power_Parity_Less_than_Rs_45000`) AS Households_Below_Poverty_Line
FROM 
    census
GROUP BY 
    `State/UT`;
""",
"Overall literacy rate (percentage of literate population) in each state" : """
SELECT 
    `State/UT` AS State_Name,
    (SUM(`Literate`) / SUM(`Population`) * 100) AS Literacy_Rate_Percentage
FROM 
    census
GROUP BY 
    `State/UT`;
"""
    # Add more queries as required
}

# Query selection dropdown
query = st.selectbox("Select a Query", list(queries.keys()))

# Run the selected query and display results
if query:
    query_to_run = queries[query]
    try:
        # Fetch the data from the database
        df = pd.read_sql(query_to_run, engine)
        st.write(f"Results for: {query}")
        #st.write(df["District"])

          # Specific query check for charting
        if query == "Overall literacy rate (percentage of literate population) in each state":

            # Example: Plotting a bar chart for LPG or PNG households
            #plt.figure(figsize=(10, 6))
            plt.figure()
            plt.bar(df['State_Name'], df['Literacy_Rate_Percentage'])
            plt.xlabel('State')
            plt.ylabel('Literacy_Rate_Percent')
            plt.xticks(rotation=45,fontsize=4)
            plt.tight_layout()
            st.pyplot(plt)

                     

        # Add more specific query checks here if needed
        else:

         st.dataframe(df)  # Display the query result in a table format
    except Exception as e:
        st.error(f"Error fetching data: {e}")
