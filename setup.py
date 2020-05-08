from setuptools import setup

setup(name='mnemopy',
      version='0.1',
      description='A GUI app for training for memory competitions',
      url='https://github.com/VivekThazhathattil/mnemopy',
      author='Vivek Thazhathattil',
      author_email='vivek.thazhathattil@gmail.com',
      license='MIT',
      packages=['mnemopy'],
      install_requires=[
          'datetime','numpy','PyQt5'
          ],
#      package_data={'': ['dat/*', 'dat/img/*', 'dat/sc/*', 'dat/sn/*']},
      entry_points="""
          [gui_scripts]
          mnemopy = mnemopy.main:main
          """,
      zip_safe=False)
