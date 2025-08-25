from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

students = [
    {"id": 1, "name": "Madhumitha", "course": "Python"},
    {"id": 2, "name": "Henna", "course": "Java"}
]

next_id = 3

@app.route('/')
def index():
    return render_template("index.html", students=students)

@app.route("/addStudent",methods = ["GET","POST"])
def add():
    global next_id
    if request.method == "POST":
        name = request.form['name']
        course = request.form["course"]

        students.append({"id":next_id,"name":name,"course":course})
        next_id+=1
        return redirect(url_for("index"))
    return render_template ("add.html")

@app.route('/edit/<int:stu_id>',methods = ["GET","POST"])
def edit(stu_id):
    student = next((s for s in students if s["id"]==stu_id),None)
    if not student:
        return "Student no found"
    if request.method=="POST":
        student["name"] = request.form["name"]
        student["course"] = request.form["course"]
        return redirect(url_for("index"))
    return render_template("edit.html",student = student)

@app.route('/delete/<int:stu_id>')
def dele(stu_id):
    global students
    students = [s for s in students if s['id']!=stu_id]
    return redirect(url_for("index"))
if __name__ == "__main__":
    app.run(debug=True)