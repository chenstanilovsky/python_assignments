import dictionary_maker as dm

def read_directives(directives_file):
    # Here we process the directive like this:
    # Since we always translate from english,
    # we will skip the first column.
    # We build directive arrays in the following format
    # [language_to_translate_to, text_to_translate_file, output_file]
    # We return a 2D array of directive arrays
    directives = []
    f = None
    try:     
        f = open(directives_file, "r")
    except OSError:
        print("ERROR, File not found")
        quit()

    for line in f:
        line = line.split()
        directive = []
        for i in range(1, len(line)):
            directive.append(line[i])
        
        directive[0] = directive[0].upper()
        directives.append(directive)
    return directives

def read_text(text_file_name):
    # this function splits the input text first by line
    # then splits each individual character into its own element
    # in each line array
    text = []
    f = None
    try:
        f = open(text_file_name, "r")
    except OSError:
        print("ERROR, file not found")
        quit()

    for line in f:
        text.append(list(line))
    return text

# for every character in the processed text array, swap it with
# the value that the translation dictionary maps the character to
def translate_text(text, translation_dict)
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j].upper() in translation_dict:
                text[i][j] = translation_dict[text[i][j].upper()]
    return text

# Join each line sepearating each element by spaces
# and write out the text to the file, line by line
def write_text(text, output_file_name):
    f = None
    f = open(output_file_name, "w")
    for line in text:
        f.write(" ".join(line))
        
# For each directive from the process directives file
# read the text file provided
# get the font name so we know which dictionary to use
# translate the text from english to the given font
# and write out the translated text to the file
def execute_directives(directives, translation_dicts):
    for directive in directives:
        text = read_text(directive[1])
        font_name = directive[0]
        translated_text = translate_text(text, translation_dicts[font_name])
        write_text(translated_text, directive[2])

# Generate translation dictionaries for each font
# Process the directive into formatted lists
# Format: [language_to_translate_to, text_to_translate_file, output_file]
# Finally, execute the directives using the translation dictionaries
def main():
    translation_dicts = dm.make_dict("fonts.txt")
    directives = read_directives("directives.txt")
    execute_directives(directives, translation_dicts)
    
  
if __name__=="__main__": 
    main() 