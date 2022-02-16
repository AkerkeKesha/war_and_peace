from Bleualign.bleualign.align import Aligner

src_file = './sample/tolstoy.ru.txt'
target_file = './sample/maude.eng.txt'
src_to_target = './sample/google-translate.ru.eng.txt'
output_src_file = './sample/ru.aligned.txt'
output_target_file = './sample/eng.aligned.txt'

options = {
    'srcfile': src_file,
    'targetfile': target_file,
    'srctotarget': [src_to_target],
    'output-src': output_src_file,
    'output-target': output_target_file
}

if __name__ == '__main__':
    aligner = Aligner(options)
    aligner.mainloop()
