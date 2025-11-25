import os

folder = "/home/algorithm/Pictures/GIMP_Result"

for name in os.listdir(folder):
    if name.startswith("GIMP_"):
        new_name = name.replace("GIMP_", "", 1)
        os.rename(
            os.path.join(folder, name),
            os.path.join(folder, new_name)
        )
