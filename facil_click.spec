# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['facil_click.py'],
    pathex=[],
    binaries=[],
    datas=[('google_icon.gif', '.'), ('whats.gif', '.'), ('face.gif', '.'), ('insta_icon.gif', '.'), ('cnn_icon.gif', '.'), ('youtube_icon.gif', '.'), ('netflix_icon.gif', '.'), ('gmail_icon.gif', '.'), ('calc_icon.gif', '.'), ('notepad_icon.gif', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='facil_click',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
