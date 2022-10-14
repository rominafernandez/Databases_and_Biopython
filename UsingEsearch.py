## Exercise 9 - Searching NCBI databases

# Create at least three different search queries for five databases of the NCBI
# Print out two different entries of your resulting dictionaries
# For more information: https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.ESearch
import Bio.Entrez as ez
ez.email = "rominafernandez@outlook.de"

with ez.esearch(db="pubmed", term="Interleukin-6[TITL]", retmax="30") as query:
    pub_list = ez.read(query)
print(pub_list["Count"])

with ez.esearch(db="gene", term="IL6[GENE] AND human[ORGN]", retmax = "30") as query:
    gene_list = ez.read(query)
print(gene_list["IdList"])

with ez.esearch(db="protein", term="IL6[GENE]") as query:
    prot_list = ez.read(query)
print(prot_list)
