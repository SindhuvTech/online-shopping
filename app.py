from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Online Shopping</title>
    </head>
    <body>
        <h1>Welcome to Online Shopping 🛒</h1>

        <h2>Our Products</h2>

        <p>T-Shirt - ₹599</p>
        <p>Shoes - ₹999</p>
        <p>Headphones - ₹799</p>
        <p>Smart Watch - ₹1499</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)