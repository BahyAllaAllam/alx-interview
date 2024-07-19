#!/usr/bin/python3
"""
Log parsing script
"""


import sys
import re
import signal


if __name__ == '__main__':
    line_count = 0
    log = {
            "file_size": 0,
            "code_frequency": {
                "200": 0,
                "301": 0,
                "400": 0,
                "401": 0,
                "403": 0,
                "404": 0,
                "405": 0,
                "500": 0
                }
            }

    def print_stats(log):
        """Print the statistics"""
        print("File size: {}".format(log["file_size"]))
        for code in sorted(log["code_frequency"]):
            if log["code_frequency"][code] > 0:
                print("{}: {}".format(code, log["code_frequency"][code]))

    def signal_handler(sig, frame):
        """Handle keyboard interruption"""
        print_stats(log)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    log_pattern = re.compile(
            r"""
            (\d{1,3}\.){3}\d{1,3}
            \s-\s
            \[\d{4}-\d{2}-\d{2}
            \s\d{2}:\d{2}:\d{2}\.\d+\]
            \s"GET\s/projects/260\sHTTP/1\.1"
            \s(\d{3})
            \s(\d+)
            """, re.VERBOSE
            )
    try:
        for line in sys.stdin:
            line = line.strip()
            match = log_pattern.match(line)
            if match:
                line_count += 1
                status_code = match.group(2)
                file_size = int(match.group(3))
                log["file_size"] += file_size
                if status_code in log["code_frequency"]:
                    log["code_frequency"][status_code] += 1
                if line_count % 10 == 0:
                    print_stats(log)
        print_stats(log)
    except Exception:
        pass
