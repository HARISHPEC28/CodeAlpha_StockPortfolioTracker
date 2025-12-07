import csv
total=0
itrable=[["stock_name","quantity","amount","TOTAl"]]
file=open("purchace.csv","a")
fwriter=csv.writer(file)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 140,
    "MSFT": 320,
    "META": 290,
    "NFLX": 420,
    "NVDA": 480,
    "AMD": 110,
    "INTC": 38,
    "IBM": 160,
    "ORCL": 120,
    "UBER": 62,
    "SONY": 88
    
}

print("\t\t!!!Stock Portfolio tracker!!!")


#printing stocks avliable

print("STOCKS AVALIABLE AER")
count=0
for i in stock_prices:
    count+=1
    print(count," . ",i," : ",stock_prices[i] )


print("!!!!!!!!!enter the stock name followed by quantity to buy!!!!!!!!!!!")

#loop to buy multiple stocks at a time

choice="Y"
while(choice=="Y"):
    
    
    stock=input("enter the stock name:")
    stock=stock.upper()
    if stock in stock_prices:
        quantity=eval(input(f"enter the quanity to buy {stock} stock :"))
        if type(quantity)==int:
            l=[stock,quantity,stock_prices[stock]*quantity]
            itrable.append(l)
            total+=(stock_prices[stock]*quantity)
        else:
            print("!!!!!!!enter the quanity in whole number!!!!!!")
    
    else:
        print(f"!!!!!!!no such stock named {stock} is avaliable!!!!!!!!!")

    choice=input("!!!!DO YOU WANTED TO BUY MORE STOCKS(Y/N) :")
    choice=choice.upper()
    
else:
   
    itrable.append(["","","",total])
    fwriter.writerows(itrable)
   
    print("\nyour transation saved in a file\n")
    print("!!!!!!!!!THANK YOU!!!!!!!!!")
    
file.close()

    



