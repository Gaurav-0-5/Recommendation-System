import pickle
import streamlit as st
import requests
import numpy as np
st.title("top movies")
popular=pickle.load(open('popular_v.pkl', 'rb'))
movie_name=list(popular['title'].values)
mid=list(popular['id'].values)
def fetch_poster(movie_id):
 url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
 data = requests.get(url)
 data = data.json()
 poster_path = data['poster_path']
 full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
 return full_path
def top(num):
    name=[]
    for i in num:
         name.append(popular.iloc[i].title)
         image.append(fetch_poster(mid[i]))
    return name,image
mno= int(st.number_input(
'type no. of top movies',step=5))
if st.button('Show movies'):
 for i in range(0,mno,5):
  cols = st.columns(5)
  cols[0].image(fetch_poster(mid[i]))
  cols[0].text(movie_name[i])
  cols[1].image(fetch_poster(mid[i+1]))
  cols[1].text(movie_name[i+1])
  cols[2].image(fetch_poster(mid[i+2]))
  cols[2].text(movie_name[i+2])
  cols[3].image(fetch_poster(mid[i+3]))
  cols[3].text(movie_name[i+3])
  cols[4].image(fetch_poster(mid[i+4]))
  cols[4].text(movie_name[i+4])