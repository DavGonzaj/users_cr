from flask import Flask, render_template, redirect, request  # Import Flask to allow us to create our app
from users import User

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('read.html',users=User.get_all())  # Return the string 'Hello World!' as a response

## MORE ROUTES HERE 

@app.route('/user/new')
def new():
    return render_template("create.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.