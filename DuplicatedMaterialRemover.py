import bpy
import math
import random

names=[]
names1=[]
min=[]
for collections in bpy.data.collections:
    for obj in collections.all_objects:
        for mat in obj.material_slots:
            name=mat.name
            split=name.split(".")
            try:
                n=int(split[-1])
                #print(n)
                try:
                    idx = names.index(split[0])
                    if (not min[idx]==None) and min[idx]>n:
                        names1[idx]=name
                        min[idx]=n
                except ValueError:
                    names.append(split[0])
                    names1.append(name)
                    min.append(n)
            except ValueError:
                print(name)
                try:
                    idx = names.index(split[0])
                    names1[idx]=name
                    min[idx]=None
                except ValueError:
                    names.append(split[0])  
                    names1.append(name)
                    min.append(None)

res=""
for i in range(len(names)):
    res+=names[i]+"," +str(min[i])+"\n";
print(res)

for collections in bpy.data.collections:
    for obj in collections.all_objects:
        for i in range(len(obj.material_slots)):
            name=obj.material_slots[i].name
            split=name.split(".")
            print(bpy.data.materials.get(names1[names.index(split[0])]))
            obj.material_slots[i].material=bpy.data.materials.get(names1[names.index(split[0])])