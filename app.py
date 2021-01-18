from flask import Flask
from flask import render_template
from flask import request
from judge_level import calc

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        scores = request.form["score"]
        times = request.form["time"]
    
        new_scores = int(scores)
        if 100 < new_scores or new_scores < 0 or None:
            sentence = "得点は０から１００の数値を入力してください"
            return render_template("form.html", sentences=sentence)
        new_times = int(times)
        if 24 < new_times or new_times < 0 or None:
            jikan = "学習時間は０から24の数値を入力してください"
            return render_template("form.html", jikans=jikan)    
        level = calc(new_scores, new_times)
        return render_template("result.html", levels=level)
    else:
        return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)