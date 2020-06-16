from shutil import copyfileobj
import os
import random
from re import search
def garbagecodeinsert(mut_prob,ftemp,myfile):
    open('out.smali', 'w').close()  # clear file before processing
    LINE_TO_INSERT = '     const-string v0, " "\n'
    PATTERN_OF_LINE = '.locals 1'
    theLINE_TO_INSERT = '    .line 0\n '
    thePATTERN_OF_LINE = '.locals 2'
    for line in ftemp:
        myfile.write(line)
        no_times = random.choice(range(1, 10, 2))
        i=0
        while (i < no_times):
            if random.uniform(0, 1) < mut_prob:
                match = search(PATTERN_OF_LINE, line)
                if match:
                    myfile.write(LINE_TO_INSERT)
            elif random.uniform(0, 1) > mut_prob:
                match = search(thePATTERN_OF_LINE, line)
                if match:
                    myfile.write(theLINE_TO_INSERT)
            i = i + 1
    myfile.close()
    ftemp.close()
    return None

def instructionreordering(ftemp,myfile):
    open('out.smali', 'w').close()  # clear file before processing
    for line in ftemp:
        myfile.write(line)
        no_times = random.choice(range(1, 10, 2))
        p=0
        thePATTERN_OF_LINE = '.locals 8'
        for x in range(0, no_times):
            theLINE_TO_INSERT = '    goto :goto_{}'.format(p) + '\n  \n    :cond_{}'.format(
                    p) + '\n    const-string v0, " "\n    :goto_{}'.format(p) + '\n '
            match = search(thePATTERN_OF_LINE, line)
            if match:
                myfile.write(theLINE_TO_INSERT)
            p += 1
    myfile.close()
    ftemp.close()
    return None

def variablerename(mut_prob,ftemp,myfile):
    open('out.smali', 'w').close()  # clear file before processing
    LINE_TO_INSERT = '     const-string v0, "check"\n'
    PATTERN_OF_LINE = '.locals 0'
    thePATTERN_OF_LINE = '.locals 4'
    for line in ftemp:
        myfile.write(line)
        i = 0
        no_times = random.choice(range(1, 10, 2))
        while (i < no_times):
            if random.uniform(0, 1) < mut_prob:
                match = search(PATTERN_OF_LINE, line)
                if match:
                    myfile.write(LINE_TO_INSERT)
            elif random.uniform(0, 1) > mut_prob:
                match = search(thePATTERN_OF_LINE, line)
                if match:
                    myfile.write(LINE_TO_INSERT)
            i = i + 1
    myfile.close()
    ftemp.close()
    return None

def mutationmultilple(size, mut_prob):
    ops = ['garbagecodeinsert', 'instructionreordering', 'variablerename']
    j = 0
    while j < size:
        themain = open('~/HomeActivity.smali', 'r')
        open('save'+ str(j), 'w+').close()  # clear file before processing
        with open('save'+ str(j), 'wb+') as f:
            copyfileobj(themain, f)
        copyfileobj(themain, f)
        ftemp = open('save'+ str(j), 'r+')
        try:
            ftemp = open('save'+ str(j), 'r+')
            open(os.path.join('~/tosave', 'save'+ str(j)), "wb").close()
        except:
            print('cannot writeall in file:', 'save'+ str(j))
            ftemp.close()
            return None
        myfile = open(os.path.join('~/tosave', 'save'+ str(j)), "wb")
        q = random.uniform(0, 1)
        print q
        if q <> mut_prob:
            op = random.choice(ops)
            print op
            if op == 'garbagecodeinsert':
                garbagecodeinsert(mut_prob,ftemp,myfile)
            elif op == 'instructionreordering':
                instructionreordering(ftemp,myfile)
            elif op == 'variablerename':
                variablerename(mut_prob,ftemp,myfile)
            else:
                print("undefined operator: ", ops)

        j = j+1
    return None

def mutationsingle(mut_prob, file):
    ops = ['garbagecodeinsert', 'instructionreordering', 'variablerename']
    i = 0
    themain = open(file, 'r')
    while os.path.exists("~/save%s" % i):
        i += 1

    open("~/save%s" % i, 'w+').close()  # clear file before processing
    with open("~/save%s" % i, 'wb+') as f:
        copyfileobj(themain, f)
    copyfileobj(themain, f)
    ftemp = open("~/save%s" % i, 'r+')
    try:
        ftemp = open("save%s" % i, 'r+')
        open(os.path.join('/~/tosave', "save%s" % i), "wb").close()
    except:
        print('cannot writeall in file:', "save%s" % i)
        ftemp.close()
        return None
    myfile = open(os.path.join('~/tosave', "save%s" % i), "wb")
    q = random.uniform(0, 1)
    print q
    if q <> mut_prob:
        op = random.choice(ops)
        print op
        if op == 'garbagecodeinsert':
            garbagecodeinsert(mut_prob, ftemp, myfile)
        elif op == 'instructionreordering':
            instructionreordering(ftemp, myfile)
        elif op == 'variablerename':
            variablerename(mut_prob, ftemp, myfile)
        else:
            print("undefined operator: ", ops)
    return "~/keep%s" % i

def mutationpo(mut_prob,file):
    ops = ['garbagecodeinsert', 'instructionreordering', 'variablerename']
    i = 0
    themain = open(file, 'r')
    while os.path.exists("~/save%s" % i):
        i += 1
    open("save%s" % i, 'w+').close()  # clear file before processing
    with open("save%s" % i, 'wb+') as f:
        copyfileobj(themain, f)
    copyfileobj(themain, f)
    ftemp = open("save%s" % i, 'r+')
    try:
        ftemp = open("save%s" % i, 'r+')
        open(os.path.join('~/tosave', "save%s" % i), "wb").close()
    except:
        print('cannot writeall in file:', "save%s" % i)
        ftemp.close()
        return None
    myfile = open(os.path.join('~/tosave', "save%s" % i), "wb")
    q = random.uniform(0, 1)
    print q
    if q <> mut_prob:
        op = random.choice(ops)
        print op
        if op == 'garbagecodeinsert':
            garbagecodeinsert(mut_prob, ftemp, myfile)
        elif op == 'instructionreordering':
            instructionreordering(ftemp, myfile)
        elif op == 'variablerename':
            variablerename(mut_prob, ftemp, myfile)
        else:
            print("undefined operator: ", ops)
    return "~/save%s" % i

def mutationpop(mut_prob,file):
    ops = ['garbagecodeinsert', 'instructionreordering', 'variablerename']
    i = 0
    themain = open(file, 'r')
    while os.path.exists("~/keep%s" % i):
        i += 1

    open("~/keep%s" % i, 'w+').close()  # clear file before processing
    with open("~/keep%s" % i, 'wb+') as f:
        copyfileobj(themain, f)
    copyfileobj(themain, f)
    ftemp = open("~/keep%s" % i, 'r+')
    try:
        ftemp = open("~/keep%s" % i, 'r+')
        open(os.path.join('~/tokeep', "keep%s" % i), "wb").close()
    except:
        print('cannot writeall in file:', "keep%s" % i)
        ftemp.close()
        return None
    myfile = open(os.path.join('~/tokeep', "keep%s" % i), "wb")
    q = random.uniform(0, 1)
    print q
    if q <> mut_prob:
        op = random.choice(ops)
        print op
        if op == 'garbagecodeinsert':
            garbagecodeinsert(mut_prob, ftemp, myfile)
        elif op == 'instructionreordering':
            instructionreordering(ftemp, myfile)
        elif op == 'variablerename':
            variablerename(mut_prob, ftemp, myfile)
        else:
            print("undefined operator: ", ops)
    return "~/keep%s" % i

def mutationmultilplepop(mut_prob, thefile, size):
    ops = ['garbagecodeinsert', 'instructionreordering', 'variablerename']
    j = 0
    while j < size:
        themain = open(thefile, 'r')
        open('keep' + str(j), 'w+').close()
        with open('keep'+ str(j), 'wb+') as f:
            copyfileobj(themain, f)
        copyfileobj(themain, f)
        ftemp = open('keep'+ str(j), 'r+')
        try:
            ftemp = open('keep'+ str(j), 'r+')
            open(os.path.join('~/tokeep', 'keep'+ str(j)), "wb").close()
        except:
            print('cannot writeall in file:', 'keep'+ str(j))
            ftemp.close()
            return None
        myfile = open(os.path.join('~/tokeep', 'keep'+ str(j)), "wb")
        q = random.uniform(0, 1)
        print q
        if q <> mut_prob:
            op = random.choice(ops)
            print op
            if op == 'garbagecodeinsert':
                garbagecodeinsert(mut_prob,ftemp,myfile)
            elif op == 'instructionreordering':
                instructionreordering(ftemp,myfile)
            elif op == 'variablerename':
                variablerename(mut_prob,ftemp,myfile)
            else:
                print("undefined operator: ", ops)

        j = j+1

    f = []
    for folder, subs, files in os.walk('~/tokeep'):
        for filename in files:
           f.append(os.path.abspath(os.path.join(folder, filename)))

    return f





