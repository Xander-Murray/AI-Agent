import os


def get_files_info(working_directory, directory="."):
    try:
        abs_work = os.path.abspath(working_directory)
        abs_target = os.path.abspath(os.path.join(working_directory, directory))

        if os.path.commonpath([abs_target, abs_work]) != abs_work:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(abs_target):
            return f'Error: "{directory}" is not a directory'
        lines = []
        for name in os.listdir(abs_target):
            full = os.path.join(abs_target, name)
            lines.append(
                f"- {name}: file_size={os.path.getsize(full)} bytes, is_dir={os.path.isdir(full)}"
            )
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"
