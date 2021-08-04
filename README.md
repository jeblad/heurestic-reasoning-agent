# pyhera

Heurestic Reasoning Agent (PyHERA) with Python at host and CUDA at device.

## Usage

This is set up as an agent that runs continuously. The inputs (sensory data) are injected on the dendrities, and the outputs (motor data) are extracted from axons.

It should be enough to clone the repo, then cd into the folder, and run an `agent` with

```bash
python3 load.py -family:abraxas agent
```

If the agent can't be satified it will dump an error report. Usually because the device is somehow constrained. To check if the device has sufficient resources, use the `simulate` argument. The agent will then do all the calculations, but not load into the device.
