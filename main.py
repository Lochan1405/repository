from flask import Flask, render_template, request, url_for
import requests
all_posts= requests.get("https://api.npoint.io/733f017ca5882ae2c664").json()
app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts = all_posts)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST"])
def contact():
    if request.method=="POST":
        return "Message successfully sent!!!"
    else:
        return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
