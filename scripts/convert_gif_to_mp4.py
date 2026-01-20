from __future__ import annotations

import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Convert gifs to mp4 format
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    You can either use the UI below or run:

    ```powershell
    uv run python convert_gif_to_mp4.py -- --folder /path/to/folder
    ```
    """)
    return


@app.cell
def _():
    import os
    import subprocess
    from pathlib import Path

    return Path, os, subprocess


@app.cell
def _(Path, os, subprocess):
    def get_gifs_from_folder(input_folder):
        """Retourne la liste des GIFs (récursif)."""
        return list(Path(input_folder).glob("**/*.gif"))

    def _print_size_info(gif_path: Path, output_path: Path):
        """Affiche la réduction de taille si le fichier de sortie existe."""
        try:
            original_size = os.path.getsize(gif_path)
            new_size = os.path.getsize(output_path)
        except FileNotFoundError:
            # Sortie absente (ou supprimée), on n'affiche rien
            return

        reduction = (1 - new_size / original_size) * 100
        print(f"Réduction de taille : {reduction:.1f}%")
        print(f"Original : {original_size / 1024:.1f} KB")
        print(f"Nouvelle : {new_size / 1024:.1f} KB")
        print("-" * 50)

    def convert_gif_to_mp4(gif_files, force: bool = False, timeout_sec: int = 20):
        """
        Convertit une liste de GIF en MP4 (H.264).
        - Ne reconvertit pas si le .mp4 existe déjà, sauf si force=True.
        - Utilise -n (ne pas écraser) quand force=False, et -y (écraser) quand force=True.
        """
        if not gif_files:
            print("Aucun fichier GIF trouvé dans le dossier spécifié.")
            return

        print(f"{len(gif_files)} GIF détectés. Démarrage de la conversion...")

        for gif_path in gif_files:
            gif_path = Path(gif_path)
            output_path = gif_path.with_suffix(".mp4")

            if output_path.exists() and not force:
                print(f"[SKIP] {gif_path} — le fichier de sortie existe déjà.")
                _print_size_info(gif_path, output_path)
                continue

            print(f"[CONVERT] {gif_path} -> {output_path}")

            overwrite_flag = "-y" if force else "-n"

            # Conserve dimensions multiples de 2 (requis par H.264 yuv420p)
            vf_arg = "scale=trunc(iw/2)*2:trunc(ih/2)*2"

            cmd = [
                "ffmpeg",
                overwrite_flag,  # contrôle de l'écrasement
                "-i",
                str(gif_path),  # entrée GIF
                "-movflags",
                "faststart",  # meilleure lecture en streaming
                "-pix_fmt",
                "yuv420p",  # compatibilité players
                "-vf",
                vf_arg,
            ]

            # Audio : les GIF n’ont pas d’audio; on s’assure d’avoir une piste silencieuse si requis,
            # ou on supprime explicitement (ici on supprime).
            cmd.extend(["-an"])

            cmd.append(str(output_path))

            try:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout_sec)

                if result.returncode == 0 and output_path.exists():
                    print(f"[OK] Conversion réussie : {output_path}")
                    _print_size_info(gif_path, output_path)
                else:
                    print(f"[ERREUR] Échec conversion : {gif_path}")
                    if result.stderr:
                        print(result.stderr.strip())
                    if output_path.exists() and not force:
                        print("[INFO] FFmpeg a refusé d'écraser (option -n).")
                        _print_size_info(gif_path, output_path)

            except subprocess.TimeoutExpired:
                print(f"[TIMEOUT] {gif_path} — conversion > {timeout_sec}s")
            except Exception as e:
                print(f"[EXCEPTION] {gif_path} — {e}")

    return convert_gif_to_mp4, get_gifs_from_folder


@app.cell
def _(mo):
    folder_browser = mo.ui.file_browser(selection_mode="directory")
    force_overwrite = mo.ui.checkbox(label="Force overwrite existing files")
    return folder_browser, force_overwrite


@app.cell
def _(folder_browser, force_overwrite, mo):
    mo.vstack([folder_browser, force_overwrite])
    return


@app.cell
def _(folder_browser, get_gifs_from_folder):
    if folder_browser.value:
        folder_to_process = folder_browser.path()
        gifs = get_gifs_from_folder(folder_to_process)
    return (gifs,)


@app.cell
def _(gifs, mo):
    run_selection = mo.ui.run_button(label="Convert all in folder", disabled=len(gifs) == 0)
    run_selection
    return (run_selection,)


@app.cell
def _(convert_gif_to_mp4, force_overwrite, gifs, mo, run_selection):
    if run_selection.value:
        with mo.status.spinner("Converting GIFs to WebM..."):
            convert_gif_to_mp4(gifs, force=force_overwrite.value)
    return


@app.cell
def _(convert_gif_to_mp4, get_gifs_from_folder, mo, os):
    folder_path = mo.cli_args().get("folder")
    _force = mo.cli_args().get("force")
    if _force is None:
        _force = False

    if mo.app_meta().mode != "script":
        mo.stop(True, "Not running as a script")

    if not os.path.exists(folder_path):
        raise Exception("Specified folder does not exist!")
    else:
        convert_gif_to_mp4(get_gifs_from_folder(folder_path), force=_force)
    return


if __name__ == "__main__":
    app.run()
