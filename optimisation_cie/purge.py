
with open("sorties/localhost.txt", "r") as f:
    lines = f.readlines()
    newee = []
    for i in range(len(lines)) :
        lines[i] = lines[i].split(" ")
        print(lines[i])
        la = lines[i][3][:-1]
        lon = lines[i][2]
        lines[i][2] = lon
        lines[i][3] = la
        newee.append(" ".join(lines[i]))



newee = "\n".join(newee)

with open("dddd", "w") as f:
    f.writelines(newee)