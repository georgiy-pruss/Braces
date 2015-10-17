# Go Enbrace -- make PGO acceptable by weird Go compiler

import sys

def count_indent( s: str ):
  for i,c in enumerate(s):
    if c!=' ':
      return i
  return 0

def enbrace( fn: str ):
  t = [] # (n,type) type = "}" or ")"
  f = open( fn, "rt" )
  if not f: return
  fno = fn.endswith(".pgo") and (fn[:-4]+".go_") or (fn+".out")
  fo = open( fno, "wt" )
  incomment = False
  for ln in f:
    l = ln.rstrip().replace("\t","  ")
    b = l.strip()
    n = count_indent(l)
    if b.startswith("/*"):
      if "*/" not in b:
        incomment = True
        fo.write( l+"\n" )
        continue
    if incomment:
      if "*/" in b:
        incomment = False
      fo.write( l+"\n" )
      continue
    if len(b)==0:
      continue
    if b.startswith("else:") or b.startswith(":("):
      if len(t)>0 and n <= t[-1][0]:
        fo.write( " "*t[-1][0] )
      while len(t)>0 and n <= t[-1][0]:
        fo.write( t[-1][1] )
        if len(t)>1 and n <= t[-2][0]:
          fo.write( "\n" + " "*t[-2][0] )
        else:
          fo.write( " " )
        t.pop()
      if b.startswith(":("):
        fo.write( b[1:]+"\n" )
        continue
    else:
      while len(t)>0 and n <= t[-1][0]:
        fo.write( " "*t[-1][0]+t[-1][1]+"\n" )
        t.pop()
    if l.endswith(":") and not (b.startswith("case ") or b.startswith("default:")):
      if b=="import:" or b=="var:" or b=="const:":
        t.append( (n,")") )
        fo.write( l[:-1]+(l[-2:-1]==" " and "(\n" or " (\n") )
      else:
        t.append( (n,"}") )
        if b.startswith("else:"):
          fo.write( b[:-1]+(l[-2:-1]==" " and "{\n" or " {\n") )
        else:
          fo.write( l[:-1]+(l[-2:-1]==" " and "{\n" or " {\n") )
    else:
      fo.write( l+"\n" )
  while len(t)>0:
    fo.write( " "*t[-1][0]+t[-1][1]+"\n" )
    t.pop()
  f.close()
  fo.close()

if len(sys.argv)==2:
  enbrace( sys.argv[1] )
