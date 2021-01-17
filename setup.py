from distutils.core import setup
from os import path

DESCRIPTION = """freshlybuiltimagebol is the library made to allow users to perform various
                 operations with text and images including translation to different languages,
                 generarting audio file from text,extracting text from image and many more."""

# The directory containing this file
this_directory = path.abspath(path.dirname(__file__))

# Import the README and use it as the long-description.
try:
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name='freshlybuiltimagebol',
    packages=['freshlybuiltimagebol'],
    version='0.0.2.8',
    license='MIT',
    description='Photo Bhi Bol Uthega',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Vishal Sharma',
    author_email='vishalsharma.gbpecdelhi@gmail.com',
    url='https://github.com/FreshlyBuilt/freshlybuiltimagebol',
    download_url='https://github.com/FreshlyBuilt/freshlybuiltimagebol/archive/v0.0.2.8.tar.gz',
    keywords=['Image', 'Audio', 'Text'],
    install_requires=[
        'hyper==0.5.0',
        'tqdm==4.46.0',
        'colorama~=0.4',
        'googletrans==3.1.0a0',
        'gTTS==2.2.1',
        'gTTS-token==1.1.4',
        'Pillow~=7.0',
        'pytesseract==0.3.2',
        'opencv-python==4.1.2.30',
        'numpy==1.16.3',
        'matplotlib==3.1.3',
        'imutils==0.5.3',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
