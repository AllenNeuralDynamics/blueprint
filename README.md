<p align="center">
  <img alt="" src="./assets/pics/logo.png" width="55%">
</p>

[![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)

an interface-only repo describing standard interfaces to various instrument hardware.


## Why use blueprints
_blueprints_ defines standard interfaces to numerous types of devices: valves, syringe pumps, multi-axis stages, lasers, etc.
Think of it as a collection of abstract base classes.

Writing code that connects to any blueprints-derived driver means it can be swapped out for _any_ other driver that also derives from blueprints.

## When to use blueprints
Writing code that derives from an interface defined in blueprints maximizes its reusability across projects.

Here are some canonical use cases:
* You're writing a driver for a piece of hardware, and you'd like to create an interface for it that's common to similar device drivers.
* You're creating a generic GUI for a hardware device type, and you want it to be usable across as wide a range of similar devices as possible.


## Simulation via Stubs

This library also provides a simulated "dummy" or [stub](https://en.wikipedia.org/wiki/Stub_(distributed_computing)) version of each interface enabling you to simulate higher-level behavior using the interface without raising errors.

This is an alternative pattern to using [Mock](https://docs.python.org/3/library/unittest.mock.html) without requiring any boilerplate code.
Just import the simulated device.

## Projects using blueprints
### Instruments
* [AllenNeuralDynamics/brainwasher](https://github.com/AllenNeuralDynamics/brainwasher)

### Drivers
* [TODO]()
* [TODO]()

## Development

### Package/Project Management 

This project utilizes [uv](https://docs.astral.sh/uv/) to handle installing dependencies as well as setting up environments for this project. It replaces tool like pip, poetry, virtualenv, and conda. 

This project also uses [tox](https://tox.wiki/en/latest/index.html) for orchestrating multiple testing environments that mimics the github actions CI/CD so that you can test the workflows locally on your machine before pushing changes. 

### Code Quality Check

The following are tools used to ensure code quality in this project. 

- Unit Testing

```bash
uv run pytest tests
```

- Linting

```bash
uv run ruff check
```

- Type Check

```bash
uv run mypy src/mypackage
```

## Documentation
To generate the rst files source files for documentation, run
```bash
sphinx-apidoc -o docs/source/ src
```
Then to create the documentation HTML files, run
```bash
sphinx-build -b html docs/source/ docs/build/html
```
