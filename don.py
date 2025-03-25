import streamlit as st
from PIL import Image

# Page Title
st.set_page_config(page_title="Deepak Mathew - Portfolio", layout="wide")

# ---- Sidebar Navigation ----
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Education", "Work Experience", "Technical Skills", "Social Media", "Download Resume"])

# ---- Home Page ----
if page == "Home":
    st.title("Welcome to My Portfolio!")
    st.subheader("Deepak Mathew, B.Sc, M.Sc.")
    st.write("🚀 Data Analyst | Data Engineer | Azure Enthusiast")

    # Profile Image
    try:
        image = Image.open("deepak photo.png")
        st.image(image, width=150)
    except FileNotFoundError:
        st.warning("⚠️ Profile image not found. Please ensure 'deepak photo.png' exists.")

    # Summary Section
    st.markdown("## Summary")
    st.info('''
    - Data Analyst and Data Engineer with 2 years of experience in transforming raw data into actionable insights and building efficient data pipelines.
    - Skilled in SQL, Python, Power BI, and Azure Data Factory, with expertise in data modeling, ETL processes, and dashboard creation.
    - Adept at analyzing large datasets, optimizing workflows, and developing KPI reports to drive business insights.
    - Passionate about leveraging data engineering and analytics to drive strategic decision-making and improve operational efficiency.
    ''')

# ---- Education Section ----
elif page == "Education":
    st.markdown("## Education 🎓")
    
    st.write("### Master of Science (Mathematics)")
    st.write("*Government Arts College For Men, Chennai (2020-2022)*")
    st.write("📌 **GPA:** `7.10`")
    
    st.write("### Bachelor of Science (Mathematics)")
    st.write("*Loyola College, Chennai (2016-2019)*")
    st.write("📌 **GPA:** `6.34`")

# ---- Work Experience Section ----
elif page == "Work Experience":
    st.markdown("## Work Experience 💼")

    st.write("### **IDEATEC Real Time Data Pvt Ltd**")
    st.write("📍 Data Analyst, Chennai (Sep 2024 - Present)")
    st.markdown("""
    - Collected, processed, and analyzed real-time machine performance data to identify trends and anomalies.
    - Built predictive maintenance models to detect potential failures and reduce downtime.
    - Developed dashboards and reports in Power BI to monitor machine health and efficiency metrics.
    - Utilized SQL and Python to clean, aggregate, and model machine data for predictive maintenance insights.
    - Designed and optimized ETL pipelines for real-time data ingestion from industrial sensors and IoT devices.
    - Collaborated with engineering teams to improve data collection methods and enhance monitoring accuracy.
    """)

    st.write("### **HCL TECH**")
    st.write("📍 Associate Data Analyst, Chennai (Mar 2023 - Aug 2024)")
    st.markdown("""
    - Published reports in Excel, Power BI, and automated summary reports using SQL & Python.
    - Developed Python scripts to automate routine data processing tasks, saving 20+ hours of manual work.
    - Worked on Excel reports with Power Query, Power Pivot, and data modeling for YTD, MTD, QTD reports.
    - Assisted the Data Warehouse team in developing dimensional models and analyzing data.
    - Experience in Data Integration, ETL processes, and Data Warehousing using SSIS, SSMS, and SSAS.
    - Created various visualizations such as line charts, bar charts, scatter plots, tree maps in Power BI.
    """)

# ---- Technical Skills Section ----
elif page == "Technical Skills":
    st.markdown("## Technical Skills 🛠")

    skills = {
        "Programming": "`Python (Pandas, PySpark)`, `SQL Spark`",
        "Data Processing & Analytics": "`Power BI`, `Excel`, `Spark`, `Pandas`, `Numpy`, `Stream Analytics`",
        "Cloud Computing": "`Azure SQL Database`, `Azure Data Lake`, `Azure Data Factory`, `Azure Databricks`, `Azure Synapse Analytics`",
        "Machine Learning": "`Regression Analysis`, `Decision Tree`, `Random Forests`, `SVM`, `Neural Networks`, `NLP`, `K-Means Clustering`",
        "Server Tools": "`MS SQL Server, SSMS`, `SSIS`, `SSAS`",
        "Statistical Methods": "`Hypothesis Testing`, `ANOVA`, `Time Series`, `Cross-validation`"
    }

    for skill, details in skills.items():
        st.write(f"📌 **{skill}:** {details}")

# ---- Social Media Section ----
elif page == "Social Media":
    st.markdown("## Social Media 🌍")

    social_links = {
        "LinkedIn": "https://www.linkedin.com/in/deepakmathew1806",
        "GitHub": "https://github.com/deepak-mathew",
        "Email": "mailto:deepakmathew1806@gmail.com"
    }

    for platform, link in social_links.items():
        st.markdown(f"📎 **{platform}:** [{platform} Profile]({link})")

# ---- Resume Download Section ----
elif page == "Download Resume":
    st.markdown("## 📄 Download Resume")

    resume_path = "Deepak Mathew resume latest.pdf"
    try:
        with open(resume_path, "rb") as file:
            st.download_button(label="📥 Download Resume", data=file, file_name=resume_path, mime="application/pdf")
    except FileNotFoundError:
        st.warning("⚠️ Resume file not found. Please ensure it exists in the project directory.")
