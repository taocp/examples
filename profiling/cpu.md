### all threads of a process
  - `top -H -p <pid>`

### all cpus/cores of the system
  - `mpstat -P ALL 1`

### a specific cpu/core
  - `CORENUM=3; ps -Leo pid,tid,psr,pcpu,cmd | awk "{if(\$3==$CORENUM){print \$0}}"`
  - NOTE: due to system scheduler, maybe a thread move from one cpu/core to another
  - [FYI](https://unix.stackexchange.com/a/421302/73846)

### all threads of a process * every-cpu
  - maybe `ps -p <pid> -L -o pid,tid,psr,pcpu` works
  - [FYI](https://stackoverflow.com/a/3910155)

### perf
  - `perf record -p <pid> -g -- sleep 57` and `perf report`
  - [FlameGragh](https://github.com/brendangregg/FlameGraph)
    - perf script > out.perf
    - ./stackcollapse-perf.pl out.perf > out.folded
    - ./flamegraph.pl out.folded > out.svg
