

try:
    from googlesearch import search
except ImportError:
    print("Module Not Found")

query = input("Enter your Query \n")

for i in search(query, tld='com',num=10,stop=10,pause=2):
    print(i)