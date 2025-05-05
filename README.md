# Simple Code Pal

[![Flask](https://img.shields.io/badge/Flask-v2.3.3-blue.svg)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: PEP8](https://img.shields.io/badge/code%20style-PEP8-brightgreen.svg)](https://peps.python.org/pep-0008/)
[![Security: CSP](https://img.shields.io/badge/security-CSP-green.svg)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Maintenance](https://img.shields.io/badge/Maintained-yes-green.svg)](https://github.com/your-username/simple-code-pal/commits/main)

A minimal code generator using the Codepal.ai API. This application allows users to describe the code they need and receive generated code snippets.

![Simple Code Pal Screenshot](https://via.placeholder.com/800x450.png?text=Simple+Code+Pal+Screenshot)

## Features

- Clean, minimalist user interface
- Generate code snippets based on text descriptions
- Copy generated code to clipboard with one click
- Secure API key handling with environment variables
- Mobile-responsive design

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/your-username/simple-code-pal)
![GitHub last commit](https://img.shields.io/github/last-commit/your-username/simple-code-pal)
![Uptime Robot ratio (30 days)](https://img.shields.io/uptimerobot/ratio/m793662933-e0ff2756491c293759a5e9a9)

## Tech Stack

- **Backend**: Flask (Python) [![Flask](https://img.shields.io/badge/Flask-2.3.3-blue.svg)](https://flask.palletsprojects.com/)
- **Frontend**: HTML5, Vanilla JavaScript, CSS3 [![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow.svg)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- **Security**: API key stored in environment variables (using `python-dotenv`) [![dotenv](https://img.shields.io/badge/dotenv-1.0.0-brightgreen.svg)](https://github.com/theskumar/python-dotenv)
- **API**: [Codepal.ai](https://codepal.ai) (used securely via Flask) [![API](https://img.shields.io/badge/API-Codepal.ai-orange.svg)](https://codepal.ai)
- **Deployment**: Ready for Replit, Render, and more [![Replit Ready](https://img.shields.io/badge/Replit-ready-informational)](https://replit.com)

## Installation

### Prerequisites

- Python 3.8+ [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
- [Codepal.ai API key](https://codepal.ai) [![API Key Required](https://img.shields.io/badge/API_Key-Required-red.svg)](https://codepal.ai)

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/simple-code-pal.git
   cd simple-code-pal
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env and set your CODEPAL_API_KEY
   ```

6. Run the application:
   ```bash
   flask run
   ```

7. Open your browser and navigate to `http://127.0.0.1:5000`

## Deployment

### Replit

1. Create a new Repl and import from GitHub
2. Set the `.env` variable with your API key in Replit's Secrets tab
3. Click "Run" to start the application

### Other Platforms

The application is compatible with platforms like Render, Heroku, or Railway with minimal configuration.

## Usage

1. Enter a description of the code you need in the text area
2. Click "Generate Code" or press Ctrl+Enter
3. View the generated code snippet
4. Copy the code with the "Copy Code" button

## Security Considerations

[![Security: CSP](https://img.shields.io/badge/security-CSP-green.svg)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)
[![Security: Input Validation](https://img.shields.io/badge/security-Input_Validation-green.svg)](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
[![Security: Environment Variables](https://img.shields.io/badge/security-Environment_Variables-green.svg)](https://12factor.net/config)

- API keys are stored securely in environment variables
- Input validation is performed on both client and server sides
- Content Security Policy (CSP) implemented to prevent XSS attacks
- HTTPS recommended for all deployments

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Codepal.ai](https://codepal.ai) for providing the code generation API
- Original concept based on the Minimal Code Pal design

## Contributing

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)
[![Contributors](https://img.shields.io/github/contributors/your-username/simple-code-pal)](https://github.com/your-username/simple-code-pal/graphs/contributors)
[![Issues](https://img.shields.io/github/issues/your-username/simple-code-pal)](https://github.com/your-username/simple-code-pal/issues)
[![Open Pull Requests](https://img.shields.io/github/issues-pr/your-username/simple-code-pal)](https://github.com/your-username/simple-code-pal/pulls)

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Development Status

[![Build Status](https://img.shields.io/travis/com/your-username/simple-code-pal/main)](https://travis-ci.com/github/your-username/simple-code-pal)
[![Coverage Status](https://img.shields.io/codecov/c/github/your-username/simple-code-pal)](https://codecov.io/gh/your-username/simple-code-pal)
[![Quality Gate Status](https://img.shields.io/sonar/quality_gate/your-username_simple-code-pal?server=https%3A%2F%2Fsonarcloud.io)](https://sonarcloud.io/dashboard?id=your-username_simple-code-pal)
[![Code Quality](https://img.shields.io/codacy/grade/your-project-id)](https://www.codacy.com/gh/your-username/simple-code-pal)
[![CodeQL](https://img.shields.io/github/workflow/status/your-username/simple-code-pal/CodeQL?label=CodeQL)](https://github.com/your-username/simple-code-pal/actions/workflows/codeql-analysis.yml)
