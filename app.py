import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open("C:\\Users\\chira\\OneDrive\\Desktop\\New folder\\major projects\\movie recommend system\\movies.pkl", 'rb'))
movies = pd.DataFrame.from_dict(movies_dict)
st.title("Movie Recommender System")

option = st.selectbox("Select a movie:", movies['title'].values)