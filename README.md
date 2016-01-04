# Braces

Or rather getting rid of them.

OK, here's .pgo features:

* Numbers with underscores: 1_000_000
* Hexadecimal literals: #FF
* Intergers with radix 2 to 36: 2#1000_0111 8#777 36#xyzzy
* Floats with pi: 2p1
* Date/time as 2015.12.31_15:30:45
* # comment
* #< inline comment > #{ also } #( too ) #[ as well ]
* macros #def X xxxx; #def X(Y) xxxYxxx
* _ret_ for return
* _while_ for for condition
* _loop_ for endless loop
* for i ...n = for i:=0; i<n; i++
* ....: + indent as blocks
* (...)->... -- function type
* [...]->... -- map type: map[string]->int ==> [S]->I
* I U B R S X for int uint byte rune string interface
* $x -- len(x)
* x[$-y]
* f args,.... 'NL' don't require ()
* f g h x don't require () either
