# function to create acronym
def abbr(stng):
    # add first letter
    oupt = stng[0]


    for i in range(1, len(stng)):
        if stng[i - 1] == ' ':
        
            oupt += stng[i]

    # uppercase oupt
    oupt = oupt.upper()
    return oupt


# input string
inpt1 = "Lovely Professional Univercity"

# output acronym
print(abbr(inpt1))
