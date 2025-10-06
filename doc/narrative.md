# Shared Open Metadata as Critical AI Infrastructure
In the four years spanning 2021 to 2024, the total investment in Artificial Intelligence is estimated to
be over 1.06 trillion US dollars, with Generative AI alone accounting for $33.9 billion dollars in 2024[^1].
With this huge influx of money, existing companies and start-up companies are applying Generative AI across
most parts of the global economy. An incomplete survey the business news headlines in the past month
emphasize the wide range of human activities where AI is being applied:

- [AI recruiter Alex raises $17M to automate initial job interviews][^2] 


## Hallucinations of Large Language Models
A persistent problem, even for the frontier Large Language Models from OpenAI, Antropic, Google, and
Deep Seek, is the tendency for these models to fabricate facts in an increasingly pervasive fashion.
Because Large Language Models are transformer-based neural networks that at their core are predicting
the next series of tokens based on its context, this variability means that hallucinations are 
fundamental to this technology. 

In their paper, *Why Language Models Hallucinate*[^8], Open AI researchers assert that hallucinations
are a consequence of the how models are trained and awarded for guessing on benchmarks and tests and that
the it isn't necessarily because of the nature of the LLM architecture.
 

The commercial vendors of these LLMs all attempt to minimize 
the hallucinations of their models, with varying success, including 


## Challenges and Opportunities of AI Agents
Beyond text, image, audio, or video generation from direct user prompts, AI agents based on generative AI
pose challenges and opportunities. Broadly defined, AI agents are software systems or programs that use 
AI models to reason and initiate actions and tasks towards one or more goals. In more complex workflows,
multiple AI agents coordinate work towards shared goals for the system. Web Browsers that embed agents,
like Claude's Chrome browser extension[^3], allow these agents full access to the saved passwords and
web sites and can initiate actions like filling forms and perform other interactions with websites. 
Already these AI browsers present significant concerns in higher education where these browsers can log into 
learning management systems, respond to discussions, take quizzes, and simulate other student behavior
with no or minimal direction by the student.[^4] These new AI browsers present significant security threats 
and potential legal liability but also  offer significant time savings and productivity boosts for users 
automating their personal workflows.

Within the Blue Core Project, our first AI agent de-duplicates incoming BIBFRAME Works and Instances using
a triples vector database. Instead of implementing complex rule set, the AI agent uses both system and 
dynamic prompts based on simple descriptions of the conditions for determining if a new BIBFRAME Work or 
Instance is already duplicated in an existing Work or Instance. 


## Knowledge Graphs in Libraries, Museums, Galleries, and other Cultural Heritage Institutions 
In 2011, the Library of Congress released version 1.0 of the Bibliographic Framework vocabulary, shorted
to BIBFRAME, as a replacement for MARC in describing bibliographic entities like books, images, serials,
and other creative endeavors. BIBFRAME is a Resource Description Framework or RDF vocabulary that represents 
these endeavors as a directed graph made up subject-predicate-object triples. 

[Getty Museums]()

## Knowledge Graph RAG
A specialized case of Retrieval Augmented Generation (RAG), using Knowledge Graphs as means to ground and 
provide context for Large Language Models responses, is offered as an add-on service by Neo4J[^6], Microsoft[^7],
and other technology vendors.  

## Blue Core AI Services
### Triples Vector Database for RAG 
Similar to the recently announced Wikidata Vector Database and API[^5], the Blue Core project uses a
[Milvus](https://milvus.io/) vector database to store Work and Instance triples vectors for use by 
internal AI agents like the de-duplicate Agent. The vector database will support a planned AI Agent
for generating SPARQL queries based on a user's prompt that can be run on a combined RDF graph of 
BIBFRAME Works and Instances in the Blue Core's Graph Toolbox.  

### Work and Instance Embeddings API
The Blue Core API current Work and Instance embeddings endpoint provide two key functions. The 
first endpoint generates vectors for each BIBFRAME Work and Instance triple based on the latest version of
the entity's RDF. The second endpoint allows external services to access the triple vectors for
a Work or Instance.

## The Perils of Artificial General Intelligence
The development of Artificial General Intelligence (AGI) invokes heated emotions on many sides
of the debate. From Eliezer Yudknowsky and Nate Soares recent book, *If Anyone Builds it, Everyone Die*,
to Sam Altman's boosterism of AGI as another OpenAI product. 


## Sources
[^1]: [The 2025 AI Index Report](https://hai.stanford.edu/ai-index/2025-ai-index-report/economy) from Stanford
      University Human-Centered Artificial Intelligence
[^2]: https://techcrunch.com/2025/09/29/ai-recruiter-alex-raises-17m-to-automate-initial-job-interviews/
[^3]: [Claude for Chrome](https://www.anthropic.com/news/claude-for-chrome)
[^4]: [Colleges And Schools Must Block And Ban Agentic AI Browsers Now. Here’s Why.](https://www.forbes.com/sites/avivalegatt/2025/09/25/colleges-and-schools-must-block-agentic-ai-browsers-now-heres-why/)
[^5]: [Wikidata Embedding Project ](https://www.wikidata.org/wiki/Wikidata:Embedding_Project)
[^6]: [What is Graph RAG?](https://neo4j.com/blog/genai/what-is-graphrag/)
[^7]: [Welcome to GraphRAG](https://microsoft.github.io/graphrag/)


## What I want to say
- LLMs hallucinations are a continuing problem with RAG a primary technique for minimizing these hallucinations
- Graph RAG is a subset of RAG, provides relationship context for LLMs
- GLAM institutions moving towards representing their collections as graphs primarily using RDF but other
  graph models can and should exist.
- These graphs beyond establishing relationships are better and more powerful if they are open and can 
  seamlessly include other GLAM graphs including Wikidata
- GLAM graphs should be actively curated by both humans and AI Agents
- GLAM graphs that are open would allow other AI systems to use as part of agentic workflows to validate
  factual assertions made by LLMs
- More broadly, GLAM graphs should reflect institutional values, surfacing these values as part of the 
  open metadata graphs.
- Open question: could adding values to GLAM open metadata graphs be part of the solution for LLM alignment? 
- Blue Core's open metadata provides both raw RDF of BIBFRAME Works and Instances along with vector embeddings
  of the RDF triples available through API
- Blue Core's API endpoints as MCP Server
- Some Blue Core AI Agents will be available through API; other AI agents more internal. Provide examples of
  these multi-agent systems within a GLAM context.   

