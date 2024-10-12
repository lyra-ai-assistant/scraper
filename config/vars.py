import json
from pathlib import Path
from types import SimpleNamespace
from os.path import join, dirname


project_path = Path(dirname(__file__))
config_file = join(project_path.parent.absolute(), "config.json")

with open(config_file, "r") as configFile:
    config = json.load(configFile)

optional = config.get("optional", {})

vars = SimpleNamespace(
    scraperName=config.get("scraperName", "spider"),
    urlToScrap=config.get("urlToScrap", []),
    domainToScrap=config.get("domainToScrap", []),
    outputFileName=optional.get("outputFileName", "crawler_data"),
    outputFileFormat=optional.get("outputFileFormat", "json"),
    outputDirectory=optional.get("outputDirectory", "result"),
    verbose=optional.get("verbose", False),
    scraperTargets=config.get("selectors", {})
)
