#Write a program that collects two strings from the user
string_one = input("Enter a noun: ")
string_two = input("Enter a second noun: ")

sentence = "Yesterday I wrote a {}. I sent it to the {}!".format(string_one, string_two)
print(sentence)
