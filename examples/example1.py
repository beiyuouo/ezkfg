import os
from ezkfg import Config

if __name__ == "__main__":
    config = Config({"a": 1, "b": {"c": 2}})
    assert config.a == 1
    assert config.b.c == 2

    print(vars(config))
    print(config.dict())

    config["d.b.c"] = 6
    assert config["d.b.c"] == 6

    print(vars(config))
    print(config.dict())

    config.e.f.g = 7
    assert config.e.f.g == 7

    print(vars(config))
    print(config.dict())

    config.load(os.path.join(os.path.dirname(__file__), "..", "examples", "example_config.py"))
    print(config.dict())
    assert config.a == 1
    assert config.b.c == 2
    assert config.z.y.x == 233

    config.dump("dump_config.py")
