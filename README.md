# ClimatePolicyChallenge
Increasing amounts of structured data are published as Knowledge Bases. Thus we change the web from a web of documents into a web of entities. 
The ideal way for our users to query from Climate Documents is using Natural Language Interfaces, where users can express 
their information needs using Natural Language without being aware of the heterogeneous vocabulary of these documents.
Recent researches have focused on advanced Question Answering techniques over Knowledge Graphs by translating Natural Language queries into formal SPARQL queries.
For this hackathon we have created an Azure Search engine based on the legislation documents (legislations, laws and events) 
and added Cognitive Skills upon it (extraction of Names, Locations, Entities). 
This allows to perform full-text research by expressing a request in a natural language.
For instance, "What events are the laws NNN focusing on?"
The next step is to extend the understanding of the request by adding the Knowledge Graph, for a better query mapping.
Furthermore, more researches will be followed in refining the semantic similarity based type expansion algorithm to optimize both the execution time and search performance.
The ideal way for casual users to query from KGs is using Natural Language Interfaces (NLI), where users can express their information needs using Natural Language (NL) 
without being aware of the heterogeneous LOD vocabulary. The research in NLI for KGs has
its roots in the application of traditional keyword-based information retrieval techniques to indexed RDF data such as the works in semantic search.
Recent researches have focused on advanced Question Answering (QA) techniques over KGs by translating NL queries into formal SPARQL queries. 
In this work, we have restricted the queries to queries with just one relation, called Single Relation Type-based Queries (SRTQs) such as
full sentence query Give me all the universities located in Spain. An abbreviated version of SRTQ can be expressed with keywords, i.e. universities Spain. 
This example of SRTQ can be rewritten as an equivalent conjunctive formal logic expression ?x ← (?x, is, University) ∩ (?x, ?relation, Spain) where ontology class
University, and instance Spain are restrictions on the variable x.
![alt text](https://climateradardata.blob.core.windows.net/temp/Architecture.jpg)
