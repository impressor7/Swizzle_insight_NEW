
#__author__ = 'ideabove01'


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
     return render_template('1.html')

@app.route("/btn1")
def btn1():
    return render_template('btn_1.html')

@app.route("/btn2")
def btn2():
    return render_template('btn_2.html')

@app.route("/btn3")
def btn3():
    return render_template('btn_3.html')

@app.route('/btn4')
def btn4():
    return render_template('btn_4.html')

if __name__ == "__main__":
        app.run()