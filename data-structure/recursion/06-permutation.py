# Code

import copy

def permute(l):
  
  perm = [];

  if len(l) is 0:
    perm.append([])
  else:

    first = l[0];
    rest = l[1:];

    sumPermute = permute(rest);

    for p in sumPermute:
      for j in range(len(p) + 1):
        r = copy.deepcopy(p);
        r.insert(j, first);
        perm.append(r);

  return perm;

  # return perm

print(permute([1,2]))
  