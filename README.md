# pyhera

![stability-experimental](https://img.shields.io/badge/stability-experimental-orange.svg?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues-raw/jeblad/pyhera?style=for-the-badge)

Heuristic Reasoning Agent (PyHERA) with [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) at host, and [CUDA](https://en.wikipedia.org/wiki/CUDA) at device integrated with [PyCUDA](https://documen.tician.de/pycuda/), or [OpenCL](https://en.wikipedia.org/wiki/OpenCL) at device integrated with [PyOpenCL](https://documen.tician.de/pyopencl/).

There are separate subrepositories for each of the models.

## Requirements

- python 3.7+
- poetry
- cliff

Models will typically have arequirement of either `pycuda` or `pyopencl`.

## Developer notes

For those unfamiliar with poetry, it's a virtual environment and package manager. For development of this project `pyenv` is used as a layer on top of `virtualenv`.

Typically the repo is recreated by doing `git clone`, optionally with `--recursive` added to include documentation, then `pyenv` to set up the virtual environment, and then `poetry`.

Cloning the repo

```bash
git clone https://github.com/jeblad/heurestic-reasoning-agent.git # without docs
git clone --recursive https://github.com/jeblad/heurestic-reasoning-agent.git
```

Move into the repo before the next commands

```bash
cd heurestic-reasoning-agent
```

Creating the environment

```bash
pyenv install 3.7
pyenv local 3.7
```

Install poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
poetry --version
```

Init repo

```bash
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

