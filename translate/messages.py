import random
# WELCOME_MESSAGE

def get_welcome_message():
    return [
        WELCOME_MESSAGE_EN, 
        WELCOME_MESSAGE_ES
    ]
    
WELCOME_MESSAGE_EN = "Hi {0} and welcome to therapy! My name is Remi and I'm here to help you. ¿What would you like to do now"
WELCOME_MESSAGE_ES = "¡Hola {0} y bienvenido a terapia! Mi nombre es Remi y estoy aqui para ayudarte. ¿Qué te gustaría hacer ahora?"


# THERAPY_CHOICE_MESSAGE

def get_therapy_choice_message():
    return [
        THERAPY_CHOICE_MESSAGE_EN, 
        THERAPY_CHOICE_MESSAGE_ES
    ]

THERAPY_CHOICE_MESSAGE_EN = "Great! Let me choose an image for you."
THERAPY_CHOICE_MESSAGE_ES = "¡Genial! Voy a comenzar eligiendo una fotografía para comenzar."


# THERAPY_ASK_TO_CHANGE_MESSAGE

def get_therapy_ask_to_change_message():
    return [
        THERAPY_ASK_TO_CHANGE_MESSAGE_EN, 
        THERAPY_ASK_TO_CHANGE_MESSAGE_ES
    ]

THERAPY_ASK_TO_CHANGE_MESSAGE_EN = "Would you like to talk about this photo or do you prefer to change it?"
THERAPY_ASK_TO_CHANGE_MESSAGE_ES = "¿Te gustaría hablar sobre esta foto o prefieres cambiarla?"


# THERAPY_CHANGE_PHOTO_MESSAGE

def get_therapy_change_photo_message():
    return [
        THERAPY_CHANGE_PHOTO_MESSAGE_EN, 
        THERAPY_CHANGE_PHOTO_MESSAGE_ES
    ]

THERAPY_CHANGE_PHOTO_MESSAGE_EN = "Lets try with this one..."
THERAPY_CHANGE_PHOTO_MESSAGE_ES = "Vamos a probar con esta otra..."


# THERAPY_NO_MORE_QUESTIONS_MESSAGE

def get_therapy_no_more_questions_message():
    return [
        THERAPY_NO_MORE_QUESTIONS_MESSAGE_EN, 
        THERAPY_NO_MORE_QUESTIONS_MESSAGE_ES
    ]

THERAPY_NO_MORE_QUESTIONS_MESSAGE_EN = "I think it's enough, let's try with another image!"
THERAPY_NO_MORE_QUESTIONS_MESSAGE_ES = "Creo que ya es suficiente, ¡vamos a probar con otra foto!"


# THERAPY_BEGIN_FIRST_MESSAGE

def get_therapy_begin_first_message():
    return [
        THERAPY_BEGIN_FIRST_MESSAGE_EN, 
        THERAPY_BEGIN_FIRST_MESSAGE_ES
    ]

THERAPY_BEGIN_FIRST_MESSAGE_EN = "Look at the image and try to remember everything you can."
THERAPY_BEGIN_FIRST_MESSAGE_ES = "Mira la fotografía e intenta recordar todo lo que puedas."


# THERAPY_BEGIN_SECOND_MESSAGE

def get_therapy_begin_second_message():
    return [
        THERAPY_BEGIN_SECOND_MESSAGE_EN,
        THERAPY_BEGIN_SECOND_MESSAGE_ES
    ]

THERAPY_BEGIN_SECOND_MESSAGE_EN = "Do you remember when this photo was taken?"
THERAPY_BEGIN_SECOND_MESSAGE_ES = "¿Recuerdas cuando fue tomada esta foto?"


# ASK_WHAT_TO_DO

def get_ask_what_to_do_message():
    return [
        ASK_WHAT_TO_DO_EN, 
        ASK_WHAT_TO_DO_ES
    ]

ASK_WHAT_TO_DO_EN = "What would you like to do now?"
ASK_WHAT_TO_DO_ES = "¿Qué te gustaría hacer ahora?"


# ERROR_MESSAGE

def get_error_message():
    return [
        ERROR_MESSAGE_EN, 
        ERROR_MESSAGE_ES
    ]

ERROR_MESSAGE_EN = "Sorry, It seems I can't do this yet 😕. Try something else."
ERROR_MESSAGE_ES = "Vaya, parece que todavía no puedo hacer esto 😕. Prueba con otra cosa."


# GOODBYE_MESSAGE

def get_goodbye_message():
    return [
        GOODBYE_MESSAGE_EN, 
        GOODBYE_MESSAGE_ES
    ]

GOODBYE_MESSAGE_EN = "I've enjoyed talking with you. Come back whenever you want! 👋"
GOODBYE_MESSAGE_ES = "Me ha encantado hablar contigo. ¡Vueve cuando quieras! 👋"


# UPLOAD_IMAGE_MESSAGE

def get_upload_image_message():
    return [
        UPLOAD_IMAGE_MESSAGE_EN, 
        UPLOAD_IMAGE_MESSAGE_ES
    ]

UPLOAD_IMAGE_MESSAGE_EN = "Upload the images that you want to use for the therapy. Press the finish button when you are done."
UPLOAD_IMAGE_MESSAGE_ES = "Sube las imágenes que quieras utilizar para realizar la terapia. Cuando hayas terminado pulsa el botón terminar."


# FINISH_UPLOAD_IMAGE_MESSAGE

def get_finish_upload_image_message():
    return [
        FINISH_UPLOAD_IMAGE_MESSAGE_EN, 
        FINISH_UPLOAD_IMAGE_MESSAGE_ES
    ]

FINISH_UPLOAD_IMAGE_MESSAGE_EN = "Thanks for uploading your images! 😄"
FINISH_UPLOAD_IMAGE_MESSAGE_ES = "¡Gracias por subir tus imágenes! 😄"


# DELETE_DATA_MESSAGE

def get_delete_data_message():
    return [
        DELETE_DATA_MESSAGE_EN, 
        DELETE_DATA_MESSAGE_ES
    ]

DELETE_DATA_MESSAGE_EN = "This action will delete all your images, questions and answers. Once deleted it cannot be recovered. Are you sure you want to delete all your data?"
DELETE_DATA_MESSAGE_ES = "Esta acción eliminará todas tus imágenes, preguntas y respuestas. Una vez eliminado no se puede recuperar. ¿Estás seguro que quieres eliminar todos tus datos?"


# CONFIRM_DELETE_DATA_MESSAGE

def get_confirm_delete_data_message():
    return [
        CONFIRM_DELETE_DATA_MESSAGE_EN, 
        CONFIRM_DELETE_DATA_MESSAGE_ES
    ]

CONFIRM_DELETE_DATA_MESSAGE_EN = "I've remove all your data."
CONFIRM_DELETE_DATA_MESSAGE_ES = "He eliminado todos tus datos."

# NO_IMAGES_MESSAGE

def get_no_images_message():
    return [
        NO_IMAGES_MESSAGE_EN, 
        NO_IMAGES_MESSAGE_ES
    ]

NO_IMAGES_MESSAGE_EN = "To start therapy you must upload some images. To do that, select the \"Upload images\" button."
NO_IMAGES_MESSAGE_ES = "Para poder realizar la terapia necesitas subir algunas imágenes. Para ello selecciona el botón \"Subir imágenes\" del menú principal."


# FINISH_UPLOAD_IMAGE_MESSAGE

def get_bot_answer():
    random_number = random.randint(0, len(BOT_ANSWER_EN) - 1)
    
    return [
        BOT_ANSWER_EN[random_number], 
        BOT_ANSWER_ES[random_number]
    ]

BOT_ANSWER_EN = [
    "Okeey",
    "Amazing!",
    "Interesting...",
    "Perfect!",
    "That's cool!",
    "Let's keep going",
    "Here is another question",
    "Really?",
]
BOT_ANSWER_ES = [
    "Okeey",
    "¡Genial!",
    "Interesante...",
    "¡Estupendo!",
    "Que guay",
    "Sigamos avanzando",
    "Ahi va otra",
    "¿Ah si?",
]


def get_message(name):
    if (name == "WELCOME_MESSAGE"):
        return  get_welcome_message()
    elif (name == "THERAPY_CHOICE_MESSAGE"):
        return get_therapy_choice_message()
    elif (name == "THERAPY_ASK_TO_CHANGE_MESSAGE"):
        return get_therapy_ask_to_change_message()
    elif (name == "THERAPY_CHANGE_PHOTO_MESSAGE"):
        return get_therapy_change_photo_message()
    elif (name == "THERAPY_NO_MORE_QUESTIONS_MESSAGE"):
        return get_therapy_no_more_questions_message()
    elif (name == "THERAPY_BEGIN_FIRST_MESSAGE"):
        return get_therapy_begin_first_message()
    elif (name == "THERAPY_BEGIN_SECOND_MESSAGE"):
        return get_therapy_begin_second_message()
    elif (name == "ASK_WHAT_TO_DO"):
        return get_ask_what_to_do_message()
    elif (name == "ERROR_MESSAGE"):
        return get_error_message()
    elif (name == "GOODBYE_MESSAGE"):
        return get_goodbye_message()
    elif (name == "UPLOAD_IMAGE_MESSAGE"):
        return get_upload_image_message()
    elif (name == "FINISH_UPLOAD_IMAGE_MESSAGE"):
        return get_finish_upload_image_message()
    elif (name == "DELETE_DATA_MESSAGE"):
        return get_delete_data_message()
    elif (name == "CONFIRM_DELETE_DATA_MESSAGE"):
        return get_confirm_delete_data_message()
    elif (name == "NO_IMAGES_MESSAGE"):
        return get_no_images_message()
    elif (name == "BOT_ANSWER"):
        return get_bot_answer()
    
        