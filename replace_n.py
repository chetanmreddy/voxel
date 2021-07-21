filename = 'data/kitti/ImageSets/val_main.txt'
filename2 = 'data/kitti/ImageSets/val.txt'
filedata = []

with open(filename, "r") as infile:
    for line in infile.readlines():
        new_line = line.strip()
        filedata.append(new_line)

with open(filename2, "w") as outfile:
    for l in filedata:
        outfile.write(l)
