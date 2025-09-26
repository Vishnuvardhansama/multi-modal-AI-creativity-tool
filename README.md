# multi-modal-AI-creativity-tool
Generate **stories, poems, advertisements, social captions, and images** from text prompts using the power of OpenAI GPT-3.5-turbo and DALL·E, all within a streamlined Streamlit web interface.



## Table of Contents

- Features
- Live Demo
- Requirements
- Installation
- Configuration
- Usage
- Project Structure
- API Details
- Troubleshooting
- Contributing
- License


### Features

- **Text Content Generation**: Create realistic stories, poems, ad copies, and social captions with GPT-3.5-turbo.
- **Image Generation**: Produce unique AI-generated images from simple text prompts via DALL·E.
- **Streamlit Tabs UX**: Intuitive dual-tab interface for toggling between text and image generation.
- **Error Handling**: User-friendly warnings and error messages for incomplete prompts or API issues.
- **Environment Integration**: Secure API key management using Python-dotenv.



### Live Demo

_Run locally by following setup steps below. Public demo hosting may be added in future releases._



### Requirements

- **Python** >= 3.9
- **Streamlit**
- **openai** (OpenAI Python SDK)
- **python-dotenv**
- **A valid OpenAI API Key** (with DALL·E and GPT-3.5-turbo access)

_See requirements.txt for package list._



### Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/<your-username>/Creative_Content_Generator.git
   cd Creative_Content_Generator
   ```

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup**  
   - Create a `.env` file in the project root:
     ```
     OPENAI_API_KEY=YOUR_OPENAI_API_KEY
     ```
   - (Optional) Edit the file path in `load_dotenv` if your .env file is elsewhere.



### Configuration

Configure settings in your `.env` file:

```env
OPENAI_API_KEY=<your-openai-key>
```
Ensure the API key has access to both GPT and image generation endpoints. For best results, this app is tested with gpt-3.5-turbo and DALL·E.[2][1]



### Usage

1. **Launch the App**
   ```bash
   python3 -m streamlit run main.py
   ```
2. **Navigate in Browser**
   - Text Generation: Select Story, Poem, Ad Copy, or Social Caption, enter a topic, and click “Generate Text.”
   - Image Generation: Enter a descriptive prompt and click “Generate Image.”

3. **View Results**
   - Generated text will appear in an editable text area.
   - Generated images are displayed inline.



### Project Structure

| File/Folder      | Description                                    |
|------------------|------------------------------------------------|
| app.py           | Main Streamlit application code                |
| .env             | Environment variables (API keys, config)       |
| requirements.txt | Python dependencies                            |



### API Details

- Uses `openai.ChatCompletion` for text
- Uses `openai.Image.generate` for DALL·E
- API authentication via environment variable

Edit in `app.py` for custom prompt templates or additional content types as needed.[4][1]



### Troubleshooting

- _“Please enter a topic or keywords…”_: Ensure text input is non-empty.
- _API error_: Check your OpenAI API key and quota.
- _Environment issues_: Verify correct `.env` file path and content.



### Contributing

Contributions welcome!  
- Open issues for suggestions and bugs
- Submit pull requests for improvements
- Follow standard Python and Streamlit coding practices



### License

[MIT License](LICENSE)  
See LICENSE file for details.



### Acknowledgments

- OpenAI (GPT-3.5-turbo, DALL·E)
- Streamlit Community
- python-dotenv for environment management
