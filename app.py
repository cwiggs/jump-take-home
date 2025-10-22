import os
from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Grab env var for image tag so we can pass into the app from k8s.
image_tag = os.getenv("IMAGE_TAG", "default")
image_digest = os.getenv("IMAGE_DIGEST", "default")

# Create a route at the root URL that returns "Hello, World"
@app.route("/")
def hello():
    return f"Hello World. I was updated with CI! Image Tag: {image_tag}, Image Digest: {image_digest}"

if __name__ == "__main__":
    # Run the application on all interfaces/IPs.
    app.run(host="0.0.0.0")
