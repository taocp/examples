1. `top` for threads
  - `top -H -p <pid>`
1. `top` for all-cpus
  - `mpstat -P ALL 1`
1. `top` for (every-thread * every-cpu)
  - maybe `ps -p <pid> -L -o pid,tid,psr,pcpu`  works in some cases. [FYI](https://stackoverflow.com/a/3910155)
