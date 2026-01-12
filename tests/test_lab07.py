"""
Lab 07: Streamlit Search UI - Auto-grading Tests

Note: Streamlit apps are difficult to test automatically.
This test file checks for basic code structure.
"""

import pytest
import os
import ast

# Get paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_PATH = os.path.join(BASE_DIR, 'exercise', 'app.py')


@pytest.fixture(scope="session")
def app_source():
    """Read the app.py source code."""
    with open(APP_PATH, 'r', encoding='utf-8') as f:
        return f.read()


@pytest.fixture(scope="session")
def app_ast(app_source):
    """Parse the app.py into AST."""
    return ast.parse(app_source)


class TestExercise1:
    """Test Exercise 1: Page Title and Header (25 points)"""
    
    def test_streamlit_imported(self, app_source):
        assert 'import streamlit' in app_source or 'from streamlit' in app_source, \
            "Streamlit should be imported"
    
    def test_title_used(self, app_source):
        assert 'st.title' in app_source, "st.title should be used for page title"


class TestExercise2:
    """Test Exercise 2: Search Input (25 points)"""
    
    def test_text_input_used(self, app_source):
        assert 'st.text_input' in app_source, "st.text_input should be used for search input"


class TestExercise3:
    """Test Exercise 3: Display Results (25 points)"""
    
    def test_display_method_used(self, app_source):
        has_display = ('st.write' in app_source or 
                      'st.json' in app_source or 
                      'st.dataframe' in app_source or
                      'st.table' in app_source)
        assert has_display, "Should use st.write, st.json, st.dataframe, or st.table to display results"


class TestExercise4:
    """Test Exercise 4: Connect to API (25 points)"""
    
    def test_requests_or_button(self, app_source):
        has_api = ('requests' in app_source or 
                  'st.button' in app_source or
                  'httpx' in app_source)
        assert has_api, "Should use requests library or st.button for API interaction"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
