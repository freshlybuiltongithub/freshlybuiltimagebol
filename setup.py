from distutils.core import setup
setup(
  name = 'freshlybuiltimagebol',         
  packages = ['freshlybuiltimagebol'],   
  version = '0.0.1b',     
  license='MIT',        
  description = 'Image Bhi Bol Uthegi',   
  author = 'Vishal Sharma',                   
  author_email = 'vishalsharma.gbpecdelhi@gmail.com',      
  url = 'https://github.com/FreshlyBuilt/freshlybuiltimagebol',   
  download_url = 'https://github.com/FreshlyBuilt/freshlybuiltimagebol/archive/v0.0.1b.tar.gz',  
  keywords = ['Image', 'Audio', 'Text'],   
  install_requires=[            
          'hyper',
          'googletrans',
          'gTTS',
          'Pillow',
          'pytesseract'
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
