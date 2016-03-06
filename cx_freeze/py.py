#!/usr/bin/python
#
# This is a small stub that is intended to be built into an executable with a
# setup.py file using "python setup.py py2exe".  This results in an executable
# called py.exe.  This can be used to run an arbitrary python script on Windows
# (XP and later) via py.exe (name of script).
#
# Changes:
#  2.7.4.1:
#   * initial release
#  2.7.4.2:
#   * fixed an issue with __file__ and __name__
#  2.7.4.3:
#   * Added the program path to sys.path when running a program, and "" to
# sys.path when running direct or interpretted.
#  2.7.5.4:
#   * Upgraded to python 2.7.5
#  2.7.5.5:
#   * Imported submodules, such as logging.handlers, since they weren't
# included implicitly.
#  2.7.8.6:
#   * Added support for multiprocessing forking
#   * Added support for non-ttty direct usage (input and output pipes, for
# instance)
#   * Added support for -i option and PYTHONINSPECT environment variable.
#   * Turned off "frozen" flag in py.exe
#   * Upgraded pywin32 to build 219 (was 218).
#   * Upgraded to python 2.7.8
#   * Added import site to interactive prompts to get help and other commands
# added to the builtins.
#   * Added support for unbuffered -u option and PYTHONUNBUFFERED environment
# variable.
#  2.7.8.7:
#   * Added support for -E, -x, and --version options.
#   * Changed how the globals / locals dictionaries are used for greater
# consistency in different execution modes.
#   * Accept multiple single letter command line options grouped together.
#  2.7.8.8:
#   * Fixed a bug I introduced in the last version when renaming the variable
# "loc".
#  2.7.8.9:
#   * My change to make globals dictionaries more consistent broke
# multiprocessing forking.  I've reverted some of the changes.
#  2.7.9.10:
#   * Upgraded to python 2.7.9
#   * Added psutil 2.1.3 win32
#   * Added support for the -m option.
#   * Turned off the optimization flag when building py.exe.  Having it on
# interferes with some modules (such as sympy) which rely on docstring
# manipulation.

AllModules = False

import os
import sys

if len(sys.argv) == 1 and not hasattr(sys, "frozen"):
    AllModules = True
if not AllModules and sys.argv[:2][-1] != "--all":
    pass
else:
    # I think this is the complete list of modules in the Python 2.7
    # installation on Windows XP.  This was the default 2.7 installation without
    # any options, plus pywin32-219, psutil 2.1.3, setuptools, and py2exe.  I
    # generated the list of modules with help("modules").  I then commented out
    # anything that wouldn't import.  Further, there are some submodules that
    # don't automatically import with the base module.  help("modules .") lists
    # these.  Any module that isn't present with its base but can be imported
    # was then added.
    import __builtin__
    import __future__
    import _abcoll
    import _bisect
    import _collections
    import _csv
    import _functools
    import _heapq
    import _io
    import _locale
    # import _LWPCookieJar
    # import _markerlib.markers
    # # import _MozillaCookieJar
    # import _osx_support
    # import _pyio
    # import _random
    # import _strptime
    # import _threading_local
    # import _warnings
    # import _weakref
    # import _winreg
    # import abc
    # # import adodbapi
    # import aifc
    # import anydbm
    # import asynchat
    # import asyncore
    # import atexit
    # import BaseHTTPServer
    # import Bastion
    # import binhex
    # import bisect
    # import bsddb
    # import bsddb.db 
    # import bsddb.dbobj 
    # import bsddb.dbrecio
    # import bsddb.dbshelve
    # import bsddb.dbtables 
    # import bsddb.dbutils 
    # import bsddb.test 
    # import bsddb.test.test_all
    # import bsddb.test.test_associate
    # import bsddb.test.test_basics
    # import bsddb.test.test_compare
    # import bsddb.test.test_compat
    # import bsddb.test.test_cursor_pget_bug 
    # import bsddb.test.test_db 
    # import bsddb.test.test_dbenv 
    # import bsddb.test.test_dbobj 
    # import bsddb.test.test_dbshelve
    # import bsddb.test.test_dbtables 
    # import bsddb.test.test_distributed_transactions
    # import bsddb.test.test_early_close
    # import bsddb.test.test_fileid
    # import bsddb.test.test_get_none
    # import bsddb.test.test_join
    # import bsddb.test.test_lock
    # import bsddb.test.test_misc
    # import bsddb.test.test_pickle 
    # import bsddb.test.test_queue
    # import bsddb.test.test_recno
    # import bsddb.test.test_replication
    # import bsddb.test.test_sequence 
    # import bsddb.test.test_thread
    # import cgi
    # import CGIHTTPServer
    # import cgitb
    # import chunk
    # import cmath
    # import cmd
    # import code
    # import codecs
    # import codeop
    # import colorsys
    # import commands
    # import compileall
    # import compiler.ast
    # import compiler.consts 
    # import compiler.future
    # import compiler.misc 
    # import compiler.pyassem
    # import compiler.pycodegen 
    # import compiler.symbols
    # import compiler.syntax
    # import compiler.transformer
    # import compiler.visitor 
    # import ConfigParser
    # import contextlib
    # import Cookie
    # import cookielib
    # import copy
    # import copy_reg
    # import cPickle
    # import cProfile
    # import cStringIO
    # import csv
    # import ctypes._endian 
    # import ctypes.macholib
    # import ctypes.macholib.dyld
    # import ctypes.macholib.dylib
    # import ctypes.macholib.framework
    # import ctypes.test 
    # import ctypes.test.runtests
    # import ctypes.test.test_anon 
    # import ctypes.test.test_array_in_pointer 
    # import ctypes.test.test_arrays 
    # import ctypes.test.test_as_parameter 
    # import ctypes.test.test_bitfields 
    # import ctypes.test.test_buffers 
    # import ctypes.test.test_byteswap 
    # import ctypes.test.test_callbacks 
    # import ctypes.test.test_cast 
    # import ctypes.test.test_cfuncs 
    # import ctypes.test.test_checkretval 
    # import ctypes.test.test_delattr 
    # import ctypes.test.test_errno 
    # import ctypes.test.test_find 
    # import ctypes.test.test_frombuffer 
    # import ctypes.test.test_funcptr 
    # import ctypes.test.test_functions
    # import ctypes.test.test_incomplete 
    # import ctypes.test.test_init 
    # import ctypes.test.test_internals 
    # import ctypes.test.test_keeprefs 
    # import ctypes.test.test_libc 
    # import ctypes.test.test_loading 
    # import ctypes.test.test_macholib 
    # import ctypes.test.test_memfunctions 
    # import ctypes.test.test_numbers 
    # import ctypes.test.test_objects 
    # import ctypes.test.test_parameters 
    # import ctypes.test.test_pep3118 
    # import ctypes.test.test_pickling 
    # import ctypes.test.test_pointers 
    # import ctypes.test.test_prototypes 
    # import ctypes.test.test_python_api 
    # import ctypes.test.test_random_things 
    # import ctypes.test.test_refcounts 
    # import ctypes.test.test_repr 
    # import ctypes.test.test_returnfuncptrs 
    # import ctypes.test.test_simplesubclasses 
    # import ctypes.test.test_sizes 
    # import ctypes.test.test_slicing 
    # import ctypes.test.test_stringptr 
    # import ctypes.test.test_strings 
    # import ctypes.test.test_struct_fields 
    # import ctypes.test.test_structures 
    # import ctypes.test.test_unaligned_structures 
    # import ctypes.test.test_unicode 
    # import ctypes.test.test_values
    # import ctypes.test.test_varsize_struct 
    # import ctypes.test.test_win32 
    # import ctypes.test.test_wintypes 
    # import ctypes.util 
    # import ctypes.wintypes 
    # import cx_Freeze.common
    # import cx_Freeze.dist 
    # import cx_Freeze.finder
    # import cx_Freeze.freezer
    # import cx_Freeze.hooks 
    # import cx_Freeze.macdist 
    # import cx_Freeze.main 
    # import cx_Freeze.setupwriter 
    # import cx_Freeze.util 
    # import cx_Freeze.windist 
    # import datetime
    # import dbhash
    # import dbi
    # import decimal
    # import difflib
    # import dircache
    # import dis
    # import distutils.archive_util
    # import distutils.bcppcompiler
    # import distutils.ccompiler
    # import distutils.cmd
    # import distutils.command
    # import distutils.command.bdist
    # import distutils.command.bdist_dumb
    # import distutils.command.bdist_msi
    # import distutils.command.bdist_rpm
    # import distutils.command.bdist_wininst
    # import distutils.command.build
    # import distutils.command.build_clib
    # import distutils.command.build_ext
    # import distutils.command.build_py
    # import distutils.command.build_scripts
    # import distutils.command.check
    # import distutils.command.clean
    # import distutils.command.config
    # import distutils.command.install
    # import distutils.command.install_data
    # import distutils.command.install_egg_info
    # import distutils.command.install_headers
    # import distutils.command.install_lib
    # import distutils.command.install_scripts
    # import distutils.command.register
    # import distutils.command.sdist
    # import distutils.command.upload
    # import distutils.config
    # import distutils.core
    # import distutils.cygwinccompiler
    # import distutils.debug 
    # import distutils.dep_util
    # import distutils.dir_util
    # import distutils.dist
    # import distutils.emxccompiler
    # import distutils.errors
    # import distutils.extension
    # import distutils.fancy_getopt
    # import distutils.file_util
    # import distutils.filelist
    # import distutils.log
    # import distutils.msvc9compiler
    # import distutils.msvccompiler
    # import distutils.spawn
    # import distutils.sysconfig
    # import distutils.tests
    # import distutils.tests.setuptools_build_ext 
    # import distutils.tests.setuptools_extension 
    # import distutils.tests.support
    # import distutils.tests.test_archive_util
    # import distutils.tests.test_bdist
    # import distutils.tests.test_bdist_dumb
    # import distutils.tests.test_bdist_msi
    # import distutils.tests.test_bdist_rpm
    # import distutils.tests.test_bdist_wininst
    # import distutils.tests.test_build
    # import distutils.tests.test_build_clib
    # import distutils.tests.test_build_ext 
    # import distutils.tests.test_build_py
    # import distutils.tests.test_build_scripts
    # import distutils.tests.test_ccompiler
    # import distutils.tests.test_check
    # import distutils.tests.test_clean
    # import distutils.tests.test_cmd
    # import distutils.tests.test_config
    # import distutils.tests.test_config_cmd
    # import distutils.tests.test_core
    # import distutils.tests.test_dep_util
    # import distutils.tests.test_dir_util
    # import distutils.tests.test_dist
    # import distutils.tests.test_file_util
    # import distutils.tests.test_filelist
    # import distutils.tests.test_install
    # import distutils.tests.test_install_data
    # import distutils.tests.test_install_headers
    # import distutils.tests.test_install_lib
    # import distutils.tests.test_install_scripts
    # import distutils.tests.test_msvc9compiler
    # import distutils.tests.test_register
    # import distutils.tests.test_sdist
    # import distutils.tests.test_spawn
    # import distutils.tests.test_sysconfig
    # import distutils.tests.test_text_file
    # import distutils.tests.test_unixccompiler
    # import distutils.tests.test_upload
    # import distutils.tests.test_util
    # import distutils.tests.test_version
    # import distutils.tests.test_versionpredicate
    # import distutils.text_file
    # import distutils.unixccompiler
    # import distutils.util
    # import distutils.version
    # import distutils.versionpredicate
    # import doctest
    # import DocXMLRPCServer
    # import dumbdbm
    # import dummy_thread
    # import dummy_threading
    # import email
    # import email._parseaddr
    # import email.base64mime
    # import email.charset 
    # import email.encoders
    # import email.errors
    # import email.feedparser
    # import email.generator
    # import email.header
    # import email.iterators
    # import email.message
    # import email.mime 
    # import email.mime.application
    # import email.mime.audio
    # import email.mime.base
    # import email.mime.image
    # import email.mime.message
    # import email.mime.multipart
    # import email.mime.nonmultipart
    # import email.mime.text
    # import email.parser
    # import email.quoprimime
    # import email.test 
    # import email.test.test_email 
    # import email.test.test_email_codecs 
    # import email.test.test_email_codecs_renamed 
    # import email.test.test_email_renamed 
    # # import email.test.test_email_torture 
    # import email.utils
    # import encodings.aliases
    # import encodings.ascii
    # import encodings.base64_codec
    # import encodings.big5 
    # import encodings.big5hkscs 
    # import encodings.bz2_codec
    # import encodings.charmap
    # import encodings.cp037
    # import encodings.cp1006
    # import encodings.cp1026
    # import encodings.cp1140
    # import encodings.cp1250
    # import encodings.cp1251
    # import encodings.cp1252
    # import encodings.cp1253
    # import encodings.cp1254
    # import encodings.cp1255
    # import encodings.cp1256
    # import encodings.cp1257
    # import encodings.cp1258
    # import encodings.cp424
    # import encodings.cp437
    # import encodings.cp500
    # import encodings.cp720
    # import encodings.cp737
    # import encodings.cp775
    # import encodings.cp850
    # import encodings.cp852
    # import encodings.cp855
    # import encodings.cp856
    # import encodings.cp857
    # import encodings.cp858
    # import encodings.cp860
    # import encodings.cp861
    # import encodings.cp862
    # import encodings.cp863
    # import encodings.cp864
    # import encodings.cp865
    # import encodings.cp866
    # import encodings.cp869
    # import encodings.cp874
    # import encodings.cp875
    # import encodings.cp932 
    # import encodings.cp949 
    # import encodings.cp950 
    # import encodings.euc_jis_2004 
    # import encodings.euc_jisx0213 
    # import encodings.euc_jp 
    # import encodings.euc_kr 
    # import encodings.gb18030 
    # import encodings.gb2312 
    # import encodings.gbk 
    # import encodings.hex_codec
    # import encodings.hp_roman8
    # import encodings.hz 
    # import encodings.idna 
    # import encodings.iso2022_jp 
    # import encodings.iso2022_jp_1 
    # import encodings.iso2022_jp_2 
    # import encodings.iso2022_jp_2004 
    # import encodings.iso2022_jp_3 
    # import encodings.iso2022_jp_ext 
    # import encodings.iso2022_kr 
    # import encodings.iso8859_1
    # import encodings.iso8859_10
    # import encodings.iso8859_11
    # import encodings.iso8859_13
    # import encodings.iso8859_14
    # import encodings.iso8859_15
    # import encodings.iso8859_16
    # import encodings.iso8859_2
    # import encodings.iso8859_3
    # import encodings.iso8859_4
    # import encodings.iso8859_5
    # import encodings.iso8859_6
    # import encodings.iso8859_7
    # import encodings.iso8859_8
    # import encodings.iso8859_9
    # import encodings.johab 
    # import encodings.koi8_r
    # import encodings.koi8_u
    # import encodings.latin_1
    # import encodings.mac_arabic
    # import encodings.mac_centeuro
    # import encodings.mac_croatian
    # import encodings.mac_cyrillic
    # import encodings.mac_farsi
    # import encodings.mac_greek
    # import encodings.mac_iceland
    # import encodings.mac_latin2
    # import encodings.mac_roman
    # import encodings.mac_romanian
    # import encodings.mac_turkish
    # import encodings.mbcs
    # import encodings.palmos
    # import encodings.ptcp154
    # import encodings.punycode
    # import encodings.quopri_codec
    # import encodings.raw_unicode_escape
    # import encodings.rot_13
    # import encodings.shift_jis 
    # import encodings.shift_jis_2004 
    # import encodings.shift_jisx0213 
    # import encodings.string_escape
    # import encodings.tis_620
    # import encodings.undefined
    # import encodings.unicode_escape
    # import encodings.unicode_internal
    # import encodings.utf_16
    # import encodings.utf_16_be
    # import encodings.utf_16_le
    # import encodings.utf_32
    # import encodings.utf_32_be
    # import encodings.utf_32_le
    # import encodings.utf_7
    # import encodings.utf_8
    # import encodings.utf_8_sig
    # import encodings.uu_codec
    # import encodings.zlib_codec
    # import ensurepip.__main__ 
    # import ensurepip._uninstall
    # import errno
    # import exceptions
    # import filecmp
    # import FileDialog
    # import fileinput
    # import fnmatch
    # import formatter
    # import fpformat
    # import fractions
    # import ftplib
    # import functools
    # import future_builtins
    # import gc
    # import getopt
    # import getpass
    # import gettext
    # import glob
    # import gzip
    # import heapq
    # import hmac
    # import hotshot
    # import hotshot.log 
    # import hotshot.stats
    # import hotshot.stones 
    # import htmlentitydefs
    # import htmllib
    # import HTMLParser
    # import httplib
    # import idlelib
    # import idlelib.aboutDialog
    # import idlelib.AutoComplete
    # import idlelib.AutoCompleteWindow
    # import idlelib.AutoExpand 
    # import idlelib.Bindings
    # import idlelib.CallTips
    # import idlelib.CallTipWindow
    # import idlelib.ClassBrowser
    # import idlelib.CodeContext
    # import idlelib.ColorDelegator 
    # import idlelib.configDialog
    # import idlelib.configHandler
    # import idlelib.configHelpSourceEdit 
    # import idlelib.configSectionNameDialog
    # import idlelib.Debugger 
    # import idlelib.Delegator 
    # import idlelib.dynOptionMenuWidget
    # import idlelib.EditorWindow 
    # import idlelib.FileList 
    # import idlelib.FormatParagraph
    # import idlelib.GrepDialog 
    # import idlelib.help
    # import idlelib.HyperParser
    # import idlelib.idle 
    # import idlelib.idle_test 
    # import idlelib.idle_test.htest 
    # import idlelib.idle_test.mock_idle 
    # import idlelib.idle_test.mock_tk
    # import idlelib.idle_test.test_autocomplete 
    # import idlelib.idle_test.test_autoexpand
    # import idlelib.idle_test.test_calltips 
    # import idlelib.idle_test.test_config_name
    # import idlelib.idle_test.test_configdialog 
    # import idlelib.idle_test.test_delegator 
    # import idlelib.idle_test.test_formatparagraph 
    # import idlelib.idle_test.test_grep
    # import idlelib.idle_test.test_hyperparser
    # import idlelib.idle_test.test_idlehistory 
    # import idlelib.idle_test.test_io 
    # import idlelib.idle_test.test_parenmatch
    # import idlelib.idle_test.test_pathbrowser 
    # import idlelib.idle_test.test_rstrip 
    # import idlelib.idle_test.test_searchdialogbase 
    # import idlelib.idle_test.test_searchengine 
    # import idlelib.idle_test.test_text 
    # import idlelib.idle_test.test_textview 
    # import idlelib.idle_test.test_warning 
    # import idlelib.idle_test.test_widgetredir
    # import idlelib.IdleHistory 
    # import idlelib.idlever
    # import idlelib.IOBinding 
    # import idlelib.keybindingDialog
    # import idlelib.macosxSupport
    # import idlelib.MultiCall
    # import idlelib.MultiStatusBar 
    # import idlelib.ObjectBrowser 
    # import idlelib.OutputWindow 
    # import idlelib.ParenMatch
    # import idlelib.PathBrowser 
    # import idlelib.Percolator 
    # import idlelib.PyParse 
    # import idlelib.PyShell 
    # import idlelib.RemoteDebugger
    # import idlelib.RemoteObjectBrowser 
    # import idlelib.ReplaceDialog 
    # import idlelib.rpc
    # import idlelib.RstripExtension 
    # import idlelib.run 
    # import idlelib.ScriptBinding
    # import idlelib.ScrolledList 
    # import idlelib.SearchDialog 
    # import idlelib.SearchDialogBase 
    # import idlelib.SearchEngine 
    # import idlelib.StackViewer 
    # import idlelib.tabbedpages
    # import idlelib.textView
    # import idlelib.ToolTip 
    # import idlelib.TreeWidget 
    # import idlelib.UndoDelegator 
    # import idlelib.WidgetRedirector 
    # import idlelib.WindowList 
    # import idlelib.ZoomHeight 
    # import ihooks
    # import imaplib
    # import imghdr
    # import importlib
    # import inspect
    # import io
    # import isapi.install
    # import isapi.isapicon
    # import isapi.simple
    # import isapi.threaded_extension
    # import itertools
    # import json
    # import json.decoder
    # import json.encoder
    # import json.scanner
    # import json.tests 
    # import json.tests.test_check_circular 
    # import json.tests.test_decode 
    # import json.tests.test_default 
    # import json.tests.test_dump 
    # import json.tests.test_encode_basestring_ascii 
    # import json.tests.test_fail 
    # import json.tests.test_float 
    # import json.tests.test_indent 
    # import json.tests.test_pass1 
    # import json.tests.test_pass2 
    # import json.tests.test_pass3 
    # import json.tests.test_recursion 
    # import json.tests.test_scanstring 
    # import json.tests.test_separators 
    # import json.tests.test_speedups 
    # import json.tests.test_tool 
    # import json.tests.test_unicode 
    # import json.tool
    # import keyword
    # # import lib2to3.__main__ 
    # # import lib2to3.btm_matcher
    # # import lib2to3.btm_utils 
    # # import lib2to3.fixer_base
    # # import lib2to3.fixer_util
    # # import lib2to3.fixes 
    # # import lib2to3.fixes.fix_apply
    # # import lib2to3.fixes.fix_asserts
    # # import lib2to3.fixes.fix_basestring
    # # import lib2to3.fixes.fix_buffer
    # # import lib2to3.fixes.fix_callable
    # # import lib2to3.fixes.fix_dict
    # # import lib2to3.fixes.fix_except
    # # import lib2to3.fixes.fix_exec
    # # import lib2to3.fixes.fix_execfile
    # # import lib2to3.fixes.fix_exitfunc
    # # import lib2to3.fixes.fix_filter
    # # import lib2to3.fixes.fix_funcattrs
    # # import lib2to3.fixes.fix_future
    # # import lib2to3.fixes.fix_getcwdu
    # # import lib2to3.fixes.fix_has_key
    # # import lib2to3.fixes.fix_idioms
    # # import lib2to3.fixes.fix_import
    # # import lib2to3.fixes.fix_imports
    # # import lib2to3.fixes.fix_imports2
    # # import lib2to3.fixes.fix_input
    # # import lib2to3.fixes.fix_intern
    # # import lib2to3.fixes.fix_isinstance
    # # import lib2to3.fixes.fix_itertools
    # # import lib2to3.fixes.fix_itertools_imports
    # # import lib2to3.fixes.fix_long
    # # import lib2to3.fixes.fix_map
    # # import lib2to3.fixes.fix_metaclass
    # # import lib2to3.fixes.fix_methodattrs
    # # import lib2to3.fixes.fix_ne
    # # import lib2to3.fixes.fix_next
    # # import lib2to3.fixes.fix_nonzero
    # # import lib2to3.fixes.fix_numliterals
    # # import lib2to3.fixes.fix_operator
    # # import lib2to3.fixes.fix_paren
    # # import lib2to3.fixes.fix_print
    # # import lib2to3.fixes.fix_raise
    # # import lib2to3.fixes.fix_raw_input
    # # import lib2to3.fixes.fix_reduce
    # # import lib2to3.fixes.fix_renames
    # # import lib2to3.fixes.fix_repr
    # # import lib2to3.fixes.fix_set_literal
    # # import lib2to3.fixes.fix_standarderror
    # # import lib2to3.fixes.fix_sys_exc
    # # import lib2to3.fixes.fix_throw
    # # import lib2to3.fixes.fix_tuple_params
    # # import lib2to3.fixes.fix_types
    # # import lib2to3.fixes.fix_unicode
    # # import lib2to3.fixes.fix_urllib
    # # import lib2to3.fixes.fix_ws_comma
    # # import lib2to3.fixes.fix_xrange
    # # import lib2to3.fixes.fix_xreadlines
    # # import lib2to3.fixes.fix_zip
    # # import lib2to3.main
    # # import lib2to3.patcomp
    # # import lib2to3.pgen2
    # # import lib2to3.pgen2.conv
    # # import lib2to3.pgen2.driver
    # # import lib2to3.pgen2.grammar
    # # import lib2to3.pgen2.literals
    # # import lib2to3.pgen2.parse
    # # import lib2to3.pgen2.pgen 
    # # import lib2to3.pgen2.token
    # # import lib2to3.pgen2.tokenize
    # # import lib2to3.pygram
    # # import lib2to3.pytree
    # # import lib2to3.refactor
    # # import lib2to3.tests
    # # import lib2to3.tests.pytree_idempotency
    # # import lib2to3.tests.support
    # # import lib2to3.tests.test_all_fixers
    # # import lib2to3.tests.test_fixers
    # # import lib2to3.tests.test_main 
    # # import lib2to3.tests.test_parser
    # # import lib2to3.tests.test_pytree
    # # import lib2to3.tests.test_refactor
    # # import lib2to3.tests.test_util
    # import linecache
    # import locale
    # import logging
    # import logging.config
    # import logging.handlers
    # import macpath
    # import macurl2path
    # import mailbox
    # import mailcap
    # import markupbase
    # import math
    # import mimetools
    # import mimetypes
    # import MimeWriter
    # import mimify
    # import modulefinder
    # import msilib.schema 
    # import msilib.sequence 
    # import msilib.text 
    # import multifile
    # import multiprocessing.connection 
    # import multiprocessing.dummy 
    # import multiprocessing.dummy.connection 
    # import multiprocessing.forking 
    # import multiprocessing.heap 
    # import multiprocessing.managers 
    # import multiprocessing.pool 
    # import multiprocessing.process 
    # import multiprocessing.queues 
    # import multiprocessing.reduction 
    # import multiprocessing.sharedctypes 
    # import multiprocessing.synchronize 
    # import multiprocessing.util 
    # import netrc
    # import new
    # import nntplib
    # import ntpath
    # import nturl2path
    # import numbers
    # import operator
    # import optparse
    # import os
    # import os2emxpath
    # import parser
    # import pdb
    # import pickle
    # import pip.__main__ 
    # import pip._vendor
    # import pip._vendor._markerlib 
    # import pip._vendor._markerlib.markers
    # import pip._vendor.cachecontrol
    # import pip._vendor.cachecontrol._cmd 
    # import pip._vendor.cachecontrol.adapter 
    # import pip._vendor.cachecontrol.cache
    # import pip._vendor.cachecontrol.caches 
    # import pip._vendor.cachecontrol.caches.file_cache 
    # import pip._vendor.cachecontrol.caches.redis_cache 
    # import pip._vendor.cachecontrol.compat 
    # import pip._vendor.cachecontrol.controller
    # import pip._vendor.cachecontrol.filewrapper 
    # import pip._vendor.cachecontrol.heuristics 
    # import pip._vendor.cachecontrol.serialize 
    # import pip._vendor.cachecontrol.wrapper 
    # import pip._vendor.colorama 
    # import pip._vendor.colorama.ansi 
    # import pip._vendor.colorama.ansitowin32 
    # import pip._vendor.colorama.initialise 
    # import pip._vendor.colorama.win32 
    # import pip._vendor.colorama.winterm 
    # import pip._vendor.distlib 
    # import pip._vendor.distlib._backport
    # import pip._vendor.distlib._backport.misc
    # import pip._vendor.distlib._backport.shutil
    # import pip._vendor.distlib._backport.sysconfig
    # import pip._vendor.distlib._backport.tarfile 
    # import pip._vendor.distlib.compat 
    # import pip._vendor.distlib.database
    # import pip._vendor.distlib.index 
    # import pip._vendor.distlib.locators 
    # import pip._vendor.distlib.manifest
    # import pip._vendor.distlib.markers
    # import pip._vendor.distlib.metadata
    # import pip._vendor.distlib.resources 
    # import pip._vendor.distlib.scripts 
    # import pip._vendor.distlib.util 
    # import pip._vendor.distlib.version
    # import pip._vendor.distlib.wheel 
    # import pip._vendor.html5lib
    # import pip._vendor.html5lib.constants 
    # import pip._vendor.html5lib.filters 
    # import pip._vendor.html5lib.filters._base 
    # import pip._vendor.html5lib.filters.alphabeticalattributes 
    # import pip._vendor.html5lib.filters.inject_meta_charset 
    # import pip._vendor.html5lib.filters.lint 
    # import pip._vendor.html5lib.filters.optionaltags 
    # import pip._vendor.html5lib.filters.sanitizer 
    # import pip._vendor.html5lib.filters.whitespace 
    # import pip._vendor.html5lib.html5parser 
    # import pip._vendor.html5lib.ihatexml 
    # import pip._vendor.html5lib.inputstream 
    # import pip._vendor.html5lib.sanitizer 
    # import pip._vendor.html5lib.serializer 
    # import pip._vendor.html5lib.serializer.htmlserializer 
    # import pip._vendor.html5lib.tokenizer 
    # import pip._vendor.html5lib.treeadapters 
    # import pip._vendor.html5lib.treeadapters.sax 
    # import pip._vendor.html5lib.treebuilders
    # import pip._vendor.html5lib.treebuilders._base 
    # import pip._vendor.html5lib.treebuilders.dom 
    # import pip._vendor.html5lib.treebuilders.etree 
    # import pip._vendor.html5lib.treebuilders.etree_lxml
    # import pip._vendor.html5lib.treewalkers
    # import pip._vendor.html5lib.treewalkers._base 
    # import pip._vendor.html5lib.treewalkers.dom 
    # import pip._vendor.html5lib.treewalkers.etree 
    # import pip._vendor.html5lib.treewalkers.genshistream 
    # import pip._vendor.html5lib.treewalkers.lxmletree 
    # import pip._vendor.html5lib.treewalkers.pulldom 
    # import pip._vendor.html5lib.trie 
    # import pip._vendor.html5lib.trie._base 
    # import pip._vendor.html5lib.trie.datrie 
    # import pip._vendor.html5lib.trie.py 
    # import pip._vendor.html5lib.utils 
    # import pip._vendor.ipaddress
    # import pip._vendor.lockfile
    # import pip._vendor.lockfile.linklockfile 
    # import pip._vendor.lockfile.mkdirlockfile 
    # import pip._vendor.lockfile.pidlockfile
    # import pip._vendor.lockfile.sqlitelockfile 
    # import pip._vendor.lockfile.symlinklockfile 
    # import pip._vendor.packaging 
    # import pip._vendor.packaging.__about__ 
    # import pip._vendor.packaging._compat 
    # import pip._vendor.packaging._structures 
    # import pip._vendor.packaging.markers 
    # import pip._vendor.packaging.specifiers 
    # import pip._vendor.packaging.version 
    # import pip._vendor.pkg_resources
    # import pip._vendor.progress 
    # import pip._vendor.progress.bar 
    # import pip._vendor.progress.counter 
    # import pip._vendor.progress.helpers 
    # import pip._vendor.progress.spinner 
    # import pip._vendor.pyparsing 
    # # import pip._vendor.re-vendor 
    # import pip._vendor.requests
    # import pip._vendor.requests.adapters
    # import pip._vendor.requests.api
    # import pip._vendor.requests.auth
    # import pip._vendor.requests.certs
    # import pip._vendor.requests.compat
    # import pip._vendor.requests.cookies
    # import pip._vendor.requests.exceptions
    # import pip._vendor.requests.hooks
    # import pip._vendor.requests.models
    # import pip._vendor.requests.packages 
    # import pip._vendor.requests.packages.chardet 
    # import pip._vendor.requests.packages.chardet.big5freq 
    # import pip._vendor.requests.packages.chardet.big5prober 
    # import pip._vendor.requests.packages.chardet.chardetect
    # import pip._vendor.requests.packages.chardet.chardistribution 
    # import pip._vendor.requests.packages.chardet.charsetgroupprober 
    # import pip._vendor.requests.packages.chardet.charsetprober 
    # import pip._vendor.requests.packages.chardet.codingstatemachine 
    # import pip._vendor.requests.packages.chardet.compat 
    # import pip._vendor.requests.packages.chardet.constants 
    # import pip._vendor.requests.packages.chardet.cp949prober 
    # import pip._vendor.requests.packages.chardet.escprober 
    # import pip._vendor.requests.packages.chardet.escsm 
    # import pip._vendor.requests.packages.chardet.eucjpprober 
    # import pip._vendor.requests.packages.chardet.euckrfreq 
    # import pip._vendor.requests.packages.chardet.euckrprober 
    # import pip._vendor.requests.packages.chardet.euctwfreq 
    # import pip._vendor.requests.packages.chardet.euctwprober 
    # import pip._vendor.requests.packages.chardet.gb2312freq 
    # import pip._vendor.requests.packages.chardet.gb2312prober 
    # import pip._vendor.requests.packages.chardet.hebrewprober 
    # import pip._vendor.requests.packages.chardet.jisfreq 
    # import pip._vendor.requests.packages.chardet.jpcntx 
    # import pip._vendor.requests.packages.chardet.langbulgarianmodel 
    # import pip._vendor.requests.packages.chardet.langcyrillicmodel 
    # import pip._vendor.requests.packages.chardet.langgreekmodel 
    # import pip._vendor.requests.packages.chardet.langhebrewmodel 
    # import pip._vendor.requests.packages.chardet.langhungarianmodel 
    # import pip._vendor.requests.packages.chardet.langthaimodel 
    # import pip._vendor.requests.packages.chardet.latin1prober 
    # import pip._vendor.requests.packages.chardet.mbcharsetprober 
    # import pip._vendor.requests.packages.chardet.mbcsgroupprober 
    # import pip._vendor.requests.packages.chardet.mbcssm 
    # import pip._vendor.requests.packages.chardet.sbcharsetprober 
    # import pip._vendor.requests.packages.chardet.sbcsgroupprober 
    # import pip._vendor.requests.packages.chardet.sjisprober 
    # import pip._vendor.requests.packages.chardet.universaldetector 
    # import pip._vendor.requests.packages.chardet.utf8prober 
    # import pip._vendor.requests.packages.urllib3
    # import pip._vendor.requests.packages.urllib3._collections 
    # import pip._vendor.requests.packages.urllib3.connection 
    # import pip._vendor.requests.packages.urllib3.connectionpool 
    # import pip._vendor.requests.packages.urllib3.contrib 
    # import pip._vendor.requests.packages.urllib3.contrib.appengine 
    # import pip._vendor.requests.packages.urllib3.contrib.ntlmpool
    # import pip._vendor.requests.packages.urllib3.contrib.pyopenssl 
    # import pip._vendor.requests.packages.urllib3.exceptions 
    # import pip._vendor.requests.packages.urllib3.fields 
    # import pip._vendor.requests.packages.urllib3.filepost 
    # import pip._vendor.requests.packages.urllib3.packages 
    # import pip._vendor.requests.packages.urllib3.packages.ordered_dict 
    # import pip._vendor.requests.packages.urllib3.packages.six
    # import pip._vendor.requests.packages.urllib3.packages.ssl_match_hostname 
    # import pip._vendor.requests.packages.urllib3.packages.ssl_match_hostname._implementation
    # import pip._vendor.requests.packages.urllib3.poolmanager 
    # import pip._vendor.requests.packages.urllib3.request 
    # import pip._vendor.requests.packages.urllib3.response 
    # import pip._vendor.requests.packages.urllib3.util 
    # import pip._vendor.requests.packages.urllib3.util.connection 
    # import pip._vendor.requests.packages.urllib3.util.request 
    # import pip._vendor.requests.packages.urllib3.util.response 
    # import pip._vendor.requests.packages.urllib3.util.retry 
    # import pip._vendor.requests.packages.urllib3.util.ssl_ 
    # import pip._vendor.requests.packages.urllib3.util.timeout 
    # import pip._vendor.requests.packages.urllib3.util.url 
    # import pip._vendor.requests.sessions
    # import pip._vendor.requests.status_codes 
    # import pip._vendor.requests.structures
    # import pip._vendor.requests.utils
    # import pip._vendor.retrying 
    # import pip._vendor.six
    # import pip.basecommand
    # import pip.baseparser
    # import pip.cmdoptions
    # import pip.commands
    # import pip.commands.completion 
    # import pip.commands.download 
    # import pip.commands.freeze 
    # import pip.commands.hash 
    # import pip.commands.help 
    # import pip.commands.install 
    # import pip.commands.list 
    # import pip.commands.search 
    # import pip.commands.show 
    # import pip.commands.uninstall 
    # import pip.commands.wheel 
    # import pip.compat
    # import pip.compat.dictconfig 
    # import pip.download 
    # import pip.exceptions
    # import pip.index
    # import pip.locations
    # import pip.models 
    # import pip.models.index 
    # import pip.operations 
    # import pip.operations.freeze 
    # import pip.pep425tags
    # import pip.req 
    # import pip.req.req_file
    # import pip.req.req_install 
    # import pip.req.req_set 
    # import pip.req.req_uninstall 
    # import pip.status_codes 
    # import pip.utils 
    # import pip.utils.appdirs
    # import pip.utils.build 
    # import pip.utils.deprecation
    # import pip.utils.filesystem 
    # import pip.utils.hashes 
    # import pip.utils.logging 
    # import pip.utils.outdated 
    # import pip.utils.setuptools_build 
    # import pip.utils.ui 
    # import pip.vcs
    # import pip.vcs.bazaar 
    # import pip.vcs.git 
    # import pip.vcs.mercurial 
    # import pip.vcs.subversion 
    # import pip.wheel
    # import pipes
    # import pkg_resources._vendor 
    # import pkg_resources._vendor.packaging 
    # import pkg_resources._vendor.packaging.__about__ 
    # import pkg_resources._vendor.packaging._compat 
    # import pkg_resources._vendor.packaging._structures 
    # import pkg_resources._vendor.packaging.specifiers 
    # import pkg_resources._vendor.packaging.version 
    # import pkgutil
    # import plistlib
    # import popen2
    # import poplib
    # import posixfile
    # import posixpath
    # import pprint
    # import profile
    # import pstats
    # import psutil._common
    # import psutil._compat
    # import psutil._psbsd
    # import psutil._pslinux
    # import psutil._psosx
    # import psutil._psposix
    # import psutil._pssunos
    # import psutil._psutil_windows 
    # import psutil._pswindows
    # import psutil.tests
    # import pty
    # import py2exe.boot_com_servers 
    # import py2exe.boot_common 
    # import py2exe.boot_ctypes_com_server 
    # import py2exe.boot_service 
    # import py2exe.build_exe 
    # import py2exe.mf
    # import py2exe.py2exe_util 
    # import py2exe.resources 
    # import py2exe.resources.StringTables 
    # import py2exe.resources.VersionInfo 
    # import py_compile
    # import pyclbr
    # import pydoc
    # import pydoc_data.topics 
    # import PyInstaller.__main__
    # import PyInstaller.archive 
    # import PyInstaller.archive.pyz_crypto 
    # import PyInstaller.archive.readers
    # import PyInstaller.archive.writers
    # import PyInstaller.building 
    # import PyInstaller.building.api
    # import PyInstaller.building.build_main
    # import PyInstaller.building.datastruct 
    # import PyInstaller.building.imphook
    # import PyInstaller.building.imphookapi
    # import PyInstaller.building.makespec
    # import PyInstaller.building.osx 
    # import PyInstaller.building.templates
    # import PyInstaller.building.toc_conversion 
    # import PyInstaller.building.utils 
    # import PyInstaller.compat
    # import PyInstaller.config
    # import PyInstaller.configure
    # import PyInstaller.depend 
    # import PyInstaller.depend.analysis
    # import PyInstaller.depend.bindepend
    # import PyInstaller.depend.dylib
    # import PyInstaller.depend.utils
    # import PyInstaller.hooks 
    # # import PyInstaller.hooks.hook-_mssql 
    # # import PyInstaller.hooks.hook-_mysql
    # # import PyInstaller.hooks.hook-_tkinter 
    # # import PyInstaller.hooks.hook-amazonproduct
    # # import PyInstaller.hooks.hook-astroid 
    # # import PyInstaller.hooks.hook-babel 
    # # import PyInstaller.hooks.hook-bacon 
    # # import PyInstaller.hooks.hook-boto 
    # # import PyInstaller.hooks.hook-boto3 
    # # import PyInstaller.hooks.hook-botocore 
    # # import PyInstaller.hooks.hook-certifi 
    # # import PyInstaller.hooks.hook-clr
    # # import PyInstaller.hooks.hook-countrycode 
    # # import PyInstaller.hooks.hook-cryptography
    # # import PyInstaller.hooks.hook-cv2 
    # # import PyInstaller.hooks.hook-cx_Oracle 
    # # import PyInstaller.hooks.hook-distorm3 
    # # import PyInstaller.hooks.hook-distutils
    # # import PyInstaller.hooks.hook-django 
    # # import PyInstaller.hooks.hook-docutils 
    # # import PyInstaller.hooks.hook-enchant
    # # import PyInstaller.hooks.hook-encodings 
    # # import PyInstaller.hooks.hook-gadfly 
    # # import PyInstaller.hooks.hook-gi
    # # import PyInstaller.hooks.hook-gtk 
    # # import PyInstaller.hooks.hook-h5py
    # # import PyInstaller.hooks.hook-httplib
    # # import PyInstaller.hooks.hook-httplib2 
    # # import PyInstaller.hooks.hook-idlelib 
    # # import PyInstaller.hooks.hook-IPython 
    # # import PyInstaller.hooks.hook-jinja2 
    # # import PyInstaller.hooks.hook-jsonschema 
    # # import PyInstaller.hooks.hook-kinterbasdb 
    # # import PyInstaller.hooks.hook-kivy 
    # # import PyInstaller.hooks.hook-lensfunpy 
    # # import PyInstaller.hooks.hook-logilab 
    # # import PyInstaller.hooks.hook-markdown 
    # # import PyInstaller.hooks.hook-matplotlib 
    # # import PyInstaller.hooks.hook-nacl 
    # # import PyInstaller.hooks.hook-names 
    # # import PyInstaller.hooks.hook-ncclient
    # # import PyInstaller.hooks.hook-netCDF4 
    # # import PyInstaller.hooks.hook-OpenGL
    # # import PyInstaller.hooks.hook-OpenGL_accelerate
    # # import PyInstaller.hooks.hook-osgeo 
    # # import PyInstaller.hooks.hook-patsy 
    # # import PyInstaller.hooks.hook-PIL 
    # # import PyInstaller.hooks.hook-pint 
    # # import PyInstaller.hooks.hook-pkg_resources 
    # # import PyInstaller.hooks.hook-psychopy 
    # # import PyInstaller.hooks.hook-psycopg2 
    # # import PyInstaller.hooks.hook-pycountry 
    # # import PyInstaller.hooks.hook-pycparser 
    # # import PyInstaller.hooks.hook-pydoc
    # # import PyInstaller.hooks.hook-pygame
    # # import PyInstaller.hooks.hook-pygments
    # # import PyInstaller.hooks.hook-pylint 
    # # import PyInstaller.hooks.hook-pyodbc 
    # # import PyInstaller.hooks.hook-PyQt4 
    # # import PyInstaller.hooks.hook-PyQt5 
    # # import PyInstaller.hooks.hook-PySide 
    # # import PyInstaller.hooks.hook-pythoncom
    # # import PyInstaller.hooks.hook-pyttsx
    # # import PyInstaller.hooks.hook-pytz 
    # # import PyInstaller.hooks.hook-pywintypes
    # # import PyInstaller.hooks.hook-raven 
    # # import PyInstaller.hooks.hook-rawpy 
    # # import PyInstaller.hooks.hook-regex 
    # # import PyInstaller.hooks.hook-requests 
    # # import PyInstaller.hooks.hook-selenium 
    # # import PyInstaller.hooks.hook-setuptools 
    # # import PyInstaller.hooks.hook-shelve 
    # # import PyInstaller.hooks.hook-speech_recognition 
    # # import PyInstaller.hooks.hook-sphinx 
    # # import PyInstaller.hooks.hook-sqlalchemy 
    # # import PyInstaller.hooks.hook-sqlite3 
    # # import PyInstaller.hooks.hook-sysconfig 
    # # import PyInstaller.hooks.hook-tables 
    # # import PyInstaller.hooks.hook-u1db
    # # import PyInstaller.hooks.hook-usb 
    # # import PyInstaller.hooks.hook-vtkpython 
    # # import PyInstaller.hooks.hook-weasyprint 
    # # import PyInstaller.hooks.hook-win32com 
    # # import PyInstaller.hooks.hook-Xlib 
    # # import PyInstaller.hooks.hook-xml 
    # # import PyInstaller.hooks.hook-zmq
    # # import PyInstaller.hooks.pre_find_module_path 
    # # import PyInstaller.hooks.pre_find_module_path.hook-distutils
    # # import PyInstaller.hooks.pre_find_module_path.hook-site
    # # import PyInstaller.hooks.pre_safe_import_module 
    # # import PyInstaller.hooks.pre_safe_import_module.hook-_xmlplus 
    # # import PyInstaller.hooks.pre_safe_import_module.hook-win32com
    # import PyInstaller.lib 
    # import PyInstaller.lib.altgraph 
    # import PyInstaller.lib.altgraph.Dot 
    # import PyInstaller.lib.altgraph.Graph
    # import PyInstaller.lib.altgraph.GraphAlgo 
    # import PyInstaller.lib.altgraph.GraphStat 
    # import PyInstaller.lib.altgraph.GraphUtil 
    # import PyInstaller.lib.altgraph.ObjectGraph
    # import PyInstaller.lib.macholib
    # import PyInstaller.lib.macholib.__main__ 
    # import PyInstaller.lib.macholib._cmdline
    # import PyInstaller.lib.macholib.dyld
    # import PyInstaller.lib.macholib.dylib
    # import PyInstaller.lib.macholib.framework
    # import PyInstaller.lib.macholib.itergraphreport
    # import PyInstaller.lib.macholib.mach_o
    # import PyInstaller.lib.macholib.MachO
    # import PyInstaller.lib.macholib.macho_dump 
    # import PyInstaller.lib.macholib.macho_find 
    # import PyInstaller.lib.macholib.macho_standalone 
    # import PyInstaller.lib.macholib.MachOGraph
    # import PyInstaller.lib.macholib.MachOStandalone 
    # import PyInstaller.lib.macholib.ptypes
    # import PyInstaller.lib.macholib.SymbolTable
    # import PyInstaller.lib.macholib.util 
    # import PyInstaller.lib.modulegraph 
    # import PyInstaller.lib.modulegraph.__main__ 
    # import PyInstaller.lib.modulegraph._compat 
    # import PyInstaller.lib.modulegraph.find_modules
    # import PyInstaller.lib.modulegraph.modulegraph
    # import PyInstaller.lib.modulegraph.util 
    # import PyInstaller.lib.modulegraph.zipio
    # import PyInstaller.lib.ordlookup 
    # import PyInstaller.lib.ordlookup.oleaut32 
    # import PyInstaller.lib.ordlookup.ws2_32 
    # import PyInstaller.lib.pefile
    # import PyInstaller.lib.pefile_py2
    # import PyInstaller.lib.pefile_py3
    # import PyInstaller.loader 
    # import PyInstaller.loader.pyiboot01_bootstrap 
    # import PyInstaller.loader.pyimod01_os_path
    # import PyInstaller.loader.pyimod02_archive 
    # import PyInstaller.loader.pyimod03_importers
    # import PyInstaller.loader.rthooks 
    # import PyInstaller.loader.rthooks.pyi_rth__tkinter 
    # import PyInstaller.loader.rthooks.pyi_rth_django 
    # import PyInstaller.loader.rthooks.pyi_rth_enchant 
    # import PyInstaller.loader.rthooks.pyi_rth_gdkpixbuf 
    # import PyInstaller.loader.rthooks.pyi_rth_gi 
    # import PyInstaller.loader.rthooks.pyi_rth_gio 
    # import PyInstaller.loader.rthooks.pyi_rth_glib 
    # import PyInstaller.loader.rthooks.pyi_rth_gstreamer 
    # import PyInstaller.loader.rthooks.pyi_rth_gtk 
    # import PyInstaller.loader.rthooks.pyi_rth_kivy 
    # import PyInstaller.loader.rthooks.pyi_rth_mplconfig 
    # import PyInstaller.loader.rthooks.pyi_rth_mpldata 
    # import PyInstaller.loader.rthooks.pyi_rth_osgeo 
    # import PyInstaller.loader.rthooks.pyi_rth_pkgres 
    # import PyInstaller.loader.rthooks.pyi_rth_qml 
    # import PyInstaller.loader.rthooks.pyi_rth_qt4plugins 
    # import PyInstaller.loader.rthooks.pyi_rth_qt5 
    # import PyInstaller.loader.rthooks.pyi_rth_qt5plugins 
    # import PyInstaller.loader.rthooks.pyi_rth_qt5webengine 
    # import PyInstaller.loader.rthooks.pyi_rth_twisted 
    # import PyInstaller.loader.rthooks.pyi_rth_usb 
    # import PyInstaller.loader.rthooks.pyi_rth_win32comgenpy 
    # import PyInstaller.log
    # import PyInstaller.utils 
    # import PyInstaller.utils._gitrevision 
    # import PyInstaller.utils.cliutils 
    # import PyInstaller.utils.cliutils.archive_viewer
    # import PyInstaller.utils.cliutils.bindepend
    # import PyInstaller.utils.cliutils.grab_version 
    # import PyInstaller.utils.cliutils.makespec
    # import PyInstaller.utils.cliutils.set_version 
    # import PyInstaller.utils.git
    # import PyInstaller.utils.hooks 
    # import PyInstaller.utils.hooks.subproc 
    # import PyInstaller.utils.hooks.subproc.django_import_finder
    # import PyInstaller.utils.misc
    # import PyInstaller.utils.osx
    # import PyInstaller.utils.release
    # import PyInstaller.utils.tests
    # import PyInstaller.utils.win32 
    # import PyInstaller.utils.win32.icon 
    # import PyInstaller.utils.win32.versioninfo 
    # import PyInstaller.utils.win32.winmanifest
    # import PyInstaller.utils.win32.winresource
    # import PyInstaller.utils.win32.winutils
    # import pywin.debugger 
    # import pywin.debugger.configui 
    # import pywin.debugger.dbgcon 
    # import pywin.debugger.dbgpyapp 
    # import pywin.debugger.debugger 
    # import pywin.debugger.fail 
    # import pywin.dialogs 
    # import pywin.dialogs.ideoptions 
    # import pywin.dialogs.list 
    # import pywin.dialogs.login 
    # import pywin.dialogs.status 
    # import pywin.docking 
    # import pywin.docking.DockingBar 
    # import pywin.framework 
    # import pywin.framework.app 
    # import pywin.framework.bitmap 
    # import pywin.framework.cmdline 
    # import pywin.framework.dbgcommands 
    # import pywin.framework.dlgappcore 
    # import pywin.framework.editor 
    # import pywin.framework.editor.color 
    # import pywin.framework.editor.color.coloreditor 
    # import pywin.framework.editor.configui 
    # import pywin.framework.editor.document 
    # import pywin.framework.editor.editor 
    # import pywin.framework.editor.frame 
    # import pywin.framework.editor.ModuleBrowser 
    # import pywin.framework.editor.template 
    # import pywin.framework.editor.vss 
    # import pywin.framework.help 
    # import pywin.framework.interact 
    # import pywin.framework.intpyapp 
    # import pywin.framework.intpydde 
    # import pywin.framework.mdi_pychecker 
    # import pywin.framework.scriptutils
    # import pywin.framework.sgrepmdi 
    # import pywin.framework.startup 
    # import pywin.framework.stdin
    # import pywin.framework.toolmenu 
    # import pywin.framework.window 
    # import pywin.framework.winout 
    # import pywin.idle 
    # import pywin.idle.AutoExpand 
    # import pywin.idle.AutoIndent 
    # import pywin.idle.CallTips 
    # import pywin.idle.FormatParagraph 
    # import pywin.idle.IdleHistory 
    # import pywin.idle.PyParse 
    # import pywin.mfc 
    # import pywin.mfc.activex
    # import pywin.mfc.afxres 
    # import pywin.mfc.dialog
    # import pywin.mfc.docview 
    # import pywin.mfc.object 
    # import pywin.mfc.thread 
    # import pywin.mfc.window 
    # import pywin.scintilla 
    # import pywin.scintilla.bindings 
    # import pywin.scintilla.config 
    # import pywin.scintilla.configui 
    # import pywin.scintilla.control 
    # import pywin.scintilla.document 
    # import pywin.scintilla.find 
    # import pywin.scintilla.formatter 
    # import pywin.scintilla.IDLEenvironment 
    # import pywin.scintilla.keycodes 
    # import pywin.scintilla.scintillacon 
    # import pywin.scintilla.view 
    # import pywin.tools 
    # import pywin.tools.browseProjects 
    # import pywin.tools.browser 
    # import pywin.tools.hierlist 
    # import pywin.tools.regedit 
    # import pywin.tools.regpy 
    # import pywin.tools.TraceCollector 
    # import Queue
    # import quopri
    # import random
    # import re
    # import repr
    # import rexec
    # import rfc822
    # import rlcompleter
    # import robotparser
    # import runpy
    # import sched
    # import sets
    # import sgmllib
    # import shelve
    # import shlex
    # import shutil
    # import signal
    # import SimpleDialog
    # import SimpleHTTPServer
    # import SimpleXMLRPCServer
    # import site
    # import smtpd
    # import sndhdr
    # import socket
    # import SocketServer
    # import sqlite3.dbapi2 
    # import sqlite3.dump 
    # import sqlite3.test 
    # import sqlite3.test.dbapi 
    # import sqlite3.test.dump 
    # import sqlite3.test.factory 
    # import sqlite3.test.hooks 
    # import sqlite3.test.py25tests 
    # import sqlite3.test.regression 
    # import sqlite3.test.transactions 
    # import sqlite3.test.types 
    # import sqlite3.test.userfunctions 
    # import sre
    # import ssl
    # import sspi
    # import stat
    # import statvfs
    # import string
    # import StringIO
    # import stringold
    # import stringprep
    # import strop
    # import sunau
    # import sunaudio
    # import symbol
    # import sysconfig
    # import tabnanny
    # import tarfile
    # import telnetlib
    # import tempfile
    # # import test._mock_backport 
    # # import test.audiotests 
    # # import test.autotest 
    # # import test.bad_coding 
    # # import test.bad_coding2 
    # # import test.bad_coding3 
    # # import test.badsyntax_future3
    # # import test.badsyntax_future4
    # # import test.badsyntax_future5
    # # import test.badsyntax_future6
    # # import test.badsyntax_future7
    # # import test.badsyntax_future8
    # # import test.badsyntax_future9
    # # import test.badsyntax_nocaret 
    # # import test.buffer_tests 
    # # import test.curses_tests 
    # # import test.doctest_aliases 
    # # import test.double_const 
    # # import test.fork_wait
    # # import test.gdb_sample 
    # # import test.infinite_reload 
    # # import test.inspect_fodder 
    # # import test.inspect_fodder2 
    # # import test.leakers 
    # # import test.leakers.test_ctypes 
    # # import test.leakers.test_dictself 
    # # import test.leakers.test_gestalt 
    # # import test.leakers.test_selftype 
    # # import test.list_tests
    # # import test.lock_tests
    # # import test.make_ssl_certs
    # # import test.mapping_tests 
    # # import test.mp_fork_bomb 
    # # import test.outstanding_bugs 
    # # import test.pickletester 
    # # import test.profilee
    # # import test.pyclbr_input
    # # import test.pydoc_mod
    # # import test.pydocfodder
    # # import test.pystone
    # # import test.re_tests 
    # # import test.regrtest
    # # import test.relimport 
    # # import test.reperf 
    # # import test.sample_doctest
    # # import test.sample_doctest_no_docstrings 
    # # import test.sample_doctest_no_doctests
    # # import test.script_helper 
    # # import test.seq_tests
    # # import test.sortperf
    # # import test.ssl_servers 
    # # import test.string_tests
    # # import test.symlink_support 
    # # import test.test___all__ 
    # # import test.test___future__ 
    # # import test.test__locale 
    # # import test.test__osx_support
    # # import test.test_abc
    # # import test.test_abstract_numbers
    # # import test.test_aepack 
    # # import test.test_aifc 
    # # import test.test_al
    # # import test.test_anydbm
    # # import test.test_applesingle 
    # # import test.test_argparse 
    # # import test.test_array
    # # import test.test_ascii_formatd 
    # # import test.test_ast 
    # # import test.test_asynchat 
    # # import test.test_asyncore 
    # # import test.test_atexit 
    # # import test.test_audioop 
    # # import test.test_augassign 
    # # import test.test_base64 
    # # import test.test_bastion 
    # # import test.test_bigaddrspace 
    # # import test.test_bigmem 
    # # import test.test_binascii
    # # import test.test_binhex
    # # import test.test_binop
    # # import test.test_bisect 
    # # import test.test_bool 
    # # import test.test_bsddb
    # # import test.test_bsddb185
    # # import test.test_bsddb3
    # # import test.test_buffer
    # # import test.test_bufio 
    # # import test.test_builtin 
    # # import test.test_bytes
    # # import test.test_bz2 
    # # import test.test_calendar 
    # # import test.test_call 
    # # import test.test_capi 
    # # import test.test_cd
    # # import test.test_cfgparser 
    # # import test.test_cgi 
    # # import test.test_charmapcodec
    # # import test.test_cl
    # # import test.test_class 
    # # import test.test_cmath 
    # # import test.test_cmd
    # # import test.test_cmd_line 
    # # import test.test_cmd_line_script 
    # # import test.test_code
    # # import test.test_codeccallbacks 
    # # import test.test_codecencodings_cn 
    # # import test.test_codecencodings_hk 
    # # import test.test_codecencodings_iso2022 
    # # import test.test_codecencodings_jp 
    # # import test.test_codecencodings_kr 
    # # import test.test_codecencodings_tw 
    # # import test.test_codecmaps_cn 
    # # import test.test_codecmaps_hk 
    # # import test.test_codecmaps_jp 
    # # import test.test_codecmaps_kr 
    # # import test.test_codecmaps_tw 
    # # import test.test_codecs 
    # # import test.test_codeop
    # # import test.test_coding 
    # # import test.test_coercion 
    # # import test.test_collections 
    # # import test.test_colorsys 
    # # import test.test_commands 
    # # import test.test_compare 
    # # import test.test_compile 
    # # import test.test_compileall 
    # # import test.test_compiler 
    # # import test.test_complex 
    # # import test.test_complex_args 
    # # import test.test_contains 
    # # import test.test_contextlib
    # # import test.test_cookie 
    # # import test.test_cookielib
    # # import test.test_copy
    # # import test.test_copy_reg 
    # # import test.test_cpickle 
    # # import test.test_cprofile
    # # import test.test_crypt 
    # # import test.test_csv 
    # # import test.test_ctypes 
    # # import test.test_curses 
    # # import test.test_datetime
    # # import test.test_dbm 
    # # import test.test_decimal
    # # import test.test_decorators 
    # # import test.test_defaultdict
    # # import test.test_deque 
    # # import test.test_descr 
    # # import test.test_descrtut 
    # # import test.test_dict 
    # # import test.test_dictcomps 
    # # import test.test_dictviews 
    # # import test.test_difflib 
    # # import test.test_dircache
    # # import test.test_dis 
    # # import test.test_distutils
    # # import test.test_dl
    # # import test.test_doctest
    # # import test.test_doctest2 
    # # import test.test_docxmlrpc 
    # # import test.test_dumbdbm
    # # import test.test_dummy_thread
    # # import test.test_dummy_threading 
    # # import test.test_email 
    # # import test.test_email_codecs 
    # # import test.test_email_renamed 
    # # import test.test_ensurepip 
    # # import test.test_enumerate 
    # # import test.test_eof
    # # import test.test_epoll
    # # import test.test_errno
    # # import test.test_exception_variations 
    # # import test.test_exceptions 
    # # import test.test_extcall
    # # import test.test_fcntl
    # # import test.test_file 
    # # import test.test_file2k 
    # # import test.test_file_eintr 
    # # import test.test_filecmp 
    # # import test.test_fileinput 
    # # import test.test_fileio 
    # # import test.test_float 
    # # import test.test_fnmatch
    # # import test.test_fork1
    # # import test.test_format 
    # # import test.test_fpformat 
    # # import test.test_fractions
    # # import test.test_frozen 
    # # import test.test_ftplib
    # # import test.test_funcattrs 
    # # import test.test_functools 
    # # import test.test_future 
    # # import test.test_future1
    # # import test.test_future2
    # # import test.test_future3 
    # # import test.test_future4 
    # # import test.test_future5 
    # # import test.test_future_builtins 
    # # import test.test_gc 
    # # import test.test_gdb 
    # # import test.test_gdbm 
    # # import test.test_generators 
    # # import test.test_genericpath
    # # import test.test_genexps 
    # # import test.test_getargs
    # # import test.test_getargs2 
    # # import test.test_getopt 
    # # import test.test_gettext 
    # # import test.test_gl
    # # import test.test_glob 
    # # import test.test_global
    # # import test.test_grammar 
    # # import test.test_grp
    # # import test.test_gzip
    # # import test.test_hash 
    # # import test.test_hashlib 
    # # import test.test_heapq
    # # import test.test_hmac 
    # # import test.test_hotshot 
    # # import test.test_htmllib 
    # # import test.test_htmlparser
    # # import test.test_httplib 
    # # import test.test_httpservers
    # # import test.test_idle 
    # # import test.test_imageop
    # # import test.test_imaplib 
    # # import test.test_imgfile
    # # import test.test_imghdr 
    # # import test.test_imp 
    # # import test.test_import 
    # # import test.test_importhooks 
    # # import test.test_importlib 
    # # import test.test_index 
    # # import test.test_inspect 
    # # import test.test_int 
    # # import test.test_int_literal
    # # import test.test_io
    # # import test.test_ioctl 
    # # import test.test_isinstance 
    # # import test.test_iter 
    # # import test.test_iterlen
    # # import test.test_itertools 
    # # import test.test_json
    # # import test.test_kqueue
    # # import test.test_largefile
    # # import test.test_lib2to3 
    # # import test.test_linecache
    # # import test.test_linuxaudiodev 
    # # import test.test_list 
    # # import test.test_locale 
    # # import test.test_logging
    # # import test.test_long 
    # # import test.test_long_future 
    # # import test.test_longexp 
    # # import test.test_macos 
    # # import test.test_macostools 
    # # import test.test_macpath 
    # # import test.test_macurl2path 
    # # import test.test_mailbox 
    # # import test.test_marshal 
    # # import test.test_math 
    # # import test.test_md5 
    # # import test.test_memoryio
    # # import test.test_memoryview
    # # import test.test_mhlib
    # # import test.test_mimetools 
    # # import test.test_mimetypes 
    # # import test.test_MimeWriter
    # # import test.test_minidom 
    # # import test.test_mmap 
    # # import test.test_module 
    # # import test.test_modulefinder 
    # # import test.test_msilib
    # # import test.test_multibytecodec 
    # # import test.test_multibytecodec_support 
    # # import test.test_multifile 
    # # import test.test_multiprocessing 
    # # import test.test_mutants 
    # # import test.test_mutex 
    # # import test.test_netrc 
    # # import test.test_new 
    # # import test.test_nis 
    # # import test.test_nntplib 
    # # import test.test_normalization 
    # # import test.test_ntpath 
    # # import test.test_old_mailbox 
    # # import test.test_opcodes 
    # # import test.test_openpty 
    # # import test.test_operator 
    # # import test.test_optparse 
    # # import test.test_os 
    # # import test.test_ossaudiodev 
    # # import test.test_parser 
    # # import test.test_pdb 
    # # import test.test_peepholer 
    # # import test.test_pep247
    # # import test.test_pep263 
    # # import test.test_pep277 
    # # import test.test_pep292 
    # # import test.test_pep352 
    # # import test.test_pickle 
    # # import test.test_pickletools 
    # # import test.test_pipes 
    # # import test.test_pkg 
    # # import test.test_pkgimport 
    # # import test.test_pkgutil 
    # # import test.test_platform 
    # # import test.test_plistlib 
    # # import test.test_poll 
    # # import test.test_popen
    # # import test.test_popen2
    # # import test.test_poplib
    # # import test.test_posix 
    # # import test.test_posixpath 
    # # import test.test_pow 
    # # import test.test_pprint 
    # # import test.test_print
    # # import test.test_profile
    # # import test.test_property 
    # # import test.test_pstats 
    # # import test.test_pty 
    # # import test.test_pwd 
    # # import test.test_py3kwarn 
    # # import test.test_py_compile 
    # # import test.test_pyclbr 
    # # import test.test_pydoc 
    # # import test.test_pyexpat 
    # # import test.test_queue 
    # # import test.test_quopri 
    # # import test.test_random 
    # # import test.test_re 
    # # import test.test_readline
    # # import test.test_repr
    # # import test.test_resource 
    # # import test.test_rfc822 
    # # import test.test_richcmp 
    # # import test.test_rlcompleter 
    # # import test.test_robotparser 
    # # import test.test_runpy 
    # # import test.test_sax 
    # # import test.test_scope 
    # # import test.test_scriptpackages 
    # # import test.test_select 
    # # import test.test_set 
    # # import test.test_setcomps 
    # # import test.test_sets 
    # # import test.test_sgmllib 
    # # import test.test_sha 
    # # import test.test_shelve 
    # # import test.test_shlex 
    # # import test.test_shutil 
    # # import test.test_signal 
    # # import test.test_SimpleHTTPServer
    # # import test.test_site
    # # import test.test_slice 
    # # import test.test_smtplib 
    # # import test.test_smtpnet 
    # # import test.test_socket 
    # # import test.test_socketserver
    # # import test.test_softspace 
    # # import test.test_sort 
    # # import test.test_spwd 
    # # import test.test_sqlite 
    # # import test.test_ssl 
    # # import test.test_startfile 
    # # import test.test_stat 
    # # import test.test_str 
    # # import test.test_strftime
    # # import test.test_string 
    # # import test.test_StringIO 
    # # import test.test_stringprep 
    # # import test.test_strop 
    # # import test.test_strptime
    # # import test.test_strtod 
    # # import test.test_struct 
    # # import test.test_structmembers 
    # # import test.test_structseq 
    # # import test.test_subprocess 
    # # import test.test_sunau 
    # # import test.test_sunaudiodev 
    # # import test.test_sundry
    # # import test.test_support
    # # import test.test_symtable
    # # import test.test_syntax
    # # import test.test_sys 
    # # import test.test_sys_setprofile 
    # # import test.test_sys_settrace 
    # # import test.test_sysconfig
    # # import test.test_tarfile 
    # # import test.test_tcl 
    # # import test.test_telnetlib 
    # # import test.test_tempfile 
    # # import test.test_textwrap 
    # # import test.test_thread 
    # # import test.test_threaded_import 
    # # import test.test_threadedtempfile
    # # import test.test_threading 
    # # import test.test_threading_local 
    # # import test.test_threadsignals
    # # import test.test_time 
    # # import test.test_timeit 
    # # import test.test_timeout
    # # import test.test_tk 
    # # import test.test_tokenize 
    # # import test.test_tools
    # # import test.test_trace 
    # # import test.test_traceback
    # # import test.test_transformer 
    # # import test.test_ttk_guionly 
    # # import test.test_ttk_textonly 
    # # import test.test_tuple 
    # # import test.test_typechecks
    # # import test.test_types 
    # # import test.test_ucn
    # # import test.test_unary
    # # import test.test_undocumented_details 
    # # import test.test_unicode
    # # import test.test_unicode_file 
    # # import test.test_unicodedata
    # # import test.test_unittest 
    # # import test.test_univnewlines 
    # # import test.test_univnewlines2k 
    # # import test.test_unpack 
    # # import test.test_urllib
    # # import test.test_urllib2 
    # # import test.test_urllib2_localnet 
    # # import test.test_urllib2net 
    # # import test.test_urllibnet 
    # # import test.test_urlparse 
    # # import test.test_userdict 
    # # import test.test_userlist 
    # # import test.test_userstring 
    # # import test.test_uu
    # # import test.test_uuid 
    # # import test.test_wait3
    # # import test.test_wait4
    # # import test.test_warnings 
    # # import test.test_wave 
    # # import test.test_weakref 
    # # import test.test_weakset 
    # # import test.test_whichdb
    # # import test.test_winreg 
    # # import test.test_winsound 
    # # import test.test_with
    # # import test.test_wsgiref 
    # # import test.test_xdrlib 
    # # import test.test_xml_etree 
    # # import test.test_xml_etree_c 
    # # import test.test_xmllib 
    # # import test.test_xmlrpc 
    # # import test.test_xpickle 
    # # import test.test_xrange 
    # # import test.test_zipfile 
    # # import test.test_zipfile64 
    # # import test.test_zipimport 
    # # import test.test_zipimport_support 
    # # import test.test_zlib 
    # # import test.testall 
    # # import test.testcodec
    # # import test.tf_inherit_check 
    # # import test.threaded_import_hangers 
    # # import test.time_hashlib 
    # # import test.tracedmodules
    # # import test.tracedmodules.testmod 
    # # import test.warning_tests 
    # # import test.win_console_handler
    # # import test.xmltests 
    # import textwrap
    # import thread
    # import threading
    # import time
    # import timeit
    # import Tkdnd
    # import Tkinter
    # import toaiff
    # import token
    # import tokenize
    # import traceback
    # import ttk
    # import tty
    # import types
    # import unittest.__main__
    # import unittest.case
    # import unittest.loader
    # import unittest.main
    # import unittest.result
    # import unittest.runner
    # import unittest.signals 
    # import unittest.suite
    # import unittest.test 
    # import unittest.test.dummy 
    # import unittest.test.support 
    # import unittest.test.test_assertions 
    # import unittest.test.test_break 
    # import unittest.test.test_case 
    # import unittest.test.test_discovery 
    # import unittest.test.test_functiontestcase 
    # import unittest.test.test_loader 
    # import unittest.test.test_program 
    # import unittest.test.test_result 
    # import unittest.test.test_runner 
    # import unittest.test.test_setups 
    # import unittest.test.test_skipping 
    # import unittest.test.test_suite 
    # import unittest.util
    # import urllib
    # import urlparse
    # import user
    # import UserDict
    # import UserList
    # import uu
    # import uuid
    # import warnings
    # import wave
    # import weakref
    # import webbrowser
    # import whichdb
    # import win32com.adsi 
    # import win32com.adsi.adsi 
    # import win32com.adsi.adsicon 
    # import win32com.authorization 
    # import win32com.authorization.authorization 
    # import win32com.axcontrol 
    # import win32com.axcontrol.axcontrol 
    # import win32com.axdebug 
    # import win32com.axdebug.adb
    # import win32com.axdebug.axdebug 
    # import win32com.axdebug.codecontainer
    # import win32com.axdebug.contexts
    # import win32com.axdebug.debugger 
    # import win32com.axdebug.documents
    # import win32com.axdebug.dump 
    # import win32com.axdebug.expressions 
    # import win32com.axdebug.gateways 
    # import win32com.axdebug.stackframe
    # import win32com.axdebug.util 
    # import win32com.axscript 
    # import win32com.axscript.asputil
    # import win32com.axscript.axscript 
    # import win32com.axscript.client 
    # import win32com.axscript.client.debug 
    # import win32com.axscript.client.error
    # import win32com.axscript.client.framework
    # import win32com.axscript.client.pydumper 
    # import win32com.axscript.client.pyscript
    # import win32com.axscript.client.pyscript_rexec 
    # import win32com.axscript.client.scriptdispatch
    # import win32com.axscript.server 
    # import win32com.axscript.server.axsite 
    # import win32com.axscript.server.error
    # import win32com.bits 
    # import win32com.bits.bits 
    # import win32com.client 
    # import win32com.client.build
    # import win32com.client.CLSIDToClass
    # import win32com.client.combrowse
    # import win32com.client.connect
    # import win32com.client.dynamic
    # import win32com.client.gencache
    # import win32com.client.genpy
    # import win32com.client.makepy
    # import win32com.client.selecttlb
    # import win32com.client.tlbrowse 
    # import win32com.client.util
    # import win32com.demos 
    # import win32com.demos.connect 
    # import win32com.demos.dump_clipboard 
    # import win32com.demos.eventsApartmentThreaded 
    # import win32com.demos.eventsFreeThreaded 
    # import win32com.demos.excelAddin 
    # import win32com.demos.excelRTDServer
    # import win32com.demos.iebutton
    # import win32com.demos.ietoolbar
    # import win32com.demos.outlookAddin 
    # import win32com.demos.trybag 
    # import win32com.directsound 
    # import win32com.directsound.test 
    # import win32com.directsound.test.ds_record 
    # import win32com.directsound.test.ds_test 
    # import win32com.ifilter 
    # import win32com.ifilter.ifilter 
    # import win32com.ifilter.ifiltercon 
    # import win32com.internet 
    # import win32com.internet.inetcon 
    # import win32com.internet.internet 
    # import win32com.makegw 
    # import win32com.makegw.makegw
    # import win32com.makegw.makegwenum
    # import win32com.makegw.makegwparse
    # import win32com.mapi 
    # import win32com.mapi.emsabtags 
    # import win32com.mapi.mapi 
    # import win32com.mapi.mapitags 
    # import win32com.mapi.mapiutil 
    # import win32com.olectl
    # import win32com.propsys 
    # import win32com.propsys.propsys 
    # import win32com.propsys.pscon 
    # import win32com.server 
    # import win32com.server.connect
    # import win32com.server.dispatcher
    # import win32com.server.exception
    # import win32com.server.factory 
    # import win32com.server.localserver 
    # import win32com.server.policy
    # import win32com.server.register
    # import win32com.server.util
    # import win32com.servers 
    # import win32com.servers.dictionary
    # import win32com.servers.interp
    # import win32com.servers.perfmon
    # import win32com.servers.PythonTools 
    # import win32com.servers.test_pycomtest 
    # import win32com.shell 
    # import win32com.shell.shell 
    # import win32com.shell.shellcon 
    # import win32com.storagecon
    # import win32com.taskscheduler 
    # import win32com.taskscheduler.taskscheduler 
    # import win32com.test 
    # import win32com.test.daodump 
    # import win32com.test.errorSemantics 
    # import win32com.test.GenTestScripts 
    # import win32com.test.pippo_server 
    # import win32com.test.policySemantics 
    # import win32com.test.testAccess 
    # import win32com.test.testADOEvents 
    # import win32com.test.testall 
    # import win32com.test.testArrays 
    # import win32com.test.testAXScript 
    # import win32com.test.testClipboard 
    # import win32com.test.testCollections 
    # import win32com.test.testDCOM 
    # import win32com.test.testDictionary 
    # import win32com.test.testDynamic 
    # import win32com.test.testExchange 
    # import win32com.test.testExplorer 
    # import win32com.test.testGatewayAddresses 
    # import win32com.test.testGIT
    # import win32com.test.testIterators 
    # import win32com.test.testmakepy 
    # import win32com.test.testMarshal
    # import win32com.test.testMSOffice 
    # import win32com.test.testMSOfficeEvents 
    # import win32com.test.testNetscape 
    # import win32com.test.testPersist 
    # import win32com.test.testPippo 
    # import win32com.test.testPyComTest 
    # import win32com.test.testROT 
    # import win32com.test.testServers 
    # import win32com.test.testShell 
    # import win32com.test.testStorage 
    # import win32com.test.testStreams 
    # import win32com.test.testvb 
    # import win32com.test.testvbscript_regexp 
    # import win32com.test.testWMI 
    # import win32com.test.testxslt 
    # import win32com.test.util 
    # import win32com.universal 
    # import win32com.util
    # import win32evtlogutil
    # import win32rcparser
    # import win32verstamp
    # import winxptheme
    # import wsgiref.handlers
    # import wsgiref.headers
    # import wsgiref.simple_server
    # import wsgiref.util
    # import wsgiref.validate
    # import xdrlib
    # import xml
    # import xml.dom
    # import xml.dom.domreg
    # import xml.dom.expatbuilder
    # import xml.dom.minicompat
    # import xml.dom.minidom
    # import xml.dom.NodeFilter 
    # import xml.dom.pulldom 
    # import xml.dom.xmlbuilder
    # import xml.etree 
    # import xml.etree.cElementTree 
    # import xml.etree.ElementInclude 
    # import xml.etree.ElementPath 
    # import xml.etree.ElementTree 
    # import xml.parsers
    # import xml.parsers.expat
    # import xml.sax
    # import xml.sax._exceptions
    # import xml.sax.expatreader
    # import xml.sax.handler
    # import xml.sax.saxutils
    # import xml.sax.xmlreader
    # import xmllib
    # import xmlrpclib
    # import xxsubtype
    # import zipfile
    # import zipimport

def alternate_raw_input(prompt=None):
    """Write the prompt to stderr, then call raw_input without a prompt.
     This is to try to mimic better what the python executable does.
    Enter: prompt: prompt to print to stderr."""
    if prompt and len(prompt):
        sys.stderr.write(prompt)
        sys.stderr.flush()
    return raw_input("")


if hasattr(sys, "frozen"):
    delattr(sys, "frozen")
Help = False
DirectCmd = None
ImportSite = True
Interactive = "check"
RunModule = False
ShowVersion = False
SkipFirstLine = False
Start = None
Unbuffered = False
UseEnvironment = True
skip = 0
for i in xrange(1, len(sys.argv)):
    if DirectCmd is not None:
        break
    if skip:
        skip -= 1
        continue
    arg = sys.argv[i]
    if arg.startswith("-") and arg[1:2] != "-":
        for let in arg[1:]:
            if let == "c":
                DirectCmd = " ".join(sys.argv[i+1+skip:])
                DirectCmd = sys.argv[i+1+skip:]
            elif let == "E":
                UseEnvironment = False
            elif let == "i":
                Interactive = True
            elif let == "m" and i+1 < len(sys.argv):
                RunModule = sys.argv[i+1]
                skip = 1
            elif let == "S":
                ImportSite = False
            elif let == "u":
                Unbuffered = True
            elif let == "V":
                ShowVersion = True
            elif let == "x":
                SkipFirstLine = True
            elif let in ("E", "O"):
                # ignore these options
                pass
            else:
                Help = True
    elif arg == "--all":
        continue
    elif arg == "--help" or arg == "-h" or arg == "/?":
        Help = True
    elif arg == "--multiprocessing-fork":
        skip = 1
        import multiprocessing.forking
        multiprocessing.forking.freeze_support()
    elif arg == "--version":
        ShowVersion = True
    elif arg.startswith("-"):
        Help = True
    elif not Start:
        Start = i
        break
if Help:
    print """Stand-Alone Python Interpreter

Syntax: py.exe [--all] [--help] [-c (cmd) | -m (module) | (python file) [arg]]
                    [-i] [-S] [-u] [-V] [-x]
                    [--multiprocessing-fork (handle)]

--all attempts to import all modules.
-c runs the remaining options as a program.
-E ignores environment variables.
-i forces a prompt even if stdin does not appear to be a terminal; also
  PYTHONINSPECT=x
--help, -h, or /? prints this message.
-m runs the specified python module.
--multiprocessing-fork supports the multiprocessing module.
-S supresses importing the site module
-u runs in unbuffered mode; also PYTHONUNBUFFERED=x
-V prints the version and exits (--version also works).
-x skips the first line of a source file.
If no file is specified and stdin is a terminal, the interactive interpreter is
  started."""
    # print sys.argv, repr(sys.argv)
    sys.exit(0)
if ShowVersion:
    from py_version import Version, Description
    print "%s, Version %s" % (Description, Version)
    sys.exit(0)
if Interactive == "check" and UseEnvironment:
    if os.environ.get("PYTHONINSPECT"):
        Interactive = True
if Unbuffered is False and UseEnvironment:
    if os.environ.get("PYTHONUNBUFFERED"):
        Unbuffered = True
if Unbuffered:
    sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 0)
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', 0)
if ImportSite:
    import site
# Generate the globals/locals environment
globenv = {}
for key in globals().keys():
    if key.startswith("_"):  # or key=="AllModules":
        globenv[key] = globals()[key]
if Start:
    sys.argv = sys.argv[Start:]
    __name__ = "__main__"
    __file__ = sys.argv[0]
    sys.path[0:0] = [os.path.split(__file__)[0]]
    # If I try to use the simplified global dictionary, multiprocessing doesn't
    # work.
    if not SkipFirstLine:
        #execfile(sys.argv[0], globenv)
        execfile(sys.argv[0])
    else:
        fptr = open(sys.argv[0])
        discard = fptr.readline()
        src = fptr.read()
        fptr.close()
        # exec src in globenv
        # exec src
elif RunModule:
    import runpy
    runpy.run_module(RunModule, run_name='__main__')
elif DirectCmd:
    sys.path[0:0] = [""]
    sys.argv = DirectCmd
    exec DirectCmd[0] in globenv
else:
    if Interactive == "check":
        Interactive = sys.stdin.isatty()
    sys.path[0:0] = [""]
    if Interactive:
        import code
        cons = code.InteractiveConsole(locals=globenv)
        if not sys.stdout.isatty():
            cons.raw_input = alternate_raw_input
            if not Unbuffered:
                sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
                sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', 0)
        cons.interact()
    elif False:
        # This will run code as it comes it, rather than wait until it has parsed
        # it all; it doesn't seem to be what the main python interpreter ever
        # does, however.
        import code
        interp = code.InteractiveInterpreter(locals=globenv)
        src = []
        for line in sys.stdin:
            if not len(line.rstrip("\r\n")):
                continue
            if line.startswith("#"):
                continue
            if line.rstrip("\r\n")[0:1] not in (" ", "\t"):
                if len(src):
                    interp.runsource("".join(src), "<stdin>")
                    src = []
            src.append(line)
        if len(src):
            interp.runsource("".join(src))
    else:
        src = sys.stdin.read()
        # This doesn't work the way I expect for some reason
        #interp = code.InteractiveInterpreter(locals=globenv)
        #interp.runsource(src, "<stdin>")
        # But an exec works fine
        exec src in globenv
