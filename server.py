from flask import Flask, render_template, request, redirect, session

app = Flask( __name__ )
app.secret_key = "veryMuchSecret"

@app.route( "/", methods=['GET'] )
def survey():
    return render_template( "index.html" )

@app.route( '/process', methods=['POST'] )
def addInfoProcess():
    session['userName'] = request.form['userName']
    session['dojoLocation'] = request.form['dojoLocation']
    session['favLanguage'] = request.form['favLanguage']
    session['userComments'] = request.form['userComments']
    return redirect('/viewInfo')

@app.route('/viewInfo')
def sucess():
    return render_template('result.html')



if __name__ == "__main__":
    app.run( debug = True )