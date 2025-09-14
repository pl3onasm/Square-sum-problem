$\huge\color{cadetblue}{\text{Square-sum Problem}}$

<br/>

The problem as explained by Matt Parker:  
  
[![Problem](https://img.youtube.com/vi/G1m7goLCJDY/0.jpg)](https://www.youtube.com/watch?v=G1m7goLCJDY)

<br/>

${\Large\color{rosybrown}\text{Program usage}}$

  
The program makes use of a backtracking algorithm, guided by a heuristic that prioritizes vertices having the least degree (i.e. the least number of edges connecting them to the remaining unvisited ones) in order to avoid potential dead ends. The program is capable of computing Hamiltonian paths for inputs up to 20'000 relatively easily. If no path exists, the output is ```None```.  

<br/>

${\large\color{darkseagreen}\text{Example input}}$

```shell
python3 squaresum.py 23
```

<br/>

${\large\color{darkseagreen}\text{Example output}}$

```shell
[18, 7, 9, 16, 20, 5, 11, 14, 2, 23, 13, 12, 4, 21, 15, 10, 6, 19, 17, 8, 1, 3, 22]
```

<br/>

If this example leaves you with an appetite for more, have a look at the Hamiltonian path for 21'000: [path](https://pastebin.com/tfJsQEDH).  

Please note that for large paths, you may have to increase the stack size in order to avoid a segmentation fault. This can be done in the terminal:  

```shell
ulimit -s unlimited
```
