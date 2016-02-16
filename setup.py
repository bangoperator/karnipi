from distutils.core import setup

setup(
    name='karnipi',
    version='1.0',
    packages=['lib.python2.7.distutils', 'lib.python2.7.encodings', 'lib.python2.7.site-packages.pip',
              'lib.python2.7.site-packages.pip.req', 'lib.python2.7.site-packages.pip.vcs',
              'lib.python2.7.site-packages.pip.utils', 'lib.python2.7.site-packages.pip.compat',
              'lib.python2.7.site-packages.pip.models', 'lib.python2.7.site-packages.pip._vendor',
              'lib.python2.7.site-packages.pip._vendor.distlib',
              'lib.python2.7.site-packages.pip._vendor.distlib._backport',
              'lib.python2.7.site-packages.pip._vendor.colorama', 'lib.python2.7.site-packages.pip._vendor.html5lib',
              'lib.python2.7.site-packages.pip._vendor.html5lib.trie',
              'lib.python2.7.site-packages.pip._vendor.html5lib.filters',
              'lib.python2.7.site-packages.pip._vendor.html5lib.serializer',
              'lib.python2.7.site-packages.pip._vendor.html5lib.treewalkers',
              'lib.python2.7.site-packages.pip._vendor.html5lib.treeadapters',
              'lib.python2.7.site-packages.pip._vendor.html5lib.treebuilders',
              'lib.python2.7.site-packages.pip._vendor.lockfile', 'lib.python2.7.site-packages.pip._vendor.progress',
              'lib.python2.7.site-packages.pip._vendor.requests',
              'lib.python2.7.site-packages.pip._vendor.requests.packages',
              'lib.python2.7.site-packages.pip._vendor.requests.packages.chardet',
              'lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3',
              'lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.util',
              'lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.contrib',
              'lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.packages',
              'lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.packages.ssl_match_hostname',
              'lib.python2.7.site-packages.pip._vendor.packaging', 'lib.python2.7.site-packages.pip._vendor._markerlib',
              'lib.python2.7.site-packages.pip._vendor.cachecontrol',
              'lib.python2.7.site-packages.pip._vendor.cachecontrol.caches',
              'lib.python2.7.site-packages.pip._vendor.pkg_resources', 'lib.python2.7.site-packages.pip.commands',
              'lib.python2.7.site-packages.pip.operations', 'lib.python2.7.site-packages.wheel',
              'lib.python2.7.site-packages.wheel.test', 'lib.python2.7.site-packages.wheel.test.simple.dist.simpledist',
              'lib.python2.7.site-packages.wheel.test.complex-dist.complexdist',
              'lib.python2.7.site-packages.wheel.tool', 'lib.python2.7.site-packages.wheel.signatures',
              'lib.python2.7.site-packages._markerlib', 'lib.python2.7.site-packages.setuptools',
              'lib.python2.7.site-packages.setuptools.command', 'lib.python2.7.site-packages.pkg_resources',
              'lib.python2.7.site-packages.pkg_resources._vendor',
              'lib.python2.7.site-packages.pkg_resources._vendor.packaging', 'main', 'main.daemons', 'main.management',
              'main.management.commands', 'main.templatetags', 'local.lib.python2.7.distutils',
              'local.lib.python2.7.encodings', 'local.lib.python2.7.site-packages.pip',
              'local.lib.python2.7.site-packages.pip.req', 'local.lib.python2.7.site-packages.pip.vcs',
              'local.lib.python2.7.site-packages.pip.utils', 'local.lib.python2.7.site-packages.pip.compat',
              'local.lib.python2.7.site-packages.pip.models', 'local.lib.python2.7.site-packages.pip._vendor',
              'local.lib.python2.7.site-packages.pip._vendor.distlib',
              'local.lib.python2.7.site-packages.pip._vendor.distlib._backport',
              'local.lib.python2.7.site-packages.pip._vendor.colorama',
              'local.lib.python2.7.site-packages.pip._vendor.html5lib',
              'local.lib.python2.7.site-packages.pip._vendor.html5lib.trie',
              'local.lib.python2.7.site-packages.pip._vendor.html5lib.filters',
              'local.lib.python2.7.site-packages.pip._vendor.html5lib.serializer',
              'local.lib.python2.7.site-packages.pip._vendor.html5lib.treewalkers',
              'local.lib.python2.7.site-packages.pip._vendor.html5lib.treeadapters',
              'local.lib.python2.7.site-packages.pip._vendor.html5lib.treebuilders',
              'local.lib.python2.7.site-packages.pip._vendor.lockfile',
              'local.lib.python2.7.site-packages.pip._vendor.progress',
              'local.lib.python2.7.site-packages.pip._vendor.requests',
              'local.lib.python2.7.site-packages.pip._vendor.requests.packages',
              'local.lib.python2.7.site-packages.pip._vendor.requests.packages.chardet',
              'local.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3',
              'local.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.util',
              'local.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.contrib',
              'local.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.packages',
              'local.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.packages.ssl_match_hostname',
              'local.lib.python2.7.site-packages.pip._vendor.packaging',
              'local.lib.python2.7.site-packages.pip._vendor._markerlib',
              'local.lib.python2.7.site-packages.pip._vendor.cachecontrol',
              'local.lib.python2.7.site-packages.pip._vendor.cachecontrol.caches',
              'local.lib.python2.7.site-packages.pip._vendor.pkg_resources',
              'local.lib.python2.7.site-packages.pip.commands', 'local.lib.python2.7.site-packages.pip.operations',
              'local.lib.python2.7.site-packages.wheel', 'local.lib.python2.7.site-packages.wheel.test',
              'local.lib.python2.7.site-packages.wheel.test.simple.dist.simpledist',
              'local.lib.python2.7.site-packages.wheel.test.complex-dist.complexdist',
              'local.lib.python2.7.site-packages.wheel.tool', 'local.lib.python2.7.site-packages.wheel.signatures',
              'local.lib.python2.7.site-packages._markerlib', 'local.lib.python2.7.site-packages.setuptools',
              'local.lib.python2.7.site-packages.setuptools.command', 'local.lib.python2.7.site-packages.pkg_resources',
              'local.lib.python2.7.site-packages.pkg_resources._vendor',
              'local.lib.python2.7.site-packages.pkg_resources._vendor.packaging', 'local.main', 'local.main.daemons',
              'local.main.management', 'local.main.management.commands', 'local.main.templatetags', 'local.camera',
              'local.camera.migrations', 'local.config', 'local.karnipi', 'local.karnipi.local', 'local.terrarium',
              'local.maintenance', 'local.maintenance.migrations', 'camera', 'camera.migrations', 'config', 'karnipi',
              'karnipi.local', 'terrarium', 'maintenance', 'maintenance.migrations'],
    url='',
    license='',
    author='bangoperator',
    author_email='',
    description=''
)
