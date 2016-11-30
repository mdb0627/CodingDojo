from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=['POST'])
def result():

   your_name = request.form['your_name']
   dojo_location = request.form['dojo_location']
   favorite_language = request.form['favorite_language']
   comment = request.form['comment']

   return render_template("result.html", your_name= your_name, dojo_location = dojo_location, favorite_language =favorite_language, comment = comment)

@app.route('/GoBack', methods=['POST'])
def GoBack():

   return redirect('/')
app.run(debug=True) # run our server
