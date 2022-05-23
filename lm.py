#lm.py

def tri(t) :
	for i in range(len(t)-1) :
		if t[i] + 1 != t[i+1] :
			return False

	return True


liste = [16 for o in range(10)]

print(liste)
print(tri(liste))