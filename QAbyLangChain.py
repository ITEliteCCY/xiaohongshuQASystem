import openai
openai_api_key = 'xxx' #openai官网获取
# openai.api_key = openai_api_key
openai_api_base = 'xxx' #反代理https://api.openai.com的域名
# openai.api_base = openai_api_base
openai_model_name="gpt-3.5-turbo"
from ProcessData import processData



from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import ChatVectorDBChain, ConversationalRetrievalChain

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate)


if __name__ == '__main__':

    #用户在小红薯上复制的链接
    inputXHSShareURL = "40 黑娃呦～发布了一篇小红书笔记，快来看吧！ 😆 4hydQI4uMU4D8yf 😆 http://xhslink.com/8VNHfu，复制本条信息，打开【小红书】App查看精彩内容！"

    #处理链接、拿到网址、拿到MP4URL、下载MP4、转录到音频、基于openai的whisper模型将音频转录到文本
    text_path = processData(inputXHSShareURL)
    text_path = "/Users/caochongyang/Downloads/text/  01e4c2381a456fca010370038996ad241c_259.text"
    loader = TextLoader(text_path, encoding="utf-8")

    # 将数据转成 document
    documents = loader.load()
    print(documents[0].page_content)

    # 初始化文本分割器
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=20
    )

    # 分割 documents
    documents = text_splitter.split_documents(documents)

    # 初始化 openai embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key,openai_api_base=openai_api_base)

    # 将数据存入向量存储
    vector_store = Chroma.from_documents(documents, embeddings)
    # 通过向量存储初始化检索器
    retriever = vector_store.as_retriever()

    system_template = """
    Use the following context to answer the user's question.
    If you don't know the answer, say you don't, don't try to make it up. And answer in Chinese.
    -----------
    {question}
    -----------
    {chat_history}
    """

    # 构建初始 messages 列表，这里可以理解为是 openai 传入的 messages 参数
    messages = [
        SystemMessagePromptTemplate.from_template(system_template),
        HumanMessagePromptTemplate.from_template('{question}')
    ]

    # 初始化 prompt 对象
    prompt = ChatPromptTemplate.from_messages(messages)

    # 初始化问答链
    qa = ConversationalRetrievalChain.from_llm(
        ChatOpenAI(temperature=0, max_tokens=2048,openai_api_key=openai_api_key,openai_api_base=openai_api_base,model_name=openai_model_name),
        retriever,
        condense_question_prompt=prompt
    )

    chat_history = []
    while True:
        question = input('问题：')
        # 开始发送问题 chat_history 为必须参数,用于存储对话历史
        result = qa({'question': question, 'chat_history': chat_history})
        chat_history.append((question, result['answer']))
        print(result['answer'])
