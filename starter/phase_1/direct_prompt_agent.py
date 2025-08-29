# Test script for DirectPromptAgent class

from workflow_agents.base_agents import DirectPromptAgent
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# TODO: 2 - Load the OpenAI API key from the environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the Capital of France?"

direct_agent = DirectPromptAgent(openai_api_key)

# TODO: 3 - Instantiate the DirectPromptAgent as direct_agent
# TODO: 4 - Use direct_agent to send the prompt defined above and store the response
direct_agent_response = direct_agent.respond(prompt)

# Print the response from the agent
print(direct_agent_response)

# TODO: 5 - Print an explanatory message describing the knowledge source used by the agent to generate the response
print("=== KNOWLEDGE SOURCE EXPLANATION ===")
print("The DirectPromptAgent uses the LLM's pre-trained knowledge base to generate responses.")
print("This knowledge comes from:")
print("- Extensive training on diverse text data including geography, history, science, etc.")
print("- General world knowledge about countries, capitals, and facts")
print("- No external knowledge sources or databases are accessed")
print("- The response is generated purely from the model's internal training data")


# Create output content for file
output_content = []
output_content.append("=== DIRECT PROMPT AGENT OUTPUT ===")
output_content.append(f"Prompt: {prompt}")
output_content.append(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
output_content.append("")
output_content.append("Agent Response:")
output_content.append(direct_agent_response)
output_content.append("")
output_content.append("=== KNOWLEDGE SOURCE EXPLANATION ===")
output_content.append("The DirectPromptAgent uses the LLM's pre-trained knowledge base to generate responses.")
output_content.append("This knowledge comes from:")
output_content.append("- Extensive training on diverse text data including geography, history, science, etc.")
output_content.append("- General world knowledge about countries, capitals, and facts")
output_content.append("- No external knowledge sources or databases are accessed")
output_content.append("- The response is generated purely from the model's internal training data")

# Save to output file
output_filename = f"output/direct_prompt_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
with open(output_filename, 'w') as f:
    f.write('\n'.join(output_content))

# Also print to console
print("=== DIRECT PROMPT AGENT OUTPUT ===")
print(f"Prompt: {prompt}")
print(f"Output saved to: {output_filename}")
print("")
print("Agent Response:")
print(direct_agent_response)
print("")
print("=== KNOWLEDGE SOURCE EXPLANATION ===")
print("The DirectPromptAgent uses the LLM's pre-trained knowledge base to generate responses.")
print("This knowledge comes from:")
print("- Extensive training on diverse text data including geography, history, science, etc.")
print("- General world knowledge about countries, capitals, and facts")
print("- No external knowledge sources or databases are accessed")
print("- The response is generated purely from the model's internal training data")
