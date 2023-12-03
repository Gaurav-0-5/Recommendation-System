import streamlit as st
st.sidebar.success('select a page above')
st.markdown("""
<style>
.big-font {
font-size:100px !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="big-font">Recommender System</p>', unsafe_allow_html=True)
st.header('here we have movies and book recommender system')
st.write('here we are giving top no. of movies and books')
st.write('recommender system recommends book on the basis of name of the book entered')
st.write('movies recommender works same as book recommender')