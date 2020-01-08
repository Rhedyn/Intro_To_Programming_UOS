lyrics = """
I'll be the roundabout
The words will make you out 'n' out
I spend the day your way
Call it morning driving through the sound and
In and out the valley
The music dance and sing
They make the children really ring
I spend the day your way
Call it morning driving through the sound and
In and out the valley
In and around the lake
Mountains come out of the sky and they stand there
One mile over we'll be there and we'll see you
Ten true summers we'll be there and laughing too
Twenty four before my love you'll see
I'll be there with you
I will remember you
Your silhouette will charge the view
Of distance atmosphere
Call it morning driving through the sound and
Even in the valley
In and around the lake
Mountains come out of the sky and they stand there
One mile over we'll be there and we'll see you
Ten true summers we'll be there and laughing too
Twenty four before my love you'll see
I'll be there with you
Along the drifting cloud
The eagle searching down on the land
Catching the swirling wind
The sailor sees the rim of the land
The eagle's dancing wings
Create as weather spins out of hand
Go closer hold the land
Feel partly no more than grains of sand
We stand to lose all time
A thousand answers by in our hand
Next to your deeper fears
We stand surrounded by a million years
I'll be the roundabout
The words will make you out 'n' out
I'll be the roundabout
The words will make you out 'n' out
In and around the lake
Mountains come out of the sky and they stand there
Twenty four before my love and I'll be there
I'll be the roundabout
The words will make you out 'n' out
I spend the day your way
Call it morning driving through the sound and
In and out the valley
In and around the lake
Mountains come out of the sky and they stand there
One mile over we'll be there and we'll see you
Ten true summers we'll be there and laughing too
Twenty four before my love you'll see
I'll be there with you
Da la la la da da la
""".lower()

def create_fd(lyr):
	fd = {} #frequency dictionary
	for i in lyr.translate({ord(i): None for i in '.,!?'}).split(): #iterates through adjusted lyrics
		if i in fd:
			fd[i] += 1
		else:
			fd[i] = 1
	return fd

def find_mf(fd):
	wl = []
	hf = 0
	for i in fd.values():
		if i > hf:
			hf = i
	for i in fd.keys():
		if fd[i] == hf:
			wl.append(i)
	return (wl, hf)


def sort(fl):

	lv = [] #low value
	ev = [] #equal value
	hv = [] #high value

	if len(fl) > 1:
		piv = fl[0][1] #sets pivot to first position
		for i in fl:
			if i[1] < piv:
				lv.append(i)
			elif i[1] == piv:
				ev.append(i)
			elif i[1] > piv:
				hv.append(i)

		return sort(lv) + ev + sort(hv)

	else:
		return fl

def trim(fd, cutoff = 0):
	td = {} #trimmed dictionary
	for i in fd:
		if fd[i] >= cutoff:
			td[i] = fd[i]
	return td



_cutoff = int(input("Only show words above or equal to <amount> of occurences:\n\n> "))

fd = create_fd(lyrics)
print(find_mf(fd)) #prints most frequent

fd = trim(fd, cutoff=_cutoff)
fl = list(zip(fd.keys(), fd.values()))
print(sort(fl)) #prints the list of tuples

input("Program Finished...")
