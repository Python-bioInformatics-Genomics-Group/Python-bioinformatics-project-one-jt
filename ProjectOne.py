def menu_one():
    #creates a menu to  accept input of a DNA sequence
    #returns DNA sequence (dna_seq)
    menu_one_entry = 0
    print "ProjectOne can accept DNA input in either a FASTA file format or as keyboard input."
    print "Make a selection from the list below..."
    print "1. Input dna sequence directly"
    print "2. Choose a FASTA formatted file with your sequence"
    while (menu_one_entry != 1) or (menu_one_entry !=2):
        menu_one_entry = input("Enter a number (1 or 2):")
        if menu_one_entry == 1:
            dna_seq = get_dna()
            return dna_seq
        if menu_one_entry == 2:
            dna_seq = get_file()
            return dna_seq
            break
        else:
            print "Please try again."

def menu_two(dna_seq):
    #with dna sequence as DNA, ask what function to perform
    print "here in menu 2"
    print "dna sequence = ", dna_seq
    return

def get_file():
    file_name = input("Please type or paste the filename you are using:")
    #get dna seq from FASTA file
    menu_two(dna_seq)
    return
    

def get_dna():
    #accepts DNA input from keyboard
    #returns DNA sequence 
    dna_seq = raw_input("Please type or paste your DNA sequence here:")
    return dna_seq

def check_dna():
    #checks DNA sequence. Ensure all bases are uppercase and A,T,G,C or N.
    #replace any non-acceptable bases as N
    #report and return clean_sequence
    clean_sequence = []
    return clean_sequence

def find_forward_ORFs():
    pass

def translate_ORFs():
    pass



#main
DNA = menu_one()
menu_two(DNA)