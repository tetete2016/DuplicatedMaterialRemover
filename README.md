# DuplicatedMaterialRemover
This script removes duplicated materials in Blender

## How to use
Download [DuplicatedMaterialRemover.py](https://github.com/tetete2016/DuplicatedMaterialRemover/blob/master/DuplicatedMaterialRemover.py) 
and load DuplicatedMaterialRemover.py from 
the script window in blender.
Don't forget to make a backup before pressing "Run Script" button.
After running the script, you would see the material slot shown in the picture below.
The "0"s in the material slots mean that the materials are not assigned to any meshs.
The materials that are not assigned to meshs will be removed by reloading the file.

![Dupulicated Materials got removed!!](https://github.com/tetete2016/DuplicatedMaterialRemover/blob/master/image.png)

## limitation
**This script misbeahaves if "." is included in the names of materials.**
Also,this script combines materials if the names are the same:
as we see in the source, the script compare the name of the materials not the materials themselves.
