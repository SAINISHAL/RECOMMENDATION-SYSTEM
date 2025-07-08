import streamlit as st
import pickle
import pandas as pd
def recommend(movie):
    movie_index = movies[movies["original_title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        movie_id=i[0]
        recommended_movies.append(movies.iloc[i[0]].original_title)
    return recommended_movies

movies_list=pickle.load(open("movies_dict.pkl","rb"))
movies=pd.DataFrame(movies_list)
similarity=pickle.load(open("similarity.pkl","rb"))
st.title("Movie Recomendation")
selected_movie_list=st.selectbox("Select Movie for Recommandations",
                                 movies["original_title"].values)
if st.button("recommend"):
    recommendations=recommend(selected_movie_list)
    for i in recommendations:
        st.write(i)