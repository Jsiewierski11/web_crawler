# Web Crawler with LLM Integration

This project is a web crawler that fetches movie information and enhances it using a Language Model (LLM) to provide detailed summaries, reviews, runtime, reasons to watch, and recommendations.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/web_crawler.git
   cd web_crawler
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your LLM API key (if required):
   - For OpenAI's GPT-3, set the `OPENAI_API_KEY` environment variable.

## Usage

1. Run the script:
   ```bash
   python src/movie_info.py
   ```

2. Enter the movie name and choose the LLM (llama/mistral) when prompted.

## Notes

- Ensure to handle API errors and edge cases where the movie information might not be available.
- Consider adding unit tests for the new functionality.

## References

- [Hugging Face Transformers Documentation](https://huggingface.co/transformers/)