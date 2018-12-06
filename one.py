#!/usr/bin/env python

#look at readme.txt for details

from flask import Flask, jsonify
import requests as req
app = Flask(__name__)

@app.route('/trends/<search>/<size>')
def simple(search, size):
    if search is None:
        return jsonify({'error': 'empty search'})
    if size is None:
        # could also use some standard size in this case
        return jsonify({'error': 'no result size given'})
    # to get close to /trending i chose param sort=stars
    res = req.get('https://api.github.com/search/repositories', 
                  params={'q': search, 
                          'per_page': size,
                          'sort': 'stars'})
    rwatch, rstar = 0, 0
    for repo in res.json()['items']:
        rwatch += repo['watchers_count']
        rstar += repo['stargazers_count']
    return jsonify({'sum of watchers': rwatch,
                    'sum of stars': rstar})
