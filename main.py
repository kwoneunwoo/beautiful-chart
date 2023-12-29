import unicodedata


data = {
    'Na': 1,
    'W' : 2
}


def get_space(text: str, space: int) -> int:
    text_width = 0
    for t in text:
        text_width += data[unicodedata.east_asian_width(t)]
    
    r_width = space - text_width
    if r_width < 0:
        raise Exception(f'too short space. you needs more than {text_width}')

    return r_width

def print_chart(texts: dict[str, int]):
    r_text = '|'
    for text in texts.keys():
        width = get_space(text, texts[text])
        front_width = ' '*(width//2)
        back_width = ' '*(width-width//2)
        r_text += front_width+text+back_width+'|'
    
    print(r_text)


if __name__ == '__main__':
    print_chart({'':8, '고등어':8})
    print_chart({'구분':8, '지역':8})
    print_chart({'index':8, 'region':8})
