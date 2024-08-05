import pne

if __name__ == "__main__":
    response: str = pne.chat(model="gpt-3.5-turbo", messages="hello")
    print(response)
