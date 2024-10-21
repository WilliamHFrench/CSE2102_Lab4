from flask import Flask, request

app = Flask(__name__)

authAccounts ={"id" : "william.french@uconn.edu",
               "token": "token123"
}

@app.route("/")
def hello():
   return " you called \n"

# curl -d "text=Hello!&param2=value2" -X POST http://localhost:5000/echo
@app.route("/echo", methods=['POST'])
def echo():
   return "You said: " + request.form['text']

@app.route('/auth', methods=['POST'])
def login():
   print(request.form)
   if request.form['id'] in authAccounts["id"]:
      if request.form['token'] == authAccounts['token']:
         return "Yes a match"
      else:
         return "No match"
      return "nothing"


if __name__ == "__main__":
   app.run(host='0.0.0.0')
