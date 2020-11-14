import Data as dt

def decode(rle):
    decoded = []
    # Since each character in the encoded list is paired up with its number of occurances
    # we loop through the array, skipping over 1 element. That way we only visit each character.
    # upon visitng the character we create a loop using the number of repetitions at index + 1 

    # The inner loop is used to fill the array with the repetitions
    for i in range(0, len(rle), 2):
        for j in range(0, rle[i + 1]):
            decoded.append(rle[i])
    
    return decoded

def printList(lst):
    output = ""

    # Building a string by concatenating 
    # every element in the list together
    for elem in lst:
        output += elem

    print(output)

def main():
    # Uncomment these blocks of code individually
    # then run for a surprise
    # comment the block after you are done

    decoded_0 = decode(dt.DATA0)
    printList(decoded_0)
    
    #decoded_1 = decode(dt.DATA1)
    #printList(decoded_1)

    #decoded_2 = decode(dt.DATA2)
    #printList(decoded_2)

    #decoded_3 = decode(dt.DATA3)
    #printList(decoded_3)

    #decoded_4 = decode(dt.DATA4)
    #printList(decoded_4)

    #decoded_5 = decode(dt.DATA5)
    #printList(decoded_5)


if __name__ == "__main__":
    main()
