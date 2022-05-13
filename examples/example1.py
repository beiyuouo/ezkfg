from ezkfg import Config

if __name__ == "__main__":
    config = Config({"a": 1, "b": {"c": 2}})
    assert config.a == 1
    assert config.b.c == 2

    print(vars(config))

    print(config.dict())

    config["d.b.c"] = 6
    assert config["d.b.c"] == 6

    # config.e.f.g = 7
    # assert config.e.f.g == 7
