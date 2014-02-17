zinc-web
========

python scripts to fetch ZINC codes for smiles input

Examples

       ./smiles2zinc.py test.smi

should return 

COc1ccc(cc1C2OCC(CO2)(CO)[N+](=O)[O-])[N+](=O)[O-]	ZINC03616985

And so should 

       cat test.smi | ./smiles2zinc.py

Nonsensical input and SMILES that are not found simple return blank lines

        echo 'OUEOUEO' | ./smiles2zinc.py 

SMILES will be canonicalized and searched in ZINC. Due to technical 
reasons, some will return more than one ZINC code

        echo "CCC1=CC(=C(C(=C1O)C(=O)NCC2CCCN2CC)OC)Cl" | ./smiles2zinc.py 

Produces: 

CCc1cc(c(c(c1O)C(=O)NC[C@@H]2CCC[NH+]2CC)OC)Cl	ZINC00001395
CCc1cc(c(c(c1O)C(=O)NC[C@H]2CCC[NH+]2CC)OC)Cl	ZINC01997240
