import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompt_values import ChatPromptValue

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

# Chaining 
chain = model | parser
print(chain.invoke(messages))

system_template: str = "Translate the following into {language}:"

prompt_template: ChatPromptTemplate = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

result: ChatPromptValue = prompt_template.invoke({"language": "italian", "text": "hi"})

print(result)

## Print the messages in ChatPromptValue
print("Messages:")
print(result.to_messages())

# Chain with a prompt template:
chain = prompt_template | model | parser
result = chain.invoke({"language": "italian", "text": "hi"})
