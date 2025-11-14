from PyInstaller.utils.hooks import collect_submodules

# Collect all submodules of streamlit
hiddenimports = collect_submodules('streamlit')
