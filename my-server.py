from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
   return " you called \n"

# curl -d "text=Hello!&param2=value2" -X POST http://localhost:5000/echo
@app.route("/echo", methods=['POST'])
def echo():
   return "You said: " + request.form['text']

@app.route("/factors", methods=["GET"])
def factors():
    try:
        n = int(request.args.get("number"))
    except:
        return "Error: Please provide ?number=<integer>", 400

    result = []
    while n % 2 == 0:
        result.append(2)
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            result.append(p)
            n //= p
        p += 2
    if n > 1:
        result.append(n)

    return {"factors": result}

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)