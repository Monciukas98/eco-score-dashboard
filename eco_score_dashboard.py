import streamlit as st
import plotly.express as px
import pandas as pd

# Sample ESG data for Apple and competitors
esg_data = pd.DataFrame({
    "Company": ["Apple", "Microsoft", "Google", "Amazon"],
    "Environmental Score": [32, 45, 40, 28],
    "Social Score": [45, 50, 48, 35],
    "Governance Score": [38, 42, 41, 30],
})

# Calculate Total ESG Score
weights = {"Environmental": 0.4, "Social": 0.3, "Governance": 0.3}
esg_data["Total ESG Score"] = (
    esg_data["Environmental Score"] * weights["Environmental"] +
    esg_data["Social Score"] * weights["Social"] +
    esg_data["Governance Score"] * weights["Governance"]
)

# Function to assign ESG ratings
def get_esg_rating(score):
    if score <= 20:
        return "A+"
    elif score <= 30:
        return "A"
    elif score <= 40:
        return "B+"
    elif score <= 50:
        return "B"
    elif score <= 60:
        return "C+"
    elif score <= 70:
        return "C"
    elif score <= 80:
        return "D"
    else:
        return "F"

# Assign ESG Ratings
esg_data["ESG Rating"] = esg_data["Total ESG Score"].apply(get_esg_rating)

# Streamlit App
st.title("🌍 EcoScore AI - ESG Ratings Dashboard")

# Select company
company_selected = st.selectbox("Select a Company", esg_data["Company"])

# Get company-specific data
company_data = esg_data[esg_data["Company"] == company_selected].iloc[0]

# Display ESG score breakdown
st.subheader(f"📊 ESG Score Breakdown for {company_selected}")
fig = px.bar(
    x=["Environmental", "Social", "Governance"],
    y=[company_data["Environmental Score"], company_data["Social Score"], company_data["Governance Score"]],
    labels={"x": "ESG Category", "y": "Score (0-100)"},
    title=f"{company_selected} ESG Scores",
    color=["green", "blue", "orange"]
)
st.plotly_chart(fig)

# Display Total ESG Score & Rating
st.metric(label="Total ESG Score", value=round(company_data["Total ESG Score"], 2))
st.metric(label="ESG Rating", value=company_data["ESG Rating"])

# Comparison Chart
st.subheader("🏆 Competitor ESG Comparison")
fig_comp = px.bar(
    esg_data,
    x="Company",
    y="Total ESG Score",
    color="Company",
    title="Total ESG Score Comparison",
    text=esg_data["Total ESG Score"].round(2)
)
st.plotly_chart(fig_comp)
