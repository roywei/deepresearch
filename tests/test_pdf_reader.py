from backend.pdf_reader import read_pdf_text


def test_read_pdf_text():
    text = read_pdf_text('tests/sample.pdf')
    assert 'Hello World' in text
