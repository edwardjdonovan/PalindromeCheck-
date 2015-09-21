import string

def invert_text(text_tobe_inverted):
        inverted_text = text_tobe_inverted[::-1]        
        return inverted_text

def remove_punctuations(text_tobe_stripped):
        removed_punct = text_tobe_stripped.translate(string.maketrans("",""), string.punctuation)
        return removed_punct

def check_Palindrome(Palindrome_file):
        with open(Palindrome_file) as Pfile:
            content = Pfile.readlines()
        num_line = int(content.pop(0))
        i = 0
        while i < num_line:
                content[i] = content[i].strip('\n')
                i = i + 1
        Ptext = ''.join(content[0:num_line])
        Ptext = Ptext.lower()
        Ptext = Ptext.replace(" ","")
        Ptext_nopunct = remove_punctuations(Ptext)
        Ptext_inv = invert_text(Ptext_nopunct)
        if Ptext_inv == Ptext_nopunct:
                return True
        else:
                return False
        
def main():
        file_name =raw_input("Enter the name of the file to be check if it is a Palindrome:")
        if check_Palindrome(file_name):
                print ("This is a Palindrome")
        else:
                print ("This is not a Palindrome")

main()
