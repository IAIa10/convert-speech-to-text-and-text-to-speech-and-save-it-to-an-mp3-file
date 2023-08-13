import speech_recognition as sr
import pyttsx3
import soundfile as sf

# Initialize the recognizer
r = sr.Recognizer()


# Function to convert text to speech
def SpeakText(text):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.save_to_file(text, 'speech.mp3')
    engine.runAndWait()


# Loop infinitely for user to speak
while True:
    try:
        # Use the microphone as source for input
        with sr.Microphone() as source:
            # Wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level
            r.adjust_for_ambient_noise(source, duration=0.2)

            # Listen for the user's input
            audio = r.listen(source)

            # Using Google to recognize audio
            text = r.recognize_google(audio)
            text = text.lower()

            print("Did you say: ", text)

            # Convert text to speech and save as mp3
            SpeakText(text)

            # Save the recording as an mp3 file
            sf.write('recording.mp3', audio.frame_data, audio.sample_rate, 'PCM_24')

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Unknown error occurred")