<h2><i class="bi-layout-text-window-reverse"></i> Blue Core Graph Services</h2>

The Blue Core project provides two Linked Data Editors and a Graph Toolbox to enable management of Blue Core Linked Open Metadata

### Linked Data Editors
Blue Core supports two complementary editors for working with linked data:

- **Sinopia** is an open-source linked data environment that allows users to 
  create, load, and edit RDF resources through a web-based interface. While 
  optimized for BIBFRAME vocabulary, Sinopia also supports other ontologies 
  in resource graphs. 
- **Marva** is a BIBFRAME editor developed by the Library of Congress that 
  focuses on interoperability between BIBFRAME RDF resources and the MARC21 format.

Both Sinopia and Marva have been modified to use the Blue Core API and database so that 
a BIBFRAME Work or Instance resource graph can be edited and saved in one editor and 
opened and edited the other editor.

### Graph Toolbox
The Blue Core Graph Toolbox is a web-based collection of tools that provides graph-based 
functionality, along with a chat interface and assistance from Blue Core AI agents. 
Users can:

- Load RDF descriptions from Blue Core and Sinopia, planned support for Library of Congress 
  and Wikidata
- Query and Update loaded resources using SPARQL
- Convert MARC21 to BIBFRAME RDF resources
- Export loaded graphs as MARC21
- Validate BIBFRAME Works and Instances with the SHACL graphs provided by the 
  BIBFRAME Interoperability Group.

### Demonstration @ [https://dev.bcld.info/](https://dev.bcld.info/)
