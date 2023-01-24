from storage import Storage
from Length import Length
from area import Area
from mass import Mass
from volume import Volume

conversion_domain = {1: "Storage",
                     2: "Mass",
                     3: "Length",
                     4: "Area",
                     5: "Volume"}

print(conversion_domain)
domain = int(input("Which conversion domain do you want to use ?:"))
if domain == 1:
    Storage()
elif domain == 2:
    Mass()
elif domain == 3:
    Length()
elif domain == 4:
    Area()
elif domain == 5:
    Volume()
