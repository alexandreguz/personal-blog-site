import smtplib

from flask import Flask, render_template, request
import requests

response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
all_posts = response.json()

app = Flask(__name__)

@app.route("/about")
def get_about():
    return render_template("about.html")

@app.route("/footer")
def footer():
    return render_template("footer.html")

@app.route("/header")
def header():
    return render_template("header.html")

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


@app.route("/contact", methods=["POST", "GET"])
def get_contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="guzalexandre@gmail.com",
                msg=f"Subject:New Message For You from {name} \n\n message from:{name} \n email: {email} \n {phone} \n {message}"
            )


        return render_template("contact.html")


    else:
        return render_template("contact.html")

MY_EMAIL  = "wolfweissenshwarts@gmail.com"
MY_PASSWORD = "pszl evjt ypak bxsh"




if __name__ == "__main__":
    app.run(debug=True)
