
from flask import Flask

app = Flask(__name__)

@app.route('/')
def sample():
    return "Wellcome to todays webinar"
if __name__ == '__main__':
    app.run(debug = True)
    