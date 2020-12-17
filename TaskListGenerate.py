import os

def markDown( folderName:str )->str:
    res = ""
    date = folderName.replace('-', '/')
    res = "### " + date[2:] + "\n" + '\n'
    files = openFolder(folderName)
    for name in files:
        res += '[' + name + ']' + '(' + files[name][0] + ')' +'\n\n'
        files[name][1] = str(files[name][1]).replace(' ', '\ ')
        res +=  '\n > ' + '[Source Code]' + '(' + files[name][1] + ')' + '\n\n' 

    res += '\n'
    return res


def openFolder(folderName):
    res = {}
    for file in os.listdir(folderName):
        path = folderName + '/' + file
        #res.append(folderName + '/' + file)
        f = open(path)
        name = f.readline()
        link = f.readline()
        if name[0] != '#':
            name = file
        else:
            name = name.replace('\n', '')[1:]
            tk = name.split(' ')
            name = "".join([tk[i] for i in range(0, len(tk)) if tk[i] != '' ])
        
        if link[0] != '#':
            link = path
        else:
            link = link.replace('\n', '')[1:]
            tk = link.split(' ')
            link = "".join([tk[i] for i in range(0, len(tk)) if tk[i] != '' ])
        
        res[name] = [link, path]

    return res

ct = "# Leet Code Note \n\n"

for x in os.listdir('.'):
    if os.path.isdir('./' + x) and x != '.git':
        ct += markDown('./' + x)
        ct += "\n"

f = open('README.md', 'w')
f.write(ct)
f.close()