import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

model = ChatAnthropic(model="claude-3-5-sonnet-20240620")

messages = [
    SystemMessage(content=""),
    HumanMessage(content="hi!")
]

result:AIMessage = model.invoke(messages)

for attr, value in result.__dict__.items():
    print(f"{attr}: {value}")

