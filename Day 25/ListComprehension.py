
name = "Wello"
new_list = [ letter for letter in name]
final_list = [ hello*2 for hello in range(1,5)]




sentence = input()
# 🚨 Don't change code above 👆
# Write your code below 👇

sentance_List = list(sentence.split(" "))

result = {list:len(list) for list in sentance_List}


print(result)
