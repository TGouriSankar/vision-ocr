# Vision-OCR Project

In this project, I have utilized the Llama 3.2-Vision model to process and extract text from images effectively. The model was executed using Ollama, ensuring seamless integration and efficient text recognition.


Configuring Ollama with Environment Variables

Ollama can be configured to work with environment variables for different systems. Here's how to set them up depending on your platform:

Ollama server can be configured with environment variables.
Setting environment variables on Linux

If Ollama is run as a macOS application, environment variables should be set using launchctl:

  For each environment variable, call launchctl setenv.

    launchctl setenv OLLAMA_HOST "0.0.0.0:11434"

    Restart Ollama application.

Setting environment variables on Linux

If Ollama is run as a systemd service, environment variables should be set using systemctl:

  Edit the systemd service by calling systemctl edit ollama.service. This will open an editor.

  For each environment variable, add a line Environment under section [Service]:

    [Service]
    Environment="OLLAMA_HOST=0.0.0.0:11434"

Save and exit.

Reload systemd and restart Ollama:

    systemctl daemon-reload
    systemctl restart ollama



