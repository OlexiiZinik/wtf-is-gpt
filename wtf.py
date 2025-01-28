#!/home/olexii/Projects/WTF/venv/bin/python

import sys
from g4f.client import Client



def main(arg):
    cli = Client()
    resp = cli.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"system", "content":"You are a command line tool. You have to answer questions that user asks. probably a lot of them startsh with \"what is\""}, {"role":"user", "content": arg}]
    )
    print(resp.choices[0].message.content)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(" ".join(sys.argv[1:]))

