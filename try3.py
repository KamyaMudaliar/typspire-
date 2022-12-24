import random
quotes= []
a= open("random_quotes.txt")
data= a.read()
quotes=data.split(".")
print(quotes)
quote=random.sample(quotes,1)
print(quote)
#b= [elem.strip('][').split(" ") for elem in quote]
#print(b)
b= []
for elem in quote:
    b.extend(elem.strip('][').split(" "))
print(b)
b.append(" .")
print(b)