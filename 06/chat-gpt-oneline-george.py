print(next(i for i in range(len(open("in.txt").read())) if len(set(open("in.txt").read()[i:i+4])) == 4) +4)
print(next(i for i in range(len(open("in.txt").read())) if len(set(open("in.txt").read()[i:i+14])) == 14), "")+14)