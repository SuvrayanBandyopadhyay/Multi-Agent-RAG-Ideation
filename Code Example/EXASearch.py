
from exa_py import Exa

import os

exa = Exa('394a39d9-d0cd-4b9d-961b-eb6ec8ef3fc5')

result = exa.search_and_contents(
  "IIT Patna",
  type="neural",
  use_autoprompt=True,
  num_results=10,
  text=True,
)

print(result)