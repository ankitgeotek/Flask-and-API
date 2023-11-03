# Import
import paralleldots

# Setting your API key
paralleldots.set_api_key('RRs3M6U1ASUuTKzTF0DCJaqdCrNYibwAHuyWn8qZuwM')


def ner(text):
    ner = paralleldots.ner(text)

    return ner
