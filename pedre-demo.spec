# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller spec file for pedre-demo game.

Builds standalone executables for Linux, Windows, and macOS.
"""

import os
import sys
from pathlib import Path

block_cipher = None

# Get the project root directory
project_root = Path(SPECPATH)

# Collect all asset files
assets_datas = []
asset_path = project_root / 'assets'

if asset_path.exists():
    for root, dirs, files in os.walk(asset_path):
        for file in files:
            src = os.path.join(root, file)
            # Calculate destination path relative to project root
            rel_path = os.path.relpath(root, project_root)
            assets_datas.append((src, rel_path))

# Include settings.py if it exists
settings_file = project_root / 'settings.py'
if settings_file.exists():
    assets_datas.append((str(settings_file), '.'))

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=assets_datas,
    hiddenimports=[
        'pedre',
        'arcade',
        'pyglet',
        'PIL',
        'pytiled_parser',
        # Pedre plugins (dynamically imported, must be explicit)
        'pedre.plugins.audio',
        'pedre.plugins.audio.actions',
        'pedre.plugins.cache',
        'pedre.plugins.camera',
        'pedre.plugins.camera.actions',
        'pedre.plugins.debug',
        'pedre.plugins.dialog',
        'pedre.plugins.dialog.actions',
        'pedre.plugins.dialog.events',
        'pedre.plugins.pause_menu',
        'pedre.plugins.input',
        'pedre.plugins.interaction',
        'pedre.plugins.interaction.events',
        'pedre.plugins.interaction.conditions',
        'pedre.plugins.inventory',
        'pedre.plugins.inventory.actions',
        'pedre.plugins.inventory.events',
        'pedre.plugins.inventory.conditions',
        'pedre.plugins.npc',
        'pedre.plugins.npc.actions',
        'pedre.plugins.npc.events',
        'pedre.plugins.npc.conditions',
        'pedre.plugins.particle',
        'pedre.plugins.particle.actions',
        'pedre.plugins.pathfinding',
        'pedre.plugins.portal',
        'pedre.plugins.portal.events',
        'pedre.plugins.save',
        'pedre.plugins.script',
        'pedre.plugins.script.events',
        'pedre.plugins.script.conditions',
        'pedre.plugins.waypoint',
        'pedre.plugins.player',
        'pedre.plugins.physics',
        'pedre.plugins.scene',
        'pedre.plugins.scene.actions',
        'pedre.plugins.scene.events',
    ],
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
    [],
    exclude_binaries=True,
    name='pedre-demo',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Windowed app (no console)
    disable_windowing_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # TODO: Add icon (Windows: .ico, macOS: .icns)
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='pedre-demo',
)

# macOS .app bundle
if sys.platform == 'darwin':
    app = BUNDLE(
        coll,
        name='pedre-demo.app',
        icon=None,  # TODO: Add icon path: 'assets/icon.icns'
        bundle_identifier='com.pedre.demo',
        info_plist={
            'NSPrincipalClass': 'NSApplication',
            'NSHighResolutionCapable': 'True',
        },
    )
