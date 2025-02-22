# PokeAPI SDK
The following contains src, setup & install instructions for the PokeAPI SDK.
# Setup, Build & Installation, and Testing
## Setup
```
# Recommended to setup venv
python3 -m venv poke
source poke/bin/activate

# Ensure you have `setuptools` installed =>
pip install setuptools
```
## Build & Installation
```
#Once you've installed setup tools, execute
python setup.py bdist_wheel sdist

#You can then install the package locally
pip install .
```

## Running Tests
```
#You can see tests by running
python run.py
```

### Prompt Requirements
+ Please ensure to include a README file alongside your SDK for user guidance.
  + This should clearly detail the installation process, usage, and testing instructions for the SDK.
+ Please add a section in the readme describing any critical design decisions you’ve taken or links to any tools used.
+ Please design and implement an integration test that makes use of your SDK to send an API request and validate the response. Again, you are free to use
any tool that you deem fit for this purpose.
+ It's important to note that the SDK doesn't necessarily have to replicate the API exactly. You're encouraged to add abstractions and/or amalgamate different calls to enhance the functionality.