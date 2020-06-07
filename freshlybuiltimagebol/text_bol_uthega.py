from googletrans import Translator
from .bhasha_codes import bhasha_kosh
from gtts import gTTS

class ShabdDhwani:
    bhasha_codes = dict(map(reversed, bhasha_kosh.items()))
    
    def code_se_naam(bhasha_code):
        bhasha=list(bhasha_kosh.keys())[list(bhasha_kosh.values()).index(bhasha_code)]
        return bhasha

    def shabd_se_dhwani(shabd,bhasha,filename):
        """ shabd = text,
            bhasaa = language(mainly allowed in code)
                = file
            filename=app//audio.mp3
            anuvadak = Translator
            anuvadit = Translated
        """
        # translates the text into german language
        bhasha= ShabdDhwani.code_se_naam(bhasha)
        anuvadak = Translator().translate(shabd,dest=bhasha)
        anuvadit_file=gTTS(text=anuvadak.text,lang=anuvadak.dest)    
        anuvadit_file.save(filename)

    def shabd_ki_bhasha_badlo(shabd,bhasha):
        bhasha= ShabdDhwani.code_se_naam(bhasha)
        return Translator().translate(shabd, dest=bhasha).text

    def bhasa_badlkr_kya_bole(shabd,bhasha):
        bhasha= ShabdDhwani.code_se_naam(bhasha)
        return Translator().translate(shabd, dest=bhasha).pronunciation

    def shabd_ki_bhasha_jaano(shabd):
        return bhasha_kosh[Translator().detect(shabd).lang]

    def shabd_ki_bhasha_jaano_code(shabd):
        return Translator().detect(shabd).lang
