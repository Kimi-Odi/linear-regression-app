import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# --- CRISP-DM: Business Understanding ---
st.set_page_config(layout="wide")
st.title("Interactive Simple Linear Regression")
st.write("""
This app demonstrates a simple linear regression model.
Following the **CRISP-DM** methodology, this tool helps in understanding the relationship between variables by allowing you to generate data and visualize the regression line.
- **Business Understanding**: The goal is to provide an interactive tool for learning and experimenting with linear regression.
- **Data Understanding & Preparation**: You generate the data by setting the parameters on the left.
- **Modeling**: A linear regression model is fitted to the data.
- **Evaluation**: The model is evaluated visually through the plot and quantitatively with metrics like R-squared. Outliers are identified.
- **Deployment**: This Streamlit app is the deployed result.
""")

# --- CRISP-DM: Data Understanding & Preparation ---
st.sidebar.header("Data Generation Parameters")

# User-selectable parameters in the sidebar
n_points = st.sidebar.slider("Number of data points (n)", 100, 1000, 500)
a_coeff = st.sidebar.slider("Coefficient (a)", -10.0, 10.0, 2.5, 0.1)
b_coeff = st.sidebar.slider("Intercept (b)", -50.0, 50.0, 10.0, 0.1)
variance = st.sidebar.slider("Noise Variance (var)", 0, 1000, 100)

# Generate synthetic data
@st.cache_data
def generate_data(n, a, b, var):
    # Generate x values (e.g., from 0 to 100)
    x = np.random.rand(n) * 100
    # Generate noise
    noise = np.random.normal(0, np.sqrt(var), n)
    # Generate y values
    y = a * x + b + noise
    df = pd.DataFrame({'x': x, 'y': y})
    return df

data_df = generate_data(n_points, a_coeff, b_coeff, variance)

# --- CRISP-DM: Modeling ---
# Reshape data for sklearn
X = data_df[['x']]
y = data_df['y']

# Fit the linear regression model
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# --- CRISP-DM: Evaluation ---
# Calculate residuals to find outliers
data_df['y_pred'] = y_pred
data_df['residuals'] = np.abs(data_df['y'] - data_df['y_pred'])
outliers = data_df.nlargest(5, 'residuals')

# Get model results
calculated_a = model.coef_[0]
calculated_b = model.intercept_
r_squared = model.score(X, y)

# Display results
st.header("Regression Results")
col1, col2, col3 = st.columns(3)
col1.metric("Calculated Coefficient (a)", f"{calculated_a:.2f}")
col2.metric("Calculated Intercept (b)", f"{calculated_b:.2f}")
col3.metric("R-squared", f"{r_squared:.2f}")

# --- Visualization ---
st.header("Data and Regression Line")
fig, ax = plt.subplots(figsize=(10, 6))

# Plot data points
ax.scatter(data_df['x'], data_df['y'], alpha=0.6, label='Generated Data')

# Plot regression line
ax.plot(data_df['x'], y_pred, color='red', linewidth=2, label='Regression Line')

# Highlight and label outliers
ax.scatter(outliers['x'], outliers['y'], color='orange', s=100, edgecolors='k', zorder=5, label='Top 5 Outliers')
for i, row in outliers.iterrows():
    ax.text(row['x'] + 0.5, row['y'] + 0.5, f'({row["x"]:.1f}, {row["y"]:.1f})', fontsize=9)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Simple Linear Regression")
ax.legend()
ax.grid(True)

st.pyplot(fig)

st.header("Generated Data & Outliers")
st.write("The table below shows the generated data points, the predicted values from the model, and the calculated residuals.")
st.dataframe(data_df)

st.write("Top 5 Outliers (points furthest from the regression line):")
st.dataframe(outliers)
