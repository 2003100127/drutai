from setuptools import setup, find_packages

setup(
    name="drutai",
    version="0.0.1",
    keywords=["pip", "drutai"],
    description="drutai",
    long_description="deep learning drug-target interaction",
    license="GPL-3.0",

    url="https://github.com/2003100127",
    author="Jianfeng Sun",
    author_email="jianfeng.sunmt@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    python_requires='>=3.11,<3.12',
    install_requires=[
        'pandas',
        'biopython',
        'pyfiglet',
        'click',
        'rdkit',
        'numpy==1.24.3',
        'tensorflow==2.14',

        # 'pandas',
        # 'numpy==1.19.5',
        # 'biopython==1.79',
        # 'pyfiglet==0.8.post1',
        # 'click',
        # # 'rdkit-pypi==2022.3.2',
        # # 'tensorflow-gpu==2.6.0',
    ],
    entry_points={
        'console_scripts': [
            'drutai=drutai.predict:run',
            'drutai_download=drutai.predict:download',
        ],
    }
)