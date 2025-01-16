from langchain_openai import ChatOpenAI
import getpass
import os
from langchain_core.messages import HumanMessage, SystemMessage

if not os.environ.get('OPENAI_API_KEY'):
    print("Please set OPENAI_API_KEY")

model = ChatOpenAI(model='gpt-4o-mini')


messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]
model.invoke(messages)1311


# Line Graph
#Lang Smith

