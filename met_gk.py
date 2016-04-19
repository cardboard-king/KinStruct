

import pandas as pd
import os


import __main__
__main__.pymol_argv = [ 'pymol', '-cqm'] # Quiet and no GUI

import pymol
pymol.finish_launching()
print "pymol launched"



myurl1 = "/Users/matthias/Documents/hibit.in/KLIFS_LigandBound2/HUMAN/"
myurl2 = "/Users/matthias/Documents/hibit.in/KLIFS_LigandUnBound2/HUMAN/"


def make_extraction(dir_path):
	file_path = dir_path + "/pocket.mol2"
	print file_path
	pymol.cmd.load(file_path)
	pymol.cmd.remove("all")


def make_extractions(organism_path):
	kinases = pd.Series([
		name for name in os.listdir(organism_path) if os.path.isdir(organism_path + name)])
	print "kinases extract"
	for kinase in kinases:
		kinase_path = organism_path + "/" + kinase
		alternatives = pd.Series([
			name for name in os.listdir(kinase_path) if os.path.isdir(kinase_path + name)])
		print "alternatives extract"
		for alternative in alternatives:
			make_extraction(kinase_path + "/" + alternative)

print "start"
make_extractions(myurl1)


pymol.cmd.quit()




