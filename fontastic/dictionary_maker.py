# Returns an 2D dictionary, one for each font
# and an array containing the names of the fonts.
# We use the array of font names to find the index 
def make_dict(fonts_file_name):
    # Open file for reading
    f = None
    try:
        f = open(fonts_file_name, "r")
    except IOError:
        print("ERROR, file not found")
    # Read metadata line from file and split on spaces into a list
    line = f.readline().split()
    # This dictionary will map the name of the font to a dictionary
    # that maps the english letter that that font's letter
    # Its like a 2D dictionary, each key has a value that is a dictionary
    translation_dicts = {}
    # This is to keep track of the order that the fonts
    # show up in on the fonts.txt file
    fonts = []

    # Here we start from 2 because we want to skip the first two
    # columns which are "METADATA" and "ENGLISH"
    # since we don't need a dictionary to translate from
    # english to english
    for i in range(2,len(line)):
        # For each font name, add it as a key to the 
        # translation dictionary. Set its value to 
        # a map of spaces to slashes since this is 
        # how we will replace spaces in all fonts.
        translation_dicts[line[i]] = {" ":"/"}
        # we will add the font name to the fonts array
        fonts.append(line[i])

    for line in f:
        # For each line after the metadata line split it on spaces
        translation = line.split()
        # Get the english letter that the rest of the symbols
        # coorespond with.
        english = line[0]
        for i in range(1, len(translation)):
            # Get the font name based on the current column - 1
            # we do minus 1 because the fonts array starts with
            # morse while the fonts file starts with english
            # so we are 1 ahead.
            font = fonts[i - 1]
            # Find the proper dictionary to add to with the 
            # font name as the key.
            # Then in that dictionary, set the key of the english letter
            # to the value of the translation. i.e. 'A' : .- 
            translation_dicts[font][english] = translation[i]
    
    return translation_dicts

        