import streamlit
import pandas as pd
import requests
import snowflake.connector 
from urllib.error import URLError


streamlit.title("My Parents New Healthy Diner")

streamlit.header("Breafast Menu")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocade Toast")

streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")



my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Adding a pick list so users can select the fruit they want
fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display table on page
streamlit.dataframe(fruits_to_show)


# New section to display Fruityvice API response
fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response)

#streamlit.text(fruityvice_response.json())

fruitvice_normalized = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruitvice_normalized)

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/" + fruit_choice)
    fruitvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruitvice_normalized

  
#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!!!")
try:
    fruit_choice = streamlit.text_input("What fruit would you like information about?")
    if not fruit_choice:
        #streamlit.write("The user entered ", fruit_choice)
        streamlit.error("Please select a fruit to get information!")
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()
  


streamlit.header("View Our Fruit List - Add Your Favorutes!")
#Snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
        return my_cur.fetchall()

#Add a button to load the fruit
if streamlit.button('Get Fruit List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)





# Allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("INSERT INTO FRUIT_LOAD_LIST VALUES ('" + new_fruit + "')")
        return "Thanks for adding " + new_fruit

add_my_fruit = streamlit.text_input("What fruit would you like to add?") 
if streamlit.button('Add a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_button = insert_row_snowflake(add_my_fruit)
    my_cnx.close()
    streamlit.text(back_from_button)



# Don't run anything past here while we troubleshoot
streamlit.stop()

