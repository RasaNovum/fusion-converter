# Fusion Converter
A script to automate the conversion from CTM (or other) file formats to Fusion using Midnighttigger's **MT-Fusion-Converter**

- Move [MT-Fusion-Converter](https://github.com/Midnighttigger/MT-Fusion-Converter/tree/main) into a folder
- Move all files from this repository into the same folder
- Run ``run.bat`` to generated requrired folders
- Setup the desired conversion based on [MT-Fusion-Converter's ``setup.txt`` process](https://github.com/Midnighttigger/MT-Fusion-Converter/blob/main/readmeformats.png) and move it into ``/import/automation/``
- Move desired images into ``/auto_import/``
- Run ``run.bat`` and processed textures will appear in ``/auto_export/``

This currently only supports conversions that both start and end as a single image (ie. CTM compact -> Fusion Full).
