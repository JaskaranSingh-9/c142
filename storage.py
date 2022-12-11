import csv

all_article = []

with open("article.csv",encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_article = data[1:]

liked_article = []
not_liked_article = []