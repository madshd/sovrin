import importlib

import os
from sovrin.common.util import getConfig


def writeAnonCredPlugin(baseDir):
    config = getConfig()
    pluginsPath = os.path.expanduser(os.path.join(baseDir, config.PluginsDir))

    if not os.path.exists(pluginsPath):
        os.makedirs(pluginsPath)

    initFile = pluginsPath + "/__init__.py"
    with open(initFile, "a"):
        pass

    anonPluginFilePath = pluginsPath + "/anoncreds.py"
    anonPluginContent = "" \
                        "import importlib\n" \
                        "import anoncreds.protocol.issuer\n" \
                        "import sovrin.anon_creds.issuer\n" \
                        "from sovrin.client.client import Client\n" \
                        "\n" \
                        "Name = \"Anon creds\"\n" \
                        "Version = 1.1\n" \
                        "SovrinVersion = 2.1\n" \
                        "\n" \
                        "sovrin.anon_creds.issuer.Issuer = " \
                        "anoncreds.protocol.issuer.Issuer\n" \
                        "importlib.reload(sovrin.client.client)\n" \
                        "importlib.reload(sovrin.test.helper)\n"
    # "newMro = Client.__mro__[:4] + (sovrin.anon_creds.issuer.Issuer,
    # ) + Client.__mro__[5:]\n" \
    # "sovrin.client.client.Client = type(Client.__name__, tuple(newMro),
    # dict(Client.__dict__))"

    with open(anonPluginFilePath, "a") as myfile:
        myfile.write(anonPluginContent)


def loadPlugins(baseDir):
    config = getConfig()
    pluginsDirPath = os.path.expanduser(os.path.join(baseDir, config.PluginsDir))
    if os.path.exists(pluginsDirPath):
        for pluginName in config.PluginsToLoad:
            print("********* plugin: {}".format(pluginName))
            pluginPath = os.path.join(pluginsDirPath, pluginName + ".py")
            spec = importlib.util.spec_from_file_location(pluginName,
                                                          pluginPath)
            plugin = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(plugin)

    print("done")
