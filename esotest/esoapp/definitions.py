class definitions:
    about = {
        "brainfuck": "It's brainfuck yo!",
        "esoterrible": "It's esoterrible yo!",
        "malbolge": "It's malbolge yo!",
        "spl": "It's shakespere yo!",
    }
    example = {
        "brainfuck": "It's brainfuck yo!",
        "esoterrible": "It's esoterrible yo!",
        "malbolge": "It's malbolge yo!",
        "spl": "It's shakespere yo!",
    }

    def get_definition(self, lang):
        if lang not in self.about.keys():
            return " "
        else:
            return self.about[lang]

    def get_examples(self, lang):
        if lang not in self.example.keys():
            return " "
        else:
            return self.example[lang]
