print("Enter as much writing as wanted(please don't use capslock)")
users_inp = input()

character_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ", ",", ".","?","!"] #if i had more time i could add more characters to my list
lengthOfCharacters = len(character_list)

listOfExistingCharacter = [] #creates empty list
for index in range(lengthOfCharacters):
    if character_list[index] in users_inp: #if a character in character_list exists in users_inp
        listOfExistingCharacter.append(character_list[index])#add that character to listOfExistingCharacter
#print("these are the characters in your input" + str(listOfExistingCharacter))


length2 = len(listOfExistingCharacter)
numbList = []    #creates an empty list to store the number of times each element was used

for x in range(length2):      #go through each element in listOfExistingCharacter and print the amount of times they appear
    numbList.append(users_inp.count(listOfExistingCharacter[x])) #counts the number of times each character appears and adds to numbList

lengthOfNumb = len(numbList)
for location1 in range(lengthOfNumb):   #For every element in numbList
    for location2 in range(lengthOfNumb):   #compare location1 element to the other elements
        if numbList[location1] > numbList[location2]:   #if the integer is smaller then the others
            temp = numbList[location2]
            numbList[location2] = numbList[location1]
            numbList[location1] = temp  #^^ code swaps position of the two integers in numbList

            temp2 = listOfExistingCharacter[location2]
            listOfExistingCharacter[location2] = listOfExistingCharacter[location1]
            listOfExistingCharacter[location1] = temp2  #code^^ swaps positions of the letters in the listOfExistingCharacter
                                                        #this is because the two lists(int and character) corellate
for t in range(length2):
    print("The frequency of character " + str(listOfExistingCharacter[t]) + " is " + str(numbList[t]))#prints each character with its frequency in descending order


