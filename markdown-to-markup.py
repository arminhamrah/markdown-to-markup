import re

#———New lines———
def handle_newlines(contents):
    NewLines = []
    OldLines = contents.split("\n")

    for line in OldLines:
        new_line = re.sub(r"^\s*$", r"<br>", line)  # if a line has only space characters, \s, we make an HTML newline <br>
        NewLines.append(new_line)

    new_contents = "\n".join(NewLines)   # join with \n characters so it's readable by humans
    return new_contents

# Test
if True:
    old_contents = """\
# Title"""
    new_contents = handle_newlines(old_contents)
    print(new_contents)


#———Headers———
def handle_headers(contents):
    """ replace all of the #, ##, ###, ... ###### headers with <h1>, <h2>, <h3>, ... <h6> """
    NewLines = []
    OldLines = contents.split("\n")

    for line in OldLines:
        new_line = line
        new_line = re.sub(r"^###### (.*)", r"<h6>\1<h6>", new_line)
        new_line = re.sub(r"^##### (.*)", r"<h5>\1<h5>", new_line)
        new_line = re.sub(r"^#### (.*)", r"<h4>\1<h4>", new_line)
        new_line = re.sub(r"^### (.*)", r"<h3>\1<h3>", new_line)
        new_line = re.sub(r"^## (.*)", r"<h2>\1<h2>", new_line)
        new_line = re.sub(r"^# (.*)", r"<h1>\1<h1>", new_line)
        NewLines.append(new_line)
    
    new_contents = "\n".join(NewLines)
    return new_contents

#Test
if True:
    old_contents = """\
# Title
<br>
## Testing H2
#### Testing H4
###### Testing H6
"""
    new_contents = handle_headers(old_contents)
    print(new_contents)

#———Code———
def handle_code(contents):
    NewLines = []
    OldLines = contents.split("\n")

    for line in OldLines:
        new_line = re.sub(r"`(.*)`", r"<tt>\1</tt>", line)
        NewLines.append(new_line)

    new_contents = "\n".join(NewLines)
    return new_contents

# Test
if True:
    old_contents = """\
This is <tt>42</tt>   
<br> 
Our regex library:  <tt>import re</tt>"""
    new_contents = handle_code(old_contents)
    print(new_contents)

#———Italics———
def handle_italics(contents):
    NewLines = []
    OldLines = contents.split("\n")

    for line in OldLines:
        new_line = line
        new_line = re.sub(r"\*([^\*]+)\*", r"<i>\1</i>", new_line)
        NewLines.append(new_line)
    
    new_contents = "\n".join(NewLines)
    return new_contents

#Test
if True:
    old_contents = """\
# _Hello world_
*Hello world*
"""
    new_contents = handle_italics(old_contents)
    print(new_contents)

#———Bold———
def handle_bold(contents):
    NewLines = []
    OldLines = contents.split("\n")

    for line in OldLines:
        new_line = line
        new_line = re.sub(r"\*\*([^\*]+)\*\*", r"<b>\1</b>", new_line)
        new_line = re.sub(r"__([^_]+)__", r"<b>\1</b>", new_line) #used GPT for these two lines
        NewLines.append(new_line)
    
    new_contents = "\n".join(NewLines)
    return new_contents

#Test
if True:
    old_contents = """\
This is **bold with asterisks**
This is __bold with underscores__
This is normal text with **some bold** words
This is normal text with __other__ bold words ('other' should have been bolded)
"""
    new_contents = handle_bold(old_contents)
    print(new_contents)

#———Underscores———
def handle_underscores(contents):
    NewLines = []
    OldLines = contents.split("\n")

    for line in OldLines:
        new_line = line
        new_line = re.sub(r"(?<!_)_([^_]+)_(?!_)", r"<u>\1</u>", new_line)
        NewLines.append(new_line)
    
    new_contents = "\n".join(NewLines)
    return new_contents

# Test
if True:
    old_contents = """\
_Underscore this_
Don't underscore this.
"""
    new_contents = handle_underscores(old_contents)
    print(new_contents)

#———Strikethrough———
def handle_strikethrough(contents):
    NewLines = []
    OldLines = contents.split("\n")

    for line in OldLines:
        new_line = line
        new_line = re.sub(r"~~([^~]+)~~", r"<s>\1</s>", new_line)
        NewLines.append(new_line)
    
    new_contents = "\n".join(NewLines)
    return new_contents

#Test
if True:
    old_contents = """\
This is ~~strikethrough text~~
This is normal text with ~~some strikethrough~~ words
This combines **bold**, *italic*, and ~~strikethrough~~ styles
Some ~~longer strikethrough text with multiple words~~
"""
    new_contents = handle_strikethrough(old_contents)
    print(new_contents)


#———List———
def handle_list(contents):
    NewLines = []
    OldLines = contents.split("\n")
    in_list = False

    for line in OldLines:
        stripped_line = line.strip()
        if stripped_line.startswith('+'):
            if not in_list:
                NewLines.append("<ul>")
                in_list = True
            list_item = stripped_line[1:].strip()
            NewLines.append(f"<li>{list_item}</li>")
        else:
            if in_list:
                NewLines.append("</ul>")
                in_list = False
            NewLines.append(line)

    if in_list:
        NewLines.append("</ul>")

    new_contents = "\n".join(NewLines)
    return new_contents
#This one was especially challenging and I used Claude 3.5 sonnet to help me debug & 
#fix my code my intially unsuccessful (or, may we call it 'successfully learning') code

# Test
if True:
    old_contents = """\
List:
+ A
+ B
+ CDE

Not list

+ List
"""
    new_contents = handle_list(old_contents)  # Changed 'contents' to 'old_contents'
    print(new_contents)

#———URLs———
def handle_url(contents):
    NewLines = []
    OldLines = contents.split("\n")

    for line in OldLines:
        new_line = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', line)
        NewLines.append(new_line)

    new_contents = "\n".join(NewLines)
    return new_contents

# Test
if True:
    old_contents = """\
Here are links to each of my TED Talks:
[1](https://www.ted.com/talks/armin_hamrah_how_social_media_takes_away_our_humanness).
[2](https://www.ted.com/talks/armin_hamrah_living_our_dreams_lucid_dreaming)
[3](https://www.ted.com/talks/armin_hamrah_the_inhumane_humanities).
[4](https://www.ted.com/talks/armin_hamrah_generative_ai_what_do_we_want_it_to_be).
"""
    new_contents = handle_url(old_contents)
    print(new_contents)

#———Delete all hellos———
def delete_all_hellos(contents):
    NewLines = []
    OldLines = contents.split("\n")

    for line in OldLines:
        new_line = re.sub(r'\bhello\b', '', line, flags=re.IGNORECASE)
        NewLines.append(new_line)
    
    new_contents = "\n".join(NewLines)
    return new_contents

# Test
if True:
    old_contents = """\
There are 3 'Hellos' here about to be deleted: Hello hello hello (Ha, you can't see them, only their ghosts!)
helloster & hellothere should not be replaced
Hello World, we are doomed.
"""
    new_contents = delete_all_hellos(old_contents)
    print(new_contents)

#———Replace AI with artificial intelligence———
def replace_AI_with_artificial_intelligence(contents):
    NewLines = []
    OldLines = contents.split("\n")

    for line in OldLines:
        new_line = re.sub(r'(^|\. )AI\b', r'\1Artificial intelligence', line) #AI at start of sentence
        new_line = re.sub(r'\bAI\b', 'artificial intelligence', new_line) #AI in middle of sentence
        NewLines.append(new_line)
    
    new_contents = "\n".join(NewLines)
    return new_contents

# Test
if True:
    old_contents = """\
AI is revolutionizing many industries.
The field of AI has seen rapid advancements.
AIzilla is not a real word and should not be replaced.
We're studying AI at the AI Institute. AI is everywhere.
AI, more AI, and even more AI. AI is the future.
"""
    new_contents = replace_AI_with_artificial_intelligence(old_contents)
    print(new_contents)