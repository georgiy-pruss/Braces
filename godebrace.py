# Go Debrace -- making Go the way it should have been

import sys,re

def debrace( fn: str ):
  f = open( fn, "rt" )
  if not f: return
  fno = fn.endswith(".go") and (fn[:-3]+".pgo") or (fn+".out")
  fo = open( fno, "wt" )
  cases = []
  inds = 0
  for ln in f:
    l = ln.rstrip().replace("\t","  ")
    m = re.search( "{ *//.*$", l )
    if m:
      l = l[:m.start()+1]
    b = l.lstrip()
    if l.endswith("{") or l.endswith("("):
      if b.startswith("} else"):
        l = l.replace("} else","else")
      if l[-2:-1]==" ":
        fo.write( inds*"  "+l[:-2]+":\n" )
      else:
        fo.write( inds*"  "+l[:-1]+":\n" )
    elif b=="}" or b==")":
      if len(cases)>0 and len(l) - len(b) == cases[-1]:
        cases.pop()
        inds -= 1
    elif b.startswith("}("):
      fo.write( inds*"  "+l.replace("}(",":(")+"\n" )
    elif b.startswith("case ") or b.startswith("default:"):
      n = len(l) - len(b)
      if len(cases)==0 or n != cases[-1]:
        cases.append(n)
        inds += 1
      fo.write( inds*"  "+l+"\n" )
    else:
      fo.write( inds*"  "+l+"\n" )
  f.close()
  fo.close()

if len(sys.argv)==2:
  debrace( sys.argv[1] )
