from page_gen import generate_pages_recursive
from public_dir_gen import generate_public_dir


def main():
    print("running main....")
    generate_public_dir()
    generate_pages_recursive("content/", "template.html", "public/")


main()
