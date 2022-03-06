from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "keep it safe"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dojo', methods=['POST'])
def submit():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    return redirect('/post')

@app.route('/post')
def posted():
    return render_template("post.html")

if __name__ == "__main__":
    app.run(debug=True)