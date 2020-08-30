from distutils.core import setup
setup(
  name = 'email_sender',         # How you named your package folder (MyLib)
  packages = ['email_sender'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Simple classes to send emails.',   # Give a short description about your library
  author = 'Luca Bozzi',                   # Type in your name
  author_email = 'lucabozzi04@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Izzobacul/email_sender',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Izzobacul/email_sender/archive/v1.0.tar.gz',    # I explain this later on
  keywords = ['EMAIL', 'SMTP'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'smtplib'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Communications',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)