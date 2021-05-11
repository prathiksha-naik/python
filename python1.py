flights=100
takeoffs=int(input("enter the number of takeoffs from airport"))
landings=int(input("enter the number of landing from airport"))
current=(flights+landings)-takeoffs
print("number of flight currently in airport",current)
