# Timed asynchronous systems

One of the things to consider is that in reality clocks exist and a human knows the passing of time. *I.e.* If I browse the net and the page it too slow I try to refresh it or I close it.

In this model we make assumptions on the behavior of processes, communication and HW clocks:

- all services are times. So they can define time-outs
- communication is done through datagrams (non reliable)
- processes are subject to crash or timing failures (**NO** byzantine failures)
- processes can access local clocks that have limited clock drift
- there is no limit to the failure rate of the processes (so they are "normal" and must be anticipated in our model)

*Note:* we assume that the clock drift is bounded by a certain value. So in any moment the drift is within [-p, p] but it doesn't have to be constant, just within the limit
