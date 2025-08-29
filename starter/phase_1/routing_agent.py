
# TODO: 1 - Import the KnowledgeAugmentedPromptAgent and RoutingAgent
import os
from datetime import datetime
from dotenv import load_dotenv
from workflow_agents.base_agents import RoutingAgent, KnowledgeAugmentedPromptAgent

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

persona = "You are a college professor"

knowledge = "You know everything about Texas"
texas_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

knowledge = "You know everything about Europe"
europe_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

persona = "You are a college math professor"
knowledge = "You know everything about math, you take prompts with numbers, extract math formulas, and show the answer without explanation"
math_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

#Edited the code here to make it work from using {} to []
routing_agent = RoutingAgent(openai_api_key, [])
agents = [
    {
        "name": "texas agent",
        "description": "Answer a question about Texas",
        "func": lambda x: texas_agent.respond(x)
    },
    {
        "name": "europe agent",
        "description": "Answer a question about Europe",
        "func": lambda x: europe_agent.respond(x)
    },
    {
        "name": "math agent",
        "description": "When a prompt contains numbers, respond with a math formula",
        "func": lambda x: math_agent.respond(x)
    }
]

routing_agent.agents = agents

# Create output content for file
output_content = []
output_content.append("=== ROUTING AGENT OUTPUT ===")
output_content.append(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
output_content.append("")
output_content.append("=== AGENT CONFIGURATION ===")
output_content.append("Available Agents:")
for agent in agents:
    output_content.append(f"- {agent['name']}: {agent['description']}")
output_content.append("")
output_content.append("=== ROUTING RESULTS ===")

# Test routing with different queries
queries = [
    "Tell me about the history of Rome, Texas",
    "Tell me about the history of Rome, Italy", 
    "One story takes 2 days, and there are 20 stories"
]

for i, query in enumerate(queries, 1):
    output_content.append(f"Query {i}: {query}")
    output_content.append("-" * 50)
    
    # Capture the routing process output
    import io
    import sys
    
    # Capture print output during routing
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    
    # Get the response
    response = routing_agent.route(query)
    
    # Get captured output
    captured_output = new_stdout.getvalue()
    sys.stdout = old_stdout
    
    # Add captured output and response to file content
    output_content.append("Routing Process:")
    output_content.append(captured_output)
    output_content.append("Final Response:")
    output_content.append(response)
    output_content.append("")
    output_content.append("=" * 60)
    output_content.append("")

# Add analysis
output_content.append("=== ANALYSIS ===")
output_content.append("This routing system demonstrates:")
output_content.append("- Semantic similarity-based agent selection")
output_content.append("- Multi-agent coordination and routing")
output_content.append("- Domain-specific knowledge specialization")
output_content.append("- Intelligent query-to-agent matching")

# Save to output file
output_filename = f"output/routing_agent_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
with open(output_filename, 'w') as f:
    f.write('\n'.join(output_content))

# Also print to console
print("=== ROUTING AGENT OUTPUT ===")
print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Output saved to: {output_filename}")
print("")
print("=== AGENT CONFIGURATION ===")
print("Available Agents:")
for agent in agents:
    print(f"- {agent['name']}: {agent['description']}")
print("")
print("=== ROUTING RESULTS ===")

for i, query in enumerate(queries, 1):
    print(f"Query {i}: {query}")
    print("-" * 50)
    
    # Capture the routing process output
    import io
    import sys
    
    # Capture print output during routing
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    
    # Get the response
    response = routing_agent.route(query)
    
    # Get captured output
    captured_output = new_stdout.getvalue()
    sys.stdout = old_stdout
    
    # Print captured output and response
    print("Routing Process:")
    print(captured_output)
    print("Final Response:")
    print(response)
    print("")
    print("=" * 60)
    print("")

print("=== ANALYSIS ===")
print("This routing system demonstrates:")
print("- Semantic similarity-based agent selection")
print("- Multi-agent coordination and routing")
print("- Domain-specific knowledge specialization")
print("- Intelligent query-to-agent matching")