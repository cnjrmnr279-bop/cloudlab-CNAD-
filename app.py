from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    user_message = ""
    
    # Handle data sent from the HTML form
    if request.method == "POST":
        user_name = request.form.get("username")
        user_message = f"Hello, {user_name}! Your data reached app.py."

    # Render index.html and pass Python variables into it
    return render_template("index.html", title="My Python Web App", message=user_message)

if __name__ == "__main__":
    app.run(debug=True)

