import streamlit as st
import pymongo
from pymongo import MongoClient
import pandas as pd

st.title("Census standardization")

client=MongoClient("mongodb+srv://jayasenthur:1234@cluster0.78ilsyt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").test.matches
db=client['census']
collection=db['census_collection']

page=st.sidebar.selectbox("Select Page",["Home","District","State"])

if page == "Home" :
    st.write("Use the sidebar to navigate between different collections")

elif page == "District" :
 st.header("Display Data districtwise")
 st.write("Districtwise data")

 col1, col2=st.columns(2)

 with col1 :
     if st.button("Clear", key="clear_page") :
      st.empty()
      st.experimental_rerun()

     if st.button("Population",key="districtwise_population") :
      data=list(collection.find())
      df=pd.DataFrame(data,columns=["District","Population"])
      st.dataframe(df)

     if st.button("Literates Male & Female",key="districtwise_male_female_literate"):
      data=list(collection.find())
      df=pd.DataFrame(data,columns=["District","Literate_Male","Literate_Female"])   
      st.dataframe(df)
    
     if st.button("Percentage of workers",key="percenatge_workers") : 
      data=list(collection.find())

     if st.button("LPG or PNG",key="lpg_png") :
      data=list(collection.find())
      df=pd.DataFrame(data,columns=["District","LPG_or_PNG_Households"])
      st.dataframe(df)

 with col2 :

   if st.button("Religious composition",key="religious_composition") :
    data=list(collection.find())
    df=pd.DataFrame(data,columns=["Hindus","Muslims","Christians"])
    st.dataframe(df)

   if st.button("Internet access",key="internet_access") :
    data=list(collection.find())
    df=pd.DataFrame(data,columns=["District","Households_with_Internet"])
    st.dataframe(df)

   if st.button("Edu attainment dist",key="edu_attain_disribution") :
    data=list(collection.find())
    df=pd.DataFrame(data,columns=["District","Below_Primary_Education", "Primary_Education", "Middle_Education", "Secondary_Education"])
    st.dataframe(df)

   if st.button("Modes of transport",key="modes_of_transport") :
    data=list(collection.find())
    df=pd.DataFrame(data,columns=["District","Households_with_Bicycle","Households_with_Car_Jeep_Van","Households_with_Radio_Transistor","Households_with_Television"])
    st.dataframe(df)

   if st.button("Cond. of census houses",key="condition_of_occupied_census_houses") :
    data=list(collection.find())
    df=pd.DataFrame(data,columns=["District","Condition_of_occupied_census_houses_Dilapidated_Households","Households_with_separate_kitchen_Cooking_inside_house","Having_bathing_facility_Total_Households","Having_latrine_facility_within_the_premises_Total_Households"])
    st.dataframe(df)


   if st.button("Household size distribution",key="household_size_distribution") :
    data=list(collection.find())
    df=pd.DataFrame(data,columns=["District","Household_size_1_person_Households","Household_size_2_persons_Households","Household_size_3_to_5_persons_Households"])
    st.dataframe(df)
       
elif page == "State" :
  st.header("Display data statewise")
  
  #st.write("Statewise data")

  col1, col2=st.columns(2)
  with col1 :
    if st.button("Clear",key="clear_page1") :
     st.empty()
     st.experimental_rerun()

    if st.button("Total Households",key="total_no_households") :
      data=list(collection.find())
      df=pd.DataFrame(data,columns=["State/UT","Households"])
      st.dataframe(df)
  
    if st.button("Latrine facility",key="latrine_facility") :
      data=list(collection.find())
      df=pd.DataFrame(data,columns=["State/UT","Having_latrine_facility_within_the_premises_Total_Households"])
      st.dataframe(df)
    
    if st.button("Avg household size",key="avg_households") :
      data=list(collection.find())


    if st.button("Owned households vs rent",key="own_rent") :
      data=list(collection.find())
      df=pd.DataFrame(data,columns=["State/UT","Ownership_Owned_Households","Ownership_Rented_Households"])
      st.dataframe(df)


    if st.button("Diff types of latrine facility",key="diff_types_latrine_facility") :
      data=list(collection.find())

    with col2 :
      if st.button("Access to drinking water",key="access_to_drinking_water") :
        data=list(collection.find())

      if st.button("Avg income distribution",key="avg_income_distribution") :
        data=list(collection.find())

      if st.button("Married couple with diff household size", key="married_couple_diff_household_size") :
        data=list(collection.find())

      if st.button("No. of households fall below poverty line",key="households_below_poverty") :
         data=list(collection.find())

      if st.button("Overall literacy rate",key="overall_literacyrate") :
         data=list(collection.find())


            


#mongoClient = MongoClient('mongodb://localhost:8501/')
#database_names = client.list_database_names()
#optmongo = st.selectbox('Choose the database',(database_names))
#my_db2 = mongoClient[optmongo]
#collection_list = my_db2.list_collection_names()
#optmongo2 = st.selectbox('Choose the collection',(collection_list))
#my_cols2 = my_db2.optmongo2



#def init_connection():
 #   return pymongo.MongoClient(**st.secrets["mongo"])


#client = init_connection()
#@st.cache_data(ttl=600)
#def get_data():
 #   db = client.census
  #  items = db.mycollection.find()
   # items = list(items)  # make hashable for st.cache_data
    #return items

#items = get_data()

# Title of the app


# Input fields for two numbers
#num1 = st.number_input("Enter first number", value=0)
#num2 = st.number_input("Enter second number", value=0)

# Calculate the sum
#sum_result = num1 + num2

#for item in items:
 #   st.write(f"{item['Population']} has a :{item['Jammu And Kashmir']}:")

# Display the result
#st.write(f"The sum of {num1} and {num2} is {sum_result}")