### Monoalphabetic Cipher System
### April 2013
### QJ

############################## IMPORTED MODULES ##############################
# Used: Frequency shift analysis. "collections.defaultdict(int)" - Crawls through entire text counting occurrence of each letter
import collections
# Used: Frequency shift/keyword analysis. Count the most common words found from the dictionary and sort by occurrance
from collections import Counter
# Used: Frequency keyword analysis. Gives every possible combination for a number
import itertools

############################## ENCRYPTION ##############################
def encryption(message,choice,shift_key):
    if choice == "shift":
        # -------------------- SHIFT -------------------- #

        secret_message = ''
        shifted_alphabet = []

        # If frequency analysis is randomly trying different shifts, pass them through trying each one until a valid word is found
        if shift_key != '':
            shift = int(shift_key)
        else:
            # Ask user for desired shift
            shift = error_typing('shift',0,1)
        
        # Store new alphabet with each letter from normal alphabet shifted individually
        for i in range(0,26):
            shifted_alphabet.append(alphabet[(i+shift)%26])

        for i in message:
            if alphabet.count(i):
                secret_message += shifted_alphabet[alphabet.index(i)]
            else:
                secret_message += i

        # Save encrypted message to local file
        file_handling("write","encrypted",secret_message)
        
        return secret_message
    
    else:
        # -------------------- KEYWORD -------------------- #

        # Convert keyword to lowercase
        keyword = shift_key.lower()
        
        # Remove spaces in keyword
        keyword = "".join(keyword.split())
        # Remove duplicate letters in keyword
        keyword = ''.join(sorted(set(keyword), key=keyword.index))

        # Make sure keyword > 2 (For frequency analysis reasons)
        # Also it checks if user enters repeated characters such as "aaaaaaa" which slims down to "a", therfore length = 1
        while (len(keyword) < 3):
            keyword = input("\nPlease enter a keyword containing more than 2 different characters: ").lower()
            keyword = "".join(keyword.split())
            keyword = ''.join(sorted(set(keyword), key=keyword.index))
            
        # Sort keyword alphabetically
        keyword_sorted = sorted(list(keyword))

        # Determines if an extra row needs to be added to compensate for uneven table creation
        # Check message length entered divided by keyword length
        remainder = (len(message))%(len(keyword_sorted))

        rows = 0

        if remainder == 0:
            # If the word will fit in perfectly in table with no under/overflow
            rows = round((len(message) / (len(keyword_sorted))))
        else:
            # If the word will NOT fit in table, we need to added extra row
            rows = (round((len(message) / (len(keyword_sorted)))))
            if remainder == 1 or remainder == 2:
                rows = rows + 1
            # Calculate the amount of boxes we're gona require for a given message + keyword
            boxes = (rows * (len(keyword_sorted)))
            remaining_char = boxes - (len(message))
            # In remaining empty boxes in table created, fill in with 'space'
            message = message + (" " * remaining_char)

        # Construct even table framework
        keyword_table = [ [ 0 for i in range(len(keyword_sorted)) ] for j in range(rows) ]

        # Put message in rows and columns
        for i in range(round(rows)):
            for j in range(len(keyword_sorted)):
                keyword_table[i][j]= message[i*len(keyword_sorted) + j]

        encrypted_keyword =[]
        keyword_order = []
        keyword_copy = keyword
        counter = 0

        # Finding Keyword characters order of encryption
        while len(keyword_copy) > 0:
            minimum = keyword_copy[0]
            minimum_index = 0
            for i in range(len(keyword_copy)):
                if (ord(keyword_copy[i]) < ord(minimum)):
                    minimum = keyword_copy[i]
                    minimum_index = i
                    
            keyword_order.append(keyword.find(minimum))
            keyword_copy = keyword_copy[:minimum_index] + keyword_copy[minimum_index+1:]

        # Read each letter from keyword in alphabetic order, and extract the column below it one at a time.
        # When done, encrypted message is obtained
        for i in range(len(keyword_order)):
            for b in range(len(keyword_table)):
                encrypted_keyword.append(keyword_table[b][keyword_order[counter]])
                
                if b == len(keyword_table) - 1:
                    if counter == keyword_order:
                        counter = 0
                    else:
                        counter = counter + 1

        file_handling("write","encrypted",''.join(encrypted_keyword))
       
        return encrypted_keyword

############################## DECRYPTION ##############################
def decryption(message, choice, shift):
    if choice == "shift":

        # -------------------- SHIFT -------------------- #
        decrypt_message = ''
        shifted_alphabet = []

        if shift != '':
            shift = int(shift)
        else:
            shift = error_typing('shift',0,1)
            
        for i in range(0,26):
            shifted_alphabet.append(alphabet[(i+shift)%26])
            
        for i in message:
            if alphabet.count(i):
                decrypt_message += alphabet[shifted_alphabet.index(i)]
            else:
                decrypt_message += i
                
        file_handling("write","decrypted",decrypt_message)

        return decrypt_message
        
    else:
        # -------------------- KEYWORD -------------------- #
        if shift == "":
            ask_Keyword = input("Enter Keyword: ")
        else:
            ask_Keyword = shift
            
        ask_Keyword = "".join(ask_Keyword.split())
        ask_Keyword = ''.join(sorted(set(ask_Keyword), key=ask_Keyword.index))
        Keyword = list(ask_Keyword)
        rows = len(message) // len(Keyword)
        message_table = [[message[j*rows + i] for i in range(rows)] for j in range(len(Keyword))]                           
        message_table = list(map(lambda x: ["".join(x)], message_table))
        message_length = len(message_table[0][0])*len(message_table)
        keyword_alphabetic = sorted(Keyword)

        table =[]
        decrypt_message = []

        counter = 0
        increment = 0
        for i in range(len(message_table)):
            p = keyword_alphabetic.index(Keyword[i])
            table += message_table[p]
            
        for i in range(message_length):
            decrypt_message += (table[increment][counter])
            increment += 1

            if increment == len(Keyword):
                increment = 0
                counter += 1
                
        file_handling("write","decrypted",''.join(decrypt_message))

        return decrypt_message   

############################## SHIFT FREQUENCY ANALYSIS ##############################
# -- Performs analysis on an encrypted text.
# -- If this function has no success it will automatically jump to the Keyword analysis.
def frequency_shift(message_gui):
    
    # List of top used letters arranged in popularity in the English language.
    eng_letters = ['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']

    # Look through encrypted message and count occurance of each letter. e.g. ('s', 4)
    freq_chars = collections.defaultdict(int)
    
    # If text has been entered to be analysed, read passed variable, else read from file
    if message_gui == '':
        analys_file = open('encrypted_file.txt')
    else:
        analys_file = message_gui

    for line in analys_file:
        line = line.rstrip('\n')
        for c in line:
            freq_chars[c] += 1

    # Show most occuring letters first        
    sort_keys = list(sorted(freq_chars, key=freq_chars.__getitem__, reverse=True))
    
    first_letter = sort_keys[1]
    find = alphabet.index(first_letter)

    # [0] being 'e' being -4 position in alphabet because letter e is most popular
    find_shift = find - alphabet.index(eng_letters[0])

    if message_gui == '':
        # Get encrypted message from text file
        message_decrypt = file_handling("read","decrypt","")
    else:
        message_decrypt = message_gui
    
    # Call decryption function with calculated found shift from above
    decrypt_message = decryption(message_decrypt, "shift", find_shift)

    total_words_match = 0
    found_shift = 0
    
    # Start working from each combination, until the word is found
    for index in range(26):
        # Call decryption function for evry single possible shift 0 to 26
        decrypt_message2 = decryption(message_decrypt, "shift", index)
        decrypt_message2 = ''.join(decrypt_message2)

        for q in range(len(popular_words)):
            for word in popular_words:
                # If message contains popular english words
                if (decrypt_message2.__contains__(word)):
                        total_words_match += 1
                        found_message = decrypt_message2
                        found_shift = index
                        break

    if total_words_match != 0 and (found_shift == find_shift):
        notification("Frequency Analysis Successful:\n",decrypt_message)
        print("Type of Encryption used: Shift\nShift found: ", found_shift,"\n\n")
        return decrypt_message
    
    elif found_shift != 0:
        # This else if will mosty give us option 1 as being correct, but just in case a popular word has not been found at all. Safety net.
        
        get_decision = 0
        
        if found_message != decrypt_message:        
            print("\n2 possibilites:")
            print("\n##### Option - [1] #####\n")
            # Truncate long message and store to list
            print(found_message[:60] + (found_message[60:] and '...'))

            print("\n\n##### Option - [2] #####\n")
            # Truncate long message and store to list
            print(decrypt_message[:60] + (decrypt_message[60:] and '...'))
            print("\n")

            print("##### Option - [3] #####\n")
            print("Neither of them.")
            print("\n\n")

            print("Which one reads correct?")
            get_decision = error_typing('decision',4,1)
        else:
            get_decision = 1
            
        if get_decision == 1:
            print("\n#################################")
            print("The shift used: ", found_shift)
            print("#################################\n")
            notification("The full message analysed:\n",found_message)
            # Save decrypted message
            file_handling("write","decrypted",found_message)
            return
        elif get_decision == 2:
            print("\n#################################")
            print("The shift used: ", find_shift)
            print("#################################\n")
            notification("The full message analysed:\n",found_message)
            # Save decrypted message
            file_handling("write","decrypted",decrypt_message)
            return
        else:
            print("\nWell that shouldn't have happened.\nThe encrypted message could be in a different language.\nKeyword analysis will now be performed just in case...")
            result = frequency_keyword()
            return result
    else:
        print("\n#################################")
        print("\nNo match found.\nThis message was probably not encrypted with shift encryption.")
        print("\nAttempt 2 - Keyword frequency Analysis will now be performed...")
        
        # Go into keyword analysis
        result = frequency_keyword()
        return result

############################## KEYWORD FREQUENCY ANALYSIS ##############################
# -- After Shift analysis has been performed and no success, usually it means the message has probably been encrypted with keyword. 
def frequency_keyword():
    
    # Read encrypted message from file
    analys_file = open('encrypted_file.txt')
    message = analys_file.read()
    analys_file.close()

    if (len(message)) < 70:
        return "* Message is too short to analyise *"
    
    # Get all factors and convert set to list
    get_factors = list(factors(len(message)))

    common_occurances = 0
    key_at_common = 0
    counter = 0

    # Store factors only with length 3 or greater
    possible_factors = []

    for l in range(len(get_factors)):
        # Check factor size
        if (get_factors[l]) >= 3 and (get_factors[l]) <= 9:
            possible_factors.append(get_factors[l])

    full_length_factor=[0]

    # if number = 3, this will get the leading numbers, 0,1,2,3
    # So it creates from one number a same 'word' length '0123' key

    for p in range(len(possible_factors)):
        for z in range(possible_factors[p]-1):
                full_length_factor.append(z + 1)
        # Convert int list, to a single string each
        key_possible = ''.join(str(v) for v in full_length_factor)
         
        total_keys_possible = 0
        
        # All possible combinations of keyword rearranged
        possibilities = []

        # A big list of messages shortned, if multiple keys are found.
        analysed_messages_short = []

        # All the possible keys
        # This would be better in  a dictionary with analysed_messages_short
        analysed_keys = []

        # Cycle through all the different possible combinations of a given number
        for combination in itertools.permutations(key_possible):
                possibilities.append(''.join(combination))   

        # Start working from each combination, until the word is found
        for index in range(len(possibilities)):
            # Call decryption function for evry single possible combination
            decrypt_message = decryption(message, "keyword", possibilities[index])
            decrypt_message = ''.join(decrypt_message)


            for word in popular_words:
                # If message contains popular english words
                if (decrypt_message.__contains__(word)):
                        coomon_occurances = Counter(decrypt_message.split()).most_common()
                        check_common_occurances = coomon_occurances[0][1]
                        
                        print "*",
                        
                        if check_common_occurances > common_occurances:
                            common_occurances = check_common_occurances
                            key_at_common = possibilities[index]
                        break

            # To prevent hundreds of options/results showing up
            counter += 1
            if counter == 200:
                break

            for word in popular_words:
                # If message contains popular english words
                if (decrypt_message.__contains__(word)):
                        total_keys_possible += 1
                        print(" ",)
 
                        # Truncate long message and store to list
                        analysed_messages_short.append(decrypt_message[:60] + (decrypt_message[60:] and '...'))
                        analysed_keys.append(possibilities[index])
                        break

        if common_occurances < 6:
            if total_keys_possible > 1:
                print("\n\nPossible keys found: ",total_keys_possible)
                print("Listed below are the analysed messages, SHORTNED.\nPlease choose the number which seems most readable:\n")

                for big_list in range(len(analysed_messages_short)):
                    print("[",big_list,"] -", analysed_messages_short[big_list])
                    
                print("\nWhich one reads correct the most?")
                get_decision = error_typing('decision',total_keys_possible,0)

                print("\nThe key found: ", analysed_keys[get_decision])
                message = decryption(message, "keyword", analysed_keys[get_decision])
                notification("The full message analysed:\n",''.join(message))
                break
            elif total_keys_possible == 1:
                print("\nSolution found!")
                print("\nThe key: ", analysed_keys[0])
                message = decryption(message, "keyword", analysed_keys[0])
                notification("The full message analysed:\n",''.join(message))
                break
        else:
            print("\n\n###### Most likley key: ",key_at_common)
            print("\nMatches: ",common_occurances)
            message = decryption(message, "keyword", key_at_common)
            notification("The full message analysed:\n",''.join(message))
            break

        # If end of all combinations is reached, with no found solution
        full_length_factor=[0]
    return ''.join(message)

############################## GET FACTORS ##############################
# -- Get all possible factors of message length
def factors(n):    
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        # Quotient and remainder of the division divmod(x, y) returns ((x-x%y)/y, x%y)
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result

############################## FILE HANDLER ##############################
# -- Manages local files, which contain plain/encrypted/decrypted messages
def file_handling(operation,command,message):
    if operation == "read":
        if command == "encrypted":
            original_file = open("original_file.txt","r")
            message_original = original_file.read()
            original_file.close()
            return message_original
        else:
            encrypted_file = open("encrypted_file.txt","r")
            message_decrypt = encrypted_file.read()
            encrypted_file.close()
            return message_decrypt
    elif operation == "write":
        if command == "encrypted":    
            encrypted_file = open("encrypted_file.txt", "w")
            encrypted_file.write(message)
            encrypted_file.close()
        else:
            decrypted_file = open("decrypted_file.txt","w")
            decrypted_file.write(message)
            decrypted_file.close()
    else:
        # Create 3 empty files locally. If files already exist, then don't overwrite.
        try:
           with open('original_file.txt') as a: pass
        except IOError as b:
            empty_file = open("original_file.txt","w")
            empty_file.close()
        try:
           with open('encrypted_file.txt') as c: pass
        except IOError as d:
            empty_file = open("encrypted_file.txt","w")
            empty_file.close()
        try:
           with open('decrypted_file.txt') as e: pass
        except IOError as f:
            empty_file = open("decrypted_file.txt","w")
            empty_file.close()

############################## NOTIFICATIONS #################################
# -- Displays successful completed operations
def notification(n_text, n_variable):
    print("\n********************************")
    print("*",n_text, (n_variable))
    print("********************************\n\n")

############################## INPUT VALIDATION ##############################
# -- Displays successful completed operations
def error_typing(error_type,condition,start_range):
    # Infinite loop, until valid input is given
    while True:
        try:
          if error_type != 'shift':
              decision = int(input("Enter number: "))
              # Get range of options allowed to pick
              while decision not in range(start_range, condition):
                  print("\n---------------------------------")
                  decision = int(input("Invalid action!\nValid range is "+str(start_range)+"-"+str(condition-1)+".\nTry Again: "))
              return decision
          else:
              shift = int(input("How many shifts?: "))
              return shift
        except ValueError:
          if error_type == 'shift':
              print("\n---------------------------------")
              print("Invalid! Please enter a number.")  
          pass
 
# Start -----------------------------------------------------------------------------------------------------------------------

# English alphabet used for shift encryption/decryption
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# Dictionary of most common words
popular_words = [' the ',' and ',' are ',' two ',' who ',' his ',' her ',' for ',' them ',' now ',' few ',' has ', ' have ']

# Create 3 files in the root for saving messages
file_handling("create","","")

# -----------------------------------------------------------------------------------------------------------------------------
