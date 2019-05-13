import sys
import random
import pickle

row2 = [0,0,0,0,0,0,0,0,0]
moved = []
with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
  while True:
    try:
      moved.extend(pickle.load(openfile))
    except EOFError:
      break
b = int(input("Input Dataset Size To Generate: "))
a = 0
while(a<=b):
    n = 0
    for f in row2:
        if f != 0:
          n += 1
    if n >= 8:
        pout = open('/content/gdrive/My Drive/TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue
        
    sys.stdout.write("\rGenereting Dataset... %i Of %i Game Completed" % (a,b))
    sys.stdout.flush()
    rand = random.randrange(0,9)
    while(row2[rand] == -1 or row2[rand] == 1):
        rand = random.randrange(0,9)
    row1 = row2 + [rand]
    moved.extend([row1])
    row1 = []
    row2[rand] = -1
    
    if row2[2] == 1 and row2[4] == 1 and row2[6] == 1:
        pout = open('/content/gdrive/My Drive/TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue  
    if row2[0] == 1 and row2[1] == 1 and row2[2] == 1:
        pout = open('/content/gdrive/My Drive/TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue
    if row2[3] == 1 and row2[4] == 1 and row2[5] == 1:
        pout = open('/content/gdrive/My Drive/TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue
    if row2[6] == 1 and row2[7] == 1 and row2[8] == 1:
        pout = open('/content/gdrive/My Drive/TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue
    if row2[0] == 1 and row2[3] == 1 and row2[6] == 1:
        pout = open('/content/gdrive/My Drive/TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue
    if row2[1] == 1 and row2[4] == 1 and row2[7] == 1:
        pout = open('/content/gdrive/My Drive/TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue
    if row2[2] == 1 and row2[5] == 1 and row2[8] == 1:
        pout = open('/content/gdrive/My Drive/TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue
    if row2[0] == 1 and row2[4] == 1 and row2[8] == 1:
        pout = open('/content/gdrive/My Drive/TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue

    rand1 = random.randrange(0,9)
    while(row2[rand1] == -1 or row2[rand1] == 1):
        rand1 = random.randrange(0,9)
    row3 = row2 + [rand1]
    moved.extend([row3])
    row3 = []
    row2[rand1] = 1

    if row2[0] == -1 and row2[1] == -1 and row2[2] == -1:
        pout = open('/content/gdrive/My Drive/TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue 
    if row2[3] == -1 and row2[4] == -1 and row2[5] == -1:
        pout = open('/content/gdrive/My Drive/TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue 
    if row2[6] == -1 and row2[7] == -1 and row2[8] == -1:
        pout = open('/content/gdrive/My Drive/TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue 
    if row2[0] == -1 and row2[3] == -1 and row2[6] == -1:
        pout = open('/content/gdrive/My Drive/TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue 
    if row2[1] == -1 and row2[4] == -1 and row2[7] == -1:
        pout = open('/content/gdrive/My Drive/TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue 
    if row2[2] == -1 and row2[5] == -1 and row2[8] == -1:
        pout = open('/content/gdrive/My Drive/TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue 
    if row2[0] == -1 and row2[4] == -1 and row2[8] == -1:
        pout = open('/content/gdrive/My Drive/TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue 
    if row2[2] == -1 and row2[4] == -1 and row2[6] == -1:
        pout = open('/content/gdrive/My Drive/TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue   

    if row2[0] == -1 and row2[1] == -1 and row2[2] == -1:
        pout = open('TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue 
    if row2[3] == -1 and row2[4] == -1 and row2[5] == -1:
        pout = open('TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue 
    if row2[6] == -1 and row2[7] == -1 and row2[8] == -1:
        pout = open('TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue 
    if row2[0] == -1 and row2[3] == -1 and row2[6] == -1:
        pout = open('TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue 
    if row2[1] == -1 and row2[4] == -1 and row2[7] == -1:
        pout = open('TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue 
    if row2[2] == -1 and row2[5] == -1 and row2[8] == -1:
        pout = open('TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue 
    if row2[0] == -1 and row2[4] == -1 and row2[8] == -1:
        pout = open('TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue 
    if row2[2] == -1 and row2[4] == -1 and row2[6] == -1:
        pout = open('TTOdataset.pickle', 'wb')#Open/Create A New Pickle File
        pickle.dump(moved, pout)#Dump The DataFrame Into The Pickle File
        pout.close()
        row2 = [0,0,0,0,0,0,0,0,0]
        moved = []
        with (open("/content/gdrive/My Drive/TTOdataset.pickle", "rb")) as openfile:
          while True:
            try:
              moved.extend(pickle.load(openfile))
            except EOFError:
              break
        a += 1
        continue   
