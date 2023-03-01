import ezkfg as ez


class TestMerge:
    def test_merge(self):
        config1 = ez.load(["--model=resnet18", "--batch-size=32", "--lr=0.01"])
        config2 = ez.load(["--epoch=100", "--lr=0.001"])

        config1.merge(config2, overwrite=False)
        assert config1.model == "resnet18"
        assert config1.batch_size == "32"
        assert config1.lr == "0.01"
        assert config1.epoch == "100"

        config1.merge(config2, overwrite=True)
        assert config1.model == "resnet18"
        assert config1.batch_size == "32"
        assert config1.lr == "0.001"
        assert config1.epoch == "100"
