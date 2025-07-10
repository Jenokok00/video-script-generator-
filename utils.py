from langchain.prompts import ChatPromptTemplate  # Define prompt template
from langchain_openai import ChatOpenAI           # Connect to OpenAI-compatible LLM (e.g., DeepSeek)

def generate_script(subject, video_length, creativity, api_key):
    # (Video topic, duration in minutes, creativity/temperature, API key)

    # Title generation prompt
    title_template = ChatPromptTemplate.from_messages([
        ("human", "Please come up with an attention-grabbing video title for the topic '{subject}'.")
    ])

    # Script generation prompt
    script_template = ChatPromptTemplate.from_messages([
        ("human",
         """You are a short video content creator. Based on the following title and details, write a video script.
         Video title: {title}
         Video duration: {duration} minutes

         The script length should roughly match the video duration.
         Make sure the intro grabs attention, the middle part provides valuable content, and the ending has a twist or surprise.
         Format the script into three sections: [Introduction, Middle, Ending].

         The tone should be fun and engaging to appeal to a young audience.
         """)
    ])

    # Initialize the model (DeepSeek API)
    model = ChatOpenAI(
        openai_api_key=api_key,
        temperature=creativity,
        model_name="deepseek-chat",  # or use "deepseek-coder" for code-related tasks
        openai_api_base="https://api.deepseek.com/v1"
    )

    # Create the chains: connect the prompt to the model
    title_chain = title_template | model  # Pass prompt to model and get response
    script_chain = script_template | model

    # Generate title using the title prompt
    title = title_chain.invoke({"subject": subject}).content

    # Generate script using the title and video duration
    script = script_chain.invoke({
        "title": title,
        "duration": video_length
    }).content

    return title, script  # Return both the title and script
