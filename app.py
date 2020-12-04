from flask import Flask, render_template, request

#import auth as auth (to use everything in file)
# or 
# from auth import <Class> (to use everything in Class)

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        output = ""
    else:
        output = request.form['phrase']
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run()    