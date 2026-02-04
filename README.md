# A work in progress demo for Pedre

## Install dependencies

```bash
uv sync
```

## Run the game

```bash
uv run python main.py
```

## Building Installers

This project includes PyInstaller configuration for creating standalone executables.

### Build locally

1. Install dev dependencies:

   ```bash
   uv sync --extra dev
   ```

2. Build the executable:

   ```bash
   uv run pyinstaller pedre-demo.spec
   ```

3. The executable will be in `dist/pedre-demo/` (or `dist/pedre-demo.app` on macOS)

### Testing the app

To run the macOS app from terminal and see console output:

```bash
./dist/pedre-demo.app/Contents/MacOS/pedre-demo
```

For Linux:

```bash
./dist/pedre-demo/pedre-demo
```

For Windows:

```bash
dist\pedre-demo\pedre-demo.exe
```

### GitHub Releases

Installers are automatically built for Linux, Windows, and macOS when you:

- Push a tag starting with `v` (e.g., `v1.0.0`)
- Manually trigger the workflow from the Actions tab

The workflow will create a GitHub release with the following artifacts:

- `pedre-demo-Linux.tar.gz` - Linux executable bundle
- `pedre-demo-Windows.zip` - Windows executable bundle
- `pedre-demo-macOS.tar.gz` - macOS executable bundle
- `pedre-demo.app` - macOS application bundle

## Assets

[Icons](https://clockworkraven.itch.io/raven-fantasy-icons)
[Tilesets & Characters](https://kenmi-art.itch.io/cute-fantasy-rpg)
[Music](https://pizzadoggy.itch.io/cozy-tunes)
[Voice SFX](https://dillonbecker.itch.io/sdap)
[Map](https://lukasfdahl.itch.io/world-map)
