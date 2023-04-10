import streamlit as st
from PIL import Image
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("Projects & Accomplishments")

st.write('\n')
st.write(
    """
All of the projects  created during my learning proccess to obtain knowledge - strong foundations on OOP programming
 are stored on my personal GitHub.
Bellow you can find some projects that I'm really proud of and showcase my knowledge on Java Backend and FrontEnd developpement.
"""
)
st.write('\n')
# --- Anti Fraud  ---
st.subheader("1️⃣ Anti Fraud System")
st.write("https://github.com/ngalinos95/Anti-Fraud-System")
st.write('\n')
st.write("Features")
st.write(
    """
- 🔹 Authenitication
- 🔹 Authorization
- 🔹 Databases
- 🔹 Transactional Operations
- 🔹 Spring Beans, Components and Configurations
- 🔹 Project Lombok
- 🔹 Exceptions
"""
)
st.write('\n')

st.write(
    """
This project demonstrates (in a simplified form) the principles of anti-fraud systems in the financial sector. The system contains an expanded role model, a set of REST endpoints responsible for interacting with users, and an internal transaction validation logic based on a set of heuristic rules.
Transaction Validation
This Anti-fraud System consists of the following validations:
Heuristics rules that prevents fraudsters from illegally transferring money from an account.
Card number and Ip Address (IPv4) block list.
Rule-based system (Ip Address/Regions correlation). 
"""
)


st.write('\n')


# --- Restaurant  ---
st.subheader("2️⃣ Recipes Rest API")
st.write("https://github.com/ngalinos95/Anti-Fraud-System")
st.write('\n')
st.write("Features")
st.write(
    """
- 🔹 Authenitication
- 🔹 Authorization
- 🔹 Databases
- 🔹 Transactional Operations
- 🔹 Spring Beans, Components and Configurations
- 🔹 Project Lombok
"""
)
st.write('\n')

st.write(
    """
The project is a RESTful API with implementation of 
SpringBoot and Spring Security framework updating deliting and creating new entries
 on a H2 database base based on USERS autorization and authentication.The USERS information will 
 be stored on the H2 database with the user being able to create new users whose passwords are stored encrypted
"""
)
st.write('\n')

# --- Cinema  ---
st.subheader("3️⃣ Cinema Room Rest Service")
st.write("https://github.com/ngalinos95/CinemaREST")
st.write('\n')
st.write("Features")
st.write(
    """
- 🔹 Databases
- 🔹 JSON 
- 🔹 Spring REST
- 🔹 Project Lombok
- 🔹 Spring Boot
"""
)
st.write('\n')

st.write(
    """
Always wanted to have your private movie theater and screen only the movies you like? 
You can buy a fancy projector and set it up in a garage, but how can you sell tickets? 
Having a booth is old-fashioned, so let's create a special service for that! Make good use of 
Spring and write a REST service that can show the available seats, sell and refund tickets,
 and display the statistics of your venue. Pass me the popcorn, please!
In this project, I learned how to create a simple Spring REST service that will help you manage a small movie theatre. 
Handle HTTP requests in controllers, create services and respond with JSON objects.
"""
)
st.write('\n')

# --- Car  ---
st.subheader("4️⃣ Car Sharing Service")
st.write("https://github.com/ngalinos95/CarSharing")
st.write("Features")
st.write(
    """
- 🔹 Databases SQL H2 and DAO patterns
- 🔹 JDBC 
- 🔹 SQL Querries
- 🔹 ArrayLists and Arrays manipulation
- 🔹 Read and write files form local file path
"""
)
st.write('\n')

st.write(
    """
During the project implementation, I use the basics of SQL and work with the H2 database. 
Use of advanced Java features such as Collections.

Car-sharing is becoming a more and more popular green alternative to owning a car. 
Let's create a program that manages a car-sharing service allowing 
companies to rent out their cars and find customers.
"""
)
st.write('\n')

# --- Calculator  ---
st.subheader("5️⃣ Simple Calcucaltor")
st.write("https://github.com/ngalinos95/Calculator")
st.write("Features")
st.write(
    """
- 🔹 SQLite databases
- 🔹 Swing GUI framework 
- 🔹 Exceptions
- 🔹 ArrayLists and Arrays manipulation
- 🔹 Read and write files form local file path
"""
)
st.write('\n')

st.write(
    """
A simple calculator app with GUI build on Swing Framework with Java
"""
)
image1 = Image.open('proj/image1.png')
st.image(image1,width=400)


st.write('\n')

# --- SQLite Viwer  ---
st.subheader("6️⃣ SQL Viewer")
st.write("https://github.com/ngalinos95/SQLViewer")
st.write("Features")
st.write(
    """
- 🔹 Strong OOP use with many obj and classes
- 🔹 Strong OOP use with many obj and classes
- 🔹 Swing GUI framework 
- 🔹 Exceptions
- 🔹 ArrayLists and Arrays manipulation
"""
)
st.write('\n')

st.write(
    """
A swing SQLite database viewer ,used to read two distinct given(or any given local database) 
database files Example firstDatabase.db secondDatabase.db extracting the data from the SQL 
database and presenting them in a table format with a GUI using the Swing Framework in Java"""
)
st.write('\n')

image2 = Image.open('proj/image2.png')
st.image(image2, width=600)
