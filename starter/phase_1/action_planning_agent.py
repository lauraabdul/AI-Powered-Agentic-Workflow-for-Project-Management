# TODO: 1 - Import all required libraries, including the ActionPlanningAgent
import os
import re
from datetime import datetime
from dotenv import load_dotenv
from workflow_agents.base_agents import ActionPlanningAgent

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

knowledge = """
# Fried Egg
1. Heat pan with oil or butter
2. Crack egg into pan
3. Cook until white is set (2-3 minutes)
4. Season with salt and pepper
5. Serve

# Scrambled Eggs
1. Crack eggs into a bowl
2. Beat eggs with a fork until mixed
3. Heat pan with butter or oil over medium heat
4. Pour egg mixture into pan
5. Stir gently as eggs cook
6. Remove from heat when eggs are just set but still moist
7. Season with salt and pepper
8. Serve immediately

# Boiled Eggs
1. Place eggs in a pot
2. Cover with cold water (about 1 inch above eggs)
3. Bring water to a boil
4. Remove from heat and cover pot
5. Let sit: 4-6 minutes for soft-boiled or 10-12 minutes for hard-boiled
6. Transfer eggs to ice water to stop cooking
7. Peel and serve
"""

# TODO: 3 - Instantiate the ActionPlanningAgent, passing the openai_api_key and the knowledge variable
agent = ActionPlanningAgent(openai_api_key, knowledge)

# TODO: 4 - Print the agent's response to the following prompt: "One morning I wanted to have scrambled eggs"
prompt = "One morning I wanted to have scrambled eggs"
steps = agent.extract_steps_from_prompt(prompt)

# Create output content
output_content = []
output_content.append("=== ACTION PLANNING AGENT OUTPUT ===")
output_content.append(f"Prompt: {prompt}")
output_content.append(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
output_content.append("")
output_content.append("Extracted steps:")
for i, step in enumerate(steps, 1):
    # Clean up the step text by removing any leading numbers and dots
    cleaned_step = re.sub(r'^\d+\.\s*', '', step.strip())
    output_content.append(f"{i}. {cleaned_step}")

# Save to output file
output_filename = f"output/action_planning_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
with open(output_filename, 'w') as f:
    f.write('\n'.join(output_content))

# Also print to console
print("=== ACTION PLANNING AGENT OUTPUT ===")
print(f"Prompt: {prompt}")
print(f"Output saved to: {output_filename}")
print("")
print("Extracted steps:")
for i, step in enumerate(steps, 1):
    cleaned_step = re.sub(r'^\d+\.\s*', '', step.strip())
    print(f"{i}. {cleaned_step}")
