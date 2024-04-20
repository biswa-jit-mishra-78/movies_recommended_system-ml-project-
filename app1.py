import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=fc588a7a2fc1cfb000708d075296c010'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']
def recommend(movie):
    movie_index=movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]
    recommended_movie = []
    recommended_movie_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie,recommended_movie_posters
    
movies_list = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarit.pkl','rb'))

st.title('Movies Recommended System..')
select_movies_name=st.selectbox('how would u like to be contacted?',(movies['title'].values))

if st.button('recommend'):
    name,posters = recommend(select_movies_name)
    st.text(name[0])
    st.image(posters[0])
    st.link_button(name[0])
    st.text(name[1])
    st.image(posters[1])
    st.text(name[2])
    st.image(posters[2])
    st.text(name[3])
    st.image(posters[3])
    # col1,col2,col3,col4,col5 = st.beta_columns(5)
    # with col1:
    #     st.text(name[0])
    #     st.image(posters[0])
    # with col2:
    #     st.text(name[1])
    #     st.image(posters[1])
    # with col3:
    #     st.text(name[2])
    #     st.image(posters[2])
    # with col4:
    #     st.text(name[3])
    #     st.image(posters[3])
    # with col5:
    #     st.text(name[4])
    #     st.image(posters[4])