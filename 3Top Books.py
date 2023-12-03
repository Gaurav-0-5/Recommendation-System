import pickle
import streamlit as st
import requests
import numpy as np
st.title("top books")
popular_b=pickle.load(open('popular.pkl','rb'))
book_name=list(popular_b['Book-Title'].values)
book_author=list(popular_b['Book-Author'].values)
image=list(popular_b['Image-URL-M'].values)
mno= int(st.number_input(
'type no. of top books',step=5
))
if st.button('Show books'):
  for i in range(0,mno,5):
   cols = st.columns(5)
   cols[0].image(image[i])
   cols[0].text(book_name[i])
   cols[0].text(book_author[i])
   cols[1].image(image[i+1])
   cols[1].text(book_name[i+1])
   cols[1].text(book_author[i+1])       
   cols[2].image(image[i+2])
   cols[2].text(book_name[i+2])
   cols[2].text(book_author[i+2])
   cols[3].image(image[i+3])
   cols[3].text(book_name[i+3])
   cols[3].text(book_author[i+3])
   cols[4].image(image[i+4])
   cols[4].text(book_name[i+4])
   cols[4].text(book_author[i+4])