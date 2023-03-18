from setuptools import setup, find_packages

setup(
    name="drutai",
    # version="0.0.1",
    version="0.0.0.0.1",
    keywords=("pip", "drutai"),
    description="drutai",
    long_description="deep learning drug-target interaction",
    license="MIT",

    url="https://github.com/2003100127",
    author="Jianfeng Sun",
    author_email="jianfeng.sunmt@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    python_requires='>3.6',
    install_requires=[
        'pandas==1.3.5',
        'numpy==1.19.5',
        'biopython==1.79',
        'pyfiglet==0.8.post1',
        'click==8.1.3',
        # 'rdkit-pypi==2022.3.2',
        # 'tensorflow-gpu==2.6.0',
    ],
    entry_points={
        'console_scripts': [
            'drutai=drutai.Main:main',
            'drutai_download=drutai.Main:download',
        ],
    }
)