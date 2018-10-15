import setuptools
setuptools.setup(
    name="doe",
    version="0.1.3",
    url="https://github.com/pawanaichra/doe",
    author="Pawan Aichra",
    author_email="aichrapawan@gmail.com",
    description="A simple library for design of experiments and analysis in Python",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=[
        'DOE',
        'design of experiments',
        'experimental design',
        'analysis of experiments',
        'crd rcbd latin square'
        ],
    license='MIT',
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'pandas', 'scipy', 'PTable'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
    ],
)