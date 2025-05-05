# Simple Code Pal

A minimal code generator using the Codepal.ai API. This application allows users to describe the code they need and receive generated code snippets.

![Simple Code Pal Screenshot](https://via.placeholder.com/800x450.png?text=Simple+Code+Pal+Screenshot)

## Features

- Clean, minimalist user interface
- Generate code snippets based on text descriptions
- Copy generated code to clipboard with one click
- Secure API key handling with environment variables
- Mobile-responsive design

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, Vanilla JavaScript, CSS3
- **Security**: API key stored in environment variables (using `python-dotenv`)
- **API**: [Codepal.ai](https://codepal.ai) (used securely via Flask)

## Installation

### Prerequisites

- Python 3.8+
- [Codepal.ai API key](https://codepal.ai)

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

- API keys are stored securely in environment variables
- Input validation is performed on both client and server sides
- Content Security Policy (CSP) implemented to prevent XSS attacks

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Codepal.ai](https://codepal.ai) for providing the code generation API
- Original concept based on the Minimal Code Pal design

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
