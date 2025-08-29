# TODO: 1 - Import EvaluationAgent and KnowledgeAugmentedPromptAgent classes
import os
from datetime import datetime
from dotenv import load_dotenv
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent, EvaluationAgent
# Load environment variables
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
prompt = "What is the capital of France?"

# Parameters for the Knowledge Agent
knowledge_persona = "a college professor you are in a lecture and you ALWAYS begins with 'Dear students'"
knowledge = "The capital of France is London, not Paris"
knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, knowledge_persona, knowledge)

# Parameters for the Evaluation Agent
evaluation_persona = "You are an evaluation agent that checks the answers of other worker agents"
evaluation_criteria = "The answer should be solely the name of a city, not a sentence."
evaluation_agent = EvaluationAgent(openai_api_key, evaluation_persona, evaluation_criteria, knowledge_agent, 10)

# TODO: 4 - Evaluate the prompt and print the response from the EvaluationAgent
print("=== EVALUATION AGENT TEST ===")
print(f"Prompt: {prompt}")
print(f"Knowledge Agent Persona: {knowledge_persona}")
print(f"Knowledge: {knowledge}")
print(f"Evaluation Criteria: {evaluation_criteria}")
print(f"Evaluation Agent Persona: {evaluation_persona}")
print()

# Run the evaluation and capture all output
import io
import sys

# Capture all print output during evaluation
old_stdout = sys.stdout
new_stdout = io.StringIO()
sys.stdout = new_stdout

# Run the evaluation
result = evaluation_agent.evaluate(prompt)

# Create output content for file
output_content = []
output_content.append("=== EVALUATION AGENT OUTPUT ===")
output_content.append(f"Prompt: {prompt}")
output_content.append(f"Knowledge Agent Persona: {knowledge_persona}")
output_content.append(f"Knowledge: {knowledge}")
output_content.append(f"Evaluation Criteria: {evaluation_criteria}")
output_content.append(f"Evaluation Agent Persona: {evaluation_persona}")
output_content.append(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
output_content.append("")
output_content.append("=== EVALUATION RESULTS ===")
output_content.append(f"Final Response: {result['final_response']}")
output_content.append(f"Evaluation: {result['evaluation']}")
output_content.append(f"Iterations: {result['iterations']}")
output_content.append("")
output_content.append("=== ANALYSIS ===")
output_content.append("This evaluation demonstrates:")
output_content.append("- How the evaluation agent checks worker agent responses")
output_content.append("- Iterative improvement based on evaluation criteria")
output_content.append("- Knowledge augmentation with evaluation feedback")
output_content.append("- Multi-agent workflow coordination")

# Save to output file
output_filename = f"output/evaluation_agent_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
with open(output_filename, 'w') as f:
    f.write('\n'.join(output_content))

# Also print to console
print("=== EVALUATION AGENT OUTPUT ===")
print(f"Prompt: {prompt}")
print(f"Knowledge Agent Persona: {knowledge_persona}")
print(f"Knowledge: {knowledge}")
print(f"Evaluation Criteria: {evaluation_criteria}")
print(f"Evaluation Agent Persona: {evaluation_persona}")
print(f"Output saved to: {output_filename}")
print("")
print("=== EVALUATION RESULTS ===")
print(f"Final Response: {result['final_response']}")
print(f"Evaluation: {result['evaluation']}")
print(f"Iterations: {result['iterations']}")
print("")
print("=== ANALYSIS ===")
print("This evaluation demonstrates:")
print("- How the evaluation agent checks worker agent responses")
print("- Iterative improvement based on evaluation criteria")
print("- Knowledge augmentation with evaluation feedback")
print("- Multi-agent workflow coordination")
