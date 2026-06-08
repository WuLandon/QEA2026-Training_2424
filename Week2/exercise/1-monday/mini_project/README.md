# Mini Project: Student Management System using Flask

## Objective

Build a Flask application that manages a list of students and supports the four basic CRUD operations:

- Create
- Read
- Update
- Delete

The application will maintain an in-memory list of students.

---

## Student Data Structure

Each student should contain the following fields:

| Field  | Type    |
| ------ | ------- |
| id     | Integer |
| name   | String  |
| course | String  |

Example:

```python
students = [
    {
        "id": 1,
        "name": "Alice",
        "course": "Computer Science"
    },
    {
        "id": 2,
        "name": "Bob",
        "course": "Data Science"
    }
]
```

---

# Requirements

## 1. View All Students

Display all students.

### Endpoint

```
GET /students
```

### Example Response

```json
[
  {
    "id": 1,
    "name": "Alice",
    "course": "Computer Science"
  },
  {
    "id": 2,
    "name": "Bob",
    "course": "Data Science"
  }
]
```

---

## 2. View a Single Student

Retrieve information for a particular student using the student ID.

### Endpoint

```
GET /students/<id>
```

Example:

```
GET /students/1
```

### Example Response

```json
{
  "id": 1,
  "name": "Alice",
  "course": "Computer Science"
}
```

Return a suitable error message if the student does not exist.

---

## 3. Add a New Student

Create a new student and add it to the list.

### Endpoint

```
POST /students
```

### Request Body

```json
{
  "name": "John",
  "course": "Artificial Intelligence"
}
```

### Expected Response

```json
{
  "id": 3,
  "name": "John",
  "course": "Artificial Intelligence"
}
```

Return HTTP status code:

```
201 Created
```

---

## 4. Update Student Information

Modify an existing student's details.

### Endpoint

```
PUT /students/<id>
```

Example:

```
PUT /students/2
```

### Request Body

```json
{
  "name": "Robert",
  "course": "Machine Learning"
}
```

### Expected Response

```json
{
  "id": 2,
  "name": "Robert",
  "course": "Machine Learning"
}
```

Return an error message if the student ID does not exist.

---

## 5. Delete a Student

Remove a student from the list.

### Endpoint

```
DELETE /students/<id>
```

Example:

```
DELETE /students/2
```

### Expected Response

```json
{
  "message": "Student deleted successfully"
}
```

---

# Project Constraints

- Use Flask.
- Store data in a Python list (no database).
- Use appropriate HTTP methods.
- Return JSON responses using `jsonify()`.
- Handle invalid student IDs gracefully.
- Use meaningful HTTP status codes.

---

# Suggested Project Structure

```
project/
│
├── app.py
└── templates/
```

---

# Stretch Goal: Web Interface with Jinja Templates

Instead of returning only JSON, create HTML pages using Jinja templates.

## Pages to Implement

### Home Page

```
GET /
```

Displays links to all operations.

---

### Student List Page

```
GET /students
```

Display all students in an HTML table.

| ID  | Name  | Course           |
| --- | ----- | ---------------- |
| 1   | Alice | Computer Science |
| 2   | Bob   | Data Science     |

---

### Add Student Form

```
GET /students/new
```

Provide a form containing:

- Name
- Course

Submit the form to create a new student.

---

### Edit Student Form

```
GET /students/edit/<id>
```

Allow users to modify student information.

---

### Delete Student Button

Provide a Delete button next to each student in the table.

---

# Bonus Challenges

1. Add input validation.
2. Prevent duplicate IDs.
3. Display custom 404 pages.
4. Use Bootstrap for styling.
5. Show success messages after create, update, and delete operations.
6. Add a search feature:

```
GET /students/search?name=alice
```

7. Store data in a JSON file so that records persist after restarting the application.

---

# Learning Outcomes

By completing this project, students will practice:

- Flask routes
- Dynamic URL parameters
- HTTP methods (GET, POST, PUT, DELETE)
- Request and response objects
- JSON APIs
- Status codes
- Jinja templates
- HTML forms
- Basic application structure
