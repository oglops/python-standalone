I have often wanted a stand-alone version of python that would be a single
Windows executable.  This is my attempt to make a generally useful executable.

It consists of Python 2.7.9, pywin32-219, and psutil 2.1.3, and includes all
packages that py2exe sensibly includes without extra work.

It was built with setuptools.py 0.6c11 and py2exe 0.6.9.

To build, make sure you have the following files:
  py.py          # the main source file
  py_version.py  # simple version information
  setup.py       # the file needed for py2exe
type:
  python setup.py py2exe

You'll end up with a file called dist\py.exe.

Go ahead and use the executable or source as you see fit.  Credit is
appreciated, but not necessary.  I accept no liability.

If you found this useful, let me know.  If there is an issue, also let me know.
Obviously, one could include more or less libraries to either add features or
reduce the size of the executable.  I don't intend to make alternate versions
with different libraries.

1/4/15 - David Manthey - manthey@orbitals.com

