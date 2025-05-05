# Pushing the Simple Code Pal to GitHub

Follow these instructions to push the Simple Code Pal application to GitHub:

## 1. Create Local Repository

First, let's create a local directory for the project and initialize it as a Git repository:

```bash
# Create a directory for the project
mkdir simple-code-pal
cd simple-code-pal

# Initialize Git repository
git init
```

## 2. Create Project Structure

Create the following folder structure:

```
simple-code-pal/
├── static/
├── templates/
```

```bash
# Create directories
mkdir static templates
```

## 3. Add Project Files

Add all the files we've created:

1. `app.py` in the root directory
2. `requirements.txt` in the root directory
3. `.env.example` in the root directory
4. `.gitignore` in the root directory
5. `README.md` in the root directory
6. `static/style.css` in the static directory
7. `static/script.js` in the static directory
8. `templates/index.html` in the templates directory

Copy the code from each artifact into the respective files.

## 4. Create .env File (Not for Git)

Create a `.env` file with your actual API key:

```bash
# Create .env file (this won't be committed due to .gitignore)
echo "CODEPAL_API_KEY=your_actual_api_key_here" > .env
echo "FLASK_APP=app.py" >> .env
echo "FLASK_DEBUG=False" >> .env
```

## 5. Stage and Commit Files

Add and commit all the files to the local repository:

```bash
# Add all files to staging
git add .

# Verify what's being committed (should NOT include .env)
git status

# Make initial commit
git commit -m "Initial commit: Simple Code Pal application"
```

## 6. Connect to GitHub Repository

Now connect your local repository to the GitHub repository:

```bash
# Add the remote repository URL (replace with your actual GitHub username)
git remote add origin https://github.com/your-username/simple-code-pal.git

# Verify the remote was added
git remote -v
```

## 7. Push to GitHub

Push your code to GitHub:

```bash
# Push to the main branch
git push -u origin main
```

If your default branch is called "master" instead of "main", use:

```bash
git push -u origin master
```

## 8. Verify on GitHub

Go to your GitHub account and verify that the repository has been updated with all the files.

## Additional Setup (Optional)

To make your repository more complete, you might want to:

1. Add a proper LICENSE file from GitHub's interface
2. Configure GitHub Pages to host a demo (for static content)
3. Set up GitHub Actions for continuous integration

## Testing the Application Locally

Before or after pushing to GitHub, you can test the application locally:

```bash
# Activate virtual environment (if you haven't already)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
flask run
```

Open your browser and navigate to `http://127.0.0.1:5000` to see the application in action.

## Running Tests

To run the tests using `pytest`, follow these steps:

1. Ensure you have installed the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the tests:
   ```bash
   pytest
   ```

## Setting Up Rate Limiting

To set up rate limiting using Flask-Limiter, follow these steps:

1. Install the Flask-Limiter package:
   ```bash
   pip install Flask-Limiter
   ```

2. Configure rate limiting rules in `app.py` to limit requests per user or IP address.

3. Apply rate limiting to specific routes using decorators.

4. Customize error messages for rate limit exceedance.
