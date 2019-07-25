def permutations(string):
  perm = [];

  if len(string) is 0:
    perm.append('');
  else:
    first = string[0];
    rest = string[1:];

    subpermute = permutations(rest);
    
    for  p in subpermute:
      for j in range(len(p) + 1):
        str = p[:j] + first + p[j:]
        perm.append(str);


  return perm;


print(permutations('ab'));