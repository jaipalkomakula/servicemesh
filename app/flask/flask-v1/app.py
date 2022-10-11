from flask import Flask, render_template, url_for

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/v1')
def login():
    return render_template('v1.html')



if __name__ == '__main__':
    app.run(debug=True)



