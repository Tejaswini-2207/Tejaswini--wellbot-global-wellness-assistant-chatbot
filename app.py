from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

users = []


# Home
@app.route("/")
def home():
    return "WellBot Backend is Running 💚"


# Register
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    user = {
        "name": data.get("name"),
        "email": data.get("email"),
        "password": data.get("password")
    }

    users.append(user)

    return jsonify({"message": "User registered successfully"})


# Login
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    for user in users:
        if user["email"] == data.get("email") and user["password"] == data.get("password"):
            return jsonify({"message": "Login successful"})

    return jsonify({"message": "Invalid email or password"}), 401


# Chat
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message")

    if message and "stress" in message.lower():
        reply = "Try deep breathing and take a short walk."
    else:
        reply = "I am your WellBot. How can I help you?"

    return jsonify({"reply": reply})


# Test route (for browser testing)
@app.route("/test")
def test():
    users.append({
        "name": "Tejaswini",
        "email": "teja@gmail.com",
        "password": "1234"
    })
    return "Test user added"

@app.route("/ui")
def ui():
    return render_template("index.html")


# Run server (only once)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


