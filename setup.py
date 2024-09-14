from setuptools import setup

setup(name='bntx-extractor',
      version='0.6',
      description='BNTX Extractor',
      entry_points = {
          'console_scripts': ['bntx-extractor=bntx_extract:main']
        },
      packages=['bntx_extract'],
      setup_requires=["cython"],
      install_requires=[
        'pillow',
        'astc-decomp-faster',
        'Cython'
        ]
        )
