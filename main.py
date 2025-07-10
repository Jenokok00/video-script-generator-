import streamlit as st  # Streamlit: lets you quickly build web apps for demos
from utils import generate_script  # Import your custom script generator function

# Web App Title
st.title("🎬 Video Script Generator")

# Sidebar for user input
with st.sidebar:
    openai_api_key = st.text_input("🔑 Enter your OpenAI API Key:", type="password")
    st.markdown("[Get your API Key](https://platform.openai.com/account/api-keys)")

# Main Input Section
subject = st.text_input("💡 Enter the topic of your video")
video_length = st.number_input("⏱️ Approximate video duration (in minutes)", min_value=0.1, step=0.1)
creativity = st.slider("✨ Creativity level (lower = more factual...)", min_value=0.0, max_value=1.0, value=0.2, step=0.1)
submit = st.button("Generate Script")

# Input Validation: Show a message if any required field is missing
if submit and not openai_api_key:
    st.info("Please enter your OpenAI API key")
    st.stop()
if submit and not subject:
    st.info("Please enter the video topic")
    st.stop()
if submit and not video_length >= 0.1:
    st.info("Video length must be at least 0.1 minutes")
    st.stop()

# Run script generation when button is pressed
if submit:
    with st.spinner("⏳ Generating script with AI, please wait..."):
        title, script = generate_script(subject, video_length, creativity, openai_api_key)

    # Display the result
    st.success("✅ Script generated successfully!")
    st.subheader("🔥 Title:")
    st.write(title)

    st.subheader("📝 Script:")
    st.write(script)
