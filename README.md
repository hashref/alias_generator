# Alias Generator

This is a simple application that takes an email address and adds a '+' alias. For example...

`foo@gmail.com` converts to `foo+12345@gmail.com`

Once the conversion is done, the aliased email is copied to the clipboard ready for use.

## Setup

```sh
# Install dependencies
pipenv install --dev

# Setup pre-commit hooks
pipenv run pre-commit install -t pre-commit
```

## MacOS Application

It works best for me to create a simple MacOS application that launches this application. To make this work, you'll need to do the following...

### Create a wrapper

I call mine `AliasGenerator`. The wrapper code is as follows...

```bash
#!/usr/bin/env bash

cd {PATH TO alias_generator REPO}
{PATH TO PIPENV EXE}/pipenv run genalias
```

### Create the MacOS Application Package

```sh
mkdir -p ~/Applications/AliasGenerator.app/Contents/MacOS
cp AliasGenerator ~/Applications/AliasGenerator.app/Contents/MacOS/.
```

That should be all you need to do. Now you can launch it like you would any other application. You can add a fancy Icon too.

### Further Details

Follow this guide to creating the MacOS Application Package if you are confused.

https://mathiasbynens.be/notes/shell-script-mac-apps

## License

Distributed under the MIT License. See [LICENSE](https://github.com/hashref/aliasgenerator/blob/master/LICENSE) for more information.
