from flask import Flask, render_template, request, redirect, url_for
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)



# List posts from /content directory
@app.route('/')
def index():
    content_dir = os.path.join(os.path.dirname(__file__), '../content')
    posts = []
    for fname in os.listdir(content_dir):
        if fname.endswith('.md'):
            with open(os.path.join(content_dir, fname), 'r') as f:
                title = f.readline().strip('#').strip()
            posts.append({'filename': fname, 'title': title})
    posts.sort(key=lambda x: x['filename'], reverse=True)
    return render_template('index.html', posts=posts)


@app.route('/test')
def test():
    return 'Test'

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)


# Generate a new post in /content directory
@app.route('/generate', methods=['POST'])
def generate():
    content_dir = os.path.join(os.path.dirname(__file__), '../content')
    from datetime import datetime
    now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    fname = f'{now}-generated-post.md'
    with open(os.path.join(content_dir, fname), 'w') as f:
        f.write(f'# Generated Post\n\nThis post was generated at {now}.\n\nDate: {now[:10]}')
    return redirect(url_for('index'))
