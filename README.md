# Braces

Or rather getting rid of them.

OK, here's future/potential .pgo (Pretty Go, Perfect Go, Proper Go, Pythonic Go) features:

## Lexis

* Numbers with underscores: `1_000_000`
* Hexadecimal literals: `#FFFF`
* Integers with radix 2 to 36 and more: `2#1000_0111 8#777 36#xyzzy 1000#11`
* Floats with pi: `2p1`, Inf and NaN: `1I` `-1I` `1N`
* true `1#` false `0#`
* Date/time as `2015.12.31_15:30:45[tz]` tz=(w|e)(H[:MM]|H.H|MMM)  
* `ret` for "return"
* `#` eol-comment
* `#< inline comment >` `#{ also }` `#( too )` `#[ as well ]`
* hex strings `#"1a 2b 34 56 8978 abff"`
* split strings `"abc" 13 10 "def" " " "ghi"`
* multi-line strings with `#|` and other control sequences `
* interpreted strings: `"x=#{x}, y=#{y}, x+y=#{x+y}."`
* masked eol `~` (?)

## Syntax, Semantics, etc

* ...`:` + indent as blocks (also for const,var,import,struct,etc)
* `while` for "for condition"
* `loop` for endless loop
* `for i ...n` = for i:=0; i<n; i++ (or `k...n` for ...:=k...<n...)
* `for i n...` = for i:=n; i>0; i--
* break|continue|return [...] `if` condition
* `import xxx,yyy` -- w/o ""
* `(...)->...` -- function type
* `[...]->...` -- map type: `map[string]->int` ==> `[S]->I`
* `I` `U` `B` `R` `S` `X` `E` for int uint byte rune string interface error
* `if !err` and `if err` (maybe `?`err)
* binops `~⊗` `~|` append `~/` take `~\` drop `~@` select `~:` filter `~*` repeat `~#` reshape
  `~%` replace `~>` expand `~<` shrink `~^` starts `~$` ends `~?` contains `~=` match `~~` approx `~-` remove
* unops (`$` len, `|` abs, `/` floor, `%` frac, `^` upper)
* `$`x -- len(x)
* condition x `?` y `:` z (or x `?` y `!` z)
* x`[$-y]` for indexing relative to the end
* `f args,.... <eol>` don't require ()
* `f g h x` don't require () either
* `1 2 3 4 5` -- new([]int){1,2,3,4,5}
* `!`T -- new(T), T`!`n -- make(T,n)
* n`$`values -- reshape, new array
* macros `#def X xxxx; #def X(Y) xxxYxxx` or other compile-time generation
