from flask import Flask, request
app=Flask(__name__)
@app.route('/upper')
def upper_fun():
    #return "welcome to the upper page"
    a= request.args.get('a')#/upper?a=hello
    return a.upper()
if __name__ == '__main__':
    app.run() 