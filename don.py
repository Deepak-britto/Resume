import streamlit as st
from PIL import Image

# ✅ Page Configuration
st.set_page_config(page_title="Deepak Mathew - Portfolio", layout="wide")

# ✅ Navigation Menu at the Top
st.markdown("<h1 style='text-align: center;'>Deepak Mathew - Portfolio</h1>", unsafe_allow_html=True)

menu = st.radio("Navigate to:", ["Home", "Education", "Work Experience", "Technical Skills", "Social Media", "Download Resume"], horizontal=True)

st.markdown("---")  # Separator Line

# ✅ Home Page
if menu == "Home":
    st.write("# Welcome to my Portfolio!")

    # ✅ Display Image with Error Handling
    col1, col2 = st.columns([1, 3])
    with col1:
        try:
            image = Image.open("deepak photo.png")
            st.image(image, width=150)
        except FileNotFoundError:
            st.warning("⚠️ Profile image not found. Ensure 'deepak photo.png' exists in the directory.")

    with col2:
        st.markdown(
            """
            <div style="text-align: left;">
                <h2>DEEPAK MATHEW, B.Sc, M.Sc.</h2>
                <h5><em>Data Analyst</em></h5>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ✅ Summary Section
    st.markdown('## Summary')
    st.info('''
    - Data Analyst and Data Engineer with 2 years of experience in transforming raw data into actionable insights and building efficient data pipelines.
    - Skilled in SQL, Python, Power BI, and Azure Data Factory, with expertise in data modelling, ETL processes, and dashboard creation.
    - Passionate about leveraging data engineering and analytics to drive strategic decision-making and improve operational efficiency.
    ''')

# ✅ Education Section
elif menu == "Education":
    st.markdown("## Education 🎓")

    st.write("### Master of Science (Mathematics)")
    st.write("*Government Arts College For Men, Chennai (2020-2022)*")
    st.write("📌 **GPA:** `7.10`")

    st.write("### Bachelor of Science (Mathematics)")
    st.write("*Loyola College, Chennai (2016-2019)*")
    st.write("📌 **GPA:** `6.34`")

# ✅ Work Experience Section
elif menu == "Work Experience":
    st.markdown("## Work Experience 💼")

    st.write("### **IDEATEC Real Time Data Pvt Ltd**")
    st.write("📍 Data Analyst, Chennai (Sep 2024 - Present)")
    st.markdown("""
    - Collected, processed, and analyzed real-time machine performance data to identify trends and anomalies.
    - Built predictive maintenance models to detect potential failures and reduce downtime.
    - Developed dashboards and reports in Power BI to monitor machine health and efficiency metrics.
    """)

    st.write("### **HCL TECH**")
    st.write("📍 Associate Data Analyst, Chennai (Mar 2023 - Aug 2024)")
    st.markdown("""
    - Published reports in Excel, Power BI, and automated summary reports using SQL & Python.
    - Developed Python scripts to automate routine data processing tasks, saving 20+ hours of manual work.
    """)

# ✅ Technical Skills Section
elif menu == "Technical Skills":
    st.markdown("## Technical Skills 🛠")

    skills = {
        "Programming": "`Python (Pandas, PySpark)`, `SQL Spark`",
        "Data Analytics": "`Power BI`, `Excel`, `Pandas`, `Numpy`",
        "Cloud Computing": "`Azure SQL`, `Azure Data Factory`, `Azure Databricks`, `Azure Synapse Analytics`",
        "Machine Learning": "`Regression`, `Decision Tree`, `Random Forest`, `SVM`, `Neural Networks`",
        "Server Tools": "`MS SQL Server, SSMS`, `SSIS`, `SSAS`",
        "Statistics": "`Hypothesis Testing`, `ANOVA`, `Time Series`"
    }

    for skill, details in skills.items():
        st.write(f"📌 **{skill}:** {details}")

# ✅ Social Media Section
elif menu == "Social Media":
    st.markdown("## Social Media 🌍")

    social_links = {
        "LinkedIn": "https://www.linkedin.com/in/deepakmathew1806",
        "GitHub": "https://github.com/deepak-mathew",
        "Email": "mailto:deepakmathew1806@gmail.com"
    }

    for platform, link in social_links.items():
        st.markdown(f"📎 **{platform}:** [{platform} Profile]({link})")

# ✅ Resume Download Section
elif menu == "Download Resume":
    st.markdown("## 📄 Download Resume")

    resume_path = "Deepak Mathew resume latest.pdf"
    try:
        with open(resume_path, "rb") as file:
            st.download_button(label="📥 Download Resume", data=file, file_name=resume_path, mime="application/pdf")
    except FileNotFoundError:
        st.warning("⚠️ Resume file not found. Ensure it exists in the correct directory.")
