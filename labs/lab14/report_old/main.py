file = open('./clipboard.txt', encoding='utf-8')
newf = open('save.txt', 'wt', encoding='utf-8')
count = 0
cl = 0
for line in file:
    cl += 1
    if "{#fig:001 width=90%}" in line:
        count+=1
        new = (line
               .replace("#fig:001 width=90%", "#fig:" + "0"*(3-len(str(count))) + str(count) + " width=90%")
               .replace("(image/1.PNG)", f"(image/{count}.PNG)"))
        print(f"Changed line: {cl}| {line} to {new}")
        newf.write(new)
    else:
        newf.write(line)
input()