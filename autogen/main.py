import dotenv

dotenv.load_dotenv()

# basic example
import os

from autogen import ConversableAgent

# llm config contains a list of configurations for the LLMs
# See LLM Configuration for more: https://microsoft.github.io/autogen/docs/topics/llm_configuration
example_llm_config = {
    "config_list": [
        {
            "model": "gpt-4",
            "api_key": os.environ.get("OPENAI_API_KEY")
        }
    ]
}
# demonstrates ConversableAgent with LLM configuration. GPT-4 is switched on and
# other components are switched off:
agent = ConversableAgent(
    "chatbot",
    llm_config=example_llm_config,
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
)

# generate a response with generate_reply:
example_messages = [
    {
        "content": "Tell me a joke.", 
        "role": "user"
    }
]

# reply = agent.generate_reply(messages=example_messages)
# print(reply)

# Roles and conversations

cathy_config = {
    "config_list": [
        {"model": "gpt-4", 
         "temperature": 0.9, 
         "api_key": os.environ.get("OPENAI_API_KEY")}]}

joe_config = {
    "config_list": [
        {"model": "gpt-4", 
         "temperature": 0.7, 
         "api_key": os.environ.get("OPENAI_API_KEY")}]}

cathy = ConversableAgent(
    "cathy",
    system_message="Your name is Cathy and you are a part of a duo of comedians.",
    llm_config=cathy_config,
    human_input_mode="NEVER",  # Never ask for human input.
)

joe = ConversableAgent(
    "joe",
    system_message="Your name is Joe and you are a part of a duo of comedians.",
    llm_config=joe_config,
    human_input_mode="NEVER",  # Never ask for human input.
)
# use initiate_chat with max_turns as 2 to limit the conversation to 2 turns
result = joe.initiate_chat(cathy, message="Cathy, tell me a joke.", max_turns=2)


