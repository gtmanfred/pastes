from flask import Flask
from flask import request
from flask import render_template

import paste_funcs as pf
import pmysql

app = Flask(__name__)
domain = 'localhost'

@app.route('/')
def my_form():
    return 'Welcome to my pastebin.'


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['p']
    paste_id = ''
    while not paste_id is False:
        paste_id = pf.gen_random()

    pmysql.post_paste(paste_id, text)

    return 'http://{0}/{1}'.format(domain, paste_id)


@app.route('/<pasteid>', methods=['GET'])
def get_paste(pasteid):
    text = pmysql.lookup(pasteid)
    if text is False:
        return 'Paste id {0} not found.'.format(pasteid)
    return text

if __name__ == '__main__':
    app.run()
