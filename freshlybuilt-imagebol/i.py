from googletrans import Translator
from bhasha_codes import bhasha_kosh

translations = Translator().translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)


print(bhasha_kosh[Translator().detect('이 문장은 한글로 쓰여졌습니다.').lang])

