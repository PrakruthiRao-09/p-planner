from flask import Flask, render_template, request, session
import sqlite3 as sq

app=Flask(__name__)
app.config["SECRET_KEY"]="APDA12349"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["GET","POST"])
def login():
    return render_template('login.html')

@app.route('/user_validation', methods=["POST"])
def user_validation():
    username=request.form.get("username")
    password=request.form.get("password")
    return_value=verify_user(username, password)
    if return_value==True:
        session["authenticated"]=True
        return render_template('loginsuccess.html',username=username)
    else:
        session["authenticated"]=False

        return render_template('loginfailure.html')
    # with sq.connect("todo.db") as conn:
    #       cur=conn.cursor()
    #       message = "OPERATION FAILED"
    #       cur.execute("SELECT * from user where username =? and password =?", (username, password))
    #       rows = cur.fetchall()
    #       for row in rows:
    #         message = "OPERATION IS SUCCESFULL"
    # if message == "OPERATION IS SUCCESFULL":
    #     return render_template('loginsuccess.html',message=message)
    # else:    
    #     return render_template('loginfailure.html',message=message)
def verify_user(username, password):
    loginsuccess=False
    conn=sq.connect("todo.db")
    conn.row_factory=sq.Row
    cur=conn.cursor()
    cur.execute("SELECT password from user WHERE username =?", [username])
    records = cur.fetchall()
    dbpassword=""
    for record in records:
        dbpassword=record[0]
    if dbpassword==password:
        loginsuccess=True
    else:
        loginsuccess=False
    return loginsuccess

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup_user', methods=["POST"])
def signup_user():
    user=request.form.get("username")
    password=request.form.get("password")
    confirmpassword=request.form.get("confirmpassword")
    email=request.form.get("email")
    with sq.connect("todo.db") as conn:
        cur=conn.cursor()
        cur.execute("INSERT into user(username, password, confirmpassword, email) VALUES(?, ?, ?, ?)",(user, password, confirmpassword, email))
        conn.commit()
        print("CHANGES ARE COMITTED")
        message="OPERATION IS SUCCESFULL"
    return render_template('signupsuccess.html',message=message)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/create_task')
def create_task():
    return render_template('create_task.html')
@app.route('/add_task', methods=["POST", "GET"])
def add_task():
    task_name=request.form.get("task_name")
    priority=request.form.get("priority")
    status=request.form.get("status")
    with sq.connect("Todo.db") as conn:
        cur=conn.cursor()
        print("Database Connected")
        cur.execute("INSERT INTO todo(task_name, priority, status)values(?,?,?);",(task_name, priority, status))
        conn.commit()
        print("Commited")
        message="Your changes are saved successfully"
    conn.close()
    return render_template('tasks.html', message=message)

@app.route('/view_todo', methods=["POST", "GET"])
def view_todo():
    conn=sq.connect("Todo.db") 
    conn.row_factory=sq.Row
    cur=conn.cursor()
    cur.execute("SELECT * from todo")
    records=cur.fetchall()
    print(records)
    return render_template("view_todo.html", records=records)

@app.route('/aboutme', methods=["GET","POST"])
def aboutme():
    return render_template('aboutme.html')

@app.route('/deletetodo')
def deletetodo():
    id=request.args.get("id")
    conn=sq.connect("Todo.db") 
    conn.row_factory=sq.Row
    cur=conn.cursor()
    cur.execute("DELETE from todo where id=?",[id])
    conn.commit()
    message="Your task has been deleted"
    return render_template('deletetodo.html', message=message)

if __name__=="__main__":
    app.run(debug=True)  