from setuptools import setup, find_packages

setup(
    name="chatbot_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai",
        "python-dotenv",
    ],
    entry_points={
        'console_scripts': [
            'chatbot=src.main:main',
        ],
    },
    author="Seu Nome",
    author_email="seu.email@dominio.com",
    description="Um chatbot utilizando a API do OpenAI",
    license="MIT",
    keywords="chatbot openai",
)
