### Monoalphabetic Cipher System
### April 2013
### QJ

from Tkinter import * 
from Functions import*

class App:

    def __init__(self, master=None):
##################### --> process <--#############################################
        def process_action():
            check_empty()
            self.btn_process.configure(bg = "green")
            ############### Text Input Encryption ######################
            if sub_button == 1:
                message = (self.txt_input.get(1.0, END)).lower()

               # message = message.replace("\n", " ")
                shift = self.txt_shift_key.get(1.0, END)

                # Call function and pass on
                result = encryption(message,'shift',shift)

                # Delete any existing old text
                self.txt_result.delete(1.0, END)
                # Add new text
                self.txt_result.insert(END,(result))

            ############### Text File Encryption ######################
            elif sub_button == 2:
                message = self.txt_input.get(1.0, END)
                
                shift = self.txt_shift_key.get(1.0, END)

                # Call function and pass on
                result = encryption(message,'shift',shift)

                # Delete any existing old text
                self.txt_result.delete(1.0, END)
                # Add new text
                self.txt_result.insert(END,(result))
                
            ############### Keyword Text Encryption ######################
            elif sub_button == 3:
                message = self.txt_input.get(1.0, END)
                message = message.replace("\n","")
                
                keyword = self.txt_shift_key.get(1.0, END)

                # Call function and pass on
                result = encryption(message,'keyword',keyword)
                result = ''.join(result)

                # Delete any existing old text
                self.txt_result.delete(1.0, END)
                # Add new text
                self.txt_result.insert(END,(result))
                
            ############### Keyword File Encryption ######################
            elif sub_button == 4:
                message = self.txt_input.get(1.0, END)
                message = message.replace("\n","")
                
                keyword = self.txt_shift_key.get(1.0, END)

                # Call function and pass on
                result = encryption(message,'keyword',keyword)
                result = ''.join(result)

                # Delete any existing old text
                self.txt_result.delete(1.0, END)
                # Add new text
                self.txt_result.insert(END,(result))

                
            ############### Text Input Decryption ######################
            elif sub_button == 5:
                message = (self.txt_input.get(1.0, END)).lower()

               # message = message.replace("\n", " ")
                shift = self.txt_shift_key.get(1.0, END)

                # Call function and pass on
                result = decryption(message,'shift',shift)

                # Delete any existing old text
                self.txt_result.delete(1.0, END)
                # Add new text
                self.txt_result.insert(END,(result))

            ############### Text File Decryption ######################
            elif sub_button == 6:
                message = self.txt_input.get(1.0, END)
                
                shift = self.txt_shift_key.get(1.0, END)

                # Call function and pass on
                result = decryption(message,'shift',shift)

                # Delete any existing old text
                self.txt_result.delete(1.0, END)
                # Add new text
                self.txt_result.insert(END,(result))
                
            ############### Keyword Text Decryption ######################
            elif sub_button == 7:
                message = self.txt_input.get(1.0, END)
                message = message.replace("\n","")
                
                keyword = self.txt_shift_key.get(1.0, END)

                # Call function and pass on
                result = decryption(message,'keyword',keyword)
                result = ''.join(result)

                # Delete any existing old text
                self.txt_result.delete(1.0, END)
                # Add new text
                self.txt_result.insert(END,(result))
                
            ############### Keyword File Decryption ######################
            elif sub_button == 8:
                message = self.txt_input.get(1.0, END)
                message = message.replace("\n","")
                
                keyword = self.txt_shift_key.get(1.0, END)

                # Call function and pass on
                result = decryption(message,'keyword',keyword)
                result = ''.join(result)

                # Delete any existing old text
                self.txt_result.delete(1.0, END)
                # Add new text
                self.txt_result.insert(END,(result))

            ############### FILE Frequency Analysis ######################
            elif sub_button == 9:
                message = self.txt_input.get(1.0, END)
                message = message.replace("\n","")

                # Call function to analyse message
                result = frequency_shift('')

                # Delete any existing old text
                self.txt_result.delete(1.0, END)
                # Add new text
                self.txt_result.insert(END,(result))
                
            ############### TEXT Frequency Analysis ######################
            elif sub_button == 10:
                message = self.txt_input.get(1.0, END)
                message = message.replace("\n","")

                if len(message) < 3:
                    notification("The text entered is too short.\n* Please enter more text.","")
                    return
                else:

                    # Call function to analyse message
                    result = frequency_shift(message)

                    # Delete any existing old text
                    self.txt_result.delete(1.0, END)
                    # Add new text
                    self.txt_result.insert(END,(result))
        def dialog_empty_inputs():
            child_win = Toplevel()
            message = "Please make sure you fill in all required fields."
            Label(child_win, text=message, justify=LEFT).pack(pady=7, padx=7)
            Button(child_win, text='  OK  ', command=child_win.destroy).pack(pady=7, padx=7)

        def check_empty():
            if sub_button != 9 and sub_button != 10:
                if len(self.txt_shift_key.get(1.0, END)) == 1:
                    self.txt_shift_key.focus()
                    dialog_empty_inputs()
                    return 
            if len(self.txt_input.get(1.0, END)) == 1:
                self.txt_input.focus()
                dialog_empty_inputs()
                return 

        def clear_inputs(all):
            if all == 1:
                self.txt_shift_key.delete(1.0, END)
                self.txt_input.delete(1.0, END)
                self.txt_result.delete(1.0, END)
            else:
                self.txt_shift_key.delete(1.0, END)
                self.txt_result.delete(1.0, END)

###################################################--> BUTTONS COLOURS <--########################################################
        def encshift1_colour():
            # BUTTON COLOURS
            # --- Active
            self.encshift1.configure(bg = "green")
            # --- Inactive
            self.enckeyword1.configure(bg = "gray")
            self.encshift2.configure(bg = "gray")
            self.enckeyword2.configure(bg = "gray")
            self.btn_process.configure(bg = "gray")
            
        def encshift2_colour():
            # BUTTON COLOURS
            # --- Active
            self.encshift2.configure(bg = "green")
            # --- Inactive
            self.enckeyword1.configure(bg = "gray")
            self.encshift1.configure(bg = "gray")
            self.enckeyword2.configure(bg = "gray")
            self.btn_process.configure(bg = "gray")

        def enckeyword1_colour():
            # BUTTON COLOURS
            # --- Active
            self.enckeyword1.configure(bg = "green")
            # --- Inactive
            self.encshift2.configure(bg = "gray")
            self.encshift1.configure(bg = "gray")
            self.enckeyword2.configure(bg = "gray")
            self.btn_process.configure(bg = "gray")

        def enckeyword2_colour():
            # BUTTON COLOURS
            # --- Active
            self.enckeyword2.configure(bg = "green")
            # --- Inactive
            self.encshift2.configure(bg = "gray")
            self.encshift1.configure(bg = "gray")
            self.enckeyword1.configure(bg = "gray")
            self.btn_process.configure(bg = "gray")
            

        def decshift1_colour():
            # BUTTON COLOURS
            # --- Active
            self.decshift1.configure(bg = "green")
            # --- Inactive
            self.deckeyword1.configure(bg = "gray")
            self.decshift2.configure(bg = "gray")
            self.deckeyword2.configure(bg = "gray")
            self.btn_process.configure(bg = "gray")
            
        def decshift2_colour():
            # BUTTON COLOURS
            # --- Active
            self.decshift2.configure(bg = "green")
            # --- Inactive
            self.deckeyword1.configure(bg = "gray")
            self.decshift1.configure(bg = "gray")
            self.deckeyword2.configure(bg = "gray")
            self.btn_process.configure(bg = "gray")

        def deckeyword1_colour():
            # BUTTON COLOURS
            # --- Active
            self.deckeyword1.configure(bg = "green")
            # --- Inactive
            self.decshift2.configure(bg = "gray")
            self.decshift1.configure(bg = "gray")
            self.deckeyword2.configure(bg = "gray")
            self.btn_process.configure(bg = "gray")

        def deckeyword2_colour():
            # BUTTON COLOURS
            # --- Active
            self.deckeyword2.configure(bg = "green")
            # --- Inactive
            self.decshift2.configure(bg = "gray")
            self.decshift1.configure(bg = "gray")
            self.deckeyword1.configure(bg = "gray")
            self.btn_process.configure(bg = "gray")


###################################################--> ENC BUTTONS <--########################################################
        def encshift1():
            # BUTTON COLOURS
            encshift1_colour()
            # Store what button has been presssed
            global sub_button
            sub_button = 1

            # Delete any text in input box
            clear_inputs(1)
            
####### hide ############
            self.label10.grid_forget()
            self.label7.grid_forget()
####### show ############
            frame8.grid(row=8, column=0, columnspan=6, pady=4)
            self.help3.grid(row=7, column=2)
            self.txt_shift_key.grid(row=7, column=1, padx=10)
            frame5. grid(row=7, column=0, sticky=W)
            self.label9.grid(row=7, column=0, sticky=W)
            self.txt_result.grid(row=10, column=2, padx=8, rowspan=3)
            self.btn_process.grid(row=10, column=1, padx=8)
            frame6. grid(row=9, column=0)
            self.txt_input.grid(row=10, column=0, padx=8, rowspan=3)
            self.label11.grid(row=9, column=2, sticky=W)
            self.label6.grid(row=9, column=0, sticky=W)
            self.label6.config(text = "4. Text Input")
            frame7.grid(row=6, column=0, columnspan=6, pady=4)

        def encshift2():
            # BUTTON COLOURS
            encshift2_colour()
            # Store what button has been presssed
            global sub_button
            sub_button = 2
            
            # Show message on input box
            message = file_handling('read','encrypted','').lower()

            if len(message) < 3:
                notification("The file has no text.\n* Please input some text to the file 'original_file.txt'","")
                return
            
            # Delete any text in input box
            clear_inputs(0)

            # Delete any existing old text
            self.txt_input.delete(1.0, END)
            # Add new text
            self.txt_input.insert(END,(message))

####### hide ############

            self.label7.grid_forget()
            self.label6.grid_forget()
####### show ############
            frame8.grid(row=8, column=0, columnspan=6, pady=4)
            self.help3.grid(row=7, column=2)
            self.txt_shift_key.grid(row=7, column=1, padx=10)
            frame5. grid(row=7, column=0, sticky=W)
            self.label9.grid(row=7, column=0, sticky=W)
            self.txt_result.grid(row=10, column=2, padx=8, rowspan=3)
            self.btn_process.grid(row=10, column=1, padx=8)
            self.label10.grid(row=9, column=0, sticky=W)
            self.label10.config(text = "4. Input from file")
            frame6. grid(row=9, column=0)
            self.txt_input.grid(row=10, column=0, padx=8, rowspan=3)
            self.label11.grid(row=9, column=2, sticky=W)
            frame7.grid(row=6, column=0, columnspan=6, pady=4)

        def enckeyword1():
            # BUTTON COLOURS
            enckeyword1_colour()
            # Store what button has been presssed
            global sub_button
            sub_button = 3

            # Delete any text in input box
            clear_inputs(1)
            
####### hide #############
            self.label10.grid_forget()
            self.label9.grid_forget()
####### show #############
            frame8.grid(row=8, column=0, columnspan=6, pady=4)
            self.help3.grid(row=7, column=2)
            self.txt_shift_key.grid(row=7, column=1, padx=10)
            frame5. grid(row=7, column=0, sticky=W)
            self.label7.grid(row=7, column=0, sticky=W)
            self.txt_result.grid(row=10, column=2, padx=8, rowspan=3)
            self.btn_process.grid(row=10, column=1, padx=8)
            frame6. grid(row=9, column=0)
            self.txt_input.grid(row=10, column=0, padx=8, rowspan=3)
            self.label11.grid(row=9, column=2, sticky=W)
            self.label6.grid(row=9, column=0, sticky=W)
            self.label6.config(text = "4. Text Input")
            frame7.grid(row=6, column=0, columnspan=6, pady=4)

        def enckeyword2():
            # BUTTON COLOURS
            enckeyword2_colour()
            # Store what button has been presssed
            global sub_button
            sub_button = 4
            
            # Show message on input box
            message = file_handling('read','encrypted','').lower()

            if len(message) < 3:
                notification("The file has no text.\n* Please input some text to the file 'original_file.txt'","")
                return
            
            # Delete any text in input box
            clear_inputs(0)

            # Delete any existing old text
            self.txt_input.delete(1.0, END)
            # Add new text
            self.txt_input.insert(END,(message))

####### hide #############
            self.label9.grid_forget()
            self.label6.grid_forget()
####### show #############
            frame8.grid(row=8, column=0, columnspan=6, pady=4)
            self.help3.grid(row=7, column=2)
            self.txt_shift_key.grid(row=7, column=1, padx=10)
            frame5. grid(row=7, column=0, sticky=W)
            self.label7.grid(row=7, column=0, sticky=W)
            self.txt_result.grid(row=10, column=2, padx=8, rowspan=3)
            self.btn_process.grid(row=10, column=1, padx=8)
            self.label10.grid(row=9, column=0, sticky=W)
            self.label10.config(text = "4. Input from File")
            frame6. grid(row=9, column=0)
            self.txt_input.grid(row=10, column=0, padx=8, rowspan=3)
            self.label11.grid(row=9, column=2, sticky=W)
            frame7.grid(row=6, column=0, columnspan=6, pady=4)

            
#######################################################--> DEC BUTTONS <--########################################################

        def decshift1():
            # BUTTON COLOURS
            decshift1_colour()
            # Store what button has been presssed
            global sub_button
            sub_button = 5

            # Delete any text in input box
            clear_inputs(1)
            
####### hide ############
            self.label7.grid_forget()
            self.label10.grid_forget()
####### show ############
            frame8.grid(row=8, column=0, columnspan=6, pady=4)
            self.help3.grid(row=7, column=2)
            self.txt_shift_key.grid(row=7, column=1, padx=10)
            frame5. grid(row=7, column=0, sticky=W)
            self.label9.grid(row=7, column=0, sticky=W)
            self.txt_result.grid(row=10, column=2, padx=8, rowspan=3)
            self.btn_process.grid(row=10, column=1, padx=8)
            frame6. grid(row=9, column=0)
            self.txt_input.grid(row=10, column=0, padx=8, rowspan=3)
            self.label11.grid(row=9, column=2, sticky=W)
            self.label6.grid(row=9, column=0, sticky=W)
            self.label6.config(text = "4. Text Input")
            frame7.grid(row=6, column=0, columnspan=6, pady=4)

        def decshift2():
            # BUTTON COLOURS
            decshift2_colour()
            # Store what button has been presssed
            global sub_button
            sub_button = 6

            # Show message on input box
            message = file_handling('read','decrypted','').lower()

            if len(message) < 3:
                notification("The file has no text.\n* Please input some text to the file 'encrypted_file.txt'","")
                return

            # Delete any text in input box
            clear_inputs(0)

            # Delete any existing old text
            self.txt_input.delete(1.0, END)
            # Add new text
            self.txt_input.insert(END,(message))
            
####### hide ############
            self.label6.grid_forget()
            self.label7.grid_forget()
####### show ############
            frame8.grid(row=8, column=0, columnspan=6, pady=4)
            self.help3.grid(row=7, column=2)
            self.txt_shift_key.grid(row=7, column=1, padx=10)
            frame5. grid(row=7, column=0, sticky=W)
            self.label9.grid(row=7, column=0, sticky=W)
            self.txt_result.grid(row=10, column=2, padx=8, rowspan=3)
            self.btn_process.grid(row=10, column=1, padx=8)
            self.label10.grid(row=9, column=0, sticky=W)
            self.label10.config(text = "4. Input from File")
            frame6. grid(row=9, column=0)
            self.txt_input.grid(row=10, column=0, padx=8, rowspan=3)
            self.label11.grid(row=9, column=2, sticky=W)
            frame7.grid(row=6, column=0, columnspan=6, pady=4)

        def deckeyword1():
            # BUTTON COLOURS
            deckeyword1_colour()
            # Store what button has been presssed
            global sub_button
            sub_button = 7

            # Delete any text in input box
            clear_inputs(1)
            
####### hide #############
            self.label9.grid_forget()
            self.label10.grid_forget()
####### show #############
            frame8.grid(row=8, column=0, columnspan=6, pady=4)
            self.help3.grid(row=7, column=2)
            self.txt_shift_key.grid(row=7, column=1, padx=10)
            frame5. grid(row=7, column=0, sticky=W)
            self.label7.grid(row=7, column=0, sticky=W)
            self.txt_result.grid(row=10, column=2, padx=8,rowspan=3)
            self.btn_process.grid(row=10, column=1, padx=8)
            frame6. grid(row=10, column=0)
            self.txt_input.grid(row=10, column=0, padx=8, rowspan=3)
            self.label11.grid(row=9, column=2, sticky=W)
            self.label6.grid(row=9, column=0, sticky=W)
            self.label6.config(text = "4. Text Input")
            frame7.grid(row=6, column=0, columnspan=6, pady=4)

        def deckeyword2():
            # BUTTON COLOURS
            deckeyword2_colour()
            # Store what button has been presssed
            global sub_button
            sub_button = 8

            # Show message on input box
            message = file_handling('read','decrypted','').lower()

            if len(message) < 3:
                notification("The file has no text.\n* Please input some text to the file 'encrypted_file.txt'","")
                return

            # Delete any text in input box
            clear_inputs(0)

            # Delete any existing old text
            self.txt_input.delete(1.0, END)
            # Add new text
            self.txt_input.insert(END,(message))
            
####### hide #############
            self.label6.grid_forget()     
            self.label9.grid_forget()
####### show #############
            frame8.grid(row=8, column=0, columnspan=6, pady=4)
            self.help3.grid(row=7, column=2)
            self.txt_shift_key.grid(row=7, column=1, padx=10)
            frame5. grid(row=7, column=0, sticky=W)
            self.label7.grid(row=7, column=0, sticky=W)
            self.txt_result.grid(row=10, column=2, padx=8,rowspan=3)
            self.btn_process.grid(row=10, column=1, padx=8)
            self.label10.grid(row=9, column=0, sticky=W)
            self.label10.config(text = "4. Input from File")
            frame6. grid(row=9, column=0)
            self.txt_input.grid(row=10, column=0, padx=8, rowspan=3)
            self.label11.grid(row=9, column=2, sticky=W)
            frame7.grid(row=6, column=0, columnspan=6, pady=4)


#####################################--> Frequency analysis buttons <--###########################################

        def file():
            # Store what button has been presssed
            global sub_button
            sub_button = 9

            # Show message on input box
            message = file_handling('read','decrypted','').lower()

            if len(message) < 3:
                notification("The file has no text.\n* Please input some text to the file 'encrypted_file.txt'","")
                return

            # Delete any text in input box
            clear_inputs(0)

            # Delete any existing old text
            self.txt_input.delete(1.0, END)
            # Add new text
            self.txt_input.insert(END,(message))
            
            #**** show ****#
            self.btn_process.grid(row=10, column=1, padx=8)
            self.label10.grid(row=9, column=0, sticky=W)
            self.label10.config(text = "3. Input from File")
            self.txt_input.grid(row=10, column=0, padx=8, rowspan=3)
            #*****HIDE*****#
            self.label6.grid_forget()
            # BUTTON COLOURS
            # --- Active
            self.file.configure(bg = "green")
            # --- Inactive
            self.text.configure(bg = "gray")

        def text():
            # Store what button has been presssed
            global sub_button
            sub_button = 10

            # Delete any text in input box
            clear_inputs(1)

            
            #**** HIDE ****#
            self.label10.grid_forget()
            #****SHOW****#
            self.label6.grid(row=9, column=0, sticky=W)
            self.label6.config(text = "3. Text Input")
            self.txt_input.grid(row=10, column=0, padx=8, rowspan=3)
            self.btn_process.grid(row=10, column=1, padx=8)
            frame6. grid(row=9, column=0)
            self.txt_input.grid(row=10, column=0, rowspan=3, padx=8)
            # BUTTON COLOURS
            # --- Active
            self.text.configure(bg = "green")
            # --- Inactive
            self.file.configure(bg = "gray")

############################### help buttons ###############################################################

        def help3():
            #****ENTER SHIFT/KEYWORD HELP BUTTON***#
            # create child window
            child_win = Toplevel()
            message = "Shift - Enter the amount of places you would like each character to be shifted along\n\nKeyword - Select a word you will remember to encrypt/decrypt your message."
            Label(child_win, text=message, justify=LEFT).pack(pady=7, padx=7)
            Button(child_win, text='  OK  ', command=child_win.destroy).pack(pady=7, padx=7)

        def help2():
            #***** TEXT/FILE HELP BUTTON******#
            # create child window
            child_win = Toplevel()
            message = "Text - Select if you wish to manually enter the text in the inputbox.\n\nFile - Select if you wish the text from a File to be read"
            Label(child_win, text=message, justify=LEFT).pack(pady=7, padx=7)
            Button(child_win, text='  OK  ', command=child_win.destroy).pack(pady=7, padx=7)
            
############################---> PRIMARY BUTTONS <---########################################################

        def help1():
            #****PRIMARY HELP BUTTON****#
            # create child window
            child_win = Toplevel()
            message = "Encrypt - Select if you wish to encrypt plain text.\n\nDecrypt - Select if you have ciphered text to decrypt to plain text.\n\nFrequency Analysis - Use to crack down encypted message without key."
            Label(child_win, text=message, justify=LEFT).pack(pady=7, padx=7)
            Button(child_win, text='  OK  ', command=child_win.destroy).pack(pady=7, padx=7)
       
        def prim_enc():
            global main_button
            main_button = 1

            #****HIDE***#
            frame7.grid_forget()
            self.deckeyword2.grid_forget()
            self.decshift2.grid_forget()
            self.deckeyword1.grid_forget()
            self.decshift1.grid_forget()
            frame4.grid_forget()
            frame6.grid_forget()
            self.label10.grid_forget()
            self.label11.grid_forget()
            self.btn_process.grid_forget()
            self.txt_input.grid_forget()
            self.txt_result.grid_forget()
            frame5.grid_forget()
            #****SHOW*****#
            frame2.grid(row=3, column=0, rowspan=3, columnspan=5, sticky=W)
            self.label17.grid(row=3, column=0, padx=4, columnspan=3)
            self.label4.grid(row=4, column=0)
            self.label5.grid(row=5, column=0)
            self.encshift1.grid(row=4, column=1)
            self.enckeyword1.grid(row=4, column=2)
            self.encshift2.grid(row=5, column=1)
            self.enckeyword2.grid(row=5, column=2)
            frame3.grid(row=2, column=0, columnspan=6)
            # BUTTON COLOURS
            # --- Active
            self.encrypt.configure(bg = "green")
            # --- Inactive
            self.dencrypt.configure(bg = "gray")
            self.frequency.configure(bg = "gray")
            
        def prim_dec():
            global main_button
            main_button = 2

            #****HIDE***#
            frame7.grid_forget()
            self.label17.grid_forget()
            self.enckeyword1.grid_forget()
            self.encshift1.grid_forget()
            self.encshift2.grid_forget()
            self.enckeyword2.grid_forget()
            frame4.grid_forget()
            frame6.grid_forget()
            self.label10.grid_forget()
            self.label11.grid_forget()
            self.btn_process.grid_forget()
            self.txt_input.grid_forget()
            self.txt_result.grid_forget()
            frame5.grid_forget()
            #****SHOW*****#
            self.label4.grid(row=4, column=0)
            self.label5.grid(row=5, column=0)
            self.label17.grid(row=3, column=0, padx=4, columnspan=3)
            frame2.grid(row=3, column=0, rowspan=3, columnspan=5, sticky=W)
            self.deckeyword2.grid(row=5, column=2)
            self.decshift2.grid(row=5, column=1)
            self.deckeyword1.grid(row=4, column=2)
            self.decshift1.grid(row=4, column=1)
            frame3.grid(row=2, column=0, columnspan=6)
            # BUTTON COLOURS
            # --- Inactive
            self.encrypt.configure(bg = "gray")
            self.frequency.configure(bg = "gray")
            # --- Active
            self.dencrypt.configure(bg = "green")
            
        def prim_FA():
            global main_button
            main_button = 3

            # Delete any text in input box
            clear_inputs(1)
            
            #****HIDE***#
            frame5.grid_forget()
            self.label10.grid_forget()
            frame2.grid_forget()
            frame8.grid_forget()
            #****SHOW*****#
            self.txt_input.grid(row=10, column=0, padx=8, rowspan=3)
            self.btn_process.grid(row=10, column=1, padx=8, sticky=N)
            self.txt_result.grid(row=10, column=2, rowspan=3, padx=8)
            self.label11.grid(row=9, column=2, sticky=W)
            frame6. grid(row=9, column=0)
            frame4.grid(row=3, column=0, sticky=W)
            frame3.grid(row=2, column=0, columnspan=6)
            # BUTTON COLOURS
            # --- Inactive
            self.encrypt.configure(bg = "gray")
            self.dencrypt.configure(bg = "gray")
            # --- Active
            self.frequency.configure(bg = "green")
            
# # #  # # # # # # # #  # # # # # # # # # # # # # # #  ##  # # # # ------->>>>>>>>>>> [1] <<<<<<<<<<<----------- # # # # #  # # # # # # # # # # # # # # # # # #  # # # #  # # #

        frame1 = Frame(master)
        frame1.grid(row=0, column=0, padx=7, pady=7, sticky=W)

        self.label12 = Label(frame1, text="1. Select Encryption/Decryption Method:")
        self.label12.grid(row=0, column=0, columnspan=3, pady=4, sticky=W)

        self.encrypt = Button(frame1, text="Encrypt", command=prim_enc)
        self.encrypt.grid(row=1, column=0, padx=3, pady=4)

        self.dencrypt = Button(frame1, text="Decrypt", command=prim_dec)
        self.dencrypt.grid(row=1, column=1, padx=3, pady=4)

        self.frequency = Button(frame1, text="Freguency Analysis", command=prim_FA)
        self.frequency.grid(row=1, column=2, padx=3, pady=4)

        self.help1 = Button(frame1, text="?", width=3, command=help1)
        self.help1.grid(row=1, column=3, padx=8, pady=4)


# # #  # # # # # # # #  # # # # # # # # # # # # #  ## # # # # # # #  ------->>>>>>>>>>> [2] <<<<<<<<<<<----------- # # # # #  # # # # # # # # # # # # # # # # # # # # #  # # #  # 

        frame2 = Frame(master)
        frame2. grid(row=3, column=0, rowspan=3, columnspan=5, sticky=W)
        frame2.grid_forget()

        self.label17 = Label(frame2, text="2. Select a method of operation")
        self.label17.grid(row=3, column=0, padx=4, columnspan=3)
        self.label17.grid_forget()

        self.label4 = Label(frame2, text="Text")
        self.label4.grid(row=4, column=0)
        self.label4.grid_forget()

        self.label5 = Label(frame2, text="File")
        self.label5.grid(row=5, column=0)
        self.label5.grid_forget()

        self.encshift1 = Button(frame2, text="Shift", width=8, command=encshift1)
        self.encshift1.grid(row=4, column=1)
        self.encshift1.grid_forget()

        self.enckeyword1 = Button(frame2, text="Keyword", width=8, command=enckeyword1)
        self.enckeyword1.grid(row=4, column=2)
        self.enckeyword1.grid_forget()

        self.encshift2 = Button(frame2, text="Shift", width=8, command=encshift2)
        self.encshift2.grid(row=5, column=1)                                                                      
        self.encshift2.grid_forget()

        self.enckeyword2 = Button(frame2, text="Keyword", width=8, command=enckeyword2)
        self.enckeyword2.grid(row=5, column=2)
        self.enckeyword2.grid_forget()

############ D E C BUTTONS ###########

        self.decshift1 = Button(frame2, text="Shift", width=8, command=decshift1)
        self.decshift1.grid(row=4, column=1)
        self.decshift1.grid_forget()

        self.deckeyword1 = Button(frame2, text="Keyword", width=8, command=deckeyword1)
        self.deckeyword1.grid(row=4, column=2)
        self.deckeyword1.grid_forget()

        self.decshift2 = Button(frame2, text="Shift", width=8, command=decshift2)
        self.decshift2.grid(row=5, column=1)
        self.decshift2.grid_forget()

        self.deckeyword2 = Button(frame2, text="Keyword", width=8, command=deckeyword2)
        self.deckeyword2.grid(row=5, column=2)
        self.deckeyword2.grid_forget()

# # #  # # # # # # # #  # # # # # # # # # # #  # # # # # #  # ------->>>>>>>>>>> [4] <<<<<<<<<<<----------- # # # # #  # # # # # # # # # # # # # # # # # # # # #  # ## # # # # # # # # # #

        frame4 = Frame(master)
        frame4.grid(row=3, column=0, sticky=W)
        frame4.grid_forget()

        self.label8 = Label(frame4, text="2. Select a method of operation")
        self.label8.grid(row=3, column=0, columnspan=3)

        self.text = Button(frame4, text="Text", width=7, command=text)
        self.text.grid(row=4, column=0, padx=5)

        self.file = Button(frame4, text="File", width=7, command=file)
        self.file.grid(row=4, column=1)

        self.help2 = Button(frame4, text="?", width=3, command=help2)
        self.help2.grid(row=4, column=2, padx=5)

# # #  # # # # # # # #  # # # # # # # # # # # # # # # # # # #  ------->>>>>>>>>>> [5] <<<<<<<<<<<----------- # # # # #  # # # # # # # # # # # # # # # # # #  # # # ## # # # # # # # # # # # #

        frame5 = Frame(master)
        frame5. grid(row=7, column=0, sticky=W)
        frame5.grid_forget()

        self.label9 = Label(frame5, text="3. Enter number of shifts:")
        self.label9.grid(row=7, column=0, sticky=W)
        self.label9.grid_forget()

        self.label7 = Label(frame5, text="3. Enter a keyword:")                 
        self.label7.grid(row=7, column=0, sticky=W)
        self.label7.grid_forget()

        self.txt_shift_key = Text(frame5, width=30, height=1)
        self.txt_shift_key.grid(row=7, column=1, padx=10)
        self.txt_shift_key.grid_forget()

        self.help3 = Button(frame5, text="?", width=3, command=help3)
        self.help3.grid(row=7, column=2)
        self.help3.grid_forget()

# # #  # # # # # # # #  # # # # # # # # # # # # # # # # # #  ------->>>>>>>>>>> [6] <<<<<<<<<<<----------- # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  # # # # # # # # # # # # # #

        frame6 = Frame(master)
        frame6.grid(row=9, column=0, rowspan=4, padx=10)
        frame6.grid_forget()

        self.label10 = Label(frame6, text="4.Input from file")
        self.label10.grid(row=9, column=0, sticky=W)
        self.label10.grid_forget()

        self.label6 = Label(frame6, text="4.Text input")
        self.label6.grid(row=9, column=0, sticky=W)
        self.label6.grid_forget()

        self.label11 = Label(frame6, text="Result")
        self.label11.grid(row=9, column=2, sticky=W)
        self.label11.grid_forget()

        self.btn_process = Button(frame6, text="Process", command=process_action)
        self.btn_process.grid(row=10, column=1, padx=8, sticky=N)
        self.btn_process.grid_forget()

        self.txt_input = Text(frame6, width=20, height=5)
        self.txt_input.grid(row=10, column=0, rowspan=3, padx=8)
        self.txt_input.grid_forget()
        
        self.txt_result = Text(frame6, width=20, height=5)
        self.txt_result.grid(row=10, column=2, rowspan=3, padx=8)
        self.txt_result.grid_forget()

###########************** canvas 1 *****************###################
        
        frame3 = Frame(master)
        frame3.grid(row=2, column=0, columnspan=6)
        frame3.grid_forget()

        line1 = Canvas(frame3, width=480, height=15)
        line1.grid(row=2, column=0, columnspan=6)
        line1.create_line(0, 0, 450, 0, width=5)

######********************* canvas 2 ************************#######

        frame7 = Frame(master)
        frame7.grid(row=6, column=0, columnspan=6, pady=4)
        frame7.grid_forget()

        line2 = Canvas(frame7, width=480, height=15)
        line2.grid(row=6, column=0, columnspan=6)
        line2.create_line(0, 0, 450, 0, width=5)

######********************* canvas 3 ************************#######

        frame8 = Frame(master)
        frame8.grid(row=8, column=0, columnspan=6, pady=4)
        frame8.grid_forget()

        line3 = Canvas(frame8, width=480, height=15)
        line3.grid(row=8, column=0, columnspan=6)
        line3.create_line(0, 0, 450, 0, width=5)

root = Tk()
app = App(root)
root.title("Monoalphabetic Ciphering System")
root.mainloop()
