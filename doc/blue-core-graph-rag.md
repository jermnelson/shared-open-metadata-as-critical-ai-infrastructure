<h2><i class="bi-arrows-move"></i> Blue Core Naïve Knowledge Graph RAG</h2>

### Triples Vector Database for RAG 
Similar to the recently announced Wikidata Vector Database and API[^1], the Blue Core project uses a
[Milvus](https://milvus.io/) vector database to store Work and Instance triples vectors for use by 
internal AI agents like the de-duplicate Agent. The vector database will support a planned AI Agent
for generating SPARQL queries based on a user's prompt that can be run on a combined RDF graph of 
BIBFRAME Works and Instances in the Blue Core's Graph Toolbox.

### Triple Embedding
Each "document" in the Milvus vector database is made up of a serialized n-triple along with 
a identifier to the resource version and the textual representation of the triple for easy
in integrating with the LLM's prompt. Prior to serialization, the RDF graph is skolemized so 
that blank-nodes retrain part of the context and association with related URLs.

```code
<https://dev.bcld.info/instances/f769fe62-cba7-4e09-bf21-99357600285d#b23490> <http://id.loc.gov/ontologies/bibframe/mainTitle> "Americans in Spain" .
```

This approach is different from other Knowledge Graph RAG implementations in that the 
we're not running a triple-store that the LLM uses for querying the datastore or using the
LLMs for entity identification. Depending on the requirements, properties of the directed RDF 
graph can be added for additional context like:

- Directionality i.e. `subject` -> `predicate` -> `object`
- Grammar
- Graph Operations 

[^1]: [Wikidata Embedding Project ](https://www.wikidata.org/wiki/Wikidata:Embedding_Project)

