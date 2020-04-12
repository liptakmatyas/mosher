#!/usr/bin/env python3
"""Mosher

Usage:
    mosher.py --video VIDEO... --plugin PLUGIN... --output-file OUTPUT_FILE
    mosher.py --version
    mosher.py --help

Options:
    --video VIDEO, -v               input VIDEO
    --plugin PLUGIN, -p             use effect from PLUGIN
    --output-file OUTPUT_FILE, -o   save result to OUTPUT_FILE
    --help, -h                      show this help
    --version                       show version

Notes:
-   VIDEO_{0,1} must already be preprocessed to have one I-frame (as the first
    frame in the video) and the rest is all P-frames.
-   VIDEO_0 should already be moshed.
-   The script depends on `ffprobe`.
"""

import importlib
from docopt import docopt
from jinja2 import Environment, PackageLoader
import subprocess

import mosher


def main(args):
    video = [mosher.Video(video_idx, input_file)
             for video_idx, input_file in enumerate(args['--video'])]

    frame_ranges = []
    for plugin_name in args['--plugin']:
        plugin = importlib.import_module('mosher.plugin.{}'.format(plugin_name))
        frame_ranges += plugin.frame_ranges(video)

    segments = [ seg for range in frame_ranges for seg in range ]

    parameters = {
        'input_videos': args['--video'],
        'segments': segments,
        'total_duration_us': sum([ seg['duration_us'] for seg in segments ]),
        'output_path': args['--output-file'],
    }

    #   Load the Jinja template and render the script code
    jenv = Environment(loader = PackageLoader('mosher', 'templates'))
    tmpl = jenv.get_template('avidemux.py.j2')
    script_code = tmpl.render(**parameters)

    #   Save the rendered script code
    script_filename = "{}.py".format(args['--output-file'])
    print("Saving avidemux script to {}".format(script_filename))
    with open(script_filename, 'w') as script_file:
        script_file.write(script_code)

    #   Run generated script
    print("Running avidemux script {}".format(script_filename))
    avidemux = 'avidemux2.7_cli'
    yes_twice = "y\ny\n".encode()
    subprocess.run([ avidemux, '--run', script_filename ], input = yes_twice)


if __name__ == '__main__':
    args = docopt(__doc__, version='0.0.0')
    main(args)

