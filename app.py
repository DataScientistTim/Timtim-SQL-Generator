import streamlit as st
import google.generativeai as genai


GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')


def main():
    st.set_page_config(page_title="Timtim's SQL Query Generator", page_icon="robot:")
    st.markdown(
    """
    <style>

        @import url('https://fonts.googleapis.com/css2?family=Sour+Gummy:ital,wght@0,100..900;1,100..900&display=swap');

        body {
            margin: 0;
            padding: 0;
            height: 100vh;  /* Full height of the viewport */
            width: 100vw;
            display: flex;
            justify-content: center; 
            align-items: center;  
            font-family: 'Sour Gummy', serif !important;
        }

        .content-container {
            text-align: center;
            padding: 40px;
            background: linear-gradient(to bottom right, rgba(21, 244, 238, 0.5), rgba(146, 199, 199, 1));  /* Light grey gradient */
            border-radius: 10px;
            box-shadow: 0 8px 16px rgba(21, 244, 238, 0.5);  /* Optional: Adds shadow around the box */
            width: 100vw;  /* Adjust width as needed */
            max-width: 800px;  /* Optional: Set a maximum width */
        }

        .description {
            color: black;
            font-size: 18px;
            font-family: 'Sour Gummy', serif !important;
        }

        h1 {
            color: #333;
            font-family: 'Sour Gummy', cursive !important;
            font-size: 70px; /* Increased size of the main title */
        }

        h3 {
            color: #333;
            font-family: 'Sour Gummy', cursive !important;
            font-size: 35px; /* Increased size of subheading */
        }

        h4 {
            color: #333;
            font-family: 'Sour Gummy', cursive !important;
            font-size: 25px; /* Increased size of smaller subheading */
        }

    </style>
    <div class="content-container">
        <h1>Timtim's SQL Query Generator</h1>
        <img src="https://static.vecteezy.com/system/resources/thumbnails/036/044/336/small/sql-database-icon-logo-design-ui-or-ux-app-png.png" alt="Image Description" width="200">
        <h3>🤖 I can generate SQL queries for you</h3>
        <h4>Just tell me what you need</h4>
        <p class="description">This tool allows you to generate SQL queries based on your prompts.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

    text_input = st.text_area("Enter your text here:", height=100)

    submit = st.button("Generate SQL Query")
    if submit:
        with st.spinner("Generating SQL Query..."):
            template = """
               Create a SQL query snippet using the below text:

                ```
                   {text_input}
                ```
                I just want a SQL query.
            
            """

            formulated_template = template.format(text_input=text_input)

            response = model.generate_content(formulated_template)
            sql_query = response.text

            sql_query = sql_query.strip().lstrip("```sql").rstrip("```")


            expected_output = """
                What would be the expected response of this SQL query snippet:
                ```
                    {sql_query}
                ```
                Provide sample tabular response with no explanation:"""
            
            expected_output_formatted = expected_output.format(sql_query=sql_query)
            output = model.generate_content(expected_output_formatted)
            output = output.text

            explanation = """
                Explain this SQL query snippet:
                ```
                    {sql_query}
                ```
                Provide with simplest of explanation:"""
            
            explanation_formatted = explanation.format(sql_query=sql_query)
            explanation_output = model.generate_content(explanation_formatted)
            explanation_output = explanation_output.text

            with st.container():
                st.success("SQL Query Generated Successfully! Here is your Query Below:")
                st.code(sql_query, language="sql")

                st.success("Expected Output of this SQL query will be:")
                st.markdown(output)

                st.success("Explanation of this SQL Query:")
                st.markdown(explanation_output)
                

main()
