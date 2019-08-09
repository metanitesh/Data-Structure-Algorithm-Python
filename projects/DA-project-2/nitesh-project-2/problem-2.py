import os;

def find_files_recursive(suffix, path, output):
  files = os.listdir(path);

  for file in files:
    filePath = os.path.join(path, file);  
    
    if os.path.isfile(filePath):
      filename, file_extension = os.path.splitext(filePath)

      if file_extension == suffix:
        output.append(filePath)
    
    if os.path.isdir(filePath):
      find_files_recursive(suffix, filePath, output)

def find_files(suffix, path):
  isDir = os.path.isdir(path);
  if(not isDir):
    return 'This path doesn\'t exist!';

  output = []
  find_files_recursive(suffix, path, output);
  return output
  
  
# Test-1
output = find_files('.c', './testdir')
print(output)
['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']

#Test-2
output = find_files('.txt', './testdir')
print(output)
# ['']

#Test-3
output = find_files('', './testdir')
print(output)
# ['./testdir/subdir4/.gitkeep', './testdir/subdir2/.gitkeep']

output = find_files('', './wrong-path')
print(output)
# This path doesn't exist!