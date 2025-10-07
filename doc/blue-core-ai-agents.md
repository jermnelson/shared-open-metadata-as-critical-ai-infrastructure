## Blue Core AI Agents
From its inception, Blue Core is building AI functionality into its 
infrastructure. As explained in a previous slide, Blue Core Triples
Vector store, provides Graph-based RAG for use by both internal and
external AI Agents.

Our first AI agent de-duplicates incoming BIBFRAME Works and Instances using
a triples vector database. Instead of implementing complex rule set, the AI agent uses both system and 
dynamic prompts based on simple descriptions of the conditions for determining if a new BIBFRAME Work or 
Instance is already duplicated in an existing Work or Instance. 

The second AI agent in active development is a search agent that queries 
the Blue Core database, Library of Congress id.loc.gov linked data services,
and Wikidata and from the search results, a user can construct BIBFRAME Works
and Instances for further manipulation and saving to the Blue Core database.

The third AI agent provides help in constructing SPARQL queries for retrieving
and updating information in the loaded graph.
 
