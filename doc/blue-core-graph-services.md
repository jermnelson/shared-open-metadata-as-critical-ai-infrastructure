## Blue Core Graph Services
To enable management of Blue Core Linked Open Metadata, the Blue Core project provides
two Linked Data Editors and a new Graph Toolbox.

### Linked Data Editors
- **Sinopia**: Sinopia is an open-source linked data environment, allowing users to create,
  load, and edit RDF resources in a web-based editor. Sinopia is optimized for BIBFRAME 
  vocabulary but other ontologies can be used as well in the resource graphs. 
- **Marva**: Marva is a BIBFRAME editor from the Library of Congress that focuses on 
  interoperability between BIBFRAME RDF resources and the MARC21 format. 

Both Sinopia and Marva have been modified to use the Blue Core API and database so that 
a BIBFRAME Work or Instance resource graph can be edited and saved in one editor and 
opened and edited the other editor.

### Graph Toolbox
The Blue Core Graph toolbox, is a web-based collection of tools for more graph-based
functionality along with chat interface and help from the Blue Core AI agents. From
the graph toolbox, users can:

- Load RDF descriptions from Library of Congress, Sinopia, and Wikidata
- Query and Update loaded resources using SPARQL
- Convert MARC21 to BIBFRAME RDF resources
- Export loaded graphs as MARC21
- Validate BIBFRAME Works and Instances with the SHACL graphs provided by the 
  BIBFRAME Interoperability Group.
