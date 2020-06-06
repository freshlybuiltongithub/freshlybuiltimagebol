# freshlybuiltimagebol
Image to audio file python libary in development

freshlybuiltimagebol is the library made to allow users to perform various operations with text and images including translation to different languages, generarting audio file from text,extracting text from image and many more.

## Installation
To use the library just run the command `pip install freshlybuiltimagebol` from your terminal. If the library is already installed than try `pip install --upgrade freshlybuiltimagebol`.

If any occurs persists then reinstalling the library might help, try `pip install --force-reinstall freshlybuiltimagebol`.

## Features
1. Translating and generating audio files from text
 
 a) Translating Text
 This is used to translate text in different languages.
 Run `freshlybuiltimagebol.ShabdDhwani.shabd_ki_bhasha_badlo(shabd,bhasha)`.
 Here 'shabd' is the text you want to translate and bhasha is the language in which you want to translate. Use lowercase in language name.
 
**Example**
freshlybuiltimagebol.ShabdDhwani.shabd_ki_bhasha_badlo("Welcome to Freshlybuilt","hindi")

b) Pronounciation of the translated text
We can also get a glimpse of how to prnounce the translated text.
Run `freshlybuiltimagebol.ShabdDhwani.bhasa_badlkr_kya_bole(shabd,bhasha)`.

c) Know the language of text (shabd_ki_bhasha_jaano)
Run `freshlybuiltimagebol.ShabdDhwani.shabd_ki_bhasha_jaano(shabd)`.

d)Convert text to sound output(shabd_se_dhwani)
Run `freshlybuiltimagebol.ShabdDhwani.shabd_se_dhwani(shabd,bhasha,filename)`.