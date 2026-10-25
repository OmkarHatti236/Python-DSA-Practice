def location(lat,long):
    dms1=lat.split(";")
    d1,m1,s1=dms1
    

    dms2=long.split(";")
    d2,m2,s2=dms2
    return int(d1)+(int(m1)/60)+(float(s1)/3600),int(d2)+(int(m2)/60)+(float(s2)/3600)


latitude=input("Enter latitude:")
longitude=input("Enter Longitude:")
lat,long=location(latitude,longitude)
print(lat,long)

