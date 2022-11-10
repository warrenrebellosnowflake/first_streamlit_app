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

# Adding a pick list so users can select the fruit they want
streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index))

# Display table on page
streamlit.dataframe(my_fruit_list)
