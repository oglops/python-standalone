from cx_Freeze import setup, Executable
from py_version import Version, Description
# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('py.py', base=base)
]

setup(name='oglop',
      version = Version,
      description = Description,
      options = dict(build_exe = buildOptions),
      executables = executables)
