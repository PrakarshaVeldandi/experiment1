from flask import Flask

app = Flask(_name_)

def add(a, b):
    return a + b

@app.route("/")
def home():
    return "Addition: " + str(add(5, 3))

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
