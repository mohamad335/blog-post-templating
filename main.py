from flask import Flask,render_template
import requests
import smtplib
my_email="type your email"
my_password="type password"

from flask import request
API_KEY = "https://api.npoint.io/649f1724390381724336"
response = requests.get(API_KEY)
posts = response.json()
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template("index.html", collection=posts)
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")
@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)
@app.route("/form-entry", methods=["POST"])
def receive_data():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        post= "Successfully sent message."
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=email,
             to_addrs=my_email,
             msg=f"Subject:New Message\n\nName:{name}\nEmail:{email}\nPhone:{phone}\nMessage:{message}")
    return render_template("contact.html", post=post)
        
    
            
if __name__ == "__main__":
    app.run(debug=True,host="localhost", port="5000")
