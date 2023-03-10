import requests
number = input("Enter Your Number: ")
amount = int(input ("Enter Your Amount: "))
for i in range (amount):
 r= requests.get("http://deepitsolution.in/api.php?number="+number)
 f= r.content
 print(f)
