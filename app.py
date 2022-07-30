# from sanic import Sanic,text,response

# app=Sanic("helloworld")

# # @app.route('/')
# # def handle_request(request):
# #    return response.html('<p>Hello Sanic!</p>')
# # @app.route("/")
# # async def home(request):
# #    return response.text("Hello Sanic")
# @app.route('/form')
# async def form(request):
#    print(request.args)
#    return response.text("Reading request")
# @app.route('/')
# def handle_request(request):
#    return response.file('index.html')

# @app.route("/myhomepage")
# async def homepage(request):
#     return text("my home page")

# @app.route("/myurl")
# async def myurl(request, methods=['GET' , 'POST']):
#    return text("My home page2!")

# app.static('/floral_image.jpg','E:/Sanic/floral_image.jpg')
# app.static('/result','E:/Sanic/first year result (Akash Verma).pdf')

# @app.route('/items/<what>')
# async def item_handler(request, what):
# #    var='Item - {}'.format(what)
#    var=f'Item - {what}'
# #    print('Item - {}'.format(what))
#    print(var)
#    return response.text(var)
# if __name__=='__main__':
#     app.run(host='0.0.0.0',port=5005,debug=True)

# app.py
# from sanic import Sanic, response
# app = Sanic(__name__)

# @app.route('/welcome/<item>')
# async def welcome_handler(request,item):
#    user = request.args['user'][int(item)]
#    html = '<h2>Welcome ' + user + '!</h2>'
#    return response.html(html)

# if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=8000, debug=True)


from sanic import Sanic,response
from sanic.response import json

app = Sanic(__name__)

in_memory_student_db = [
    {
        "name": "Akash verma",
        "grade": "9",
        "roll no": 1,
        "email": "aakashverma4102@gmail.com",
        "phone no": "9818032019",
        "subjects": ["maths", "english", "hindi", "physics", "chemistry", "computer science"],
        "friends": ["sachin", "vipin", "anand", "vikash", "vinay", "harsh"]
    }
]

# @app.get("/")
# async def get_student(request):
#     return response.json(in_memory_student_db)

@app.get("/")
async def get_student(request):
    id_ = request.args.get("id")
    if id_:
        if int(id_) in range(len(in_memory_student_db)):
            return response.json(in_memory_student_db[int(id_)])
        else:
            return response.json(
                {
                "status": "error",
                "message": f"data with id {id_} not found. Try with different id!!!"
                }
            )
    return response.json(in_memory_student_db)

@app.post("/")
async def post_student(request):
    student = request.json
    in_memory_student_db.append(student)
    return response.json(student)

# @app.put("/<id_:int>")
# async def update_student(request,id_):
#     student = request.json
#     in_memory_student_db[id_] = student
#     return response.json(student)
@app.put("/<id_:int>")
async def update_student(request,id_):
    student = request.json
    if id_ in range(len(in_memory_student_db)):
        in_memory_student_db[id_] = student
    else:
        return response.json({"error":"No Student with given id"})
    return response.json(student)

# @app.delete("/<id_:int>")
# async def delete_student(request,id_):
#     del in_memory_student_db[id_]
#     return response.json({"message":"Deleted student successfully"})

@app.delete("/<id_:int>")
async def delete_student(request,id_):
    if id_ in range(len(in_memory_student_db)):
        del in_memory_student_db[id_]
    else:
        return response.json({"error": "No Student with given id"})
    return response.json({"message": "Deleted student successfully"})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True, auto_reload=True)
