import streamlit as st
from fun import *


page_lang = 'es-ES'

sources_container = st.sidebar.empty()

search_term = st.sidebar.text_input('Search')

# Preselect Top Stories
topic = st.sidebar.selectbox('News topic', sorted(list(TOPIC_IDS.keys())), 5)


if (len(search_term) > 0):
    
    feed = feedparser.parse(create_google_news_search_rss_url(search_term, page_lang))
    sources = get_feed_available_sources(feed)
    source = sources_container.radio('News source', sources)

    create_markdown_news(search_term, feed, source)

else:
    
    feed = feedparser.parse(create_google_news_topic_rss_url(topic, page_lang))
    sources = get_feed_available_sources(feed)
    source = sources_container.radio('News source', PREFERRED_SOURCES[page_lang])

    create_markdown_news(topic, feed, source)
