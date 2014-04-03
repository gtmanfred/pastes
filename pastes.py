from flask import Flask
from flask import request
from flask import render_template
from flask import make_response


import paste_funcs as pf
import pmysql

app = Flask(__name__)
domain = 'notapasteb.in'
index = """ Welcome to my pastebin.
curl -F 'p=<-' {0}
""".format(domain)

@app.route('/')
def index_py():
    response = make_response(index)
    response.headers["content-type"] = "text/plain"
    return response

@app.route('/', methods=['POST'])
def post():
    text = request.form['p']

    paste_id = pf.gen_random()
    while pmysql.lookup(paste_id).fetch_row():
        paste_id = pf.gen_random()

    pmysql.post_paste(paste_id, text)

    return 'http://{0}/{1}\n'.format(domain, paste_id)


@app.route('/<pasteid>', methods=['GET'])
def get_paste(pasteid):

    text = pmysql.lookup(pasteid)
    if text is False:
        return 'Paste id {0} not found.'.format(pasteid)
    response = make_response(text.fetch_row()[0][0])
    response.headers["content-type"] = "text/plain"
    return response


if __name__ == '__main__':
    app.run()
