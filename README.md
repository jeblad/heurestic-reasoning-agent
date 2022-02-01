# pyhera

![stability-experimental](https://img.shields.io/badge/stability-experimental-orange.svg?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues-raw/jeblad/pyhera?style=for-the-badge)

Heuristic Reasoning Agent (PyHERA) with [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) at host and [CUDA](https://en.wikipedia.org/wiki/CUDA) at device, integrated with [PyCUDA](https://documen.tician.de/pycuda/).

There are separate subrepositories for each of the models.

## Usage

The managing software creates and runs an agent continuously. The inputs (sensory data) are injected on the [dendrites](https://en.wikipedia.org/wiki/Dendrite) artificial [synapses](https://en.wikipedia.org/wiki/Synapse), and the outputs (motor data) are extracted from [axons](https://en.wikipedia.org/wiki/Axon).

### Primary commands

It should be enough to clone the repo, then `cd` into the folder, and then build a [software agent](https://en.wikipedia.org/wiki/Software_agent) with

```bash
hera --family abraxas build
```

and run the agent with

```bash
hera --identifier <whatever> up
```

A running agent can then be stopped with

```bash
hera --identifier <whatever> down
```

and then destroyed with

```bash
hera --identifier <whatever> destroy
```

