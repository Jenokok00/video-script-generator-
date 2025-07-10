from langchain.prompts import ChatPromptTemplate #define prompt template
from langchain_openai import ChatOpenAI # connect openai LLM

def generate_script(subject, video_length, creativity, api_key): #(theme of video , unit = mins , temperature , api key)
    # title generate prompt
    title_template = ChatPromptTemplate.from_messages(
        [("human", "请为'{subject}'这个主题的视频想一个吸引人的标题")]
    )
    # script generation prompt
    script_template = ChatPromptTemplate.from_messages(
        [("human",
             """你是一位短视频频道的博主。根据以下标题和相关信息，为短视频频道写一个视频脚本。
             视频标题：{title}，视频时长：{duration}分钟，生成的脚本的长度尽量遵循视频时长的要求。
             要求开头抓住限球，中间提供干货内容，结尾有惊喜，脚本格式也请按照【开头、中间，结尾】分隔。
             整体内容的表达方式要尽量轻松有趣，吸引年轻人。
             """)]
    )
    # initialize the openai model
    model = ChatOpenAI(
        openai_api_key=api_key,
        temperature=creativity,
        model_name="deepseek-chat",  # or "deepseek-coder" if you're coding
        openai_api_base="https://api.deepseek.com/v1"
    )

    #create chains - connect different modules (make.com)
    title_chain = title_template | model #send template to model -> model give you response
    script_chain = script_template | model

    title = title_chain.invoke({"subject": subject}).content #generate title - using invoke - 1 [module setting]

    # generate script - 2 [script contains title, duration, wikipedia_search] - module setting
    script = script_chain.invoke({
        "title": title,
        "duration": video_length
    }).content

    return title, script # return the result -> you will get those two things - end the definition

# congrats you finished the backend script generator 






