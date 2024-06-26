def obfuscatevar(code, alphabet, sets_num, min_name_length):
    # This is the list that gets used to generate the name of each Set
    Il = ["I", "l"]

    # Here your alphabet gets shuffled
    mixed_alphabet = ''.join(random.sample(alphabet, len(alphabet)))

    alphabets = []
    sets = []
    for x in range(sets_num): # Creating all the Sets
        name = ''.join(random.choices(Il, k=min_name_length)) # Generating an random hard readable name
        while name in sets: # if the name is already used it is now generating a new one
            min_name_length += 1
            name = ''.join(random.choices(Il, k=min_name_length))
        sets.append(name)

    for l in np.array_split(list(mixed_alphabet), sets_num): # Splitting your alphabets in a few parts
        li = []
        for i in l:
            li.append(i)
        alphabets.append(li) # and adding the single parts in one list

    new = "@echo off\n"
    for x in range(len(sets)): # Writing all Set commands
        new = new + "Set " + sets[x] + "=" + ''.join(alphabets[x]) + "\n"
    new = new + "cls\n\n" # hiding them

    for c in code: # Starting to replace every char
        last = False # To don't write the char multiple time cause the multiple alphabets...
        for x in range(len(alphabets)):
            if c in alphabets[x]:
                if last:
                    new = new[:-1] # ... removing the last char if it was already written once
                new = new + "%" + sets[x] + ":~" + str(''.join(alphabets[x]).find(c)) + ",1%"
                break
            else:
                if not last:
                    new = new + c # writing the char that wasn't found in your alphabet
                    last = True

    return new
