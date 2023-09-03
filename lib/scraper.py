# from turtle import ht
from bs4 import BeautifulSoup
import requests

# import tkinter

headers = {"user-agent": "my-app/0.0.1"}
html = requests.get("https://flatironschool.com/", headers=headers)

doc = BeautifulSoup(html.text, "html.parser")

courses = doc.select(".heading-25-extrabold")
for course in courses:
    print(course.contents[0].strip())
