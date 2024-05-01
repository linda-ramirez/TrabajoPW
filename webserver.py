from flask import Flask, render_template

app = Flask(" my-first-website-in-python")

if __name__ == "__main__":
 app.run(debug=True, host="0.0.0", port="5000")
 
 