import streamlit as st
from bs4 import BeautifulSoup
import requests

st.title("Web Scraper — E-commerce Products")

base_url = "https://webscraper.io/test-sites/e-commerce/static"
st.write(f"**Base URL:** {base_url}")

add_category = st.radio("Do you want to add Category?", ["No", "Yes"], horizontal=True)

url = base_url

if add_category == "Yes":
    category = st.radio("Select Category", ["computers", "phones"], horizontal=True)
    url = f"{base_url}/{category}"

    add_subcategory = st.radio("Do you want to add Subcategory?", ["No", "Yes"], horizontal=True)

    if add_subcategory == "Yes":
        if category == "computers":
            subcategory = st.radio("Select Subcategory", ["laptops", "tablets"], horizontal=True)
        elif category == "phones":
            subcategory = st.radio("Select Subcategory", ["touch"], horizontal=True)

        url = f"{base_url}/{category}/{subcategory}"

st.write(f"Final Scraping URL: **{url}**")

if st.button("Scrape Now"):
    try:
        html_template = requests.get(url).text
        soup = BeautifulSoup(html_template, 'lxml')

        products = soup.find_all('div', class_='product-wrapper card-body')

        if not products:
            st.warning("No products found. Try another combination.")

        for product in products:
            product_image = product.img['src']
            product_descriptio = product.find('div', class_='caption')
            product_name = product_descriptio.find('a', class_='title').text.strip()
            product_price = product_descriptio.h4.span.text
            product_ratting = product.find('div', class_='ratings').p.span.text
            product_details = product_descriptio.find('a', class_='title')['href']

            st.write("----")
            st.image("https://webscraper.io" + product_image)
            st.write(f"**Name:** {product_name}")
            st.write(f"Price:** {product_price}")
            st.write(f"Rating:** {product_ratting}")
            st.write(f"Details:** https://webscraper.io{product_details}")

    except Exception as e:
        st.error(f"Error: {e}")
