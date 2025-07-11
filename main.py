import streamlit as st  # Streamlit: lets you quickly build web apps for demos
from utils import generate_script  # Import your custom script generator function
import requests

# This code uses Streamlit to create a simple web form where users can submit their video ideas. When submitted, the data is sent to a webhook using a POST request.
def post_to_webhook(**data): #this function sends data to a webhook URL - **data = accepts any number of keyword arguments
    webhook_url = "" #Paste your webhook URL obtained from the 'Create a webhook' module in Make.com.
    if webhook_url:
        response = requests.post(webhook_url, json=data) #sends a POST requests to the url with the data in JSON format
        return response
    else:
        st.error("Webhook URL is missing") #show error
        st.stop() #stop the app if the url is missing
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
    # build the data dictionary to send
    data = {
        "subject": subject,
        "video_length": video_length,
        "creativity": creativity,
        "title": title,
        "script": script
    }
    # Post data to webhook
    response = post_to_webhook(**data)

    # show result of webhook submission
    if response.status_code == 200:
        st.success("✅ Script generated and sent successfully!")
    else:
        st.error("❌ Script generated, but failed to send to webhook.")

    # Display the result
    st.success("✅ Script generated successfully!")
    st.subheader("🔥 Title:")
    st.write(title)

    st.subheader("📝 Script:")
    st.write(script)
