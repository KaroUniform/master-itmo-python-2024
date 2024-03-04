import click


def count_lines_words_bytes(file_path):
    """
    Count the number of lines, words, and bytes in a given file.

    Args:
        file_path (str): Path to the file.

    Returns:
        tuple: A tuple containing the number of lines, words, and bytes.
    """
    lines, words, bytes_count = 0, 0, 0

    with open(file_path, "rb") as file:
        for line in file:
            lines += 1
            words += len(line.split())
            bytes_count += len(line)

    return lines, words, bytes_count


@click.command()
@click.argument("files", nargs=-1, type=click.Path(exists=True))
def wc(files):
    """
    Display the number of lines, words, and bytes in one or more files.

    Args:
        files (tuple): A tuple of file paths.
    """
    if not files:
        # If no files are provided, read from standard input
        lines, words, bytes_count = count_lines_words_bytes("/dev/stdin")
        click.echo(f"  {lines}\t{words}\t{bytes_count}")
    else:
        total_lines, total_words, total_bytes = 0, 0, 0

        for file_path in files:
            lines, words, bytes_count = count_lines_words_bytes(file_path)
            total_lines += lines
            total_words += words
            total_bytes += bytes_count

            click.echo(f"  {lines}\t{words}\t{bytes_count}\t{file_path}")

        # Print total statistics if multiple files are provided
        if len(files) > 1:
            click.echo(f"  {total_lines}\t{total_words}\t{total_bytes}\ttotal")


if __name__ == "__main__":
    wc()
