import streamlit as st
from PIL import Image
import os
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("Certifications")

image1 = Image.open('certmain/image1.png')
image2 = Image.open('certmain/image2.png')

col1, col2 = st.columns(2)
with col1:
    st.image(image1, use_column_width=True)
with col2:
    st.image(image2, use_column_width=True)

    st.write('\n')
    st.write('\n')
st.write(
    """
After the completion of 2 large courses on Hyperskill in collaboration with JetBrains Academy 
I've completed more than 13 hands on projects on Java Obect Oriented Programing and solved 600 topics with questions and problems 
focusing on BackEnd practices - FrontEnd applications with Swing Framework and reinforced practices on Spring Framework and Spring Security
All of the projects are on my Github portfolio!.
"""
)
st.write('\n')
st.write('\n')
st.subheader("Learned Skills")
st.write(
    """
- ► OOP programming
- ► Data Structures and Design Patterns
- ► Clean Code Practices
- ► Python Programming Language skills
- ► Java Programming Language skills
- ► Streamlit Framework on Python
- ► Spring Framework - Spring Boot -Spring Security (Java BackEnd Frameworks)
- ► Swing Framework - (Java FrontEnd GUI Framework)
- ► Fundamental knowledge of CI/CD solutions, Git and GitHub
"""
)





# --- CERT & QUALIFICATIONS ---
st.write('\n')
st.write('\n')
st.subheader("Certifications obtained")
st.write(
    """
- ✅ Spring Securtity for Java Backend Developers : JetBrains Academy :https://hyperskill.org/certificates/6769fa79-49e9-46d8-ba9a-5fe4247f6fd0.pdf
- ✅ Java Backend Developper : JetBrains Acadmey : https://hyperskill.org/certificates/85cf605b-91a9-4c35-9fd8-83ba3b9d1a10.pdf
- ✅ Java Spring : Test Dome : https://www.testdome.com/certificates/4950e8979b724e47928f1797aa35ac87
- ✅ Java Spring Boot : Test Dome : https://www.testdome.com/certificates/1b3bf81368cd46ae9b836252bb742bcd
- ✅ Create REST APIs with Spring and Java : Codecademy : https://www.codecademy.com/profiles/ngal95/certificates/60f1edf0ac9368001c6025c4
- ✅ Problem Solving : HackerRank : https://www.hackerrank.com/certificates/d40ffcff7d1c
- ✅ Software Testing Foundations Test Techniques : LinkedIn : https://shorturl.at/twDX6
- ✅ Java Skill Certification : HackerRank : https://www.hackerrank.com/certificates/e54013a9830b
- ✅ Learn Java Course : Codecademy : https://www.codecademy.com/profiles/ngal95/certificates/d3f89367b558583e361640f778191345
- ✅ Pass the Technical Interview with Java: Codecademy : https://www.codecademy.com/profiles/ngal95/certificates/5f29ae1fc9647d0013a7284b
- ✅ Data Structures & Algorithms in Python : Udacity : 
- ✅ Git Tutorail : Great Learning : https://olympus1.mygreatlearning.com/course_certificate/TZRHUJHR
- ✅ Java for Programmers Course : Codecademy : https://www.codecademy.com/profiles/ngal95/certificates/90966026f83232720c6d04c056fb3360
- ✅ Python Skill Certification : HackerRank : https://www.hackerrank.com/certificates/iframe/a5dd21aa5511
- ✅ Learn the Command Line  : Codecademy : https://www.codecademy.com/profiles/ngal95/certificates/c87ba0541f8be78bc2f4ba1128233f6f
"""
)






# --- CERTIFICATIONS PNG SECTION ---
st.write('\n')
st.subheader("CERTIFICATIONS")
st.write("---")

image_folder = 'cert'
images = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith('.png')]

def resize_image(image, width=800, height=650):
    img = Image.open(image)
    img = img.resize((width, height))
    return img

col1, col2, col3 = st.columns(3)

with col1:
    st.image(resize_image(images[0]), use_column_width=True)

with col2:
    st.image(resize_image(images[1]), use_column_width=True)

with col3:
    st.image(resize_image(images[2]), use_column_width=True)

col4, col5, col6 = st.columns(3)

with col4:
    st.image(resize_image(images[3]), use_column_width=True)

with col5:
    st.image(resize_image(images[4]), use_column_width=True)

with col6:
    st.image(resize_image(images[5]), use_column_width=True)

col7, col8, col9 = st.columns(3)

with col7:
    st.image(resize_image(images[6]), use_column_width=True)

with col8:
    st.image(resize_image(images[7]), use_column_width=True)

with col9:
    st.image(resize_image(images[8]), use_column_width=True)

col10, col11, col12 = st.columns(3)

with col10:
    st.image(resize_image(images[9]), use_column_width=True)

with col11:
    st.image(resize_image(images[10]), use_column_width=True)

with col12:
    st.image(resize_image(images[11]), use_column_width=True)