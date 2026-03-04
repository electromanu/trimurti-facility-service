from flask import Flask, render_template, request,redirect
from flask_mail import Mail, Message

app = Flask(__name__)

# Email Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'electromanu123@gmail.com'
app.config['MAIL_PASSWORD'] = 'uqfznqlnniyayggz'  # Use Gmail App Password

mail = Mail(app)


# Home Page (Only shows page)
@app.route("/")
def home():
    return render_template("index.html")


# Contact Form Submission
@app.route("/contact", methods=["POST"])
def contact():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    msg = Message(
        subject="New Contact Form Message",
        sender=app.config['MAIL_USERNAME'],   # always use your email
        recipients=["manohara8123@gmail.com"]
    )

    msg.body = f"""
    Name: {name}
    Email: {email}
    Phone: {phone}
    Message: {message}
    """

    mail.send(msg)

    return redirect("/")


@app.route("/service")
def service():
    return render_template("service.html")


if __name__ == "__main__":
    app.run(debug=True)