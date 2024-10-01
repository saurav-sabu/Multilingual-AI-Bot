from setuptools import setup, find_packages

setup(
    name = "MultiLingual Bot",
    version="0.0.1",
    author="Saurav Sabu",
    author_email='saurav.sabu9@gmail.com',
    packages=find_packages(),
    install_requires=["SpeechRecognition","pinwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)