import streamlit as st
import requests

def main():
    st.title("🎬 Movie Search App")
    st.write("Enter the name of a movie to search for its details.")

    movie_name = st.text_input("Movie Name")

    if st.button("Search"):
        if movie_name:
            response = requests.get("https://freetestapi.com/api/v1/movies")
            try:
                if response.status_code == 200:
                    data = response.json()
                    # Filter movie by name
                    filtered_movies = [movie for movie in data if movie_name.lower() in movie["title"].lower()]
                    
                    if filtered_movies:
                        for movie in filtered_movies:
                            st.subheader(movie["title"])
                            st.write(f"🎭 Genre: {movie.get('genre', 'N/A')}")
                            st.write(f"📅 Release Year: {movie.get('year', 'N/A')}")
                            st.write(f"⭐ Rating: {movie.get('rating', 'N/A')}")
                            st.write(f"💲 Box Office: {movie.get('boxOffice', 'N/A')}")
                            st.write(f"🔄 Country: {movie.get('country', 'N/A')}")
                            st.write(f"🎬 Director: {movie.get('director', 'N/A')}")
                            st.write(f"🏆 Awards: {movie.get('awards', 'N/A')}")
                            st.write(f"⏲ Run Time: {movie.get('runtime', 'N/A')}")
                            st.write(f"📖 Trailer: {movie.get('trailer', 'N/A')}")

                            # Check poster key and show image only if it exists and is not empty
                            poster_url = movie.get("poster", "")
                            if poster_url:
                                st.image(poster_url, width=300)
                            else:
                                st.warning("🚫 No poster available for this movie.")
                    else:
                        st.warning("No matching movies found.")
                else:
                    st.error("Failed to fetch movies from the API.")
            except Exception as e:
                st.error("Error occurred while processing the data.")
                st.error(str(e))

if __name__ == "__main__":
    main()
