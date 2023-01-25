import streamlit as st
from tmp import *

# st.markdown('## World News')
# st.markdown('### BBC')
# st.markdown('[Ukraine war crisis going on](https://www.bbc.co.uk)')

# Preselect World topic
topic = st.sidebar.selectbox('News topic', sorted(list(TOPIC_IDS.keys())), 2)

feed = feedparser.parse(create_google_news_topic_rss_url(topic))

sources = get_feed_available_sources(feed)

# Preselect Guardian as default sourcew
source = st.sidebar.selectbox('News source', sources, 3)

create_markdown_news_topic_section(topic, feed, source)
