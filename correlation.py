# Add the functions in this file
import json
from math import sqrt

def load_journal ( file_name )  :

	j_file = open ( file_name , "r" )
	data = json.load ( j_file )
	
	return data
	
def compute_phi ( file_name , event ) :

	data = load_journal ( file_name )
	
	n11 = 0
	n00 = 0
	n10 = 0
	n01 = 0
	
	for i in data :
		if event in i [ 'events' ] and i [ 'squirrel' ] == True  :
			n11 += 1
		if event in i [ 'events' ] and i [ 'squirrel' ] == False  :
			n10 += 1
		if event not in i [ 'events' ] and i [ 'squirrel' ] == True  :
			n01 += 1
		if event not in i [ 'events' ] and i [ 'squirrel' ] == False  :
			n00 +=1
	n1_ = n10 + n11
	n0_ = n01 + n00
	n_1 = n01 + n11
	n_0 = n00 + n10
	
	corr=(n11 * n00 - n10 * n01) / sqrt(n1_ * n0_ * n_1 * n_0)
	return corr

def compute_correlations ( file_name ) :

	data = load_journal ( file_name )
	corr_log = dict() ;
	
	for i in data :
		for event in i [ 'events' ] :
			if event not in corr_log :
				corr_log [ event ] = compute_phi ( file_name , event )
				
	return corr_log 
	
def diagnose ( file_name ) : 

	corr_log = compute_correlations ( file_name )
	
	mx = -1024
	mn = 1024
	
	for k,v in corr_log.items() :
	
		if ( v > mx ) :
			mx = v
			max_r = k
		if ( v < mn ) :
			mn = v
			min_r = k
	return max_r , min_r 

		
