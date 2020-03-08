import textwrap

def wrap(string, max_width):
   # a,b=len(string),len(string)/4
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)