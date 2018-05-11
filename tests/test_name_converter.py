
from name_converter import NameConverter, clean_name

red = (237, 10, 63)
red_orange = (255,104,31)
robins_egg_blue = (0, 204, 204)


def test_clean_caps():
    converter = NameConverter()
    assert 'red' == clean_name('Red')
    assert 'red' == clean_name('RED')
    assert 'red' == clean_name('red')
    assert 'red' == clean_name('ReD')


def test_clean_punctuation():
    converter = NameConverter()
    assert 'red' == clean_name('Red.')
    assert 'red' == clean_name('RED!')
    assert 'red' == clean_name('red?')


def test_clean_whitespace():
    converter = NameConverter()
    assert 'red' == clean_name('   Red   ')
    assert 'red' == clean_name('\t\tRed\t\t')
    assert 'red' == clean_name('\n\nRed\n\n')


def test_exact_spelling():
    converter = NameConverter()
    assert red == converter.convert('Red')
    assert red_orange == converter.convert('Red-Orange')
    assert robins_egg_blue == converter.convert("Robin's Egg Blue")


def test_leading_and_trailing_space():
    converter = NameConverter()
    assert red == converter.convert('  Red  ')
    assert red_orange == converter.convert('\nRed-Orange\n')
    assert robins_egg_blue == converter.convert("\t\tRobin's Egg Blue\t\t")


def test_different_cases():
    converter = NameConverter()
    assert red == converter.convert('RED')
    assert red_orange == converter.convert('red-orange')
    assert robins_egg_blue == converter.convert("RoBin'S Egg blue")


def test_punctuation():
    converter = NameConverter()
    assert red == converter.convert('Red.')
    assert red_orange == converter.convert('Red-Orange!')
    assert robins_egg_blue == converter.convert("Robin's Egg Blue?")
