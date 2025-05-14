import os
import ollama

class OllamaOCR:
    """
    A class to perform OCR on images using a Llama Vision model.
    Supports Markdown or JSON output formats.
    """

    MARKDOWN = """Act as an OCR assistant. Analyze the provided image and:
    1. Recognize all visible text in the image as accurately as possible.
    2. Maintain the original structure and formatting of the text.
    3. If any words or phrases are unclear, indicate this with [unclear] in your transcription.
    Provide only the transcription without any additional comments.

    Requirements:
      - Output Only Markdown: Return solely the Markdown content without any additional explanations or comments.
      - No Delimiters: Do not use code fences or delimiters like ```markdown.
      - Complete Content: Do not omit any part of the page, including headers, footers, and subtext.
    """

    JSON = """Act as an OCR assistant. Analyze the provided image and:
    1. Recognize all visible text in the image as accurately as possible.
    2. Maintain the original structure and formatting of the text.
    3. If any words or phrases are unclear, indicate this with [unclear] in your transcription.
    Provide only the transcription without any additional comments.

    Requirements:
      - Output Only JSON: Return solely the JSON content without any additional explanations or comments.
      - No Delimiters: Do not use code fences or delimiters.
      - Complete Content: Do not omit any part of the page, including headers, footers, and subtext.
    """

    def __init__(self, model='llama3.2-vision', ollama_url=None):
        """
        Initialize the OCR class with the specified model and optional Ollama URL.

        :param model: Name of the Ollama model to use.
        :param ollama_url: Base URL of the Ollama server (e.g., "http://localhost:11434").
        """
        self.model = model
        if ollama_url:
            os.environ["OLLAMA_HOST"] = ollama_url  # sets the Ollama base URL dynamically

    def perform_ocr(self, image_path, output_format="markdown"):
        """
        Perform OCR on the given image and return the result in the specified format.

        :param image_path: Path to the image file.
        :param output_format: The desired output format ("markdown" or "json").
        :return: The OCR result in the specified format.
        """
        valid_extensions = {"jpg", "jpeg", "png"}
        extension = os.path.splitext(image_path)[1].lower().strip(".")

        if extension not in valid_extensions:
            raise ValueError(f"Invalid image format '{extension}'. Supported formats: {valid_extensions}")

        if output_format not in {"markdown", "json"}:
            raise ValueError("Invalid output format. Choose either 'markdown' or 'json'.")

        content = self.MARKDOWN if output_format == "markdown" else self.JSON

        result = ollama.chat(
            model=self.model,
            messages=[{
                'role': 'user',
                'content': content,
                'images': [image_path]
            }]
        )

        return result['message']['content']

# ocr = OllamaOCR(
#     model="llama3.2-vision",
#     ollama_url="http://localhost:11434"
# )

# result = ocr.perform_ocr("sample.png", output_format="markdown")
# print(result)
