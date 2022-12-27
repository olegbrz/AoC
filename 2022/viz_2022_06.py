#!/usr/bin/env python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses
import aoc_helper as ah
from time import sleep


def get_packet(data: str, window_size: int) -> int:
    i = window_size - 1
    found = False
    while not found:
        window = data[i - (window_size - 1) : i + 1]
        found = len(set(window)) == window_size
        i += 1
    return i


def draw(stdscr):
    stdscr.refresh()
    data = ah.get_input(2022, 6, as_string=True)
    iteration = 1
    curses.curs_set(0)

    stdscr.clear()
    while True:

        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_GREEN)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_YELLOW)
        height, width = stdscr.getmaxyx()

        title = "Advent of Code - Day 6"
        subtitle = "Written by Oleg Brezitskyy (@olegbrz)"

        DATA_TO_SHOW = 40
        PACKET_LENGHT = 14
        window = data[iteration - 1 : iteration - 1 + PACKET_LENGHT]
        found = len(set(window)) == PACKET_LENGHT

        statusbarstr = f"SCANNED PACKETS {iteration - 1 + PACKET_LENGHT} | {'PACKET FOUND' if found else ''}"

        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_data = int((width // 2) - (DATA_TO_SHOW // 2) - len(subtitle) % 2)
        start_y = int((height // 2) - 2)

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height - 1, 0, statusbarstr)
        stdscr.addstr(
            height - 1, len(statusbarstr), " " * (width - len(statusbarstr) - 1)
        )
        stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(start_y, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        stdscr.addstr(start_y + 3, (width // 2) - 2, "-" * 4)

        if found:
            stdscr.attron(curses.color_pair(4))
            stdscr.attron(curses.A_BLINK)
        else:
            stdscr.attron(curses.color_pair(5))
        stdscr.attron(curses.A_BOLD)
        stdscr.addstr(
            start_y + 5,
            start_x_data,
            data[(iteration - 1) : (iteration - 1) + PACKET_LENGHT],
        )

        stdscr.attroff(curses.A_REVERSE)
        stdscr.attroff(curses.A_BOLD)
        stdscr.attroff(curses.A_BLINK)
        stdscr.attroff(curses.color_pair(4))

        stdscr.addstr(
            start_y + 5,
            start_x_data + PACKET_LENGHT,
            data[(iteration - 1) : (iteration - 1) + DATA_TO_SHOW + 1 - PACKET_LENGHT],
        )

        # Refresh the screen
        stdscr.refresh()
        if not found:
            sleep(0.001)
            iteration += 1


def main():
    curses.wrapper(draw)


if __name__ == "__main__":
    main()
