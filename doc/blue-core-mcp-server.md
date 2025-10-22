<h2><i class="bi-pci-card-network"></i> Blue Core Model Context Protocol (MCP) Server</h2>

Released last year by [Anthropic](https://www.anthropic.com/), the 
Model Context Protocol[^1] is an open-source specification for connecting AI
agents and applications to external systems.

MCP Servers are programs that run either locally or remotely and expose specific 
functionality through three key components:

- **Tools** provide functions that the LLMs can call based on
  the user interactions. 
- **Resources** offer typically read-only access to information that 
  enriches the context provided to the model, such as file context,
  API documentation or database schemas.
- **Prompts** help the model to use the tools and resources.  

MCP uses a client-server architecture in which an MCP Host connects to one or 
more MCP Clients, each maintaining a one-to-one connection with an MCP Server. 
The MCP Client maintains the connection to its MCP Server and provides model 
context to the MCP Host, which then forwards it to a generative AI model.


[^1]: [What is the Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro)
