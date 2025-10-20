<h2><i class="bi-arrows-move"></i> Blue Core Naïve Knowledge Graph RAG</h2>

### Triples Vector Database for RAG 
Similar to the recently announced Wikidata Vector Database and API[^1], the Blue Core project uses a
[Milvus](https://milvus.io/) vector database to store Work and Instance triples vectors for use by 
internal AI agents like the de-duplicate Agent. The vector database will support a planned AI Agent
for generating SPARQL queries based on a user's prompt that can be run on a combined RDF graph of 
BIBFRAME Works and Instances in the Blue Core's Graph Toolbox.

[^1]: [Wikidata Embedding Project ](https://www.wikidata.org/wiki/Wikidata:Embedding_Project)

