from setuptools import setup, find_packages
import pathlib
from setuptools.command.install import install
import os

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

smesh_import_text = """
# Automatically added by Salome-MeshIO plugin
import salome_pluginsmanager
import SALOMExMeshIO
SALOMExMeshIO.init(salome_pluginsmanager)
# End of automatic addition
"""


class PostInstallCommand(install):
    """Add the plugin in Salome smesh_plugin.py"""
    def run(self):
        install.run(self)
        with open(os.getenv("HOME")+"/.config/salome/Plugins/smesh_plugins.py", "a") as smesh_plugins_file:
            smesh_plugins_file.write(smesh_import_text)
        


setup(
    name='SALOMExMeshIO', 
    version='0.1.0',  
    description='MeshIO plugin for Salome ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MoiseRousseau/Salome-MeshIO',
    author='Moise Rousseau',
    author_email='rousseau.moise@gmail.com', 
    classifiers=[ 
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
    ],
    keywords=["mesh", "file formats", "scientific", "engineering", "fem", "finite elements"], 
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.7, <4',
    requires=['meshio (==5.3.4)'],
    project_urls={ 
        'Bug Reports': 'https://github.com/MoiseRousseau/Salome-MeshIO/issues',
        'Source': 'https://github.com/MoiseRousseau/Salome-MeshIO/',
    },
    cmdclass={
        'install': PostInstallCommand,
    }
)
