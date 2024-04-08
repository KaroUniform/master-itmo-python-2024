import sys
import click
import os


def tail(filename, n=10):
    """Read the last 'n' lines from the given file."""
    lines = []

    with open(filename, "rb") as file:
        # Чтение файла в обратном направлении
        file.seek(0, os.SEEK_END)
        file_size = file.tell()

        byte = file_size - 1
        line_count = 0

        while byte >= 0 and line_count < n:
            file.seek(byte)
            char = file.read(1).decode("utf-8")
            if char == "\n":
                line = file.readline().decode("utf-8")
                lines.append(line)
                line_count += 1
            elif byte == 0:
                file.seek(0)
                line = file.readline().decode("utf-8")
                lines.append(line)
                line_count += 1

            byte -= 1

    return lines


def tail_stdin(num_lines=17):
    """Read the last 'num_lines' lines from standard input."""
    lines = []

    for line in sys.stdin:
        lines.append(line)
        if len(lines) == num_lines:
            break

    return lines


@click.command()
@click.argument("files", nargs=-1)
def main(files):
    """This script works like tail."""
    if not files:
        # Если файл не указан, читаем из стандартного ввода
        lines = tail_stdin()
        click.echo("".join(lines[::-1]))
    else:
        for file_path in files:
            if len(files) > 1:
                # Если указано несколько файлов, выводим разделитель и имя файла
                if file_path != files[0]:
                    click.echo("\n", nl=False)
                click.echo(f"==> {file_path} <==")

            lines = tail(file_path)
            click.echo("".join(lines[::-1]), nl=False)


if __name__ == "__main__":
    main()
