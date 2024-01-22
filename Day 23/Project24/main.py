#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


names = open(r'C:\Cyber Security\100 days of Python\Day 23\Project24\Input\Names\invited_names.txt')
names2 = open(r'C:\Cyber Security\100 days of Python\Day 23\Project24\Input\Letters\starting_letter.txt')
names_invites = []
names_invites2 = []

with open(r'C:\Cyber Security\100 days of Python\Day 23\Project24\Input\Names\invited_names.txt', 'r') as file:
    for line in file:
        cleaned_line = line.strip()
        if cleaned_line:  # This will be False for empty lines
            names_invites.append(cleaned_line)


with open(r'C:\Cyber Security\100 days of Python\Day 23\Project24\Input\Letters\starting_letter.txt', 'r') as file:
    for line in file:
        cleaned_line = line.strip()
        if cleaned_line:  # This will be False for empty lines
            names_invites2.append(cleaned_line)

x = []

for i in names_invites:
    x.append(names_invites2[0].replace("[name]", i))

for y in range(len(x)):
    names_invites2[0] = x[y]

    string = '\n'.join(names_invites2)
    with open(rf"C:\Cyber Security\100 days of Python\Day 23\Project24\Output\ReadyToSend\{names_invites[y]}.txt", "w") as f:
        text = f.write(string)
        print(text)




