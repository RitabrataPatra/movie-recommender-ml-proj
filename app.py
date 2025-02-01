import streamlit as st
import  pandas as pd
import pickle

movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl' , 'rb'))


def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    m_website_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movie_id_list=[]
    for each_movie in m_website_list:
        each_movie_id = movies_list.iloc[each_movie[0]].movie_id

        recommended_movie_id_list.append(each_movie_id)
        recommended_movies.append(movies_list.iloc[each_movie[0]].title)

    return recommended_movies, recommended_movie_id_list





st.title("Movie :blue[Recommender] System 💻")
selected_title_name = st.selectbox(
    "So , what suits your interests?",
    movies_list['title'].values,
    index=None,
    placeholder="Select any movie...",
)
if st.button("Recommend"):
    st.write("You selected " , selected_title_name)
    recommendations = recommend(selected_title_name)

    st.subheader("Top 5 :blue[Recommendations] 👇")
    titles , posters = recommendations
    for i in titles :
        st.write(i)
