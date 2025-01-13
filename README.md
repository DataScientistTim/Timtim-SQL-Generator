# Timtim's SQL Generator

Welcome to **Timtim's SQL Generator**, an interactive web tool that helps you effortlessly generate SQL queries based on your natural language prompts! Whether you're a beginner or an experienced SQL user, this tool makes it easy to quickly create SQL queries by simply describing what you need.

With **Timtim's SQL Generator**, you can:

- Input a text prompt describing your database query needs.
- Generate a clean and optimized SQL query.
- View the expected output for the query, presented in a sample tabular format.
- Get a simple explanation of the generated SQL query for better understanding.

### Key Features:
- **Natural Language to SQL**: Enter your query needs in plain English, and Timtim will handle the rest, generating the appropriate SQL query for you.
- **Expected Output**: See what the result of your SQL query would look like in a sample tabular format.
- **Simplified Explanations**: Learn how the generated query works, with explanations written in simple terms.

---

### Installation

To get started, you'll need to set up the environment and install the necessary dependencies:

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/timtim-sql-generator.git](https://github.com/DataScientistTim/Timtim-s-SQL-Generator.git
    cd timtim-sql-generator
    ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your Google Generative AI API key:
    - Go to [Google Cloud Console](https://console.cloud.google.com/), create a project, and enable the **Generative AI API**.
    - Set up your API key and store it in the environment variable or configure it in your script.

### Usage

Run the app with the following command:

```bash
streamlit run app.py
```


