import sys
from datetime import datetime

from flask import Flask, render_template, render_template_string

from flask_frozen import Freezer
from flask_flatpages import (
    FlatPages, pygmented_markdown, pygments_style_defs)

def prerender_jinja(text):
    """ Pre-renders Jinja templates before markdown. """
    prerendered_body = render_template_string(text)
    return pygmented_markdown(prerendered_body)

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_HTML_RENDERER = prerender_jinja
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

# === URL Routes === #

@app.route('/')
def index():
    page = pages.get_or_404('index')
    return render_template('pages/index.html', page=page)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('pages/page.html', page=page)

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}

# === Main function  === #

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', port=8000)
