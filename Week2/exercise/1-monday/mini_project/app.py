from typing import Dict, List, Optional

from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)

students: List[Dict] = [
    {"id": 1, "name": "Alice", "course": "Computer Science"},
    {"id": 2, "name": "Bob", "course": "Data Science"},
]


def find_student(student_id: int) -> Optional[Dict[str, str]]:
    return next((student for student in students if student["id"] == student_id), None)


def create_student(name: str, course: str) -> Dict[str, str]:
    next_id = max((student["id"] for student in students), default=0) + 1
    student = {"id": next_id, "name": name, "course": course}
    students.append(student)
    return student


def update_student_record(student: Dict[str, str], name: str, course: str) -> Dict[str, str]:
    student["name"] = name
    student["course"] = course
    return student


def delete_student_record(student: Dict[str, str]) -> None:
    students.remove(student)


@app.get("/students")
def display_students():
    wants_html = request.accept_mimetypes["text/html"] > request.accept_mimetypes["application/json"]
    if wants_html:
        return render_template("students.html", students=students)

    return jsonify(students)


@app.get("/")
def home():
    return render_template("home.html")


@app.get("/students/new")
def new_student_form():
    return render_template("student_form.html", student=None, form_action=url_for("create_student_form"))


@app.post("/students/new")
def create_student_form():
    name = request.form.get("name", "").strip()
    course = request.form.get("course", "").strip()

    if not name or not course:
        return render_template(
            "student_form.html",
            student={"name": name, "course": course},
            form_action=url_for("create_student_form"),
            error="name and course are required",
        ), 400

    create_student(name, course)
    return redirect(url_for("display_students"))


@app.get("/students/<int:student_id>")
def view_student(student_id: int):
    student = find_student(student_id)
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student)


@app.post("/students")
def add_student():
    payload = request.get_json(silent=True) or {}
    name = payload.get("name")
    course = payload.get("course")

    if not name or not course:
        return jsonify({"error": "name and course are required"}), 400

    student = create_student(name, course)
    return jsonify(student), 201


@app.get("/students/edit/<int:student_id>")
def edit_student_form(student_id: int):
    student = find_student(student_id)
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return render_template("student_form.html", student=student, form_action=url_for("update_student_form", student_id=student_id))


@app.post("/students/edit/<int:student_id>")
def update_student_form(student_id: int):
    student = find_student(student_id)
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    name = request.form.get("name", "").strip()
    course = request.form.get("course", "").strip()

    if not name or not course:
        return render_template(
            "student_form.html",
            student={"id": student_id, "name": name, "course": course},
            form_action=url_for("update_student_form", student_id=student_id),
            error="name and course are required",
        ), 400

    update_student_record(student, name, course)
    return redirect(url_for("display_students"))


@app.put("/students/<int:student_id>")
def update_student(student_id: int):
    student = find_student(student_id)
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    payload = request.get_json(silent=True) or {}
    name = payload.get("name")
    course = payload.get("course")

    if not name or not course:
        return jsonify({"error": "name and course are required"}), 400

    return jsonify(update_student_record(student, name, course))


@app.post("/students/delete/<int:student_id>")
def delete_student_form(student_id: int):
    student = find_student(student_id)
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    delete_student_record(student)
    return redirect(url_for("display_students"))


@app.delete("/students/<int:student_id>")
def delete_student(student_id: int):
    student = find_student(student_id)
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    delete_student_record(student)
    return jsonify({"message": "Student deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
