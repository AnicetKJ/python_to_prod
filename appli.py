import streamlit as st

# Je découvre d'abord toutes les fonctionnalités de Streamlit
st.title("WIDGETS DE STREAMLIT")
st.write("Voici une liste de widgets de Streamlit")
st.write("Cliquez sur les boutons pour les voir en action")

data = "Hello, world!"
st.button("Click me")
st.download_button("Download file", data, file_name="data.txt")
st.link_button("Google", url="https://www.google.com")
st.page_link("appli.py", label="Home")
# st.data_editor("Edit data", data)
st.checkbox("I agree")
st.feedback("thumbs")
st.pills("Tags", ["Sports", "Politics"])
st.radio("Pick one", ["cats", "dogs"])
st.segmented_control("Filter", ["Open", "Closed"])
st.toggle("Enable")
st.selectbox("Pick one", ["cats", "dogs"])
st.multiselect("Buy", ["milk", "apples", "potatoes"])
st.slider("Pick a number", 0, 100)
st.select_slider("Pick a size", ["S", "M", "L"])
st.text_input("First name")
st.number_input("Pick a number", 0, 10)
st.text_area("Text to translate")
st.date_input("Your birthday")
st.time_input("Meeting time")
st.file_uploader("Upload a CSV")
st.audio_input("Record a voice message")
st.camera_input("Take a picture")
st.color_picker("Pick a color")

# ON CONTINUE
# Magic commands implicitly
# call st.write().
"_This_ is some **Markdown**"
my_variable = "ma variable"
"dataframe:" + my_variable
st.write("dataframe:" + my_variable)

# suivant

st.write(["st", "is <", 3])
# st.write_stream(my_generator)
# st.write_stream(my_llm_stream)

# Use widgets' returned values in variables:
for i in range(int(st.number_input("Num:"))):
    st.write(f"num: {i}")
if st.sidebar.selectbox("Sexe:",["M","F"]) == "F":
    st.write("FEMALE")
else:
    print("else")
my_slider_val = st.slider("Quinn Mallory", 1, 8)
st.write(f"Quinn Mallory: {my_slider_val}")

# Disable widgets to remove interactivity:
st.slider("Pick a number", 0, 10, disabled=True)

import numpy as np
# Insert a chat message container.
with st.chat_message("user"):
    st.write("Yo bro, ca dit quoi aujourdhui? 👋")
    st.chat_input("Ne reponds pas alors 😒")

# Display a chat input widget at the bottom of the app.
# st.chat_input("Say something")
 
# Display a chat input widget inline
