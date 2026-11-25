import json
from pathlib import Path
from variant_normalizer import process
p=Path(__file__).parents[1]/"fixtures"/"input.json"
print(json.dumps(process(json.loads(p.read_text())),indent=2))
