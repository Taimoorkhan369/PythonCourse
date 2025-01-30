indian=["samosa","daal","naan"]
chinese=["egg roll","pot sticker","fried rice"]
italian=["pizza","pasta","risoto"]

dish=input("Enter a dish name")

if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("not in the dish")

