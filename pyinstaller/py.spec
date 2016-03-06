# -*- mode: python -*-

block_cipher = None


a = Analysis(['py.py'],
             pathex=['C:\\Users\\oglop\\Downloads\\pyexe-src-2.7.9.10\\cxfreeze'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='py',
          debug=False,
          strip=False,
          upx=True,
          console=True )
