from flask import Flask, render_template

app=Flask(__name__)




@app.route("/")
def name_ID():
    return render_template("name_ID.html")

@app.route("/profile")
def profile():
    hobby=["독서","코딩","게임"]
    return render_template("hobby.html",hobbies=hobby)


if __name__=="__main__":
    app.run(debug=True)



