import streamlit as st
from PIL import Image  # Import Image from Pillow


st.title("Hello Everyone")

st.header("WELCOME")
st.subheader("TO OUR PAGE")
st.text("wel welcome")
st.markdown('### This is a markdown')
st.success("Success")

st.info("Information")

st.warning("Warning")

st.error("Error")

exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)


st.write("Text with write")
st.write(range(10))

if st.checkbox("Show/Hide"):
    st.text("Showing the widget")
    
status = st.radio("Select Gender:", ['Male', 'Female'])

if status == 'Male':
    st.success("Male")
else:
    st.success("Female")
    
    
    
# For Image
img = Image.open("streamlit.png") # Open the image file
st.image(img, width=200) # Display the image with a specified width
    
    
hobby = st.selectbox("Select a Hobby:", ['Dancing', 'Reading', 'Sports'])

st.write("Your hobby is:", hobby)


hobbies = st.multiselect("Select Your Hobbies:", ['Dancing', 'Reading', 'Sports'])

st.write("You selected", len(hobbies), "hobbies")

st.button("Click Me")

if st.button("About"):
    st.text("Welcome to GeeksForGeeks!")
    
name = st.text_input("Enter your name", "Type here...")

if st.button("Submit"):
    result = name.title()  
    st.success(result)
    
level = st.slider("Choose a level", min_value=1, max_value=5)


st.write(f"Selected level: {level}")