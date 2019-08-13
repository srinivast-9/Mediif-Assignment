def group_by_owners(idict):
    owners = set(idict.values())
    odict = {}
    for owner in owners:
        odict.update({owner: []})

    for filename, owner in idict.items():
        odict[owner].append(filename)

    print(odict)
    return odict

d = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}

group_by_owners(d)