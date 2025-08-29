# TODO: 1 - Import the AugmentedPromptAgent class
import os
from datetime import datetime
from dotenv import load_dotenv
from workflow_agents.base_agents import AugmentedPromptAgent

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"
persona = "a college professor who always begins responses with 'Dear students,'"

# TODO: 2 - Instantiate an object of AugmentedPromptAgent with the required parameters
agent = AugmentedPromptAgent(openai_api_key, persona)
# TODO: 3 - Send the 'prompt' to the agent and store the response in a variable named 'augmented_agent_response'
augmented_agent_response = agent.respond(prompt)    
# Print the agent's response
print(augmented_agent_response)

# TODO: 4 - Add a comment explaining:
# - What knowledge the agent likely used to answer the prompt.
# - How the system prompt specifying the persona affected the agent's response.

# KNOWLEDGE USED BY THE AGENT:
# The agent likely used its pre-trained knowledge about world geography, specifically:
# - General knowledge about European countries and their capitals
# - Understanding of France as a country and Paris as its capital city
# - Basic facts about Paris (location, significance, etc.)
# This knowledge comes from the LLM's training data, not from any external knowledge base.

# HOW THE PERSONA AFFECTED THE RESPONSE:
# The system prompt specified: "You are a college professor; your answers always start with: 'Dear students,'"
# This persona transformation affects the response in several ways:
# 1. Tone: The response adopts a formal, educational tone typical of a professor
# 2. Structure: It begins with "Dear students," as instructed
# 3. Style: The language becomes more academic and instructive
# 4. Context: The agent assumes the role of an educator speaking to students
# 5. Authority: The response carries the weight and expertise expected from a professor

# Create output content for file
output_content = []
output_content.append("=== AUGMENTED PROMPT AGENT OUTPUT ===")
output_content.append(f"Prompt: {prompt}")
output_content.append(f"Persona: {persona}")
output_content.append(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
output_content.append("")
output_content.append("Agent Response:")
output_content.append(augmented_agent_response)
output_content.append("")
output_content.append("=== ANALYSIS ===")
output_content.append("KNOWLEDGE USED:")
output_content.append("- General world geography knowledge (France, Paris)")
output_content.append("- European countries and capitals")
output_content.append("- Basic facts about Paris")
output_content.append("")
output_content.append("PERSONA EFFECTS:")
output_content.append("- Formal, educational tone")
output_content.append("- Begins with 'Dear students,'")
output_content.append("- Academic language style")
output_content.append("- Educator context and authority")

# Save to output file
output_filename = f"output/augmented_prompt_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
with open(output_filename, 'w') as f:
    f.write('\n'.join(output_content))

# Also print to console
print("=== AUGMENTED PROMPT AGENT OUTPUT ===")
print(f"Prompt: {prompt}")
print(f"Persona: {persona}")
print(f"Output saved to: {output_filename}")
print("")
print("Agent Response:")
print(augmented_agent_response)
print("")
print("=== ANALYSIS ===")
print("KNOWLEDGE USED:")
print("- General world geography knowledge (France, Paris)")
print("- European countries and capitals")
print("- Basic facts about Paris")
print("")
print("PERSONA EFFECTS:")
print("- Formal, educational tone")
print("- Begins with 'Dear students,'")
print("- Academic language style")
print("- Educator context and authority")
