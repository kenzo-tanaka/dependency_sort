import requests
from bs4 import BeautifulSoup

class DepStarSort:
    def dep_url(self, url):
        return(f"{url}/network/dependents")
    
    def get_html(self):
        return("<!DOCTYPE html>")