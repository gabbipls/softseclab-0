from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hello", methods=["GET"]) 
def helloworld():
    return jsonify({"message": "Hello, World!"})

if __name__ == "__main__":
    #changed so it runs on all interfaces and port 5000 JUST FOR NOW!
    app.run(host="0.0.0.0", port=5000)

