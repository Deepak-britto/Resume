import streamlit as st
from PIL import Image

import streamlit as st

# Custom Light Gray Gradient Background CSS
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #666666   , #d9d9d9);
        background-attachment: fixed;
        color: black; /* Ensures text remains readable */
    }

    /* Ensure text remains dark */
    .stMarkdown, .stText, .stTitle, .stSubtitle, .stHeader, .stFooter {
        color: black !important;
    }

    /* Soft gray theme for buttons */
    .stButton>button {
        background-color: #1B4F72  !important;
        color: black !important;
        border-radius: 8px;
    }

    /* Optional: Modify widgets */
    .stTextInput, .stSelectbox, .stMultiselect, .stCheckbox, .stRadio, .stSlider {
        color: black !important;
        background-color: #34495E  !important;
        border-color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ✅ Assigning a value to 'page'
page = "Home"  # This variable is set but not conditionally checked

# ✅ Directly displaying content without 'if' condition
st.write("# Welcome to my Portfolio!")

with open("style1.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.markdown(
    """
    <div style="text-align: center;">
        <h2>DEEPAK MATHEW, B.Sc, M.Sc.</h2>
        <h5><em>Data Analyst & Data Engineer</em></h5>
    </div>
    """,
    unsafe_allow_html=True
)

image = Image.open('deepak photo.png')
st.image(image, width=150)

# Load external CSS
with open("style1.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

import streamlit as st

# Load external CSS
with open("style1.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

resume_path = "Deepak Mathew resume latest.pdf"

try:
    with open(resume_path, "rb") as file:
        st.download_button(
            label="📥 Download Resume",
            data=file,
            file_name="Deepak Mathew resume latest.pdf",
            mime="application/pdf"
        )
except FileNotFoundError:
    st.error("⚠️ Resume file not found. Please check the file path.")

st.markdown("<h2 style='text-align: center; color: #black;'>Summary</h2>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="custom-summary">
        <ul>
            <li>Data Analyst and Data Engineer with 2 years of experience in transforming raw data into actionable insights and building efficient data pipelines.</li>
            <li>Skilled in SQL, Python, Power BI, and Azure Data Factory, with expertise in data modeling, ETL processes, and dashboard creation.</li>
            <li>Adept at analyzing large datasets, optimizing workflows, and developing KPI reports to drive business insights.</li>
            <li>Passionate about leveraging data engineering and analytics to drive strategic decision-making and improve operational efficiency.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)


#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" target="_blank">Deepak Mathew</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#technical-skills">Technical Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#certifications">Certifications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#download-resume">Resume</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Technical skills
''')
txt3('Programming', '`Python (Pandas, PySpark)`, `SQL Spark`')
txt3('Data Processing & Analytics', '`Power BI`, `Excel`, `Spark`, `Pandas`, `Numpy`, `Stream Analytics`')
txt3('Cloud Computing', '`Azure SQL Database`, `Azure Data Lake`, `Azure Data Factory`, `Azure Databricks`, `Azure Synapse Analytics`')
txt3('Machine Learning', '`Regression Analysis`, `Decision Tree`, `Random Forests`, `SVM`, `Neural Networks`, `NLP`, `K-Means Clustering`')
txt3('Server Tools', '`MS SQL Server, SSMS`, `SSIS`, `SSAS`')
txt3('Statistical Methods', '`Hypothesis Testing`, `ANOVA`, `Time Series`, `Cross-validation`')

#####################
st.markdown('''
## Work Experience
''')

txt('**IDEATEC Real Time Data Pvt Ltd**, Data Analyst, Chennai', 'Sep 2024 - Present')
st.markdown('''
- Collected, processed, and analyzed real-time machine performance data to identify trends and anomalies.  
- Built predictive maintenance models to detect potential failures and reduce downtime.  
- Developed dashboards and reports in Power BI to monitor machine health and efficiency metrics.  
- Utilized SQL and Python to clean, aggregate, and model machine data for predictive maintenance insights.  
- Designed and optimized ETL pipelines for real-time data ingestion from industrial sensors and IoT devices.  
- Collaborated with engineering teams to improve data collection methods and enhance monitoring accuracy.
''')

txt('**HCL TECH**, Associate Data Analyst, Chennai', 'Mar 2023 - Aug 2024')
st.markdown('''
- Published reports in Excel, Power BI, and automated summary reports using SQL & Python.  
- Developed Python scripts to automate routine data processing tasks, saving 20+ hours of manual work.  
- Worked on Excel reports with Power Query, Power Pivot, and data modeling for YTD, MTD, QTD reports.  
- Assisted the Data Warehouse team in developing dimensional models and analyzing data.  
- Experience in Data Integration, ETL processes, and Data Warehousing using SSIS, SSMS, and SSAS.  
- Created various visualizations such as line charts, bar charts, scatter plots, tree maps in Power BI.
''')

###########

st.markdown('''
## Projects
''')

txt('**IDEATEC Real Time Data Pvt Ltd**, Data Analyst, Chennai', 'Sep 2024 - Present')
st.markdown('''
- Collected, processed, and analyzed real-time machine performance data to identify trends and anomalies.  
- Built predictive maintenance models to detect potential failures and reduce downtime.  
- Developed dashboards and reports in Power BI to monitor machine health and efficiency metrics.  
- Utilized SQL and Python to clean, aggregate, and model machine data for predictive maintenance insights.  
- Designed and optimized ETL pipelines for real-time data ingestion from industrial sensors and IoT devices.  
- Collaborated with engineering teams to improve data collection methods and enhance monitoring accuracy.
''')

txt('**HCL TECH**, Associate Data Analyst, Chennai', 'Mar 2023 - Aug 2024')
st.markdown('''
- Published reports in Excel, Power BI, and automated summary reports using SQL & Python.  
- Developed Python scripts to automate routine data processing tasks, saving 20+ hours of manual work.  
- Worked on Excel reports with Power Query, Power Pivot, and data modeling for YTD, MTD, QTD reports.  
- Assisted the Data Warehouse team in developing dimensional models and analyzing data.  
- Experience in Data Integration, ETL processes, and Data Warehousing using SSIS, SSMS, and SSAS.  
- Created various visualizations such as line charts, bar charts, scatter plots, tree maps in Power BI.
''')

#####################
st.markdown('''
## Education
''')
txt('**Master of Science** (Mathematics), *Government Arts College For Men*, Chennai', '2020-2022')
st.markdown('<p class="gpa-text">  GPA: 7.10</p>', unsafe_allow_html=True)

txt('**Bachelor of Science** (Mathematics), *Loyola College*, Chennai', '2016-2019')
st.markdown('<p class="gpa-text">  GPA: 6.34</p>', unsafe_allow_html=True)

txt('**Higher Secondary School** , *Madras Christian College*, Chennai', '2014-2016')
st.markdown('<p class="gpa-text">  GPA: 7.3</p>', unsafe_allow_html=True)

#####################
st.markdown('''
## Certifications
''')
txt('**Master of Science** (Mathematics), *Government Arts College For Men*, Chennai', '2020-2022')

txt('**Bachelor of Science** (Mathematics), *Loyola College*, Chennai', '2016-2019')

txt('**Higher Secondary School** , *Madras Christian College*, Chennai', '2014-2016')

#####################
st.markdown('''
## Social Media
''')
txt3('LinkedIn', '[LinkedIn Profile](https://www.linkedin.com/in/deepakmathew1806)')
txt3('GitHub', '[GitHub Profile](https://github.com/deepak-mathew)')
txt3('Email', '[Email Deepak](mailto:deepakmathew1806@gmail.com)')

#####################

import streamlit as st

st.markdown('''
## Download Resume
''')

resume_path = "Deepak Mathew resume latest.pdf"

try:
    with open(resume_path, "rb") as file:
        st.download_button(
            label="📥 Download Resume",
            data=file,
            file_name="Deepak Mathew resume latest.pdf",
            mime="application/pdf",
            key="resume_download_btn"  # ✅ Unique key added
        )
except FileNotFoundError:
    st.warning(f"⚠️ Resume file not found: `{resume_path}`. Please ensure the file exists in the project directory.")
