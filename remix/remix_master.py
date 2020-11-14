import music as ms

def print_song(curr_song):
    print("DJ!! Turn it up!!\n")
    # Prints song out line by line
    for line in curr_song:
        print(line)

def get_user_option():
    # Formatted string with line breaks ( \n ) and tabs ( \t )
    print("\nThe Juke:\n\tL: Load a different song\n\tT: Title of current song\n\tS: Substitute a word")
    print("\tP: Playback your song\n\tR: Reverse it\n\tX: Reset to original song\n\tQ: Quit")

    # Make input uppercase so that lowercase and uppercase letter input gets accepted
    option = input("Your option: ").upper()

    # If input is not valid, ask user to reenter
    while not is_valid_option(option):
        print("Invalid option entered. Please try again.")
        option = input("Your option: ").upper()

    return option

def is_valid_option(option):
    # List of valid inputs
    valid_options = ['L', 'T', 'S', 'P', 'R', 'X', 'Q']

    # If the input is contained in the list above, it is valid
    if option in valid_options:
        return True

    return False

def load_song(song):
    # Print out a numbered list of songs
    for i in range(len(ms.PLAYLIST)):
        print("\t" + str(i+1) + ". " + ms.PLAYLIST[i])

    # First prints out a prompt with the range (1 - ) is based on the length of the playlist
    # Then converts the input to an integer for use later on
    song_num = int(input("Your option: (1 - " + str(len(ms.PLAYLIST)) + ")\n> "))

    # Input validation
    while song_num < 1 or song_num > len(ms.PLAYLIST):
        print("Invalid option. Please try again.")
        song_num = int(input("Your option: (1 - " + str(len(ms.PLAYLIST)) + ")\n> "))

    # Since song numbers are 1 through some number, but arrays start counting at 0
    # we must subtract 1 when indexing
    return ms.SONGS[song_num - 1].copy()
    
def print_title(song):
    # Find song in the ms.SONGS array and get its index
    # Then prints the name of the songs by indexing the 
    # ms.PLAYLIST array
    print(ms.PLAYLIST[ms.SONGS.index(song)])
    return song

def substitute(song):
    print("What word would you like to substitute?")
    target = input("> ")

    print("What would you like to substitute it with?")
    sub = input("> ")

    # Keep track if the word was found or not
    found = False

    # Split the string on spaces into a list
    for i in range(len(song)):
        words = song[i].split()

        

        # For every word in the string, it it matches 
        # the target word replace it
        for j in range(len(words)):
            if words[j] == target:
                words[j] = sub
                found = True

        # replace original line with line that has substitutions        
        song[i] = " ".join(words)

    # If the word could not be found
    if(found == False):
        print("\nThe word you are trying to replace could not be found")

    return song

def reverse_print(song):
    # Start at the last line and iterate down to the first
    for i in range(len(song) - 1, -1, -1):

        # Split lines on spaces
        words = song[i].split()
        reverse = []
        
        # Loop through words backwards to fill array
        for j in range(len(words) - 1, -1, -1):
            reverse.append(words[j])
        # turn reversed list a string to put back into the song
        song[i] = " ".join(reverse)


def run_option(option, song, num):
    # Determined which option was selected
    # Input validation has been done beforehand
    if option == 'L':
        return load_song(song)
    if option == 'T':
        return print_title(song)
    if option == 'S':
        return substitute(song)
    if option == 'P':
        print_song(song)
        return song
    if option == 'R':
        reverse_print(song)
        return song
    if option == 'X':
        return ms.SONGS[num].copy()
    if option == 'Q':
        print("Thanks for using The Juke!")
        exit()
      

# replacing indiviual words replaces all occurances not just one
def start(curr_song, song_num):
    print("Welcome to the Juke")
    print("Here you can bump, remix, and create\n")
    print_song(curr_song)
    curr_num = song_num
    while True:
        option = get_user_option()
        curr_song = run_option(option, curr_song, curr_num)
        if curr_song in ms.SONGS:
            curr_num = ms.SONGS.index(curr_song)

        
    


    

def main():
    song = ms.SONGS[0].copy()
    start(song, 0)
    



if __name__ == "__main__":
    main()