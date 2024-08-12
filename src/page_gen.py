import os
from node_conversion import markdown_to_htmlnode
from split_functions import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    full_html = ""
    with open(template_path) as template_file:
        template_html = template_file.read()
        with open(from_path) as markdown_file:
            markdown = markdown_file.read()
            html = markdown_to_htmlnode(markdown)
            # print(html)
            markdown_title = extract_title(markdown)
            full_html = template_html.replace("{{ Title }}", markdown_title).replace(
                "{{ Content }}", html.to_html()
            )
            # print(full_html)
    try:
        os.makedirs(dest_path)
    except FileExistsError:
        pass
    finally:
        # print("Destination path : " + dest_path)
        with open(
            dest_path + os.path.basename(from_path).replace(".md", ".html"), "w"
        ) as final_html:
            # print(final_html)
            final_html.write(full_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.isfile(dir_path_content) and os.path.basename(
        dir_path_content
    ).__contains__(".md"):
        generate_page(dir_path_content, template_path, dest_dir_path)
    else:
        for sub_path in os.listdir(dir_path_content):
            new_dir_path = os.path.join(dir_path_content, sub_path)
            new_dest_dir_path = dest_dir_path
            if os.path.isdir(new_dir_path):
                new_dest_dir_path = os.path.join(dest_dir_path, sub_path + "/")

            # print(new_dir_path)
            # print(new_dest_dir_path)
            generate_pages_recursive(new_dir_path, template_path, new_dest_dir_path)
