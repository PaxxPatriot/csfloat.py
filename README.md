# csfloat.py
An API wrapper for the CSFloat API written in Python.

Installing
----------

**Python 3.10 or higher is required**

To install the library, you can just run the following command:

```bash
# Linux/macOS
$ python3 -m pip install -U csfloat.py

# Windows
> py -3 -m pip install -U csfloat.py
```

To install the development version, do the following:
```bash
$ git clone https://github.com/PaxxPatriot/csfloat.py.git
$ cd csfloat.py
$ python3 -m pip install -U .
```

Quick Example
--------------

```Python
import asyncio

import csfloat

async def main():
  client = csfloat.Client()
  # Set your personal API key, which you can get from https://csfloat.com/profile -> Developers -> + New Key
  client.set_api_key(api_key="YOUR API KEY HERE")

  # Get all listed CS2 items on csfloat.com and print the name to the console
  listings = await client.fetch_all_listings()
  async for listing in listings:
    print(listing.item.name)

if __name__ == "__main__":
    asyncio.run(main())
```
