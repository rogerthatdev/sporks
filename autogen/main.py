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

reply = agent.generate_reply(messages=example_messages)
print(reply)

