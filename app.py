t = '''<h1>First Edition Auctions</h1>
            <table>
            <tr>
            <th>Author</th>
            <th>Title</th>
            <th class="money">Reserve Price</th>
            <th class="money">Current Bid</th>
            </tr>
            <tr>
            <td>E.E. Cummings</td>
            <td>Tulips & Chimneys</td>
            <td class="money">$2,000.00</td>
            <td class="money">$2,642.50</td>
            </tr>
            <tr class="even">
            <td>Charles d'Orleans</td>
            <td>Poemes</td>
            <td class="money"></td>
            <td class="money">$5,866.00</td>
            </tr>
            <tr>
            <td>T.S. Eliot</td>
            <td>Poems 1909 - 1925</td>
            <td class="money">$1,250.00</td>
            <td class="money">$8,499.35</td>
            </tr>
            <tr class="even">
            <td>Sylvia Plath</td>
            <td>The Colossus</td>
            <td class="money"></td>
            <td class="money">$1031.72</td>
            </tr>
            </table>
            <style>
            body {
            font-family: Arial, Verdana, sans-serif;
            color: #111111;}
            table {
            width: 600px;}
            th, td {
            padding: 7px 10px 10px 10px;}
            th {
            text-transform: uppercase;
            letter-spacing: 0.1em;
            font-size: 90%;
            border-bottom: 2px solid #111111;
            border-top: 1px solid #999;
            text-align: left;}
            tr.even {
            background-color: #efefef;}
            tr:hover {
            background-color: #c3e6e5;}
            .money {
            text-align: right;}
            </style>'''
from flask import Flask
from flask import request
from flask import make_response
app = Flask(__name__)
@app.route('/')
def home():
    return t
@app.route('/user_agent')
def user():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)
@app.route('/res')
def r():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response
@app.route('/information')
def info():
    return "<h1>Puppies are cute?</h1>", 400
@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>Upper case: {}</h1>".format(name.upper())
@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    if name[-1] != 'y':
        res = name + 'y'
    else:
        res = name[:-1] + 'ful'
    return res
if __name__ == '__main__':
    app.run(port=5000, debug=True)