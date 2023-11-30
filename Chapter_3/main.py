import streamlit as st
from Views import FeedView, AddPostView
from Services import * #GetFeed, AddPost

AddPostView(add_post)
st.write("___")
FeedView(get_feed)

