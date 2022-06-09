from flask import Flask, render_template, request, session
import sqlite3 as sq
app=Flask(__name__)

friends= ["Raksa", "Eva", "Manasi", "Harshini", "Mohan"]
for friend in friends:
    print(friend)

@app.route('/')
def home():
    return render_template('app1.html', l = len(friends), friends=friends)




if __name__=="__main__":
    app.run(debug=True)  