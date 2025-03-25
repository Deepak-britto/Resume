import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# DEEPAK MATHEW, B.sc, M.sc.
##### *Data Analyst* 
''')

image = Image.open('deepak photo.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Data Analyst and Data Engineer with 2 years of experience in transforming raw data into actionable insights and building efficient data pipelines. Skilled in SQL, Python, Power BI, and Azure Data Factory, with expertise in data modelling, ETL processes, and dashboard creation.
- Adept at analysing large datasets, optimizing workflows, and developing KPI reports to drive business insights. Passionate about leveraging data engineering and analytics to drive strategic decision-making and improve operational efficiency. 
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand target="_blank">DEEPAK MATHEW</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
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
## Education
''')

txt('**Master of science** (Mathematics), *Goverments Arts College For Men*, Chennai',
'2020-2022')
st.markdown('''
- GPA: `7.10`
''')

txt('**Bachelors of Science** (Mathematics), *Loyola College*, Chennai',
'2016-2019')
st.markdown('''
- GPA: `6.34`
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**IDEATEC Real Time Data Pvt Ltd**, Data Analyst, Chennai',
'Sep 2024- Present')
st.markdown('''
- Collected, processed, and analyzed real-time machine performance data to identify trends and anomalies.  
- Built predictive maintenance models to detect potential failures and reduce downtime, improving operational efficiency. 
- Developed dashboards and reports in Power BI to monitor machine health, downtime, and efficiency metrics. 
- Utilized SQL and Python to clean, aggregate, and model machine data for predictive maintenance insights. 
- Designed and optimized ETL pipelines for real-time data ingestion and transformation from industrial sensors and IoT devices data.  
- Collaborated with engineering teams to improve data collection methods and enhance monitoring accuracy.
''')

txt('**HCL TECH**,Associate Data Analyst, Chennai',
'Mar 2023-Aug 2024')
st.markdown('''
- Having experience in publishing various report in Excel, Power BI and setting up the necessary connection settings. 
- Automated the summary reports using SQL and Python; Visualized the data on Microsoft Power BI. 
- Developed Python scripts to automate routine data processing tasks, saving an estimated 20 hours of manual work. 
- Work on excel report with power query, power pivot and data modelling to create the YTD, MTD and QTD reports. 
- Worked with Data Warehouse team in developing Dimensional model and analysing the data. 
- Experience in Data Integration & data Quality controls for ETL process and Data Warehouse using MS visual studio, SSIS, SSMS, SSAS. 
- Experienced in Python to date Manipulate & data Preparation for data loading and extraction; worked with Python like Matplotlib, Numpy, Scipy, Pandas for data analysis. 
- Having experience in creating various charts like line chart, bar chart, table, matrix table, area chart, scattered chart, tree map. 
''')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '` Python (Pandas, PySpark)`, `SQL Spark`')
txt3('Data Processing & Analytics', '`Power BI`,`Excel`,`Spark`, `pandas`, `numpy`, `Stream Analytics`')
txt3('Cloud Computing','` Azure SQL Database`, `Azure Data Lake`, `Azure Data Factory`, `Azure Databricks`, `Azure Synapse Analytics`')
txt3('Machine Learning','`Regression Analysis`, `Bayesian Method`, `Decision Tree`, `Random Forests`, `Support Vector Machine`, `Neural networks`, `sentiment analysis`, `K-Means clustering`, `KNN and Ensemble Method`, `NLP`,`scikit-learn`')
txt3('Server Tool', '`MS SQL Server, SQL Server Management Studio (SSMS)`, `MSSQL Server Integration Services (SSIS)`, `MSSQL Server Analysis Services (SSAS)`')
txt3('Statistical Methods', '` Hypothetical testingt`, `ANOVA`, `Time Series`, `Cross-validation `')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/chanin-nantasenamat')
txt2('GitHub', 'https://github.com/chaninn/')
txt2('Gmail', 'http://orcid.org/0000-0003-1040-663X')

