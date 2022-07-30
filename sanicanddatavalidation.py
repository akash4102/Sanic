from pydantic import BaseModel


class Student(BaseModel):
    name: str
    grade: str
    roll: int
    email: str
    phone: int
    subjects: List[str]
    friends: List[str]


student = Student(
    name=in_memory_student_db[0]["name"],
    grade=in_memory_student_db[0]["grade"],
    roll=in_memory_student_db[0]["roll"],
    email=in_memory_student_db[0]["email"],
    phone=in_memory_student_db[0]["phone"],
    subjects=in_memory_student_db[0]["subjects"],
    friends=in_memory_student_db[0]["friends"]
)


@app.post("/")
async def post_student(request):
    student = Student(**request.json)
    in_memory_student_db.append(student.dict())
    return response.json({"message" : "inserted"}, {"data": student.dict()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True, auto_reload=True)