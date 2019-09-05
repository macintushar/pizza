import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


cart=[]
order=[]
sure=" "

name=input("Enter your Name:")
name=str(name)
address=input("Enter your Address:")
address=str(address)
city=input("Enter your City:")
city=str(city)
pincode=input("Enter your Pincode:")
pincode=str(pincode)

print("Vegetarian: Veg Extravaganza- 1, Farm House- 2, Deluxe Veggie- 3")
print("Non Vegetarian: Non Veg Supreme- 4, Chicken Fiesta- 5")
print("Sides: Garlic Bread- 6, Veg Pasta Italiano White- 7, Non Veg Pasta Italiano White- 8")
print("Desserts: Butterscotch Mousse Cake- 9, Lava Cake- 10")
print("Beverages:Pepsi- 11, Pepsi Black Can- 12, 7UP- 13, Lipton Ice Tea- 14")
print()
print("Enter 'stop' in the cart to stop adding ")
                                    
while True:
    add=input("Enter the Code of the Dishes you want to add to your Cart: ")
    cart.append(add)
    if add=='stop':
      sure=input("Are you sure? y/n")
    if sure=="Y" or sure=="y" or sure=="yes" or sure=="Yes":
        break
    else:
         continue

    

print("The items in your cart are:")      
length=len(cart)
length=length-1
for i in range(0,length):

    if cart[i]=="1":
        a="Veg Extravaganza"
        order.append(a)

    if cart[i]=="2":
        b="Farm House"
        print(b)
        order.append(b)

    if cart[i]=="3":
        c="Deluxe Veggie"
        print(c)
        order.append(c)

    if cart[i]=="4":
        d="Non Veg Supreme"
        print(d)
        order.append(d)

    if cart[i]=="5":
        e="Chicken Fiesta"
        print(e)
        order.append(e)

    if cart[i]=="6":
        f="Garlic Bread"
        print(f)
        order.append(f)

    if cart[i]=="7":
        g="Veg Pasta Italiano White"
        print(g)
        order.append(g)

    if cart[i]=="8":
        h="Non Veg Pasta Italiano White"
        print(h)
        order.append(h)

    if cart[i]=="9":
        i="Butterscotch Mousse Cake"
        print(i)
        order.append(i)

    if cart[i]=="10":
        j="Lava Cake"
        print(j)
        order.append(j)

    if cart[i]=="11":
        k="Pepsi"
        print(k)
        order.append(k)

    if cart[i]=="12":
        l="Pepsi Black Can"
        print(l)
        order.append(l)

    if cart[i]=="13":
        m="7 UP"
        print(m)
        order.append(m)

    if cart[i]=="14":
        n="Lipton Ice Tea"
        print(n)
        order.append(n)
        


mailToAdress = "swamy_latha@yahoo.com"
mailFromServer = "smtp.gmail.com:587"   
mailFromAdress = "emailbycode@gmail.com"
mailFromPassword = "EmailCode123"

body =(name, address, city, pincode, order)
subject = "HELLO!"

msg = MIMEMultipart()
msg['From'] = mailFromAdress
msg['To'] = mailToAdress
msg['Subject'] = subject

msg.attach(MIMEText(body,'plain'))
message = msg.as_string()

try:
    server = smtplib.SMTP(mailFromServer)
    server.starttls()
    server.login(mailFromAdress, mailFromPassword)

    server.sendmail(mailFromAdress, mailToAdress, message)
    server.quit()
    print("SUCCESS - Email sent")

except Exception as e:
    print("FAILURE - Email not sent")
    print(e)





            
            
    
