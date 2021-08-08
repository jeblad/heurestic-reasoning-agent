# pyhera

Heuristic Reasoning Agent (PyHERA) with [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) at host and [CUDA](https://en.wikipedia.org/wiki/CUDA) at device, integrated with [PyCUDA](https://documen.tician.de/pycuda/).

## Usage

This software creates and runs an agent continuously. The inputs (sensory data) are injected on the [dendrites](https://en.wikipedia.org/wiki/Dendrite) artificial [synapses](https://en.wikipedia.org/wiki/Synapse), and the outputs (motor data) are extracted from [axons](https://en.wikipedia.org/wiki/Axon).

It should be enough to clone the repo, then `cd` into the folder, and then run the [software agent](https://en.wikipedia.org/wiki/Software_agent) with

```bash
python3 load.py -family:abraxas agent
```

When the agents resource requirements can't be satisfied it will dump an error report. Usually because the device is somehow constrained. To check if the device has sufficient resources, use the `-simulate` argument. The agent will then do all the calculations, but not load code and data into the device.

An agent is given a name, and upon normal termination it will write out the complete state to a named file. The file can be used for later invocation of the same instance.

The agent can be run in interactive mode, or daemonized. In both cases the agent will keep on running continuously on the device, unless it is run in single step mode. When run as a daemon stdin, stdout, and stderr will be redirected to specified devices.

## Signals

A few signals can be sent to the agent:

  * …

## Notes

**Pywikibot** – The [Pywikibot](https://www.mediawiki.org/wiki/Manual:Pywikibot) framework is used to make configuration easy, but also to provide access to the knowledge base [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia) and [Wikidata](https://en.wikipedia.org/wiki/Wikidata). Parts of the bot infrastructure are included as necessary.

**PyCUDA** – The [PyCUDA](https://documen.tician.de/pycuda/) framework is used to integrate python at the host with CUDA at the device, and facilitate easy adaptation of the code according to the actual configuration. Some kernel parameters must be known at compile time, but those parameters are only known at runtime, thus the code must be generated and compiled just before it is loaded onto the device.

**Licenses** – The project as such has a [license](./LICENSE.md) according to the Norwegian Copyright Lav ([Åndsverkloven](https://lovdata.no/dokument/NL/lov/2018-06-15-40)) with some additional rights granted. Parts from Pywikibot uses the [MIT license](https://opensource.org/licenses/MIT). As long as you don't do anything commercial, or have to change the code and republish, especially outside the educational domain like military or nuclear energy, it should be no problems at all.
