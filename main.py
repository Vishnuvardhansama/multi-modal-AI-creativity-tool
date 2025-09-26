import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path="/Users/admin/Desktop/GIT/Riteesh/Creative_Content_Generator/.env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client once
client = OpenAI(api_key=OPENAI_API_KEY)

# Prompt templates
PROMPT_TEMPLATES = {
    "Story": "Write a short, engaging story about: {topic}",
    "Poem": "Compose a creative poem about: {topic}",
    "Ad Copy": "Generate a marketing advertisement for: {topic}",
    "Social Caption": "Create a catchy social media caption for: {topic}"
}

st.set_page_config(page_title="Creative Content Generator", layout="wide")

st.title("🎨 Creative Content Generator")
st.markdown(
    """
    Generate **stories, poems, advertisements, social captions**, and **images** using OpenAI GPT-3.5-turbo and DALL·E.
    """
)

# Layout with tabs for Text and Image generation options
tab1, tab2 = st.tabs(["Text Generation", "Image Generation"])

with tab1:
    st.header("Text Content Generator")
    with st.form(key="text_form"):
        content_type = st.selectbox(
            "Select content type:",
            ["Story", "Poem", "Ad Copy", "Social Caption"],
            help="Choose what type of text content to generate"
        )
        topic = st.text_area(
            "Enter your topic or keywords:",
            height=80,
            placeholder="Type your text input here...",
            max_chars=200
        )

        submit_text = st.form_submit_button("Generate Text")
    
    if submit_text:
        if not topic.strip():
            st.warning("Please enter a topic or keywords to generate content.")
        else:
            prompt = PROMPT_TEMPLATES[content_type].format(topic=topic)
            with st.spinner("Generating text..."):
                try:
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=300,
                    )
                    generated_text = response.choices[0].message.content
                    st.success(f"Here is your generated {content_type.lower()}:")
                    st.text_area("Result", value=generated_text, height=200)
                except Exception as e:
                    st.error(f"Text generation error: {e}")

with tab2:
    st.header("Image Generator (DALL·E)")
    with st.form(key="image_form"):
        img_topic = st.text_input(
            "Enter prompt for image generation:",
            placeholder="e.g., futuristic cityscape, vibrant sunset, etc."
        )
        submit_image = st.form_submit_button("Generate Image")
    
    if submit_image:
        if not img_topic.strip():
            st.warning("Please enter a prompt to generate an image.")
        else:
            with st.spinner("Generating image..."):
                try:
                    image_response = client.images.generate(
                        prompt=img_topic,
                        n=1,
                        size="512x512",
                    )
                    image_url = image_response.data[0].url
                    st.success("Generated Image:")
                    st.image(image_url, use_column_width=True)
                except Exception as e:
                    st.error(f"Image generation error: {e}")

st.markdown("---")
st.markdown(
    "🛠️ Built with **Streamlit** and **OpenAI GPT-3.5-turbo / DALL·E**. "
    "Ensure your API key is valid and has access to required models."
)
