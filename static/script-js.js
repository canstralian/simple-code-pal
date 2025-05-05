/**
 * Simple Code Pal - Frontend JavaScript
 * Handles user interaction and API communication
 */

// DOM Elements
const generateBtn = document.getElementById("generateBtn");
const descriptionField = document.getElementById("description");
const codeOutput = document.getElementById("code-output");
const copyBtn = document.getElementById("copyBtn");
const statusMessage = document.getElementById("status-message");
const taskSelector = document.getElementById("taskSelector");

/**
 * Shows a status message to the user
 * @param {string} message - Message to display
 * @param {string} type - Message type (error or success)
 */
function showStatus(message, type = "") {
  statusMessage.textContent = message;
  statusMessage.className = "status";
  if (type) {
    statusMessage.classList.add(type);
  }
  
  // Clear message after a delay if it's a success message
  if (type === "success") {
    setTimeout(() => {
      statusMessage.textContent = "";
      statusMessage.className = "status";
    }, 3000);
  }
}

/**
 * Handles the code generation process
 * Makes API request and updates UI with result
 */
async function generateCode() {
  const description = descriptionField.value.trim();
  const taskType = taskSelector.value.trim().toLowerCase();
  
  // Validate input
  if (!description) {
    showStatus("Please describe the code you want.", "error");
    return;
  }

  // Update UI to show loading state
  generateBtn.disabled = true;
  generateBtn.textContent = "Generating...";
  codeOutput.textContent = "";
  copyBtn.hidden = true;
  showStatus("Generating code...");

  try {
    // Make API request
    const response = await fetch("/generate", {
      method: "POST",
      headers: { 
        "Content-Type": "application/json",
        // CSRF token would be added here in a production app
      },
      body: JSON.stringify({ description, task_type: taskType })
    });

    const data = await response.json();
    
    // Handle API response
    if (!response.ok) {
      throw new Error(data.error || `Error: ${response.status}`);
    }
    
    // Update UI with generated code
    if (data.code) {
      codeOutput.textContent = data.code;
      copyBtn.hidden = false;
      showStatus("Code generated successfully!", "success");
    } else {
      showStatus("No code was returned. Try rephrasing your description.", "error");
    }
  } catch (error) {
    // Handle errors
    console.error("Generation error:", error);
    showStatus(`Failed to generate code: ${error.message}`, "error");
    codeOutput.textContent = "";
  } finally {
    // Reset button state
    generateBtn.disabled = false;
    generateBtn.textContent = "Generate Code";
  }
}

/**
 * Copies generated code to clipboard
 * Updates UI to provide feedback
 */
async function copyToClipboard() {
  try {
    // Use the clipboard API to copy text
    await navigator.clipboard.writeText(codeOutput.textContent);
    
    // Provide feedback
    copyBtn.textContent = "Copied!";
    showStatus("Code copied to clipboard!", "success");
    
    // Reset button text after delay
    setTimeout(() => {
      copyBtn.textContent = "Copy Code";
    }, 2000);
  } catch (error) {
    console.error("Copy failed:", error);
    showStatus("Failed to copy code.", "error");
  }
}

// Event Listeners
generateBtn.addEventListener("click", generateCode);
copyBtn.addEventListener("click", copyToClipboard);

// Also trigger generation when user presses Enter in textarea
descriptionField.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && event.ctrlKey) {
    event.preventDefault();
    generateCode();
  }
});

// Initialize the app
document.addEventListener("DOMContentLoaded", () => {
  // Focus on description field when page loads
  descriptionField.focus();
  
  // Check if the necessary APIs are available
  if (!navigator.clipboard) {
    console.warn("Clipboard API not available");
  }
});
