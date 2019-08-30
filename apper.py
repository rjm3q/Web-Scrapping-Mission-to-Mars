import sys
from flask import Flask, render_template, jsonify, redirect
import pymongo
from config import nonsense

app= Flask(__name__)

app.config['MONGO_URI'] = f'mongodb+srv://robert.mabry86@mail.com:{nonsense}@cluster0-wadjd.mongodb.net/test?retryWrites=true&w=majority'
mongo= PyMongo(app)

@app.route("/scrape")
def scraper():
    import Scraper
    mars_db= mongo.db.mars
    mars_data= Scraper.scrape()
    mars_db.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

@app.route("/")
def index():
    mars_data= mongo.db.mars.find_one()
    return render_template('index.html', mars_data = mars_data)


if __name__ == "__main__":
    app.run(debug=True)