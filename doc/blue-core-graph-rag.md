<h2><i class="bi-arrows-move"></i> Blue Core Naïve Knowledge Graph RAG</h2>

### Triples Vector Database for RAG 
Similar to the recently announced Wikidata Vector Database and API[^1], the Blue Core project uses a
[Milvus](https://milvus.io/) vector database to store Work and Instance triples vectors for use by 
internal AI agents like the de-duplicate agent. The vector database will also support a planned AI Agent
that generate SPARQL queries based on a user's prompts, which can then be executed on a combined RDF graph of 
BIBFRAME Works and Instances in the Blue Core's Graph Toolbox.

### Triple Embedding
Each "document" in the Milvus vector database is made up of a serialized n-triple along with 
a identifier to the resource version and the textual representation of the triple for easy
integration with the LLM prompts. Prior to serialization, the RDF graph is skolemized so 
that blank-nodes retrain their context and associations with related URLs.

```code
<https://dev.bcld.info/instances/f769fe62-cba7-4e09-bf21-99357600285d#b23490> <http://id.loc.gov/ontologies/bibframe/mainTitle> "Americans in Spain" .
```

This approach is different from other Knowledge Graph RAG implementations in that it does 
not use a triple-store for LLM queries or employ LLMs for entity identification. Depending on 
the requirements, properties of the directed RDF graph can be added for additional context like:

- Directionality i.e. `subject` -> `predicate` -> `object`
- Grammar
- Graph Operations 

[^1]: [Wikidata Embedding Project ](https://www.wikidata.org/wiki/Wikidata:Embedding_Project)

