## Blue Core Model Context Protocol (MCP) Server
Released last year by [Anthropic](https://www.anthropic.com/), the 
Model Context Protocol[^1] is an open-source specification for connecting AI
agents and applications to external systems.

The MCP Servers are programs that run either
locally or remotely and expose specific functionality through
tools, resources, and pre-built instruction templates or prompts.

- MCP Server tools provide functions that the LLMs can call based on
  the user interactions. 
- MCP Resources are typically read-only access to information that 
  enrich the context that is provided to the model such as file context,
  API documentation or database schemas.
- MCP Prompts are provided to help the model to use the tools and 
  resources.  

MCP is based on a client-server architecture with a MCP 
Host that has one or more MCP clients connect one-on-one
with a MCP Server. The MCP client maintains a connection 
to the MCP Server and then provides the model context to 
the MCP Host that is forwarded to a generative AI model.

### Blue Core API MCP Server


[^1]: [What is the Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro)
