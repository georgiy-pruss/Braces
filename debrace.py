# Pythonize C/C++/C# code -- move all '{' and '}' out of site, beyond the right border

import sys

def debrace( rp: int, fn: str ):
  f = open( fn, "rt" )
  if f:
    fo = open( fn+".out", "wt" )
    out = ""
    sfx = ""
    for ln in f:
      ln = ln.rstrip()
      sln = ln.lstrip()
      if sln == "{":
        sfx += "{"
      elif sln == "}":
        sfx += "}"
      elif sln == "};":
        sfx += "};"
      else:
        while ln.strip().startswith("}"):
          p = ln.index("}")
          sfx += "}"
          ln = ln[:p]+ln[p+1:].strip()
        if out.lstrip().startswith("#"):
          print( out, file=fo )
          if sfx: print( ' '*(rp)+sfx, file=fo )
          sfx = ""
          out = ln
          continue
        if out.endswith("\\"):
          out = out[:-1].rstrip()
          if len(out)<rp:
            out += ' '*(rp-len(out))
          out += sfx + "\\"
        else:
          if len(out)<rp:
            out += ' '*(rp-len(out))
          out += sfx
        print( out, file=fo )
        sfx = ""
        while ln.endswith("}"):
          sfx += "}"
          ln = ln[:-1].rstrip()
        while ln.endswith("{"):
          sfx += "{"
          ln = ln[:-1].rstrip()
        out = ln
    if out or sfx:
      print( out+sfx, file=fo )
    f.close()
    fo.close()

if len(sys.argv)==3:
  debrace( int(sys.argv[1]), sys.argv[2] )
else:
  print("Syntax: debrace.py BRCPOS FILENAME")
  print("  e.g.: debrace.py 92 program.c")
  print("The resulting file ends with '.out'")
