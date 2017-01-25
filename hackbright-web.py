from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    project_info = hackbright.get_grades_by_github(github)
   
    return render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           project_info=project_info, 
                           )
    

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add")
def student_add():
    """Display form to add a student."""

    return render_template("student_creation.html")


@app.route("/add_acknowledgement", methods=['POST'])
def submit_form():
    """Display add student form output"""

    first = request.form.get('first', 'No first name')
    last = request.form.get('last', 'No last name')
    github = request.form.get('github', 'No github')
    hackbright.make_new_student(first, last, github)

    return render_template("add_student_confirm.html",
                           first=first,
                           last=last,
                           github=github)


    


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
