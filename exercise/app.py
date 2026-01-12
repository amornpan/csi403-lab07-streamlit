# Lab 07 Exercise: Create a Streamlit Search UI
# Save as app.py and run: streamlit run app.py

import streamlit as st
import requests

# Exercise 1: Page title and header (25 pts)
# YOUR CODE HERE - Add title "Disease Search" and a description



# Exercise 2: Search input (25 pts)
# YOUR CODE HERE - Create a text input for search query



# Exercise 3: Display results (25 pts)
# Sample data (use this if API not available)
sample_results = [
    {"name": "Rubella", "symptoms": "fever, rash"},
    {"name": "Dengue", "symptoms": "high fever, headache"}
]

# YOUR CODE HERE - Display results as a list or table



# Exercise 4: Connect to API (25 pts)
# YOUR CODE HERE - Call API when search button clicked
# API URL: http://localhost:8000/search?query=<query>



# Hint: Use these Streamlit functions:
# st.title("Title")
# st.write("Text")
# st.text_input("Label")
# st.button("Click me")
# st.json(data)
# for item in items: st.write(item)
