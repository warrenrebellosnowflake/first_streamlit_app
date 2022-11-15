import streamlit

streamlit.title("My Parents New Healthy Diner")

streamlit.header("Breafast Menu")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocade Toast")

streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")


import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Adding a pick list so users can select the fruit they want
fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display table on page
streamlit.dataframe(fruits_to_show)


# New section to display Fruityvice API response
import requests
fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!!!")
#streamlit.text(fruityvice_response.json())

fruitvice_normalized = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruitvice_normalized)
