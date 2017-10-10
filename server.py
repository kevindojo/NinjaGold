from flask import Flask, render_template, request, redirect, session
app = Flask (__name__)

app.secret_key ="22"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process():
    if request.form['building'] == 'farm':
        import random
        session ['gold'] = random.randrange(10,21)
        session ['total'] = session ['total'] + session['gold']
        print "farm gold: " , session['gold']
        session['text'] = 'Earned :' , session['gold'] , "gold from the farm"

    if request.form['building'] == 'cave':
        import random
        session ['gold'] = random.randrange(5,11)
        session ['total'] = session ['total'] + session['gold']
        print "Cave gold: " , session['gold']
        session['text'] = 'Earned :' , session['gold'] , "gold from the Cave"


    if request.form['building'] == 'house':
        import random
        session ['gold'] = random.randrange(2,6)
        session ['total'] = session ['total'] + session['gold']
        print "House gold: " , session['gold']
        session['text'] = 'Earned :' , session['gold'] , "gold from the House"


    if request.form['building'] == 'casino':
        import random
        session ['gold'] = random.randrange(-50,51)
        if session ['gold'] < 0:
            session ['total'] = session['total'] + session['gold']
            session ['text'] = "You loss", session ['gold'], "gold from the Casino.... ouch"
        else:
            session ['text'] = "You won", session ['gold'], "gold from the Casino...Hurray!"
            session ['total'] = session ['total'] + session['gold']
        print "Casino gold: " , session['gold']
        
    return redirect ('/')








app.run(debug=True)