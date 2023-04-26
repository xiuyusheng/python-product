from flask  import Flask,render_template
app=Flask(__name__)

@app.route('/')
def hello():
    return '你好胡楼'

@app.route('/test/<name>')
def hello_(name):
    return '你好胡,%s'%name

@app.route('/index')
def index():
    return render_template("index.html",val='\(@^0^@)/ ')

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port='52273')


