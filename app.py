from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_view():
		return "<h1>Welcome to eagle_programming Instagram page</h1>"


if __name__ == "__main__":
        app.run()
