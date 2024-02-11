# importing Flask and other modules
from flask import Flask, request, render_template, redirect, url_for

import random, logging

logging.basicConfig(filename='ssb.log', encoding='utf-8', level=logging.DEBUG)
logging.info("App started")

# Flask constructor
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def name():
    logging.info("new request from "+request.remote_addr)
    if request.method == "POST":
        # getting message from HTML form
        name = request.form.get("name")
        message = request.form.get("message")
        #trim message if needed
        if len(message) > 64:
            message=message[:64]
        #UPDATE THIS FUNCTION
        logging.info("new form input")
        logging.info("username: "+name)
        logging.info("password: "+message)
        return redirect(
            url_for('success', username=name, money = random.randint(0,1000000)))
    else:
        return render_template(
            "index.html",
        )

@app.route("/success")
def success():
     # access the result in the tempalte, for example {{ result.name }}
     username = request.args.get('username')
     money = request.args.get('money')
     if(money == None or username == ""):
         logging.warning("invalid username or money detected")
         return redirect(url_for('name'))
     return render_template('success.html', username = username, money = money)


if __name__ == '__main__':
    app.run()
