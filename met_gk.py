

import pandas as pd
import os
import numpy as np
import warnings


import __main__
__main__.pymol_argv = [ 'pymol', '-cqm'] # Quiet and no GUI


import pymol
pymol.finish_launching()


myurl1 = "/Users/matthias/Documents/hibit.in/KLIFS_LigandBound2/HUMAN/"
myurl2 = "/Users/matthias/Documents/hibit.in/KLIFS_LigandUnBound2/HUMAN/"

saveurl1 = "/Users/matthias/Documents/hibit.in/KLIFS_LigandBound2_gk/HUMAN/"
saveurl2 = "/Users/matthias/Documents/hibit.in/KLIFS_LigandUnBound2_gk/HUMAN/"


def gatekeeper_residue(dir_path):
	file_path = dir_path + "/pocket.mol2"
	


def make_extraction(dir_path,res,save_path = None):
	if save_path == None:
		save_path = dir_path
	file_path1 = dir_path + "/pocket.mol2"
	file_path2 = save_path + "/gk.mol2"
	pymol.cmd.load(file_path1)
	selection_name = "gk"
	selector = "resi " + str(res[0])
	print "selecting: '" + selection_name + "' with: '" + selector + "'"
	pymol.cmd.select(selection_name,selector)
	pymol.cmd.save(file_path2,selection_name)
	pymol.cmd.delete("all")


def make_extractions(organism_path,gatekeepers_path,save_path):
	kinases = pd.Series([
		name for name in os.listdir(organism_path) if os.path.isdir(organism_path + name)])
	gatekeepers = pd.read_csv(gatekeepers_path,index_col = 0).astype(np.float32)
	for kinase in kinases:
		kinase_path = organism_path + kinase + "/"
		save_path1 = save_path + kinase + "/"
		alternatives = pd.Series([
			name for name in os.listdir(kinase_path) if os.path.isdir(kinase_path + name)])
		alternative_labels = alternatives.str.replace("chain","").str.lower().str.replace("_alt[ab]","")
		for alternative, a_label in zip(alternatives,alternative_labels):
			if np.isfinite(gatekeepers.loc[a_label].values):
				save_path2 = save_path1 + alternative
				if not os.path.exists(save_path2):
				    os.makedirs(save_path2)
				make_extraction(kinase_path + alternative,
					gatekeepers.loc[a_label].values.astype(np.int),save_path2)



#make_extractions(myurl1,
#	"/Users/matthias/Documents/hibit.in/development/KinStruct/gatekeepersBound.csv",
#	saveurl1)
make_extractions(myurl2,
	"/Users/matthias/Documents/hibit.in/development/KinStruct/gatekeepersUnbound.csv",
	saveurl2)


pymol.cmd.quit()



