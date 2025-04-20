import streamlit as st
import requests

def movie_seach():
    st.title("Movie Search")
    st.write("Enter the name of a movie to search for its details.")

    # Input field for movie name
    movie_name = st.text_input("Movie Name")

    if st.button("Search"):
        if movie_name:
            # Call the API to get movie details
            response = requests.get("  https://freetestapi.com/api/v1/movies")

            try:
                data = response.json()
                
                

print(movie_seach())