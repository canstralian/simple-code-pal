import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CODEPAL_API_KEY = os.getenv("CODEPAL_API_KEY")
CODEPAL_ENDPOINT = "https://api.codepal.ai/v1/generate"

# Configure rate limiting
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

@app.route("/")
@limiter.limit("10 per minute")
def index():
    """Render the main application page."""
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
@limiter.limit("5 per minute")
def generate():
    """
    Generate code based on user description.
    
    Expects JSON data with a 'description' field.
    Returns generated code or error message.
    """
    # Get JSON data from request
    data = request.get_json()
    description = data.get("description", "").strip()
    task_type = data.get("task_type", "").strip().lower()

    # Validate input
    if not description:
        return jsonify({"error": "Please enter a description."}), 400

    # Ensure API key is available
    if not CODEPAL_API_KEY:
        return jsonify({"error": "API key not configured."}), 500

    # Task routing
    task_functions = {
        "explain": explain_code,
        "debug": debug_code,
        "refactor": refactor_code,
        "optimize": optimize_code
    }

    if task_type not in task_functions:
        return jsonify({"error": "Invalid task type."}), 400

    try:
        return task_functions[task_type](description)
    except Exception as e:
        return jsonify({"error": f"Task processing error: {str(e)}"}), 500

def explain_code(description):
    return generate_code_from_api(description, "explain")

def debug_code(description):
    return generate_code_from_api(description, "debug")

def refactor_code(description):
    return generate_code_from_api(description, "refactor")

def optimize_code(description):
    return generate_code_from_api(description, "optimize")

def generate_code_from_api(description, task_type):
    try:
        # Prepare API request
        headers = {
            "Authorization": f"Bearer {CODEPAL_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "prompt": description,
            "task_type": task_type,
            "language": "python"  # Default to Python, could be made dynamic
        }

        # Make API request with timeout for better error handling
        response = requests.post(CODEPAL_ENDPOINT, headers=headers, json=payload, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # Extract code from response
        code = response.json().get("code", "No code returned.")
        return jsonify({"code": code})

    except requests.RequestException as e:
        # Handle network errors, timeouts, and API errors
        return jsonify({"error": f"API error: {str(e)}"}), 500

if __name__ == "__main__":
    # Use debug=False in production environments
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    app.run(debug=debug_mode, host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
