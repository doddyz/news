import streamlit as st
from fun import *


page_lang = 'es-ES'

# Preselect World topic
topic = st.sidebar.selectbox('News topic', sorted(list(TOPIC_IDS.keys())), 2)

feed = feedparser.parse(create_google_news_topic_rss_url(topic, page_lang))

sources = get_feed_available_sources(feed)

# Preselect Guardian as default sourcew
source = st.sidebar.selectbox('News source', sources, 3)

create_markdown_news_topic_section(topic, feed, source)
