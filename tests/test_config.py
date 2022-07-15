import os
from typing import Dict, List, Tuple, Any, Union, Optional, Iterable

from ezkfg import Config


class TestConfig:
    def test_instruction(self):
        config = Config({"a": 1, "b": {"c": 2}, "z.y.x": 233}, __auto_create__=True)
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

    def test_dict(self):
        config = Config({"a": 1, "b": {"c": 2}, "z.y.x": 233})
        assert isinstance(config.dict(), Dict)
        assert config.dict() == {"a": 1, "b": {"c": 2}, "z": {"y": {"x": 233}}}
