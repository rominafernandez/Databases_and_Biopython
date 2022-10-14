## Exercise 16 - Generate a Tree

# Use the ElementTree module to read in one of your XML files
# Print out the data included in your Tree

import xml.etree.ElementTree as ET
mytree = ET.parse('ProteinStructure.xml')
myroot = mytree.getroot()

# Print info for each protein
for protein in myroot.findall("Protein"):
    # print all general info including the unit
    for x in range(len(protein)-1):
        if protein[x].attrib == {}:
            print(f"{protein[x].tag} = {protein[x].text}")
        else:
            print(f"{protein[x].tag} = {protein[x].text} ({protein[x].attrib['unit']})")
    print(f'The length of the sequence is {len(protein.find("Sequence").text)} amino acids')
    # Print info about secondary structure
    tmp = [elem.tag for elem in protein[6]]
    print(f'The structure consist of {tmp.count("AlphaHelix")} alpha helices, {tmp.count("BetaStrand")} beta strands, {tmp.count("Turn")} turns')
    for y in range(len(protein.find("SecondaryStructure"))):
        print(f"  {protein[6][y].tag} that starts at position {protein[6][y][0].text} and ends at position {protein[6][y][1].text}")
    print("")
print("")
