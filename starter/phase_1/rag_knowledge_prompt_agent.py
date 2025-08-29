# TODO: 1 - Import RAGKnowledgePromptAgent
import os
from datetime import datetime
from dotenv import load_dotenv
from workflow_agents.base_agents import RAGKnowledgePromptAgent
# Load environment variables from .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")

persona = "a college professor, your answer always starts with: Dear students"
RAG_knowledge_prompt_agent = RAGKnowledgePromptAgent(openai_api_key, persona)

knowledge_text = """
In the historic city of Boston, Clara, a marine biologist and science communicator, began each morning analyzing sonar data to track whale migration patterns along the Atlantic coast.
She spent her afternoons in a university lab, researching CRISPR-based gene editing to restore coral reefs damaged by ocean acidification and warming.
Clara was the daughter of Ukrainian immigrants—Olena and Mykola—who fled their homeland in the late 1980s after the Chernobyl disaster brought instability and fear to their quiet life near Kyiv.

Her father, Mykola, had been a radio engineer at a local observatory, skilled in repairing Soviet-era radio telescopes and radar systems that tracked both weather patterns and cosmic noise.
He often told Clara stories about jury-rigging radio antennas during snowstorms and helping amateur astronomers decode signals from distant pulsars.
Her mother, Olena, was a physics teacher with a hidden love for poetry and dissident literature. In the evenings, she would read from both Ukrainian folklore and banned Western science fiction.
They survived harsh winters, electricity blackouts, and the collapse of the Soviet economy, but always prioritized education and storytelling in their home.
Clara’s childhood was shaped by tales of how her parents shared soldering irons with neighbors, built makeshift telescopes, and taught physics to students with no textbooks but endless curiosity.

Inspired by their resilience and thirst for knowledge, Clara created a podcast called **"Crosscurrents"**, a show that explored the intersection of science, culture, and ethics.
Each week, she interviewed researchers, engineers, artists, and activists—from marine ecologists and AI ethicists to digital archivists preserving endangered languages.
Topics ranged from brain-computer interfaces, neuroplasticity, and climate migration to LLM prompt engineering, decentralized identity, and indigenous knowledge systems.
In one popular episode, she explored how retrieval-augmented generation (RAG) could help scientific researchers find niche studies buried in decades-old journals.
In another, she interviewed a Ukrainian linguist about preserving dialects lost during the Soviet era, drawing parallels to language loss in marine mammal populations.

Clara also used her technical skills to build Python-based dashboards that visualized ocean temperature anomalies and biodiversity loss, often collaborating with her best friend Amir, a data engineer working on smart city infrastructure.
Together, they discussed smart grids, blockchain for sustainability, quantum encryption, and misinformation detection in synthetic media.
At a dockside café near Boston Harbor, they often debated the ethical implications of generative AI, autonomous weapons, and the carbon footprint of LLM training runs.

In quieter moments, Clara translated traditional Ukrainian embroidery patterns into generative AI art, donating proceeds to digital archives preserving Eastern European culture.
She contributed to open-source projects involving semantic search, vector databases, and multimodal embeddings—often experimenting with few-shot learning and graph-based retrieval techniques to improve her podcast's episode discovery engine.

One night, while sharing homemade borscht, Clara told Amir how her grandparents once used Morse code to transmit encrypted weather updates through the Carpathian Mountains during World War II.
The story sparked a conversation about ancient navigation, space weather interference with submarine cables, and the neuroscience behind why humans create myths to understand uncertainty.

To Clara, knowledge was a living system—retrieved from the past, generated in the present, and evolving toward the future.
Her life and work were testaments to the power of connecting across disciplines, borders, and generations—exactly the kind of story that RAG models were born to find.
"""

# Test chunking first
print("Testing chunking...")
chunks = RAG_knowledge_prompt_agent.chunk_text(knowledge_text)
print(f"Created {len(chunks)} chunks")

# Create output content for file
output_content = []
output_content.append("=== RAG KNOWLEDGE PROMPT AGENT OUTPUT ===")
output_content.append(f"Persona: {persona}")
output_content.append(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
output_content.append("")
output_content.append("=== CHUNKING RESULTS ===")
output_content.append(f"Total chunks created: {len(chunks)}")
output_content.append(f"Chunk size: {RAG_knowledge_prompt_agent.chunk_size}")
output_content.append(f"Chunk overlap: {RAG_knowledge_prompt_agent.chunk_overlap}")
output_content.append("")
output_content.append("=== CHUNK DETAILS ===")
for i, chunk in enumerate(chunks):
    output_content.append(f"Chunk {i+1}:")
    output_content.append(f"  Size: {chunk['chunk_size']} characters")
    output_content.append(f"  Text: {chunk['text'][:100]}...")
    output_content.append("")

# Test embeddings
print("Testing embeddings...")
try:
    embeddings = RAG_knowledge_prompt_agent.calculate_embeddings()
    print(f"Created embeddings for {len(embeddings)} chunks")
    
    output_content.append("=== EMBEDDING RESULTS ===")
    output_content.append(f"Embeddings created: {len(embeddings)}")
    output_content.append(f"Embedding model: text-embedding-3-large")
    output_content.append("")
    
    # Test finding prompt in knowledge
    prompt = "What is the podcast that Clara hosts about?"
    print(f"Prompt: {prompt}")
    result = RAG_knowledge_prompt_agent.find_prompt_in_knowledge(prompt)
    print(f"Result: {result}")
    
    output_content.append("=== RAG QUERY RESULTS ===")
    output_content.append(f"Query: {prompt}")
    output_content.append(f"Response: {result}")
    output_content.append("")
    output_content.append("=== ANALYSIS ===")
    output_content.append("This RAG system demonstrates:")
    output_content.append("- Text chunking for manageable processing")
    output_content.append("- Vector embeddings for semantic search")
    output_content.append("- Retrieval-augmented generation")
    output_content.append("- Finding relevant knowledge chunks")
    
except Exception as e:
    print(f"Error: {e}")
    print("Chunks created:", len(chunks))
    print("First chunk:", chunks[0] if chunks else "No chunks")
    
    output_content.append("=== ERROR ENCOUNTERED ===")
    output_content.append(f"Error: {e}")
    output_content.append(f"Chunks created: {len(chunks)}")
    if chunks:
        output_content.append(f"First chunk: {chunks[0]}")

# Save to output file
output_filename = f"output/rag_knowledge_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
with open(output_filename, 'w') as f:
    f.write('\n'.join(output_content))

# Also print to console
print("=== RAG KNOWLEDGE PROMPT AGENT OUTPUT ===")
print(f"Persona: {persona}")
print(f"Output saved to: {output_filename}")
print("")
print("=== CHUNKING RESULTS ===")
print(f"Total chunks created: {len(chunks)}")
print(f"Chunk size: {RAG_knowledge_prompt_agent.chunk_size}")
print(f"Chunk overlap: {RAG_knowledge_prompt_agent.chunk_overlap}")
print("")
print("=== CHUNK DETAILS ===")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:")
    print(f"  Size: {chunk['chunk_size']} characters")
    print(f"  Text: {chunk['text'][:100]}...")
    print()

if 'embeddings' in locals():
    print("=== EMBEDDING RESULTS ===")
    print(f"Embeddings created: {len(embeddings)}")
    print(f"Embedding model: text-embedding-3-large")
    print("")
    print("=== RAG QUERY RESULTS ===")
    print(f"Query: {prompt}")
    print(f"Response: {result}")
    print("")
    print("=== ANALYSIS ===")
    print("This RAG system demonstrates:")
    print("- Text chunking for manageable processing")
    print("- Vector embeddings for semantic search")
    print("- Retrieval-augmented generation")
    print("- Finding relevant knowledge chunks")
else:
    print("=== ERROR ENCOUNTERED ===")
    print(f"Error: {e}")
    print(f"Chunks created: {len(chunks)}")
    if chunks:
        print(f"First chunk: {chunks[0]}")