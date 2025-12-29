import datetime
import requests
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/guess/<string:username>')
def blog(username):
    genderize_api_url = "https://api.genderize.io"
    agify_api_url = "https://api.agify.io"

    parameters = {
        "name": username,
    }

    genderize_response = requests.get(genderize_api_url, params=parameters)
    genderize_response.raise_for_status()
    genderize_gender = genderize_response.json()["gender"]

    agify_response = requests.get(agify_api_url, params=parameters)
    agify_response.raise_for_status()
    agify_age = agify_response.json()["age"]


    current_year = datetime.datetime.now().year
    return render_template("index.html", current_year=current_year,
                           username=username, age=agify_age,
                           gender=genderize_gender)


@app.route('/blog')
def get_blogs():
    blog_api_url = "https://api.npoint.io/bd47aada8fa910734160"
    blog_response = requests.get(blog_api_url)
    blog_response.raise_for_status()
    all_blogs = blog_response.json()

    return render_template("blog.html", all_blogs=all_blogs)


@app.route('/post/<int:num>')
def get_post(num):
    blog_api_url = "https://api.npoint.io/bd47aada8fa910734160"
    response = requests.get(blog_api_url)
    all_posts = response.json()

    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == num:
            requested_post = blog_post

    return render_template("post.html", post=requested_post)

if __name__ == '__main__':
    app.run(debug=True)



