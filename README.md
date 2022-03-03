# osupull

Pulls song from osu!

## Usage

### Pull Songs

Extracts song from osu! 
> Note: replace {SongsDir} with the actual Song Directory

``` sh
osupull {SongsDir} extracted_songs
```

### Rename

The `--rename format` renames every song with the format. The format syntax are options next to each other and is ordered. The following are options currently available.

- n - the osu! id of the beatmap
- b - the name of the beatmap
- a - the filename of the song inside the beatmap

For example the following will rename the songs with the beatmap name followed by the id.

``` sh
osupull {SongsDir} extracted_songs --rename bn
```

## Installation

> Note: This will not cover how to install this on Windows, only Linux

``` sh
git clone https://github.com/algames2019/osupull.git
cd osupull
sudo cp main.py /usr/bin/osupull
```