def main():
    tag(tag_type = "p", content = "hello")    

def html(tag):
    def str_to_html(tag_type, content):
        print(f"<{tag_type}>{content}</{tag_type}>")
        

    return str_to_html
@html
def tag(*, tag_type, content): return content
main()