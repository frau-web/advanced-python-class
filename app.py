from flask import Flask, request
from ie_utils import tokenize

app = Flask(__name__) #way of identifiyng name of the application 
# __name__ will take a different value depending on whether you import or run it

@app.route("/") #decorate function, this line makes the route of the web application
# for this url, use this function
def home():
    return "Hello World!" 

@app.route("/tokenize")
def do_tokenize():
    print(request.args) 
    sentence=request.args["sentence"] #("sentence","")
    lower = request.args.get("lower",False)
    return str(tokenize(sentence, lower=lower))
# tokenize would return a list, but we need either a string or dict, so we turn it into a string