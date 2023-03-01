import os
import ezkfg as ez


class TestPy:
    def test_load(self):
        config = ez.load(
            os.path.join(
                os.path.dirname(__file__), "..", "examples", "example_config.py"
            )
        )

        print(config.dict())

        assert config.a == 1
        assert config.b.c == 2
        assert config.d.b.c == 6
        assert config.e.f.g == 7
        assert config.z.y.x == 233

    def test_dump(self):
        config = ez.load(
            os.path.join(
                os.path.dirname(__file__), "..", "examples", "example_config.py"
            )
        )
        config.dump("dump_config.py")
        config_ = ez.load("dump_config.py")
        for k, v in config.items():
            assert config_[k] == v

        ez.save(config, "dump_config.py")
        config_ = ez.load("dump_config.py")
        for k, v in config.items():
            assert config_[k] == v
        