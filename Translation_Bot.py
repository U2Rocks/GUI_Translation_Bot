from tkinter.constants import CENTER
import requests
import tkinter as tk


# function to send translation text
def send_request():
    url = "https://nlp-translation.p.rapidapi.com/v1/translate"

    translatable_text = input_text_box.get()
    default_translation_text = "Enter a Sentence to Translate"
    if translatable_text == default_translation_text:
        return

    input_language = "en"
    target_language = lang_var.get()

    querystring = {"text": translatable_text,
                   "to": target_language, "from": input_language}

    headers = {
        'x-rapidapi-host': "nlp-translation.p.rapidapi.com",
        'x-rapidapi-key': "RAPID_API_KEY_HERE"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    # print(response.text)
    searchable_response = response.json()
    # assign response value to label
    translation_for_label = searchable_response["translated_text"][target_language]
    modify_label(translation_for_label)
    clear_input_box()


# function to modify label
def modify_label(new_text):
    translated_text_label.config(text=new_text)


# function to clear text input box
def clear_input_box():
    default_entry_text = "Enter a Sentence to Translate"
    input_text_box.delete(0, 'end')
    input_text_box.insert(0, default_entry_text)


# create tkinter root
root = tk.Tk()
root.title("English to Portuguese/Spanish Translator")
root.geometry("610x300")
root.minsize(610, 300)
root.maxsize(610, 300)
root.config(bg="#34c6eb")

# define supported languages
global supported_languages
supported_languages = ["pt", "es"]
lang_var = tk.StringVar(root)
lang_var.set(supported_languages[0])

# make tkinter objects
global translated_text_label
global select_lang
select_lang = tk.OptionMenu(root, lang_var, *supported_languages)
input_text_box = tk.Entry(root, width=60, font="Helvetica 10")
input_text_box.insert(0, "Enter a Sentence to Translate")
translation_button = tk.Button(
    root, text="Translate Text", command=send_request)
translated_text_frame = tk.Frame(root, bg="#3493eb")
translated_text_label = tk.Label(
    translated_text_frame, text="Ola, tudo bem?", font="Helvetica 15", wraplength=500)


# place tkinter objects on a grid
input_text_box.grid(row=0, column=0, padx=10, pady=10)
translation_button.grid(row=0, column=2, padx=10, pady=10)
translated_text_frame.grid(row=2, column=0, padx=10,
                           pady=10, columnspan=4, rowspan=4)
translated_text_label.grid(row=0, column=0, padx=10, pady=10)
select_lang.grid(row=0, column=1, pady=10)

# call root main loop
root.mainloop()
