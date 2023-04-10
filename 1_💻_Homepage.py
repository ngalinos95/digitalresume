from pathlib import Path
import streamlit as st
from PIL import Image

#--- PATH SETTINGS ----
current_dir=Path(__file__).parent if "_file_" in locals() else Path.cwd()
css_file =current_dir / "styles" / "main.css"
resume_file=current_dir / "assets" / "CV.pdf"
profile_pic=current_dir / "assets" / "pic.png"


#--- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Nikos Galinos"
PAGE_ICON = "👨‍💻"
NAME = "Nikos Galinos"
DESCRIPTION= """
 Software Engineer - Java BackEnd , Python
"""

EMAIL = "ngalinos95@me.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/nikosgalinos/",
    "GitHub": "https://github.com/ngalinos95",
    "HackerRank": "https://www.hackerrank.com/ngalinos95"
}

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
)

st.sidebar.success("Select a Page Above")


#--- LOAD CSS ,CV,PROFILE PIC ---

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✅ Strong Object Oriented Programming (OOP), Data Structures and Design Patterns skills
- ✅ Excellent experience on time management and problem solving using agile practices
- ✅ Strong knowledge and experience in personal projects with Java and Pyhon
- ✅ Ability to learn new technologies/frameworks fast
- ✅ Excellent team-player and displaying strong sense of initiative on tasks
- ✅ 2 Years experience in Mecahncial Engineer large scale projects and multimember teams
- ✅ Excellent knowledge of English with previous experience on multinational projects
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👨‍💻 Programming: Java ,Python ,basics on SQL
- 🛠️ Frameworks Java Backend:Spring-SpringBoot- Spring Secirity (REST APIs)
- 🛠️ Other Frameworks: Swing (Java GUI)-Streamlit (Python)
- 🗄️ Databases knowledge: Hands on projects on JDBC[ MySQL,SQLite and H2 databases]
- 📊 Data Visulization and Modeling: Matlab
- 🎟 Workflow Software: Hands on knowledge of Jira and Confluence fundamentals

"""
)
# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("👷🏻‍♂️", "**Mechanical Engineer| TEAM E-M Consulting Engineers SA**")
st.write("11/2020 - 11/2022")
st.write(
    """
- ► Used Agile Practices on managing large scale MEP projects
- ► Followed and led teams on MEP projects
- ► Strengthened time management skills through managing multiple projects,prioritizing based on the needs and schedules
- ► Worked as a team player on large projects which involved many engineering groups. 
"""
)

# --- EDUCATION
st.write('\n')
st.subheader("Education")
st.write("---")
st.write("🎓", "**Aristotle University of Thessaloniki | Master Of Engineering**")
st.write("MEng | Mechanical Engineering")

st.write("2014 -2020")
st.write('\n')
st.write(
    """
A university that formulates structured and disciplined way of thinking. 
It  turns general knowledge into science focusing on methodology of problem solving.
It opens horizons and turns general knowledge into science focusing on methodology of problem solving. 
It deepens the research and creates a starting point for a new professional who wants to give efficient solutions 
to any given problem.
"""
)
st.write(
    """
The fields of my studies cover mathematics, mechanics, engineering drawing, physics, computing,
Programming in Matlab,mechanical systems, thermodynamics, fluid mechanics, E/M energy conversion systems, 
Machine Dynamics, Hydraulic and pneumatic systems, Automation control systems, Operational Research, Industrial statistics,
management information systems, industrial electronics, Air-conditioning, production planning, ergonomics among others.
"""
)

