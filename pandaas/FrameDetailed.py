# manipulations: append, retrieve, slice, delete
from distutils.command.install_data import install_data

import pandas as pan

ldict=[{"brand":"Toshiba","price":32900},
       {"brand":"Dell","price":29800},
       {"brand":"Acer","price":23400}]
frame=pan.DataFrame(ldict,index=["item1","item2","item3"])
print(frame)

dseries={"Before Appraisal":pan.Series([7.8,12.4,3.4,1.8],index=["Annamalai","Meguraj","Vinod","Richard"]),
         "After Appraisal":pan.Series([7.9,9.8,3.6,2.1],index=["Annamalai","Meguraj","Vinod","Richard"])}
frame=pan.DataFrame(dseries)
print(frame)

# adding new column in dseries of frame
frame["Notice"]=pan.Series(["Thanks","Bye",3.9,2.3],index=["Annamalai","Meguraj","Vinod","Richard"])
print(frame)

# adding new row
temp=pan.DataFrame([[4.9,5.1,5.3]],columns=["Before Appraisal","After Appraisal","Notice"],index=["Mohamed"])
frame=frame.append(temp)
print("After new row\n",frame)

# difference between before and after appraisal
frame["margin"]=dseries["After Appraisal"]-dseries["Before Appraisal"]
print(frame)

# retrieve column
print(frame["Notice"])

#retrieve row
print(frame.loc["Annamalai"])

#slicing
print(frame["Annamalai":"Vinod"])

# deleting column
frame.pop("Notice")
print(frame)

# deleting row
frame=frame.drop("Vinod")
print(frame)