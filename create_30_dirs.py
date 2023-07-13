import os

parent_dir = os.path.normpath(r'E:\Python\Projects\Pantech Solutions - Internships\Data Analytics')
print(parent_dir)
for i in range(1, 31):
    path = os.path.join(parent_dir, "Day " + str(i))
    os.mkdir(path)

print(" Day 1 to 30 Directories has benn created under : ", parent_dir)
