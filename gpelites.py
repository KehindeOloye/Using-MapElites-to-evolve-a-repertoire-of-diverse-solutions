import random, math
import mutatesave
import glob
import os
import commands
from os import walk
import graphs

B = 20
I = 50
MUT_PROB = 0.2

def random_population():
  pop = []
  indsize = B
  mutatesave.mutationmultilple(indsize,MUT_PROB)
  save_list = glob.glob(os.path.join(os.getcwd(), "tosave"))
  for save_path in save_list:
      pop.append(save_path)
  print (pop)
  f = []
  for (dirpath, dirnames, filenames) in walk("~/tosave"):
      for filename in filenames:
          f.append(os.path.abspath(os.path.join(dirpath, filename)))
  print (f)
  return f

def mutatefornewpop(MUT_PROB, dna):
  return mutatesave.mutationpo(MUT_PROB, dna)

def featdesc(dna):
  arg = dna
  # Here you need two bash script the first one behave.txt that measures the behavioral similarity between each
  #mutant malware and the original malware and sim.txt that measures the structural similarity between each
  #mutant malware and the original malware
  b = commands.getoutput('~/behave.txt %s'  % (str(arg)))
  s = commands.getoutput('~/sim.txt %s' % (str(arg)))
  return b, s


def performance(dna):
    arg = dna
    # Here you need a bash script mal.txt that means the evasiveness of the mutants, a simple way to do this
    # would be to use virus total api which returns the number of its engines that flag a mutant as malicious
    # this number gives an indication of how evasive the mutants are.
    e = commands.getoutput('~/mal.txt %s' % (str(arg)))
    return e

ctrl_map = {}
behv_map = {}
perf_map = {}
all_coos = []


def map_elites(I=50, B=20):
    j=0
    randpop = random_population()
    for i in range(I):
        if i < B:
            c = randpop[j]
            j += 1
        else:
            rand_coo = random.choice(all_coos)
            c_prime = ctrl_map[rand_coo]
            c = mutatefornewpop(MUT_PROB, c_prime)
        behavior = featdesc(c)
        p = performance(c)
        add_mat(c, behavior, p)

RES = 20

def add_mat(ctrl, behavior, perf):
    x, y = behavior
    coo = (int((x) / 1 * RES), int((y) / 1 * RES))
    perf_old = perf_map.get(coo, float('-inf'))
    if perf_old < perf:
        if not coo in ctrl_map:
            all_coos.append(coo)
        ctrl_map[coo] = ctrl
        perf_map[coo] = perf
        behv_map[coo] = behavior

I = 50
B = 20

map_elites(I=I, B=B)
graphs.variance_map(perf_map, RES)

