# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 18:34:38 2022

@author: Rashi Khandelwal
"""
import streamlit as st
import pickle
import pandas
import requests

mov=pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


def recommend(movie):
    index = mov[mov['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies=[]
    recommended_poster=[]
    for i in distances[1:6]:
        mov_id=mov.iloc[i[0]].movie_id
        recommended_movies.append(mov.iloc[i[0]].title)
        recommended_poster.append(fetch_poster(mov_id))
    return recommended_movies, recommended_poster
        
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=2fa688227dabc8d48fab8df6a04a6587&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

st.title('Movie Recommender System')
selected_movie_name=st.selectbox(
    "Type or select a movie from the dropdown",
    mov['title'].values)

if st.button('Show Recommendation'):
    # rec_lst=recommend(selected_movie_name)
    # for i in rec_lst:
    #     st.write(i)
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
