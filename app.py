import pickle
import streamlit as st
import requests
st.header("Movie Recommendation System using Machine Learning")
st.subheader("Legal Adherence: This website uses TMDB datasets but is not endorsed, certified, or otherwise approved by TMDB.")
movies= pickle.load(open("artifacts\movie_list.pkl","rb" ))
similarity= pickle.load(open("artifacts\similarity.pkl","rb"))
movie_list= movies['title'].values
selected_movie= st.selectbox(
    "Type or select your desired movie to get further recommendation! 🎥🍿",
    movie_list
)

def recommend(movie):
    index= movies[movies['title']==movie].index[0]
    distances=sorted(list(enumerate(similarity[index])), reverse=True, key= lambda x:x[1])
    recommended_movie_names=[]
    for i in distances[1:6]:
        movie_id= movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names


if st.button("Here are the closest match(es) to your selected movie! Happy watching! 🙌🏻🥤🍿"):
    recommended_movie_names= recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
    with col2:
        st.text(recommended_movie_names[1])
    with col3:
        st.text(recommended_movie_names[2])
    with col4:
        st.text(recommended_movie_names[3])
    with col5:
        st.text(recommended_movie_names[4])

