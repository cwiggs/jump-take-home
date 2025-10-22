import os
from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Grab env var for image tag so we can pass into the app from k8s.
node_name = os.getenv("NODE_NAME", "default")
pod_ip = os.getenv("POD_IP", "default")

# Create a route at the root URL that returns "Hello, World"
@app.route("/")
def hello():
    return f"Hello World. I was updated with CI! Running on node: {node_name}, pod IP: {pod_ip}\n"

if __name__ == "__main__":
    # Run the application on all interfaces/IPs.
    app.run(host="0.0.0.0")
