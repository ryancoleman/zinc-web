zinc-web
========

python scripts to fetch ZINC codes for smiles input

Examples

 ./smiles2zinc.py test.smi

should return 

COc1ccc(cc1C2OCC(CO2)(CO)[N+](=O)[O-])[N+](=O)[O-]	ZINC03616985

And so should 

 cat test.smi | ./smiles2zinc.py
