##Created by SAL on 12/03/2024

def word_search():
    #set the default values for these strings if no user input is entered.
    Default_statement = "This is a test statement to be used and it is just the one."
    Default_My_word = "is"
    #User input for statement and word to find
    statement = input("Enter a statement and we'll count the number of occurrences of a word:") or Default_statement
    My_word = input("Enter a word and we'll count the number of occurrences of in the previous statement:") or Default_My_word
    print("Word to hunt for:", My_word)
    print("Statement entered:", statement)
    #Playing with Python F strings
    print(f'"{My_word}" occurs {statement.count(My_word)} time(s) including within words')

while True:
    word_search()
    #Don't forget to add a break or escape for the loop!
    user_input = input("Do you want to run again? (y/n): ")
    if user_input.lower() != 'y':
        break
