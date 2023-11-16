print("This is example 1 string print!")
print("This is example 2 \n new line print!") #new line using \n
print("This is example 3 \" quotation print!") #print quotation mark using backslash as an escape character \"
print("This is example 4 \ backslash print!") #print backslash mark as a string

print("\n==================== Examples using string variable ====================")
phrase = "Giraffe Academy" # String variable

print(phrase)
print("01. Hello " + phrase) # Concatenate
print("02. " + phrase.lower())
print("03. " + str(phrase.isupper()))
print("04. " + str(phrase.upper().isupper()))
print("05. " + str(len(phrase)))
print("06. " + phrase[0])
print("07. " + phrase.lower())
print("08. " + str(phrase.index("G")))
print("09. " + str(phrase.index("a")))
print("10. " + str(phrase.index("A")))
print("11. " + str(phrase.index("Academy")))
# print("12. " + str(phrase.index("z"))) # will throw an error
print("13. " + phrase.replace("Academy", "Safari"))
print("13. " + phrase.replace("A", "XYZ"))
print("13. " + phrase.replace("a", "5"))
