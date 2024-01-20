import curses

def print_file_content(stdscr, filename):
    try:
        # Open and read the file
        with open(filename, 'r') as file:
            file_content = file.read()

        # Clear the screen
        stdscr.clear()

        # Print the file content on the screen
        stdscr.addstr(0, 0, file_content)

        # Refresh the screen
        stdscr.refresh()

        # Wait for user input
        stdscr.getch()

    except Exception as e:
        # Handle file reading errors
        stdscr.addstr(0, 0, f"Error reading file: {e}", curses.A_BOLD)
        stdscr.refresh()
        stdscr.getch()

