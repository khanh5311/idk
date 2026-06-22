from flask import Flask, request

app = Flask(__name__)

PASSWORD = "mypassword123"
DRIVE_LINK = "https://drive.google.com/your-link-here"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        password = request.form.get("password")

        if password == PASSWORD:
            return f"""
            <h1>Access Granted</h1>
            <p><a href="{DRIVE_LINK}" target="_blank">Open Drive Folder</a></p>
            """
        else:
            return """
            <h1>Wrong Password</h1>
            <a href="/">Try Again</a>
            """

    return """
    <h1>Enter Password</h1>
    <form method="POST">
        <input type="password" name="password" placeholder="Password">
        <button type="submit">Submit</button>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)

