import requests 
 
initial_currency = input("enter initial currency: ").upper()
target_currency = input("enter target currency: ").upper()
 
while(True): 
    try: 
        amount = float(input("enter the amount : ")) 
        if amount<=0: 
            raise ValueError 
        break
    except ValueError: 
        print ("Amount must be a number greater than zero!") 
        break
 
url = (f"https://api.apilayer.com/fixer/convert?to={target_currency}"
f"&from={initial_currency}&amount={amount}")
 
payload = {} 
headers= { 
  "apikey": "dNQ4HPsfvjFhTTCkN8A0C8MJr4TmmnH8" 
} 
 
response = requests.request("GET", url, headers=headers, data = payload) 
if response.status_code != 200: 
    print("api error") 
    quit() 
 
status_code = response.status_code 
result = response.json() 
print(f"{amount} {initial_currency} : {result['result']} {target_currency}")