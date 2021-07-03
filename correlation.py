# Add the functions in this file
import json
from math import sqrt

def load_journal ( file_name )  :
	with open ( file_name , "r" ) as j_file :
		data = json.load ( j_file )
	return data
	
def compute_phi ( file_name , event ) :
	data = load_journal ( file_name )
	n1_ = 0
	n0_ = 0
	n_0 = 0
	n_1 = 0
	n11 = 0
	n00 = 0
	n10 = 0
	n01 = 0
	for i in data :
		if ( i ['squirrel'] == True ) :
			n_1 += 1 
			for j in i [ 'events' ] :
				if ( j == event ) : 
					n1_ += 1
					n11 += 1
				else :
					n0_ += 1
					n01 += 1
		else :
			n_0+=1 
			for j in i [ 'events' ] :
				if ( j == event ) : 
					n1_ += 1
					n10 += 1
				else :
					n0_ += 1
					n00 += 1
	corr=(n11 * n00 - n10 * n01) / sqrt(n1_ * n0_ * n_1 * n_0)
	return corr

def compute_correlations ( file_name ) :
	data = load_journal ( file_name )
	corr_log = dict();
	for i in data :
		for event in i [ 'events' ] :
			if event not in corr_log :
				corr_log [ event ] = compute_phi ( file_name , event )
	return corr_log
