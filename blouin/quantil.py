def quantil_placer(artist, price):
	q = artist
	qual = price
	### prince interval cutoffs ###
	cut_off_rivera = [6916.32, 15031.68, 33000, 66000, 1200000]
	cut_off_lam = [6600,18622.8, 35951.04, 102249.12, 1123110.21]
	cut_off_cruz = [4247.36, 9791.52, 55800, 146500, 548135]
	cut_off_carrington = [3739.2, 11250, 30240, 112000,	649451.08]
	cut_off_orozco = [2496, 6000, 14400, 42720, 698130]
	cut_off_coronel = [5427.36, 15037.44, 38347.2, 79623.2, 367317.6]
	cut_off_siqueiros = [4536, 15000, 31250, 69324, 429495]
	cut_off_tamayo = [3300, 5179.2, 17500, 168000, 1329550]
	cut_off_bermudez = [3600, 9600, 19020, 37200, 213815]
	
	if q == "Diego Rivera":
	    cut_off = cut_off_rivera
	    if qual>cut_off[4]:
	        estimator = 5
	    elif qual> cut_off[2] and qual< cut_off[4]:
	        estimator = 4
	    elif qual> cut_off[1] and qual< cut_off[2]:
	        estimator = 3
	    elif qual> cut_off[0] and qual< cut_off[1]:
	        estimator = 2
	    else:
	        estimator = 1

	elif q == "Wifredo Lam":
	    cut_off = cut_off_lam
	    if qual>cut_off[4]:
	        estimator = 5
	    elif qual> cut_off[2] and qual< cut_off[4]:
	        estimator = 4
	    elif qual> cut_off[1] and qual< cut_off[2]:
	        estimator =  3
	    elif qual> cut_off[0] and qual< cut_off[1]:
	        estimator =  2
	    else:
	        estimator = 1

	elif q == "Carlos Cruz-Diez":
	    cut_off = cut_off_cruz
	    if qual>cut_off[4]:
	        estimator = 5 #estimator5()
	    elif qual> cut_off[2] and qual< cut_off[4]:
	        estimator = 4 #estimator4()
	    elif qual> cut_off[1] and qual< cut_off[2]:
	        estimator =  3 #estimator3()
	    elif qual> cut_off[0] and qual< cut_off[1]:
	        estimator =  2 #estimator2()
	    else:
	        estimator = 1


	elif q == "Leonora Carrington":
	    cut_off = cut_off_carrington
	    if qual > cut_off[4]:
	        estimator = 5 #estimator5()
	    elif qual > cut_off[2] and qual< cut_off[4]:
	        estimator = 4 #estimator4()
	    elif qual > cut_off[1] and qual< cut_off[2]:
	        estimator =  3 #estimator3()
	    elif qual > cut_off[0] and qual< cut_off[1]:
	        estimator =  2 #estimator2()
	    else:
	        estimator = 1

	elif q == "Jose Clemente Orozco":
	    cut_off = cut_off_orozco
	    if qual>cut_off[4]:
	        estimator = 5 #estimator5()
	    elif qual> cut_off[2] and qual< cut_off[4]:
	        estimator = 4 #estimator4()
	    elif qual> cut_off[1] and qual< cut_off[2]:
	        estimator =  3 #estimator3()
	    elif qual> cut_off[0] and qual< cut_off[1]:
	        estimator =  2 #estimator2()
	    else:
	        estimator = 1

	elif q == "Pedro Coronel":
	    cut_off = cut_off_coronel
	    if qual>cut_off[4]:
	        estimator = 5 #estimator5()
	    elif qual> cut_off[2] and qual< cut_off[4]:
	        estimator = 4 #estimator4()
	    elif qual> cut_off[1] and qual< cut_off[2]:
	        estimator =  3 #estimator3()
	    elif qual> cut_off[0] and qual< cut_off[1]:
	        estimator =  2 #estimator2()
	    else:
	        estimator = 1

	elif q == "David Alfaro Siqueiros":
	    cut_off = cut_off_siqueiros
	    if qual>cut_off[4]:
	        estimator = 5 #estimator5()
	    elif qual> cut_off[2] and qual< cut_off[4]:
	        estimator = 4 #estimator4()
	    elif qual> cut_off[1] and qual< cut_off[2]:
	        estimator =  3 #estimator3()
	    elif qual> cut_off[0] and qual< cut_off[1]:
	        estimator =  2 #estimator2()
	    else:
	        estimator = 1

	elif q == "Rufino Tamayo":
	    cut_off = cut_off_tamayo
	    if qual>cut_off[4]:
	        estimator = 5 #estimator5()
	    elif qual> cut_off[2] and qual< cut_off[4]:
	        estimator = 4 #estimator4()
	    elif qual> cut_off[1] and qual< cut_off[2]:
	        estimator =  3 #estimator3()
	    elif qual> cut_off[0] and qual< cut_off[1]:
	        estimator =  2 #estimator2()
	    else:
	        estimator = 1

	elif q == "Cundo Bermudez":
	    cut_off = cut_off_bermudez
	    if qual>cut_off[4]:
	        estimator = 5 #estimator5()
	    elif qual> cut_off[2] and qual< cut_off[4]:
	        estimator = 4 #estimator2()
	    elif qual> cut_off[1] and qual< cut_off[2]:
	        estimator =  3 #estimator3()
	    elif qual> cut_off[0] and qual< cut_off[1]:
	        estimator =  2 #estimator2()
	    else:
	        estimator = 1
	else:
		estimator = 0

	return estimator

print quantil_placer("Carlos Cruz-Diez", 30000)
