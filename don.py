import streamlit as st
from PIL import Image

# ✅ Correcting "page" assignment
page = "Home"

# ✅ Conditional check if needed
if page == "Home":
    st.write("# Welcome to my Portfolio!")

# ✅ Corrected file path handling for CSS
try:
    with open("style.css", "r") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("⚠️ 'style.css' not found. Ensure the file is in the correct directory.")

st.markdown(
    """
    <div style="text-align: center;">
        <h2>DEEPAK MATHEW, B.Sc, M.Sc.</h2>
        <h5><em>Data Analyst</em></h5>
    </div>
    """,
    unsafe_allow_html=True
)

# ✅ Ensure image file exists before loading
try:
    image = Image.open('deepak photo.png')
    st.image(image, width=150)
except FileNotFoundError:
    st.warning("⚠️ Profile image not found. Ensure 'deepak photo.png' exists.")

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Data Analyst and Data Engineer with 2 years of experience in transforming raw data into actionable insights and building efficient data pipelines. 
- Skilled in SQL, Python, Power BI, and Azure Data Factory, with expertise in data modeling, ETL processes, and dashboard creation.
- Adept at analyzing large datasets, optimizing workflows, and developing KPI reports to drive business insights. 
- Passionate about leveraging data engineering and analytics to drive strategic decision-making and improve operational efficiency.
''')

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="#">DEEPAK MATHEW</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Technical-Skills">Technical Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# ---- Custom Function for Displaying Text in Columns ----
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)

def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

# ---- Education Section ----
st.markdown('## Education 🎓', unsafe_allow_html=True)

txt('**Master of Science** (Mathematics), *Government Arts College For Men*, Chennai', '2020-2022')
st.markdown('- GPA: `7.10`')

txt('**Bachelor of Science** (Mathematics), *Loyola College*, Chennai', '2016-2019')
st.markdown('- GPA: `6.34`')

# ---- Work Experience Section ----
st.markdown('## Work Experience 💼', unsafe_allow_html=True)

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

# ---- Skills Section ----
st.markdown('## Technical Skills 🛠', unsafe_allow_html=True)
txt3('Programming', '`Python (Pandas, PySpark)`, `SQL Spark`')
txt3('Data Processing & Analytics', '`Power BI`, `Excel`, `Spark`, `Pandas`, `Numpy`, `Stream Analytics`')
txt3('Cloud Computing', '`Azure SQL Database`, `Azure Data Lake`, `Azure Data Factory`, `Azure Databricks`, `Azure Synapse Analytics`')
txt3('Machine Learning', '`Regression Analysis`, `Decision Tree`, `Random Forests`, `SVM`, `Neural Networks`, `NLP`, `K-Means Clustering`')
txt3('Server Tools', '`MS SQL Server, SSMS`, `SSIS`, `SSAS`')
txt3('Statistical Methods', '`Hypothesis Testing`, `ANOVA`, `Time Series`, `Cross-validation`')

# ---- Social Media Section ----
st.markdown('## Social Media 🌍', unsafe_allow_html=True)
txt2('LinkedIn', '[LinkedIn Profile](https://www.linkedin.com/in/deepakmathew1806)')
txt2('GitHub', '[GitHub Profile](https://github.com/deepak-mathew)')
txt2('Email', '[Email Deepak](mailto:deepakmathew1806@gmail.com)')

# ---- Resume Download Section ----
st.markdown("## 📄 Download Resume", unsafe_allow_html=True)

resume_path = "Deepak Mathew resume latest.pdf"
try:
    with open(resume_path, "rb") as file:
        st.download_button(label="📥 Download Resume", data=file, file_name=resume_path, mime="application/pdf")
except FileNotFoundError:
    st.warning(f"⚠️ Resume file '{resume_path}' not found. Please ensure the file exists in the correct directory.")
