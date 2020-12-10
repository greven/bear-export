# Bear Notes Export

A quick and dirty Python script to export the MacOS [Bear App](https://bear.app) note files to an output folder (in my case One Drive, so it can sync).

## Why?

This is a workaround the fact that Bear App is not available outside the Apple ecosystem. When and if the Bear App web client arrives, this will become unnecessary.

## Configuration

There is a very simple `config.json` file with the following options:

- **cleanOutputDir**: Cleans any files in the output (target) directory before exporting the files. Defaults to `true`.
- **exportTrash**: Exports the notes in the trash. Defaults to `false`.
- **outputDir**: The default output folder. Defaults to `~/OneDrive/Notes`.

## Run

In the directory, just execute the `export.py` Python file:

```shell
$ python export.py
```

## Limitations

This is uni directional `Bear App` -> `Exported Markdown Files`. I want to keep this as simple as possible and **read-only** to avoid messing any metadata in the Bear App SQLite database.

The images folder is also exported, but not any embedded files. The format that Bear App currently uses for the images is not standard markdown and therefore the images won't render in the markdown files outside of Bear App.

## To Do

- [ ] Option to create sub-folders per tag?
