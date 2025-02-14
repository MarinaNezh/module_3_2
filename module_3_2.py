def send_email(message, recipient, sender="university.help@gmail.com"):
    # Проверка корректности адресов
    def is_valid_email(email):
        return "@" in email and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net"))

    # Проверка на корректность e-mail отправителя и получателя
    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return

    # Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # Проверка на отправителя по умолчанию
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email("Hello!", "recipient@example.com")
send_email("Hello!", "recipient@example.com", "sender@example.com")
send_email("Hello!", "recipient@example.com", "university.help@gmail.com")
send_email("Hello!", "recipient@example.com", "recipient@example.com")
send_email("Hello!", "invalid_email", "university.help@gmail.com")

