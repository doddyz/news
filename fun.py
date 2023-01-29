# Resolve Sources selection issue: either with checkbox or else as variables in bg
# See how to integrate sub topics cleanly, either as extra options in the topics selector. Create a tabbed approach if pages don't work well
# Make all pages show same widgets, search for all etc...
# Redirect to fr page by default or hide homepage 


import feedparser
import streamlit as st

BASE_RSS_HOME_URL = 'https://news.google.com/rss'

BASE_RSS_TOPIC_URL = 'https://news.google.com/rss/topics/'

BASE_RSS_SEARCH_URL = 'https://news.google.com/rss/search?q='

PREFERRED_SOURCES = {

    'gb': ['BBC', 'The Guardian', 'The Independent', 'Evening Standard']
    
}

TOPIC_IDS = {
        
    'Business': 'CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKSFFpZ0FQAQ',
    'Local': 'CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE',
    'Science': 'CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp0Y1RjU0JXVnVMVWRDR2dKSFFpZ0FQAQ',
    'Sports' : 'CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKSFFpZ0FQAQ',
    'Technology': 'CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSFFpZ0FQAQ',
    'Top Stories' : 'CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSFFpZ0FQAQ',
    'United Kingdom' : 'CAAqJQgKIh9DQkFTRVFvSUwyMHZNRGR6YzJNU0JXVnVMVWRDS0FBUAE',
    'World' : 'CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSFFpZ0FQAQ'
    
    }

TOPIC_SECTION_IDS = {

    'Tennis' : 'CAQiSkNCQVNNUW9JTDIwdk1EWnVkR29TQldWdUxVZENHZ0pIUWlJT0NBUWFDZ29JTDIwdk1EZGljekFxQ2dvSUVnWlVaVzV1YVhNb0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EWnVkR29TQldWdUxVZENHZ0pIUWlnQVABUAE'

    }

def create_google_news_home_rss_url(lang):
    return BASE_RSS_HOME_URL + '?hl=' + lang


def create_google_news_topic_rss_url(topic, lang):
    return BASE_RSS_TOPIC_URL + TOPIC_IDS[topic] + '?hl=' + lang


def create_google_news_topic_section_rss_url(topic, section, lang):
    return BASE_RSS_TOPIC_URL + '/topics/' + TOPIC_SECTION_IDS[section] + '?hl=' + lang


def create_google_news_search_rss_url(search_term, lang):
    return BASE_RSS_SEARCH_URL + search_term.replace(' ', '%20') + '&hl=' + lang


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
        

        

    
        
        
    






    
    
        
        


