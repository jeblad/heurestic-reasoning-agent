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
python3 pyhera.py --family abraxas build
```

and run the agent with

```bash
python3 pyhera.py --identifier <whatever> up
```

After building an agent, it can be identified either through `--identifier` or in some cases by `--name` if it is unique. Identifiers of UUID type should be close to unique, while a name could have a lot of collisions. An identifier could be partial as long as it uniquely identifies an agent in the given context. In the case of the subcommand `down` it means that if a single agent is running, then it is not necessary to provide any identifier.

A running agent can be stopped with

```bash
python3 pyhera.py --identifier <whatever> down
```

and then destroyed with

```bash
python3 pyhera.py --identifier <whatever> desytroy
```

When the agents resource requirements canʼt be satisfied, it will dump an error report. Usually because the device hit some limit. To check if the device has sufficient resources, use the `--simulate` argument. The agent will then do all the calculations, but not load code and data into the device.

An agent has a name, and upon normal termination it will write out the complete state to a named file. The file can be used for later invocation of the same instance.

The agent can be run in `--interactive` mode, or `--daemon` mode. In both cases the agent will keep on running continuously on the device, unless it is run in single step mode. In interactive mode the agent will not detach from the console, while in daemon mode it will detach.

### Secondary commands

Not only the software can be installed, but the built agents too. That makes it possible to start them without logging in to a specific account.

An agent can be installed with

```bash
python3 pyhera.py --identifier <whatever> install
```

and then uninstalled with

```bash
python3 pyhera.py --identifier <whatever> uninstall
```

Installing an agent can only happen when the agent is down, and there is no conflicting entries. Likewise, the agent can only be uninstalled when the agent is down and there is no conflicting entries. While installing (and uninstalling) a copy of the configuration will be placed in the “install” directory (or “work” directory), and the original removed from the “work” directory (or “install” directory).

Parts of the brain can be extended after initial configuration. Those parts are typically widths and heights, if those can be extended without conflicting offsets.

```bash
python3 pyhera.py --identifier <whatever> grow
```

It is not possible to shrink the brain the same way.

A few lists can be made for maintenance purposes

- agents – installed to the common directory
- devices – available on or from the host
- layouts – available layouts
- families – available modules

## Theory

A very short explanation of what kind of neural network this is; columns of autoencoders for each layer are evenly spaced over a neocortex, where autoencoders in each layer forms residual neural networks. There isnʼt a single autoencoder for each layer, as several neurons join together to make the autoencoder. They also represent values as sets of active neurons, and are not continuous values.

It is a kind of misnomer to say a column forms one autoencoder inside each layer, as there are several and also of different types of connections inside a column, but as a simplified description it holds.

Some layers have internal and external mixins, which has the role of hardcoded routing in more traditional deep learning networks, and in a biological neocortex it is done by corticocortical and intracortical connections.

A neocortex has an assoc that create feedback on associations on activity in each column, letting other columns act on the association, which can be interpreted as a kind of softcoded routing.

There are also a memory stack for the neocortex, the assoc, which keeps a trace of what the neocortex is doing at any given moment.

There is also patterns for creating expectations.

## Signals

A few signals can be sent to the agent:

  * …

## Notes

**PyCUDA** – The [PyCUDA](https://documen.tician.de/pycuda/) framework is used to integrate python at the host with CUDA at the device, and facilitate easy adaptation of the code according to the actual configuration. Some kernel parameters must be known at compile time, but those parameters are only known at runtime, thus the code must be generated and compiled just before it is loaded onto the device.

**Licenses** – The project as such has a [license](./LICENSE.md) according to the Norwegian Copyright Lav ([Åndsverkloven](https://lovdata.no/dokument/NL/lov/2018-06-15-40)) with some additional rights granted. As long as you donʼt do anything commercial, or have to change the code and republish, especially outside the educational domain like military or nuclear energy, it should be no problems at all.
