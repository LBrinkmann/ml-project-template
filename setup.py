from setuptools import setup, find_packages


project_name = 'iris'


def load_requirements(filename='requirements.txt'):
    with open(filename) as f:
        lines = f.readlines()
    return lines


setup(
    name=project_name,
    version="0.0.1",
    description='',
    url='',
    author='MPIB - Human and Machines',
    author_email='',
    license='',
    packages=[package for package in find_packages()
              if package.startswith(project_name)],
    zip_safe=False,
    install_requires=load_requirements(),
    extras_require={'dev': load_requirements('requirements_dev.txt')},
    scripts=[
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)
