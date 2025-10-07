## Knowledge Graph RAG
A specialized case of Retrieval Augmented Generation (RAG), using Knowledge 
Graphs as means to ground and provide context for Large Language Models 
responses, is offered as an add-on service by Neo4J[^1], Microsoft[^2],
and other technology vendors.

Some advantages of a Knowledge Graph RAG system over pure vector RAG systems 
include:

- Leverage the Knowledge Graph relationships between entities to retrieve
  more context that may not be present in the retrieved results of a vector
  RAG system.[^3]
- Capture relationships, filters and ranks retrieved results from vector RAG systems
- Helps in summarization and relationship transversal spanning large data collections or
  large documents.


[^1]: [What is Graph RAG?](https://neo4j.com/blog/genai/what-is-graphrag/)
[^2]: [Welcome to GraphRAG](https://microsoft.github.io/graphrag/)
[^3]: [Knowledge Graph-Guided Retrieval Augmented Generation](https://doi.org/10.48550/arXiv.2502.06864)
