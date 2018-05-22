from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsASecretDontTellAnyone'
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
  session['name'] = request.form['name']
  session['location'] = request.form['location']
  session['lang'] = request.form['lang']
  session['comment'] = request.form['comment']
  validation = False

  if len(session['name']) < 2:
    print('The name field needs a longer name')
    validation = True

  if len(session['name']) > 30:
    print("That name is too long")
    validation = True
  
  if len(session['comment']) > 200:
    print("That is too many characters")
    validation = True

  if validation == True:
    return redirect('/')
  else:
    return render_template('result.html')



app.run(debug=True)