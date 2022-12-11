from flask import Flask,jsonify,request
import csv
from storage import all_article, liked_article, not_liked_article
from demographicfiltering import output
from contentfiltering import get_recommendations

app=Flask(__name__)
@app.route("/get-article")
def get_article():
    article_data = {
        "url": all_article[0][11],
        "title": all_article[0][12],
        "text": all_article[0][13],
        "lang": all_article[0][14],
        "total_events": all_article[0][15]
    }
    return jsonify({
        "data": article_data,
        "status": "success"
    })

@app.route("/liked-article",methods=["POST"])
def liked_article():
    print(all_article[0])
    article=all_article[0]
    all_article=all_article[1:]
    liked_article.append(article)
    return jsonify({
        "status":"success"
    }),201
@app.route("/notliked-article",methods=["POST"])
def not_liked_article():
    article=all_article[0]
    all_article=all_article[1:]
    not_liked_article.append(article)
    return jsonify({
        "status":"success"
    }),201
@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for article in liked_article:
        output = get_recommendations(article[4])
        for data in output:
            all_recommended.append(data)
    all_recommended.sort()
    article_data = []
    for recommended in all_recommended:
        art = {
            "url": recommended[0],
            "title": recommended[1],
            "text": recommended[2],
            "lang": recommended[3],
            "total_events": recommended[4]
        }
        article_data.append(art)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 201
if __name__=="__main__":
    app.run()