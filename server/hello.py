from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '''
<h2>Hey Brad!,</h2>
<p>Im running on a raspberry pi hanging off of Monas desk!</p> 
<a href="https://photos.app.goo.gl/1TqwaGiVPQgjFjf4A"'>Click Here</a>
'''

app.run()