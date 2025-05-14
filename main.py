from ollamaocr.ollama_ocr import OllamaOCR
from dotenv import load_dotenv; load_dotenv()
import os

os.environ['ollama_url']=os.getenv("OLLAMA_URL")
os.environ['ollama_model']=os.getenv('OLLAMA_MODEL')

if __name__ == "__main__":
    ocr = OllamaOCR(model="ollama_url",ollama_url="ollama_model")
    image_path = ""
    result = ocr.perform_ocr(image_path=image_path,output_format="markdown")
    print(result)

