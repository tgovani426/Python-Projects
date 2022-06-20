from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
next_bid=True
while next_bid:
    name=input("Enter the name\n")
    bid=input("Enter you bid\n")
    auction={}
    auction[name]=bid
    
    
    more_bidder=input("IS there any other bidder??? ")
    if more_bidder=="yes":
        
        next_bid=True
        clear()
    else:
        clear()
        max_bidder=max(auction,key=auction.get)
        print(f"The Higest bidder is {max_bidder}!!!")
        next_bid=False

        ####### THIS CODE WILL RUN ONLY ON REPLIT############ 