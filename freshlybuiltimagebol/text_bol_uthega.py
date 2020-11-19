from googletrans import Translator
from gtts import gTTS

from .bhasha_codes import bhasha_kosh


class ShabdDhwani:
    """
    
    A class used for translation and audio generation of texts.
    
    The class :class:`ShabdDhwani` is made up of two two Hindi words: ``Shabd`` meaning words and ``Dhwani`` meaning sound. This class, therefore, lets you play with texts and their translations to different languages along with their sounds. You can translate a text and also listen to it, in a particular language.

    """

    bhasha_codes = dict(map(reversed, bhasha_kosh.items()))

    def code_se_naam(bhasha_code):
        bhasha = list(bhasha_kosh.keys())[list(bhasha_kosh.values()).index(bhasha_code)]
        return bhasha

    def shabd_se_dhwani(shabd, bhasha, filename):
        """
        
        Listen to text in audio, in a specific language.
        
        This function accepts a text and a corresponding language, and generates an audio file of that text in that language.

        :param shabd: text that you want to generate an audio file for.
        :type shabd: string
        :param bhasha: Language that you want the audio to be in.
        :type bhasha: string
        :param filename: path/to/filename.mp3 file name must be fed as a string. For e.g. ``shabd_se_dhwani("I am happy", "english", "happy.mp3")`` will save an audio file called ``happy.mp3`` in the same folder as your python script.
        :type filename: string

        >>> from freshlybuiltimage.text_bol_uthega import ShabdDhwani
        >>> import os
        >>> ShabdDhwani.shabd_se_dhwani("This is a wonderful world.", "english", "trans.mp3")
        >>> os.startfile("trans.mp3")

        """

        bhasha = ShabdDhwani.code_se_naam(bhasha)
        anuvadak = Translator().translate(shabd, dest=bhasha)
        anuvadit_file = gTTS(text=anuvadak.text, lang=anuvadak.dest)
        anuvadit_file.save(filename)

    def shabd_ki_bhasha_badlo(shabd, bhasha):
        """
        
        Translates a string from one language to other
        
        :param shabd: The text that you want to translate.
        :type shabd: string
        :param bhasha: The language that you want to translate your text into.
        :type bhasha: string
        :returns: translated text
        :rtype: string
        
        >>> from freshlybuiltimage.text_bol_uthega import ShabdDhwani
        >>> print(ShabdDhwani.shabd_ki_bhasha_badlo("I am so happy!", 'french'))
        Je suis très heureux.

        """

        bhasha = ShabdDhwani.code_se_naam(bhasha)
        return Translator().translate(shabd, dest=bhasha).text

    def bhasa_badlkr_kya_bole(shabd, bhasha):
        """
        
        Translate a text from one language to another.
        
        :param shabd: orginal text that needs to be translated
        :type shabd: string
        :param bhasha: language into which the text needs to be translated
        :type bhasha: string
        :returns: translated text
        :rtype: string

        >>> from freshlybuiltimage.text_bol_uthega import ShabdDhwani
        >>>print(ShabdDhwani.bhasa_badlkr_kya_bole("I am so happy", "hindi"))
        yah ek adbhut duniya hai

        """
        bhasha = ShabdDhwani.code_se_naam(bhasha)
        return Translator().translate(shabd, dest=bhasha).pronunciation

    def shabd_ki_bhasha_jaano(shabd):
        """
        
        Know the language of the text
        
        :param shabd: text
        :type shabd: string
        :returns: language of the text
        :rtype: string

        >>> print(ShabdDhwani.shabd_ki_bhasha_jaano("Itu oru aṟputamāṉa ulakam"))
        tamil

        """
        return bhasha_kosh[Translator().detect(shabd).lang]

    def shabd_ki_bhasha_jaano_code(shabd):
        return Translator().detect(shabd).lang