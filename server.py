from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'visits' not in session:
        session['visits'] = 0
    session['visits'] += 1
    return render_template("index.html")

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/addtwo')
def addtwo():
    session['visits'] += 1
    return redirect('/')

@app.route('/custom', methods=['POST'])
def custom():
    session['visits'] += int(request.form['add_visits']) - 1
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)