import pickle
import streamlit as st
import requests
import numpy as np
st.set_page_config(
page_title="Book Recommender System"
)
pt=pickle.load(open('pt.pkl','rb'))
similarity_scores=pickle.load(open('similarity_scores.pkl','rb'))
st.title("Book Recommender System")
books=pickle.load(open('books.pkl','rb'))
#book_list1=books.drop_duplicates('title')
book_list=pt.index.values
def recommend(book_name):
 # index fetch
 index1 = np.where(pt.index == book_name)[0][0]
 similar_items = sorted(list(enumerate(similarity_scores[index1])), key=lambda x: x[1], reverse=True)[1:6]
 book_title=[]
 book_author=[]
 book_image=[]

 for i in similar_items:
     temp_df = books[books['title'] == pt.index[i[0]]]
     name = temp_df.drop_duplicates('title')
     book_title.append(name.iloc[0].title)
     book_author.append(name.iloc[0].author)
     book_image.append(name.iloc[0].image)
 return book_image,book_author,book_title


selected_book = st.selectbox(
"Type or select a book from the dropdown",
book_list
)
if st.button('Show Recommendation'):
 book_image, book_author, book_title = recommend(selected_book)
 col1, col2, col3, col4, col5 = st.columns(5)
 with col1:
  st.image(book_image[0])
  st.text(book_title[0])
  st.text(book_author[0])
 with col2:
  st.image(book_image[1])
  st.text(book_title[1])
  st.text(book_author[1])
 with col3:
  st.image(book_image[2])
  st.text(book_title[2])
  st.text(book_author[2])
 with col4:
  st.image(book_image[3])
  st.text(book_title[3])
  st.text(book_author[3])
 with col5:
  st.image(book_image[4])
  st.text(book_title[4])
  st.text(book_author[4])
