#!/bin/python

from argparse import ArgumentParser
import os
from math import floor
import shutil

# color codes
colors = {
    "red":" \u001b[31m",
    "green":" \u001b[32m"
}

# parse arguments, returns (input, output, rename)
def parse_args():
    ap = ArgumentParser(prog="osupull", description="pulls songs from osu!")
    ap.add_argument("input", help="the Songs folder of osu!")
    ap.add_argument("output", help="where pulled songs are stored")
    ap.add_argument("--rename", "-r", default="nba",help="the output name. (e.g. 'ba', renames output with the beatmap name then the audio name)")
    args = ap.parse_args()
    return (args.input, args.output, args.rename)

# get the number of beatmaps
def quantify(input: str):
    quantity = len(os.listdir(input))
    return quantity
 
class UnknownPartError(Exception):
    pass

# renames song
def rename(format, beatmap, file):
    name = ""
    if len(beatmap.split(" ", 1)) < 2:
        return f"{beatmap} {file}"
    number = beatmap.split(" ", 1)[0]
    beatmap_name = beatmap.split(" ", 1)[1]
    for part in list(format):
        if part == "n":
            name += number + " "
        elif part == "b":
            name += beatmap_name + " "
        elif part == "a":
            name += file + " "
        else:
            raise UnknownPartError
    return name.strip()

# pull song from beatmap
def pull(beatmap, output, format, progress, beatmap_name):
    if not os.path.exists(output):
        os.makedirs(output)
    for file in os.listdir(beatmap):
        if file.endswith('.mp3'):
            o = rename(format, beatmap_name, file)
            if not o.endswith('.mp3'):
                o += ".mp3"
            print(f"[{progress}%]\tExtracting {os.path.join(beatmap, file)} to {output} as {o}.")
            shutil.copyfile(os.path.join(beatmap, file), os.path.join(output, o))

# main code starts here 
def main() -> int:
    try:
        input, output, rename = parse_args()
        print("Quantifiying input...")
        quantity = quantify(input)
        for i, dir in enumerate(os.listdir(input), start=1):
            pull(os.path.join(input, dir), output, rename, floor((i/quantity)*100), dir)

        print(f"{colors['green']}Extracted Succesfully")
        return 0
    except KeyboardInterrupt:
        print(f"{colors['red']}Keyboard Interrupt")
        return 1
    except UnknownPartError:
        print(f"{colors['red']}Unknown Part Error")

if __name__ == "__main__":
    exit(main())