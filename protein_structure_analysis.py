from Bio.PDB import PDBList

pdbl = PDBList()

pdb_ids =["1ALK", "1EW2", "5GTE"]

for pdb_id in pdb_ids:
    pdbl.retrieve_pdb_file(pdb_id, pdir="pdb_files/", file_format="pdb", overwrite=True)

pdbl.download_pdf_files(pdb_ids, pdir="pdb_files/", file_fomat="pdb" , overwrite=True)