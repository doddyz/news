# Next finalise G News options by testing custom topics like tennis, maths, marketing related etc ...
# L'information et l'anticipation, make this one private, see which one is currently private


import feedparser
import streamlit as st

# https://news.google.com/rss
BASE_RSS_TOPIC_URL = 'https://news.google.com/rss/topics/'

BASE_RSS_SEARCH_URL = 'https://news.google.com/rss/search?q='

PREFERRED_SOURCES = {}

TOPIC_IDS = {
    
    'United Kingdom' : 'CAAqJQgKIh9DQkFTRVFvSUwyMHZNRGR6YzJNU0JXVnVMVWRDS0FBUAE',
    'World' : 'CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSFFpZ0FQAQ',
    'Sports' : 'CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKSFFpZ0FQAQ'
    
    }


def create_google_news_topic_rss_url(topic, lang):
    return BASE_RSS_TOPIC_URL + TOPIC_IDS[topic] + '?hl=' + lang


def create_google_news_search_rss_url(search_term, lang):
    return BASE_RSS_SEARCH_URL + search_term + '&hl=' + lang


def get_feed_available_sources(feed):

    sources = []
    
    for entry in feed.entries:
        
        entry_source = entry.source.title
        if entry_source not in sources:
            sources.append(entry_source)
            
    return sources


def create_markdown_news(topic_or_search_term, feed, source):

    st.markdown(f'# {topic_or_search_term}')
    st.markdown(f'### {source}')
    
    for entry in feed.entries:

        if (entry.source.title == source):

            # Get rid of source name in the entry title
            trimmed_title = entry.title.split(' - ')[0]
            
            st.markdown(f'##### [{trimmed_title}]({entry.link})')


def create_markdown_news_topic_section(topic, feed, source):

    st.markdown(f'# {topic}')
    st.markdown(f'### {source}')
    
    for entry in feed.entries:

        if (entry.source.title == source):

            # Get rid of source name in the entry title
            trimmed_title = entry.title.split(' - ')[0]
            
            st.markdown(f'##### [{trimmed_title}]({entry.link})')
        

        

    
        
        
    






    
    
        
        


