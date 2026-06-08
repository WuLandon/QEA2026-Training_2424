from typing import Dict, List, Optional

from flask import Flask, jsonify, request

app = Flask(__name__)

students: List[Dict] = [
    {"id": 1, "name": "Alice", "course": "Computer Science"},
    {"id": 2, "name": "Bob", "course": "Data Science"},
]


def find_student(student_id: int) -> Optional[Dict[str, str]]:
    return next((student for student in students if student["id"] == student_id), None)


@app.get("/students")
def display_students():
    return jsonify(students)


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

    next_id = max((student["id"] for student in students), default=0) + 1
    student = {"id": next_id, "name": name, "course": course}
    students.append(student)

    return jsonify(student), 201


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

    student["name"] = name
    student["course"] = course
    return jsonify(student)


@app.delete("/students/<int:student_id>")
def delete_student(student_id: int):
    student = find_student(student_id)
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    students.remove(student)
    return jsonify({"message": "Student deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
