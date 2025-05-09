import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.set_page_config(page_title="Web Scraper", page_icon="🌐")

st.title("🌐 Simple Web Scraper Tool")
st.write("Enter a website URL and an HTML tag to extract content from the page.")

# User input
url = st.text_input("Enter website URL (e.g., https://books.toscrape.com)")
tag = st.text_input("Enter HTML tag to extract (e.g., p, h1, a, img)")

if st.button("Scrape"):
    if not url or not tag:
        st.warning("Please enter both URL and tag.")
    else:
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            if tag == 'a':
                elements = soup.find_all('a', href=True)
                data = [{"Link": a['href']} for a in elements]
                df = pd.DataFrame(data)
            elif tag == 'img':
                elements = soup.find_all('img', src=True)
                data = [{"Image URL": img['src']} for img in elements]
                df = pd.DataFrame(data)
            else:
                elements = soup.find_all(tag)
                data = [{"Content": el.get_text(strip=True)} for el in elements]
                df = pd.DataFrame(data)

            if df.empty:
                st.error("No elements found for the given tag.")
            else:
                st.success(f"Found {len(df)} elements.")
                st.dataframe(df)
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button("📥 Download CSV", data=csv, file_name='scraped_data.csv', mime='text/csv')

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Error fetching the website: {e}")
        except Exception as e:
            st.error(f"❌ Unexpected error: {e}")
