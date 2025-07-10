import streamlit as st #allows you to quickly build a website for demo
from utils import generate_script #import your own script generator

st.title("🎬 Video Script Generator") # web app title

with st.sidebar: # sidebar settings
    openai_api_key = st.text_input("🔑 Enter your OpenAI API Key：", type="password") #tell user to input their API KEY
    st.markdown("[Get your API Key](https://platform.openai.com/account/api-keys)") # provide a link for them to get their key - using markdown

#main input:
subject = st.text_input("💡 Enter the topic of your video")
video_length = st.number_input("⏱️ Approximate video duration (in minutes)", min_value=0.1, step=0.1) #min 0.1 mins
creativity = st.slider("✨ Creativity level (lower = more factual...)", min_value=0.0, max_value=1.0, value=0.2, step=0.1) #slider -> slide the value
submit = st.button("Generate Script") #button

#input validation - gives reminder if input something wrong after user pressing button
if submit and not openai_api_key:
    st.info("Please enter your OpenAI API key")
    st.stop()
if submit and not subject:
    st.info("Please enter the video topic")
    st.stop()
if submit and not video_length >= 0.1:
    st.info("Video length must be at least 0.1 minutes")
    st.stop()

#run script generator
if submit:
    with st.spinner("⏳ Generating script with AI, please wait..."): # show spinner show generating
         title, script = generate_script(subject, video_length, creativity, openai_api_key)
        # Execute the generate_script() Function: Retrieve the Three Variables from generate_script
    
    #show result
    st.success("✅ Script generated successfully!")
    st.subheader("🔥 Title:")
    st.write(title)
    st.subheader("📝 Script:")
    st.write(script)
