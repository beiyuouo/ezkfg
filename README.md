# ezkfg

Easy Configuration

## Installation

```bash
pip install ezkfg
```

## Usage

### Basic Usage

```python
from ezkfg import Config

if __name__ == '__main__':
    config = Config()
    config = Config({"a": 1, "b": {"c": 2}, "z.y.x": 233})
    assert config.a == 1
    assert config.b.c == 2
    assert config.z.y.x == 233

    config.a = 3
    assert config.a == 3

    config["d.e.f"] = 3
    assert config["d.e.f"] == 3
    assert config.d.e.f == 3

    config.e.f.g.h = 4
    assert config.e.f.g.h == 4
    assert config["e.f.g.h"] == 4

    config.e["h.i.j"] = 5
    assert config.e["h.i.j"] == 5
    assert config.e.h.i.j == 5
    assert config["e.h.i.j"] == 5

    config.f["i.j.k"].l = 6
    assert config.f["i.j.k"].l == 6
    assert config.f.i.j.k.l == 6
    assert config["f.i.j.k.l"] == 6

    config["g.h.i"].j = 7
    assert config.g.h.i.j == 7
    assert config["g.h.i.j"] == 7

    config.g["123.456.789"] = 8
    assert config.g["123.456.789"] == 8

    config["g.111.222.333"] = 9
    assert config.g["111.222.333"] == 9
    assert config.get("g.111.222.333") == 9
    assert config.get("g.111.222.333.544", "default") == "default"

    config.load(["--model=resnet18", "--batch-size=32", "--lr=0.01"])
    assert config.model == "resnet18"
    assert config.batch_size == "32"
    assert config.lr == "0.01"

    config.dump('config.json')  # support json, yaml, py, ini
    config.load('config.json')
```

### Advanced Usage

```python

```

## Acknowledgements

This project is inspired by the [addict](https://github.com/mewwts/addict) and [mmdetection](https://github.com/open-mmlab/mmdetection).
