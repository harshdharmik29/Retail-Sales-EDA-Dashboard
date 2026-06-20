import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Config
st.set_page_config(
    page_title="Retail Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Retail Sales Dashboard")

# Load Dataset
df = pd.read_csv("retail_sales_dataset.csv")

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

# =========================
# KPI SECTION
# =========================

total_revenue = df["Total Amount"].sum()
total_transactions = len(df)
highest_sale = df["Total Amount"].max()
lowest_sale = df["Total Amount"].min()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Transactions", total_transactions)
col3.metric("Highest Sale", f"₹{highest_sale}")
col4.metric("Lowest Sale", f"₹{lowest_sale}")

st.divider()

# =========================
# DATASET PREVIEW
# =========================

st.subheader("Dataset Preview")
st.dataframe(df.head())

# =========================
# CATEGORY ANALYSIS
# =========================

st.subheader("Revenue by Product Category")

category_sales = (
    df.groupby("Product Category")["Total Amount"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots()
category_sales.plot(kind="bar", ax=ax)

ax.set_xlabel("Category")
ax.set_ylabel("Revenue")
ax.set_title("Revenue by Product Category")

st.pyplot(fig)

# =========================
# GENDER ANALYSIS
# =========================

st.subheader("Revenue by Gender")

gender_sales = df.groupby("Gender")["Total Amount"].sum()

fig, ax = plt.subplots()
gender_sales.plot(kind="bar", ax=ax)

ax.set_xlabel("Gender")
ax.set_ylabel("Revenue")
ax.set_title("Revenue by Gender")

st.pyplot(fig)

# =========================
# MONTHLY SALES TREND
# =========================

st.subheader("Monthly Sales Trend")

monthly_sales = df.groupby(df["Date"].dt.month)["Total Amount"].sum()

fig, ax = plt.subplots()
monthly_sales.plot(marker="o", ax=ax)

ax.set_xlabel("Month")
ax.set_ylabel("Revenue")
ax.set_title("Monthly Sales Trend")

st.pyplot(fig)

# =========================
# CORRELATION HEATMAP
# =========================

st.subheader("Correlation Heatmap")

fig, ax = plt.subplots(figsize=(8, 5))

sns.heatmap(
    df[["Age", "Quantity", "Price per Unit", "Total Amount"]].corr(),
    annot=True,
    cmap="Blues",
    ax=ax
)

st.pyplot(fig)

# =========================
# INSIGHTS
# =========================

st.subheader("Key Insights")

st.markdown("""
- Electronics generated the highest revenue.
- Clothing recorded the highest sales volume.
- Female customers generated slightly higher revenue.
- Average customer age was around 41 years.
- Sales peaked in May and were lowest in September.
- Product price showed the strongest impact on revenue.
""")