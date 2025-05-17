
from flask import Flask, render_template, redirect, url_for, request, jsonify, abort

app = Flask(__name__, template_folder="client/templates", static_folder="client/static")

@app.route('/')
def LandingPage():

    return 'hi'
@app.errorhandler(Exception)
def handle_all_errors(e):
    return redirect(url_for('LandingPage'))

if __name__ == "__main__":
    app.run() 
