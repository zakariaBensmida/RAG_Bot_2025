# web_loader.py - Scrape Website Data
from langchain_community.document_loaders import WebBaseLoader
import bs4

def load_web_content(url):
    loader = WebBaseLoader(
        web_paths=(url,),
        bs_kwargs=dict(parse_only=bs4.SoupStrainer(class_=("post-content", "post-title")))
    )
    return loader.load()

