import streamlit as st
from fun import *


page_lang = 'fr-FR'

# Preselect World topic

sources_container = st.sidebar.empty()

search_term = st.sidebar.text_input('Search')

topic = st.sidebar.selectbox('News topic', sorted(list(TOPIC_IDS.keys())), 2)




# create_markdown_news_topic_section(topic, feed, source)

if (len(search_term) > 0):
    
    feed = feedparser.parse(create_google_news_search_rss_url(search_term, page_lang))
    sources = get_feed_available_sources(feed)
    source = sources_container.selectbox('News source', sources, 3)

    create_markdown_news(search_term, feed, source)

else:
    
    feed = feedparser.parse(create_google_news_topic_rss_url(topic, page_lang))
    sources = get_feed_available_sources(feed)
    source = sources_container.selectbox('News source', sources, 3)

    create_markdown_news(topic, feed, source)
