# Shared Open Metadata as Critical AI Infrastructure
In the four years spanning 2021 to 2024, the total investment in Artificial Intelligence is estimated to
be over 1.06 trillion US dollars, with Generative AI alone accounting for $33.9 billion dollars in 2024[^1].
With this huge influx of money, existing companies and start-up companies are applying Generative AI across
most parts of the global economy. An incomplete survey the business news headlines in the past month
emphasize the wide range of human activities where AI is being applied:

- [AI recruiter Alex raises $17M to automate initial job interviews][^2] 

## The Perils of Artificial General Intelligence
The development of Artificial General Intelligence (AGI) invokes heated emotions on many sides
of the debate. From Eliezer Yudknowsky and Nate Soares recent book, *If Anyone Builds it, Everyone Die*,
to Sam Altman's boosterism of AGI as another OpenAI product. 


## Hallucinations of Large Language Models
A persistent problem, even for the frontier Large Language Models from OpenAI, Antropic, Google, and
Deep Seek, is the tendency for these models to fabricate facts in an increasingly pervasive fashion.

## Alignment Challenges

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
dynamic prompts based on simple descriptions of the conditions for determining if a new Work or Instance is 
already duplicated in an existing Work or Instance. 


## Knowledge Graphs in Libraries, Museums, Galleries, and other Cultural Heritage Institutions 
In 2011, the Library of Congress released version 1.0 of the Bibliographic Framework vocabulary, shorted
to BIBFRAME, as a replacement for MARC in describing bibliographic entities like books, images, serials,
and other creative endeavors. BIBFRAME is a Resource Description Framework or RDF vocabulary that represents 
these endeavors as a directed graph.

[Getty Museums]()

## Sources
[^1]: [The 2025 AI Index Report](https://hai.stanford.edu/ai-index/2025-ai-index-report/economy) from Stanford
      University Human-Centered Artificial Intelligence
[^2]: https://techcrunch.com/2025/09/29/ai-recruiter-alex-raises-17m-to-automate-initial-job-interviews/
[^3]: [Claude for Chrome](https://www.anthropic.com/news/claude-for-chrome)
[^4]: [Colleges And Schools Must Block And Ban Agentic AI Browsers Now. Here’s Why.](https://www.forbes.com/sites/avivalegatt/2025/09/25/colleges-and-schools-must-block-agentic-ai-browsers-now-heres-why/)
