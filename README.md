# pyhera

![stability-experimental](https://img.shields.io/badge/stability-experimental-orange.svg?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues-raw/jeblad/pyhera?style=for-the-badge)

Heuristic Reasoning Agent (PyHERA) with [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) at host, and [CUDA](https://en.wikipedia.org/wiki/CUDA) at device integrated with [PyCUDA](https://documen.tician.de/pycuda/), or [OpenCL](https://en.wikipedia.org/wiki/OpenCL) at device integrated with [PyOpenCL](https://documen.tician.de/pyopencl/).

There are separate subrepositories for each of the models.

## Requirements

- python 3.7+
- poetry
- cliff

Poetry has a minimum requirement of 3.7 for python.
Models will typically have a requirement of either `pycuda` or `pyopencl`.

## Developer notes

For those unfamiliar with `poetry`, it's a virtual environment and package manager. For development of this project `pyenv` is used as a layer on top of `virtualenv`. ([Pyenv](https://github.com/pyenv/pyenv) is installed by following [this example](http://codingadventures.org/2020/08/30/how-to-install-pyenv-in-ubuntu/) or [this with homebrew](https://medium.com/@marine.ss/installing-pyenv-on-ubuntu-20-04-c3a609a20aa2) which follows the readme. [Pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) is installed by following the readme.)

Create a general environment for developments

```bash
pyenv virtualenv 3.7.0 pyhera # or some higher version
```

Create the directory, move into it, and activate the environment. The repo is recreated by cloning, optionally recursively to add the documentation. Lastly add the dependencies.

```bash
mkdir heurestic-reasoning-agent
cd heurestic-reasoning-agent
pyenv local pyhera
git clone https://github.com/jeblad/heurestic-reasoning-agent.git . # without docs
poetry init
```

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

