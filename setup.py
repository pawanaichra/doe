import setuptools
setuptools.setup(
    name="doe",
    version="0.1.0",
    url="https://github.com/pawanaichra/doe",
    author="Pawan Aichra",
    author_email="aichrapawan@gmail.com",
    description="A simple library for design of experiments and analysis",
    long_description=open('README.md').read(),
    keywords='design of experiments analysis doe',
    license='MIT',
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'pandas', 'scipy', 'PTable'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
)