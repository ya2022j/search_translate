




from flask import Flask,render_template


app = Flask(__name__)



@app.route("/")
def index():

    return render_template("index.html")


if __name__ == "__main__":
    app.run()


# gunicorn -w 4 -b 0.0.0.0:8001 --access-logfile access.log --error-logfile error.log to_run_st:app -D