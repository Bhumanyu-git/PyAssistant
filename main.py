import speech_recognition
import win32com.client
import os
import webbrowser
import datetime
from time import sleep
def take_input():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        audio = r.listen(source)
        try:
            return r.recognize_google(language = "en-IN", audio_data = audio)
        except speech_recognition.UnknownValueError:
            say("Sorry, I didn't catch that")
            return "I didn't catch that"
        except speech_recognition.RequestError:
            say("Sorry, could not connect to the internet")
            return "Sorry, could not connect to the internet"
def say(text):
    speech = win32com.client.Dispatch("SAPI.SpVoice")
    speech.Speak(text)
def show_user_input(text):
    print(text)
if __name__ == "__main__":
    say("Listening")
    while True:
        print("Listening...")
        i = take_input()
        show_user_input(i)
        if "play music" in i:
            say("Playing music")
            os.system("start C:/Users/HP/Downloads/music.mp3")
        elif "open site" in i:
            say("Please enter the name of site you want to open")
            i = input("Site: ")
            try:
                say(f"Opening {i}")
                webbrowser.open(f"https://{i}.com")
            except Exception as e:
                say(f"Sorry could not open the website '{i}. I will be able to open the site you want to open if you can provide the Uniform Resource Locater also calle URL")
                webbrowser.open(input("URL: "))
        elif "change directory" in i:
            say("Please enter the path of directory you want to open")
            os.system(f"cd {input("Directory: ")}")
        elif "open app" in i:
            say("Please enter the path of app you want to open")
            os.system(f"start {input("Path: ")}")
        elif "what is the time" in i:
            time = datetime.datetime.now().strftime("%I:%M:%S")
            say(f"The time is {time}")
            print(f"Time: {time}")
        elif "manage file" in i:
            say("What actions you want to apply to files?")
            i = input("Action: ")
            if "create" in i:
                say("Please enter the name of file you want to create(default extention is .txt)")
                try:
                    with open(input("Name of file: "), 'x') as file:
                        say("Please enter the data you want to enter to your file")
                        file.write(input("Data: "))
                        say("File created successfully")
                except FileExistsError:
                    say("File already exists")
                    print("File already exists")
                except Exception as e:
                    say("An error occurred")
                    print("An error occurred")
            elif "view" in i:
                files = os.listdir()
                if len(files) == 0:
                    say("No files found in directory")
                    print("No files found in directory")
                else:
                    say("Files in directory are:")
                    print("Files in directory are:")
                    for file in files:
                        say(file)
                        print(file)
                        sleep(1)
            elif "delete" in i:
                say("Please enter the name of file you want to delete")
                try:
                    os.remove(input("Name of file: "))
                    say("File deleted successfully")
                except FileNotFoundError:
                    say("File not found")
                    print("File not found")
                except Exception as e:
                    say("An error occurred")
                    print("An error occurred")
            elif "read" in i:
                say("Enter the name of file you want to read")
                try:
                    with open(input("Name of file: ")) as file:
                        content = file.read()
                        say(f"Data read from the file is {content}")
                        print(f"Data readd from thr file is:\n{content}")
                except FileNotFoundError:
                    say("File not found")
                    print("File not found")
                except Exception as e:
                    say("An error occurred")
                    print("An error occurred")
            elif "edit" in i:
                say("Please enter the name of file you want to edit")
                try:
                    with open(input("Name of file: "), 'w') as file:
                        say("Enter the data you want to enter in the file")
                        file.write(input("Data: "))
                        say("File edited successfully")
                except FileNotFoundError:
                    say("File not found")
                    print("File not found")
                except Exception as e:
                    say("An error occurred")
                    print("An error occurred")
        elif "python" in i:
            os.system("python")
        elif "close" in i:
            say("Goodbye, have a good day ahead")
            quit()