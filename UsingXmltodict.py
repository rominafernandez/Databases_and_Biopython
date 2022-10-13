## Exercise 15 - Using xmltodict

# Use the module xmltodict to read in one of your XML files
# Print out the dictionary
# Print out some of the values

import json
import xmltodict

with open('Proteins.xml') as fd:
    doc = xmltodict.parse(fd.read())

# print out the whole dictionary in a nice format
tmp = json.dumps(doc, indent=4)
print(tmp)
print("")

# print out info for all proteins
counter1 = 0
for protein in doc["Proteins"]["Protein"]:
    print(f"The protein {protein['Abbreviation']} consists of {protein['Amino_acids']} amino acids")
    print(f"The full name of the protein is {protein['Name']}")
    if type(doc["Proteins"]["Protein"][counter1]["Modifications"]["Modification"]) == list:
        print(f'It has {len(doc["Proteins"]["Protein"][counter1]["Modifications"]["Modification"])} post translational modifications:')
    else:
        print("It has 1 post translational modification:")
    counter1 +=1
    counter2 = 0
    if type(protein["Modifications"]["Modification"]) == dict:
        print(f'  {protein["Modifications"]["Modification"]["Name"]} at the amino acid {protein["Modifications"]["Modification"]["Amino_acid"]} at position {protein["Modifications"]["Modification"]["Position"]}')
    else:
        for mod in range(len(protein["Modifications"]["Modification"])):
            print(f'  {protein["Modifications"]["Modification"][counter2]["Name"]} at the amino acid {protein["Modifications"]["Modification"][counter2]["Amino_acid"]} at position {protein["Modifications"]["Modification"][counter2]["Position"]}')
            counter2 += 1
    print("")
