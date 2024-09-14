import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatAnthropic(model="claude-3-5-sonnet-20240620")

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

result:AIMessage = model.invoke(messages)

for attr, value in result.__dict__.items():
    print(f"{attr}: {value}")


# Output Parsers
parser = StrOutputParser()
result = model.invoke(messages)
parsedResult = parser.invoke(result)
print(parsedResult)