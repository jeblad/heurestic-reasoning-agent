# pyhera

Heurestic Reasoning Agent (PyHERA) with [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) at host and [CUDA](https://en.wikipedia.org/wiki/CUDA) at device, integrated with [PyCUDA](https://documen.tician.de/pycuda/).

## Usage

This is set up as an agent that runs continuously. The inputs (sensory data) are injected on the dendrities, and the outputs (motor data) are extracted from axons.

It should be enough to clone the repo, then cd into the folder, and then run an `agent` with

```bash
python3 load.py -family:abraxas agent
```

If the agents resource requirements can't be satified it will dump an error report. Usually because the device is somehow constrained. To check if the device has sufficient resources, use the `-simulate` argument. The agent will then do all the calculations, but not load code and data into the device.

An agent is given a name, and upon normal termination it will write out the complete state to a named file. The file can then be used for a later invocation.

The agent can be run in interactive mode, or daemonized. In both cases the agent will keep on running contineously on the device, unless it is run in single step mode. When run in daemonized mode stdin, stdout, and stderr will be redirected to specified devices.

## Signals

A few signals can be sent to the agent:

  * …
