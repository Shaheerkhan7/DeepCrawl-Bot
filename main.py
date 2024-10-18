import streamlit as st
from scrape import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content
)
from parse import parse_with_ollama
from annotated_text import annotated_text

st.title("DeepCrawl Bot")  

annotated_text(
    "DeepCrawl Bot is a ",
    ("web scraping tool", "built with Streamlit"),
    " that allows users to ",
    ("scrape", "automatically extract"),
    " and ",
    ("parse", "analyze"),
    " website content. It ",
    ("cleans", "removes unnecessary elements"),
    " the extracted data and lets you ",
    ("filter", "specify what information to extract"),
    " the content using AI.",
    " Ideal for those who need to ",
    ("gather", "collect data"),
    " and ",
    ("analyze", "extract insights from"),
    " web information efficiently."
)




url = st.text_input("Enter a Website URL:")

if st.button("Scrape Site"):
    st.write("Scraping the website...") 

 
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)


    st.session_state['dom_content'] = cleaned_content


    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)