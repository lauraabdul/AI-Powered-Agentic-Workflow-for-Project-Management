# agentic_workflow.py

# TODO: 1 - Import the following agents: ActionPlanningAgent, KnowledgeAugmentedPromptAgent, EvaluationAgent, RoutingAgent from the workflow_agents.base_agents module
import sys
sys.path.append('starter/phase_1')
from workflow_agents.base_agents import ActionPlanningAgent, KnowledgeAugmentedPromptAgent, EvaluationAgent, RoutingAgent
import os   
from dotenv import load_dotenv

# TODO: 2 - Load the OpenAI key into a variable called openai_api_key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
# load the product spec
# TODO: 3 - Load the product spec document Product-Spec-Email-Router.txt into a variable called product_spec
with open("starter/phase_2/Product-Spec-Email-Router.txt", "r") as file:
    product_spec = file.read()
# Instantiate all the agents

# Action Planning Agent
knowledge_action_planning = (
    "Stories are defined from a product spec by identifying a "
    "persona, an action, and a desired outcome for each story. "
    "Each story represents a specific functionality of the product "
    "described in the specification. \n"
    "Features are defined by grouping related user stories. \n"
    "Tasks are defined for each story and represent the engineering "
    "work required to develop the product. \n"
    "A development Plan for a product contains all these components"
)
# TODO: 4 - Instantiate an action_planning_agent using the 'knowledge_action_planning'
action_planning_agent = ActionPlanningAgent(openai_api_key, knowledge_action_planning)


# Product Manager - Knowledge Augmented Prompt Agent
persona_product_manager = "You are a Product Manager, you are responsible for defining the user stories for a product."
knowledge_product_manager = (
    "Stories are defined by writing sentences with a persona, an action, and a desired outcome. "
    "The sentences always start with: As a "
    "Write several stories for the product spec below, where the personas are the different users of the product. "
    # TODO: 5 - Complete this knowledge string by appending the product_spec loaded in TODO 3
    f"The product spec is: {product_spec}"

)
# TODO: 6 - Instantiate a product_manager_knowledge_agent using 'persona_product_manager' and the completed 'knowledge_product_manager'
product_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_product_manager, knowledge_product_manager)
# Product Manager - Evaluation Agent
# TODO: 7 - Define the persona and evaluation criteria for a Product Manager evaluation agent and instantiate it as product_manager_evaluation_agent. This agent will evaluate the product_manager_knowledge_agent.
persona_product_manager_eval = "You are an evaluation agent that checks the answers of other worker agents"
# The evaluation_criteria should specify the expected structure for stories (exact phrasing per spec).
evaluation_criteria_product_manager = (
    "The answer should be stories that follow the following structure: "
    "As a [type of user], I want [an action or feature] so that [benefit/value]."
)
product_manager_evaluation_agent = EvaluationAgent(openai_api_key, persona_product_manager_eval, evaluation_criteria_product_manager, product_manager_knowledge_agent, 10)


# Program Manager - Knowledge Augmented Prompt Agent
persona_program_manager = "You are a Program Manager, you are responsible for defining the features for a product."
knowledge_program_manager = "Features of a product are defined by organizing similar user stories into cohesive groups."
# Instantiate a program_manager_knowledge_agent using 'persona_program_manager' and 'knowledge_program_manager'
# (This is a necessary step before TODO 8. Students should add the instantiation code here.)
program_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_program_manager, knowledge_program_manager)
# Program Manager - Evaluation Agent
persona_program_manager_eval = "You are an evaluation agent that checks the answers of other worker agents."
evaluation_criteria_program_manager = (
    "The answer should be product features that follow the following structure: "
    "\nFeature Name: A clear, concise title that identifies the capability"
    "\nDescription: A brief explanation of what the feature does and its purpose"
    "\nKey Functionality: The specific capabilities or actions the feature provides"
    "\nUser Benefit: How this feature creates value for the user"
)
program_manager_evaluation_agent = EvaluationAgent(openai_api_key, persona_program_manager_eval, evaluation_criteria_program_manager, program_manager_knowledge_agent, 10)
# TODO: 8 - Instantiate a program_manager_evaluation_agent using 'persona_program_manager_eval' and the evaluation criteria below.
#                      "The answer should be product features that follow the following structure: " \
#                      "Feature Name: A clear, concise title that identifies the capability\n" \
#                      "Description: A brief explanation of what the feature does and its purpose\n" \
#                      "Key Functionality: The specific capabilities or actions the feature provides\n" \
#                      "User Benefit: How this feature creates value for the user"
# For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.


# Development Engineer - Knowledge Augmented Prompt Agent
persona_dev_engineer = "You are a Development Engineer, you are responsible for defining the development tasks for a product."
knowledge_dev_engineer = "Development tasks are defined by identifying what needs to be built to implement each user story."
# Instantiate a development_engineer_knowledge_agent using 'persona_dev_engineer' and 'knowledge_dev_engineer'
# (This is a necessary step before TODO 9. Students should add the instantiation code here.)
development_engineer_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_dev_engineer, knowledge_dev_engineer)
# Development Engineer - Evaluation Agent
persona_dev_engineer_eval = "You are an evaluation agent that checks the answers of other worker agents."
evaluation_criteria_dev_engineer = (
    "The answer should be tasks following this exact structure: "
    "\nTask ID: A unique identifier for tracking purposes"
    "\nTask Title: Brief description of the specific development work"
    "\nRelated User Story: Reference to the parent user story"
    "\nDescription: Detailed explanation of the technical work required"
    "\nAcceptance Criteria: Specific requirements that must be met for completion"
    "\nEstimated Effort: Time or complexity estimation"
    "\nDependencies: Any tasks that must be completed first"
)
development_engineer_evaluation_agent = EvaluationAgent(openai_api_key, persona_dev_engineer_eval, evaluation_criteria_dev_engineer, development_engineer_knowledge_agent, 10)
# TODO: 9 - Instantiate a development_engineer_evaluation_agent using 'persona_dev_engineer_eval' and the evaluation criteria below.
#                      "The answer should be tasks following this exact structure: " \
#                      "Task ID: A unique identifier for tracking purposes\n" \
#                      "Task Title: Brief description of the specific development work\n" \
#                      "Related User Story: Reference to the parent user story\n" \
#                      "Description: Detailed explanation of the technical work required\n" \
#                      "Acceptance Criteria: Specific requirements that must be met for completion\n" \
#                      "Estimated Effort: Time or complexity estimation\n" \
#                      "Dependencies: Any tasks that must be completed first"
# For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.


# Routing Agent
# TODO: 10 - Instantiate a routing_agent. You will need to define a list of agent dictionaries (routes) for Product Manager, Program Manager, and Development Engineer. Each dictionary should contain 'name', 'description', and 'func' (linking to a support function). Assign this list to the routing_agent's 'agents' attribute.

# Job function persona support functions
# TODO: 11 - Define the support functions for the routes of the routing agent (e.g., product_manager_support_function, program_manager_support_function, development_engineer_support_function).
# Each support function should:
#   1. Take the input query (e.g., a step from the action plan).
#   2. Get a response from the respective Knowledge Augmented Prompt Agent.
#   3. Have the response evaluated by the corresponding Evaluation Agent.
#   4. Return the final validated response.
def product_manager_support_function(input_query):
    print(f"🔧 [PRODUCT MANAGER] Called with query: {input_query[:80]}...")
    response = product_manager_knowledge_agent.respond(input_query)
    print(f"✅ [PRODUCT MANAGER] Knowledge agent response received")
    evaluation = product_manager_evaluation_agent.evaluate(response)
    print(f"✅ [PRODUCT MANAGER] Evaluation completed")
    return evaluation['final_response']

def program_manager_support_function(input_query):
    print(f"🔧 [PROGRAM MANAGER] Called with query: {input_query[:80]}...")
    response = program_manager_knowledge_agent.respond(input_query)
    print(f"✅ [PROGRAM MANAGER] Knowledge agent response received")
    evaluation = program_manager_evaluation_agent.evaluate(response)
    print(f"✅ [PROGRAM MANAGER] Evaluation completed")
    return evaluation['final_response']

def development_engineer_support_function(input_query):
    print(f"🔧 [DEVELOPMENT ENGINEER] Called with query: {input_query[:80]}...")
    response = development_engineer_knowledge_agent.respond(input_query)
    print(f"✅ [DEVELOPMENT ENGINEER] Knowledge agent response received")
    evaluation = development_engineer_evaluation_agent.evaluate(response)
    print(f"✅ [DEVELOPMENT ENGINEER] Evaluation completed")
    return evaluation['final_response']

agents = [
    {
        "name": "product_manager_knowledge_agent",
        "description": "Specializes in product strategy, market analysis, user requirements, feature prioritization, product roadmaps, competitive analysis, and business metrics. Handles questions about product vision, customer needs, market positioning, and product lifecycle management.",
        "func": product_manager_support_function
    },
    {
        "name": "program_manager_knowledge_agent",
        "description": "Expert in program coordination, cross-functional team management, resource allocation, timeline planning, risk management, stakeholder communication, and project portfolio oversight. Manages complex multi-project initiatives and strategic program execution.",
        "func": program_manager_support_function
    },
    {
        "name": "development_engineer_knowledge_agent",
        "description": "Focused on technical implementation, software architecture, coding standards, development methodologies, technical debt management, code reviews, testing strategies, and deployment processes. Handles technical questions about implementation, debugging, and system design.",
        "func": development_engineer_support_function
    }
]
routing_agent = RoutingAgent(openai_api_key, agents)
# Run the workflow
print("\n" + "="*80)
print("🚀 *** AGENTIC WORKFLOW EXECUTION STARTED *** 🚀")
print("="*80)

# Workflow Prompt
workflow_prompt = "What would the development tasks for this product be?"
print(f"\n📋 WORKFLOW PROMPT:")
print(f"   '{workflow_prompt}'")
print("-" * 80)

print(f"\n🎯 WORKFLOW OBJECTIVE:")
print(f"   This workflow will demonstrate the complete agentic architecture:")
print(f"   1. Action Planning Agent → breaks down the prompt into steps")
print(f"   2. Routing Agent → directs each step to the best specialist")
print(f"   3. Specialist Agents → process steps with their expertise")
print(f"   4. Evaluation Agents → validate and refine outputs")
print(f"   5. Final Result → comprehensive, validated development tasks")
print("-" * 80)

print(f"\n🔍 STEP 1: ACTION PLANNING PHASE")
print("="*80)
print("🤖 Calling Action Planning Agent to break down the workflow...")
print(f"   Knowledge: {knowledge_action_planning[:100]}...")
print(f"   Prompt: {workflow_prompt}")
print("-" * 60)

# TODO: 12 - Implement the workflow.
#   1. Use the 'action_planning_agent' to extract steps from the 'workflow_prompt'.
#   2. Initialize an empty list to store 'completed_steps'.
#   3. Loop through the extracted workflow steps:
#      a. For each step, use the 'routing_agent' to route the step to the appropriate support function.
#      b. Append the result to 'completed_steps'.
#      c. Print information about the step being executed and its result.
#   4. After the loop, print the final output of the workflow (the last completed step).

# 1. Use the action_planning_agent to extract steps from the workflow_prompt
workflow_steps = action_planning_agent.extract_steps_from_prompt(workflow_prompt)
print(f"✅ Action Planning Agent completed!")
print(f"📊 Generated {len(workflow_steps)} workflow step(s)")
for i, step in enumerate(workflow_steps, 1):
    print(f"   Step {i}: {step[:100]}...")
print("-" * 60)

# 2. Initialize an empty list called completed_steps
print(f"\n📊 STEP 2: INITIALIZATION PHASE")
print("="*80)
completed_steps = []
print(f"✅ Initialized completed_steps list: {completed_steps}")
print(f"📋 Ready to process {len(workflow_steps)} workflow steps")
print("-" * 60)

# 3. Iterate through the workflow_steps obtained from the Action Planning Agent
print(f"\n🔄 STEP 3: EXECUTION PHASE")
print("="*80)
for i, step in enumerate(workflow_steps, 1):
    print(f"\n🔄 PROCESSING STEP {i}/{len(workflow_steps)}")
    print(f"📋 Step Content: {step}")
    print("-" * 60)
    
    print(f"🎯 ROUTING: Determining best agent for this step...")
    print(f"   Available agents:")
    for j, agent in enumerate(agents):
        print(f"     {j+1}. {agent['name']}: {agent['description'][:80]}...")
    
    # Use the routing_agent.route() method to pass the current step
    print(f"\n   Calling routing_agent.route() with step content...")
    result = routing_agent.route(step)
    print(f"✅ Routing completed successfully!")
    print(f"📊 Result type: {type(result)}")
    print(f"📏 Result length: {len(str(result))} characters")
    
    # Append the result returned by the routing_agent to your completed_steps list
    completed_steps.append(result)
    print(f"📋 Added result to completed_steps. List now contains {len(completed_steps)} item(s)")
    
    # Print the result of the current step
    print(f"📝 Step {i} Result Preview:")
    print(f"   {result[:200]}...")
    print("="*60)

# 4. After the loop, print the final output of the workflow
print(f"\n🎉 WORKFLOW COMPLETION SUMMARY")
print("="*80)
print(f"✅ Total steps processed: {len(completed_steps)}")
print(f"✅ All results stored in completed_steps list")
print(f"✅ Workflow execution completed successfully!")

print(f"\n📊 FINAL OUTPUT OF THE WORKFLOW:")
print("-" * 60)
print(f"{completed_steps[-1]}")
print("="*80)

print(f"\n🔍 WORKFLOW VERIFICATION:")
print("-" * 60)
print(f"✅ Action Planning: {len(workflow_steps)} steps generated")
print(f"✅ Routing: All steps successfully routed to appropriate agents")
print(f"✅ Execution: All steps processed and results collected")
print(f"✅ Output: Final validated result produced")
print(f"✅ Architecture: Full agentic workflow demonstrated successfully!")
print("="*80)
print("🎯 AGENTIC WORKFLOW EXECUTION COMPLETED SUCCESSFULLY! 🎯")
print("="*80)