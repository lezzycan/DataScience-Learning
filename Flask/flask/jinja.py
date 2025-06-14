from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/submit", methods = ["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form['name']
        return f"Hello{name}"
    return render_template("form.html")


## Variable rule
@app.route('/successres/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    
    exp = {"score" : score, "result" : res}    
    return render_template("result.html", results = exp)

if __name__ == "__main__":
    app.run(debug=True)