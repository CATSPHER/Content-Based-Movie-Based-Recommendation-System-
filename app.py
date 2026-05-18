import streamlit as st
import pickle
import requests

def movie_poster(movie_id):
    url = "https://api.kinocheck.com/movies?tmdb_id={}".format(movie_id)
    data=requests.get(url)
    data=data.json()
    trailer=data.get("trailer")
    if trailer and "thumbnail" in trailer:
        return trailer["thumbnail"]

    return "data:image/png;base64,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"


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    moviess_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in moviess_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        movie_id=movies.iloc[i[0]].id
        #fetch poster from API
        recommended_movies_posters.append(movie_poster(movie_id))


    return recommended_movies,recommended_movies_posters

movies=pickle.load(open('movies.pkl','rb'))
movies_list=movies['title'].values

similarity=pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies_list,
)

if st.button("Recommend"):
    recommendations,poster=recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommendations[0])
        st.image(poster[0])

    with col2:
        st.text(recommendations[1])
        st.image(poster[1])

    with col3:
        st.text(recommendations[2])
        st.image(poster[2])

    with col4:
        st.text(recommendations[3])
        st.image(poster[3])

    with col5:
        st.text(recommendations[4])
        st.image(poster[4])
