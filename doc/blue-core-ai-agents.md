<h2><i class="bi-robot"></i> Blue Core AI Agents</h2>

From its inception, Blue Core is building AI functionality into its 
infrastructure. As explained in previously , Blue Core Triples
Vector store, provides Graph-based RAG for use by both internal and
external AI Agents.

### Current and Planned AI Agents
Our first AI agent in active development de-duplicates incoming 
BIBFRAME Works and Instances using a triples vector database. 
Instead of implementing complex rule set, the AI agent uses both system and 
dynamic prompts based on simple descriptions of the conditions 
for determining if a new BIBFRAME Work or Instance is already duplicated 
in an existing Work or Instance. 

The second AI agent will be a search agent that queries 
the Blue Core database, Library of Congress id.loc.gov linked data services,
and Wikidata and from the search results, a user can construct BIBFRAME Works
and Instances for further manipulation and saving to the Blue Core database.

The third AI agent will provide help in constructing SPARQL queries for retrieving
and updating information in the loaded graph.

### Implementation 
- Uses the [Pydantic AI](https://ai.pydantic.dev/) agent framework
- Open source code available on Github at [https://github.com/blue-core-lod/bluecore-agents](https://github.com/blue-core-lod/bluecore-agents)
