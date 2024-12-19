month=['jan','feb','mar','apr','may','jun','july','aug','sep','oct','nov','dec']
yea="202"
print([f"{i}-{month[mon]}-{yea+str(mon)}"  for mon in range(1,len(month)) for i in range(1,31)])




