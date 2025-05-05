#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Code Pal - Minimal code generator using Codepal.ai API.
Author: [Your Name]
License: MIT
"""

import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CODEPAL_API_KEY = os.getenv("CODEPAL_API_KEY")
CODEPAL_ENDPOINT = "https://api.codepal.ai/v1/generate"

@app.route("/")
def index():
    """Render the main application page."""
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    """
    Generate code based on user description.
    
    Expects JSON data with a 'description' field.
    Returns generated code or error message.
    """
    # Get JSON data from request
    data = request.get_json()
    description = data.get("description", "").strip()

    # Validate input
    if not description:
        return jsonify({"error": "Please enter a description."}), 400

    # Ensure API key is available
    if not CODEPAL_API_KEY:
        return jsonify({"error": "API key not configured."}), 500

    try:
        # Prepare API request
        headers = {
            "Authorization": f"Bearer {CODEPAL_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "prompt": description,
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
