from googletrans import Translator
from .bhasha_codes import bhasha_kosh
from gtts import gTTS

class ShabdDhwani:
    bhasha_codes = dict(map(reversed, bhasha_kosh.items()))
    def shabd_se_dhwani(shabd,bhasha,filename):
        """ shabd = text,
            bhasaa = language(mainly allowed in code)
                = file
            filename=app//audio.mp3
            anuvadak = Translator
            anuvadit = Translated
        """
        # translates the text into german language
        anuvadak = Translator().translate(shabd,dest=bhasha)
        anuvadit_file=gTTS(text=anuvadak.text,lang=bhasha)    
        anuvadit_file.save(filename)

    def shabd_ki_bhasha_badlo(shabd,bhasha):
        return Translator().translate(shabd, dest=bhasha).text

    def bhasa_badlkr_kya_bole(shabd,bhasha):
        return Translator().translate(shabd, dest=bhasha).pronunciation

    def shabd_ki_bhasha_jaano(shabd):
        return bhasha_kosh[Translator().detect(shabd).lang]

    def shabd_ki_bhasha_jaano_code(shabd):
        return Translator().detect(shabd).lang
