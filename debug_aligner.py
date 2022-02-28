from Bleualign.bleualign.align import Aligner

source = 'sample'

options = {
    'srcfile': f'./{source}/tolstoy.ru.txt',
    'targetfile': f'./{source}/maude.eng.txt',
    'srctotarget': [
        f'./{source}/google-translate.ru.eng.txt'
    ],
    'output-src': f'./{source}/ru.aligned.txt',
    'output-target': f'./{source}/eng.aligned.txt'
}

if __name__ == '__main__':
    aligner = Aligner(options)
    aligner.mainloop()
