import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Healthcare AI Copilot",
    page_icon="🏥",
    layout="wide"
)

# --------------------
# Load Data
# --------------------

df = pd.read_csv(
    "patient_reports.csv"
)

reference = pd.read_csv(
    "medical_reference.csv"
)

# --------------------
# Header
# --------------------

st.title("🏥 Healthcare AI Copilot")

st.markdown("""
AI-powered patient intelligence dashboard.

Analyze health reports,
identify abnormalities,
track trends,
and generate health insights.
""")

# --------------------
# KPIs
# --------------------

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Patients",
    df["patient_id"].nunique()
)

col2.metric(
    "Reports",
    len(df)
)

col3.metric(
    "Average Cholesterol",
    round(df["cholesterol"].mean())
)

col4.metric(
    "Average Glucose",
    round(df["glucose"].mean())
)

st.divider()

# --------------------
# Patient Selection
# --------------------

selected_patient = st.selectbox(
    "Select Patient",
    sorted(
        df["patient_id"].unique()
    )
)

patient_df = (
    df[df["patient_id"] == selected_patient]
    .sort_values("report_date")
)

latest = patient_df.iloc[-1]

# --------------------
# Latest Report
# --------------------

st.subheader(
    "📋 Latest Health Report"
)

st.dataframe(
    patient_df.tail(1),
    use_container_width=True
)

# --------------------
# Health Risk Score
# --------------------

risk = 0

if latest["glucose"] > 100:
    risk += 1

if latest["cholesterol"] > 200:
    risk += 1

if latest["ldl"] > 100:
    risk += 1

if latest["vitamin_d"] < 30:
    risk += 1

if risk <= 1:
    score = "Low"

elif risk <= 3:
    score = "Moderate"

else:
    score = "High"

st.subheader("🚨 Risk Assessment")

st.metric(
    "Health Risk Level",
    score
)

# --------------------
# Trend Charts
# --------------------

st.subheader(
    "📈 Biomarker Trends"
)

metric = st.selectbox(
    "Choose Metric",
    [
        "glucose",
        "cholesterol",
        "hdl",
        "ldl",
        "vitamin_d",
        "hemoglobin"
    ]
)

fig = px.line(
    patient_df,
    x="report_date",
    y=metric,
    markers=True,
    title=f"{metric.title()} Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------
# Population Analysis
# --------------------

st.subheader(
    "👨‍⚕ Population Health Analytics"
)

avg_metrics = df[[
    "glucose",
    "cholesterol",
    "hdl",
    "ldl",
    "vitamin_d",
    "hemoglobin"
]].mean()

fig2 = px.bar(
    x=avg_metrics.index,
    y=avg_metrics.values,
    labels={
        "x":"Metric",
        "y":"Average Value"
    }
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# --------------------
# AI Insight Engine
# --------------------

st.subheader(
    "🤖 AI Health Insights"
)

insights = []

if latest["cholesterol"] > 200:
    insights.append(
        "Elevated cholesterol detected."
    )

if latest["glucose"] > 100:
    insights.append(
        "Glucose level is above normal range."
    )

if latest["vitamin_d"] < 30:
    insights.append(
        "Vitamin D deficiency risk detected."
    )

if latest["hdl"] < 40:
    insights.append(
        "HDL cholesterol is below optimal level."
    )

if not insights:
    insights.append(
        "All primary biomarkers appear within normal limits."
    )

for item in insights:
    st.success(item)

# --------------------
# Dataset Explorer
# --------------------

st.subheader(
    "🔍 Patient Dataset"
)

st.dataframe(
    df,
    use_container_width=True
)