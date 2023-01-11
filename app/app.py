from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def start_page():
    return render_template('index.html')


@app.route('/second')
def another_page():
    return render_template('second.html')


@app.route('/third')
def actually_another_page():
    return render_template('third.html')


@app.route('/fourth')
def not_last_page():
    return render_template('fourth.html')


@app.route('/fifth')
def last_page():
    return render_template('fifth.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
