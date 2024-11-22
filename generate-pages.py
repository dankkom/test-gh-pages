import json
import urllib.request
from pathlib import Path


template = """---
title: "{title}"
---

{shortcode}

https://github.com/dankkom/datasus-metadata
"""


index_json_url = "https://cdn.statically.io/gh/dankkom/datasus-metadata/main/metadata/index.json"

with urllib.request.urlopen(index_json_url) as response:
    data = json.load(response)

for dataset, info in data["data"].items():
    print(dataset, info)
    path = Path("content", "dados", dataset + ".md")
    url = f"https://cdn.statically.io/gh/dankkom/datasus-metadata/main/metadata/data/{dataset}.json"
    shortcode = "{{< remote-data-table \"" + url + "\" >}}"
    path.write_text(template.format(title=dataset, shortcode=shortcode))

for dataset, info in data["auxiliary"].items():
    print(dataset, info)
    path = Path("content", "auxiliares", dataset + ".md")
    url = f"https://cdn.statically.io/gh/dankkom/datasus-metadata/main/metadata/auxiliary/{dataset}.json"
    shortcode = "{{< remote-files-table \"" + url + "\" >}}"
    path.write_text(template.format(title=dataset, shortcode=shortcode))

for dataset, info in data["documentation"].items():
    print(dataset, info)
    path = Path("content", "documentacao", dataset + ".md")
    url = f"https://cdn.statically.io/gh/dankkom/datasus-metadata/main/metadata/documentation/{dataset}.json"
    shortcode = "{{< remote-files-table \"" + url + "\" >}}"
    path.write_text(template.format(title=dataset, shortcode=shortcode))
