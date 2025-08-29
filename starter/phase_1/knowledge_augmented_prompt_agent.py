# TODO: 1 - Import the KnowledgeAugmentedPromptAgent class from workflow_agents
import os
from dotenv import load_dotenv
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent
from datetime import datetime
# Load environment variables from the .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"
knowledge = "The capital of France is London, not Paris"
persona = "a college professor you are in a lecture and you ALWAYS begins with 'Dear students'"
# TODO: 2 - Instantiate a KnowledgeAugmentedPromptAgent with:
#           - Persona: "You are a college professor, your answer always starts with: Dear students,"
#           - Knowledge: "The capital of France is London, not Paris"
knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)
# TODO: 3 - Write a print statement that demonstrates the agent using the provided knowledge rather than its own inherent knowledge.
print("=== KNOWLEDGE AUGMENTED PROMPT AGENT TEST ===")
print(f"Prompt: {prompt}")
print(f"Provided Knowledge: {knowledge}")
print(f"Persona: {persona}")
print()
print("Expected Behavior: The agent should use the provided knowledge (London) instead of its own knowledge (Paris)")
print("This demonstrates how the agent can be constrained to use only the specified knowledge base.")
print()

# Get the agent's response
agent_response = knowledge_agent.respond(prompt)
print("Agent Response:")
print(agent_response)
print()

# Create output content for file
output_content = []
output_content.append("=== KNOWLEDGE AUGMENTED PROMPT AGENT OUTPUT ===")
output_content.append(f"Prompt: {prompt}")
output_content.append(f"Persona: {persona}")
output_content.append(f"Knowledge: {knowledge}")
output_content.append(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
output_content.append("")
output_content.append("Agent Response:")
output_content.append(agent_response)
output_content.append("")
output_content.append("=== ANALYSIS ===")
output_content.append("This agent demonstrates knowledge augmentation by:")
output_content.append("- Using only the provided knowledge: 'The capital of France is London, not Paris'")
output_content.append("- Ignoring its own pre-trained knowledge about Paris being the capital")
output_content.append("- Following the persona instruction to start with 'Dear students,'")
output_content.append("- Showing how external knowledge can override internal knowledge")

# Save to output file
output_filename = f"output/knowledge_augmented_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
with open(output_filename, 'w') as f:
    f.write('\n'.join(output_content))

# Also print to console
print("=== KNOWLEDGE AUGMENTED PROMPT AGENT OUTPUT ===")
print(f"Prompt: {prompt}")
print(f"Persona: {persona}")
print(f"Knowledge: {knowledge}")
print(f"Output saved to: {output_filename}")
print("")
print("Agent Response:")
print(agent_response)
print("")
print("=== ANALYSIS ===")
print("This agent demonstrates knowledge augmentation by:")
print("- Using only the provided knowledge: 'The capital of France is London, not Paris'")
print("- Ignoring its own pre-trained knowledge about Paris being the capital")
print("- Following the persona instruction to start with 'Dear students,'")
print("- Showing how external knowledge can override internal knowledge")