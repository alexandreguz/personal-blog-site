from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
all_posts = response.json()

app = Flask(__name__)

@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact")
def get_contact():
    return render_template("contact.html")


@app.route("/footer")
def footer():
    return render_template("footer.html")

@app.route("/header")
def header():
    return render_template("header.html")


@app.route("/post")
def get_posts():
    return render_template("post.html")


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=all_posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
