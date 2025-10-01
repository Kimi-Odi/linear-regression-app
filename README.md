# Interactive Simple Linear Regression App

A web application built with Streamlit to demonstrate and explore simple linear regression in an interactive way.

## Description

This application allows users to generate a dataset based on a linear equation (`y = ax + b + noise`) and visualize the results. You can dynamically adjust the parameters of the data generation process to see how they affect the data distribution, the fitted regression line, and the model's performance metrics. The app also identifies and highlights the top 5 outliers in the generated dataset.

This project was developed following the CRISP-DM methodology, from understanding the business need for an educational tool to deploying it as an interactive web app.

## Features

- **Interactive Controls**: Use sliders in the sidebar to control the number of data points (`n`), the true coefficient (`a`), the true intercept (`b`), and the noise variance.
- **Live Visualization**: See the generated data points and the calculated linear regression line updated in real-time.
- **Outlier Detection**: The top 5 points furthest from the regression line are automatically identified and labeled on the plot.
- **Performance Metrics**: Key regression results, including the calculated coefficients and the R-squared value, are displayed.

## Getting Started

### Prerequisites

- Python 3.7+
- Git

### Installation & Usage

1.  **Clone the repository (or download the files):**
    ```bash
    # Make sure to replace <your-repository-url> with the actual URL from GitHub
    git clone <your-repository-url>
    cd <repository-directory>
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit app:**
    ```bash
    streamlit run linear_regression_app.py
    ```

The application should open in a new tab in your web browser.

## Deployment

This application can be deployed to various platforms. We have explored two options:

1.  **Replit**: The application can be deployed by uploading the files to a Python Repl and configuring the `.replit` file to run the Streamlit command.
2.  **Streamlit Community Cloud**: By pushing the code to a public GitHub repository, you can connect your account to Streamlit Cloud for continuous deployment.

Refer to `devlog.md` for more detailed notes on the deployment discussions.
