from flask import Flask, render_template

app=Flask(__name__)




@app.route("/")
def name_ID():
    return render_template("name_ID.html")



if __name__=="__main__":
    app.run(debug=True)



