import os
import ezkfg as ez


class TestYAML:
    def test_load(self):
        config = ez.load(
            os.path.join(
                os.path.dirname(__file__), "..", "examples", "example_config.yaml"
            )
        )

        print(config.dict())

        assert config.a == 1
        assert config.b.c == 2
        assert config.b.d.e == 3
        assert config.f.g == 4
        assert config.f.h == 5
        assert config.f.i == 6

    def test_dump(self):
        config = ez.load(
            os.path.join(
                os.path.dirname(__file__), "..", "examples", "example_config.yaml"
            )
        )
        config.dump("dump_config.yaml")
        config_ = ez.load("dump_config.yaml")
        for k, v in config.items():
            assert config_[k] == v

        ez.save(config, "dump_config.yaml")
        config_ = ez.load("dump_config.yaml")
        for k, v in config.items():
            assert config_[k] == v
