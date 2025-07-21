from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/test')
def test():
    return 'Test'

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

@app.route('/trigger', methods=['POST'])
def trigger():
    os.system(f"""curl -X POST -H "Accept: application/vnd.github.v3+json" -H "Authorization: token $GHTOKEN" https://api.github.com/repos/IgnatMaldive/micro-bothinone/dispatches -d '{{"event_type":"create-dated-file"}}'""")
    return 'OK'
