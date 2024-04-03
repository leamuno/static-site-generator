from textnode import TextNode

def main():
    test1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    test2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(test1)
    print(test1.eq(test2))
    print(test1.repr())

main()
