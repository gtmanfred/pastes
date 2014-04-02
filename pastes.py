from flask import Flask
from flask import request
from flask import render_template

import paste_funcs as pf
import pmysql

app = Flask(__name__)
domain = 'localhost'

@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['p']
    paste_id = ''
    while not paste_id is False:
        paste_id = pf.gen_random()

    pmysql.post_paste(paste_id, text)

    return 'http://{0}/{1}'.format(domain, paste_id)


if __name__ == '__main__':
    app.run()
