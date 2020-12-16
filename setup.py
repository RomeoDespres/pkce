import setuptools


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='pkce',
    version='1.0.1',
    author='Roméo Després',
    author_email='despres.romeo@gmail.com',
    description='PKCE Pyhton generator.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/RomeoDespres/pkce',
    package_data={'pkce': ['py.typed']},
    packages=['pkce'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3',
    zip_safe=False
)
