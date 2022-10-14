## Exercise 8 - using ez.einfo

# Use ez.einfo to make ten different queries about different databases to the NCBI Entrez system
# Remember you can get a list of databases by using ez.einfo without any parameters to get a list of potential databases
# Loop through Dict["DbInfo"]["FieldList"] to see what fields are available to you for searching in these databases
import Bio.Entrez as ez
ez.email = "rominafernandez@outlook.de"

# Get a list of all dbs
with ez.einfo() as query:
    query_dict = ez.read(query)
print(query_dict["DbList"])

# Get the field list for pubmed
print("")
print("PubMed")
with ez.einfo(db="pubmed") as query:
    pubmed_dict = ez.read(query)
for field in pubmed_dict["DbInfo"]["FieldList"]:
    print("%(Name)s, %(FullName)s, %(Description)s" % field)

# Get the field list for protein
print("")
print("Protein")
with ez.einfo(db="protein") as query:
    protein_dict = ez.read(query)
for field in protein_dict["DbInfo"]["FieldList"]:
    print("%(Name)s, %(FullName)s, %(Description)s" % field)

# Get the field list for nucleotide
print("")
print("Nucleotide")
with ez.einfo(db="nucleotide") as query:
    nucleotide_dict = ez.read(query)
for field in nucleotide_dict["DbInfo"]["FieldList"]:
    print("%(Name)s, %(FullName)s, %(Description)s" % field)

# Get the field list for genome
print("")
print("Genome")
with ez.einfo(db="genome") as query:
    genome_dict = ez.read(query)
for field in genome_dict["DbInfo"]["FieldList"]:
    print("%(Name)s, %(FullName)s, %(Description)s" % field)

# Get the field list for gene
print("")
print("Gene")
with ez.einfo(db="gene") as query:
    gene_dict = ez.read(query)
for field in gene_dict["DbInfo"]["FieldList"]:
    print("%(Name)s, %(FullName)s, %(Description)s" % field)
