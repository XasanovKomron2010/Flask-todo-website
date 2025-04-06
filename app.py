from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

TODOS = [
    {
        "id": 1,
        "title": "first title",
        "description": "first description"
    }
]
    
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html", todos = TODOS)

@app.route("/delete/<id>", methods=["POST"])
def delete_page(id):
    for todo in TODOS:
        if todo.get('id') == int(id):
            TODOS.remove(todo)
            return redirect(url_for('home_page'))

@app.route("/update/<id>", methods=["POST"])
def update_page(id):
    for todo in TODOS:
        if todo.get("id") == int(id):
            todo.update({"id":int(request.form['id']), 'title':request.form['title'], 'description':request.form['description']})
            return redirect(url_for('home_page'))

@app.route('/create', methods=['POST'])
def create_page():
    TODOS.append({"id": int(request.form['id']), "title":request.form['title'], 'description':request.form['description']})
    return redirect(url_for('home_page'))

if __name__ == '__main__':
    app.run(debug=True)