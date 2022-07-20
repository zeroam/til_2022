import json
from bs4 import BeautifulSoup
from functools import partial

from experiment import Experiment
from xml_adapter import get_from_bs


def main() -> None:
    with open("config.json", encoding="utf-8") as file:
        config = json.load(file)
    with open("config.xml", encoding="utf-8") as file:
        config_xml = file.read()
    bs_xml = BeautifulSoup(config_xml, "xml")
    bs_adapter_fn = partial(get_from_bs, bs_xml)
    experiment = Experiment(bs_adapter_fn)
    # experiment = Experiment(config.get)
    experiment.run()


if __name__ == "__main__":
    main()
