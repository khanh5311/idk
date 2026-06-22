from flask import Flask, request

app = Flask(__name__)

PASSWORD = "AMOGUS"
DRIVE_LINK = "https://drive.google.com/drive/folders/1P8IYpVY-rthaoM7gAuxt2h__lP40BYEa?fbclid=IwY2xjawSmJctleHRuA2FlbQIxMABicmlkETFzOGdVWnRHSjhyM0tjaE01c3J0YwZhcHBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHtTUYRpYeLXEfj4Ry_OyaCtY1vImTG2vryTb5PnfsTAi0Y10-46IfAeGha3p_aem_SQKMeKyPL9savMFPBnpXLw"

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
