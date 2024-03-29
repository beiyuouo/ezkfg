import os
from typing import Dict, List, Tuple, Any, Union, Optional, Iterable

from ezkfg import Config


class TestConfig:
    def test_instruction(self):
        config = Config({"a": 1, "b": {"c": 2}, "z.y.x": 233})
        assert config.a == 1
        assert config.b.c == 2
        assert config.z.y.x == 233

        config.a = 3
        assert config.a == 3

        config["d.e.f"] = 3
        assert config["d.e.f"] == 3
        assert config.d.e.f == 3

        config["e.f.g.h"] = 4
        assert config.e.f.g.h == 4
        assert config["e.f.g.h"] == 4

        config.e["h.i.j"] = 5
        assert config.e["h.i.j"] == 5
        assert config.e.h.i.j == 5
        assert config["e.h.i.j"] == 5
        assert config["e.h.i"].get("j", None) == 5

        config["g.h.i.j"] = 7
        assert config.g.h.i.j == 7
        assert config["g.h.i.j"] == 7

        config.load(["--model=resnet18", "--batch-size=32", "--lr=0.01"])
        assert config.model == "resnet18"
        assert config.batch_size == "32"
        assert config.lr == "0.01"

    def test_dict(self):
        config = Config({"a": 1, "b": {"c": 2}, "z.y.x": 233})
        assert isinstance(config.dict(), Dict)
        assert config.dict() == {"a": 1, "b": {"c": 2}, "z": {"y": {"x": 233}}}

    def test_dict_with_config(self):
        config = Config({"c": Config({"d": 1})})
        assert isinstance(config.dict(), Dict)
        assert config.dict() == {"c": {"d": 1}}
