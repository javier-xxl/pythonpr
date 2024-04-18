# Import necessary libraries
# import sys
# import getpass
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication

# # Gather personal information
# first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")
# email_domain = input("What is your company's email domain (e.g. example.com)? ")

# # Create the email address
# email_address = f"{first_name.lower()}.{last_name.lower()}@{email_domain}"

# # Prompt the user to confirm the email address
# confirm_email = input(f"Your new email address will be {email_address}. Is that correct? (y/n) ")

# # If the user confirms, create the email
# if confirm_email.lower() == "y":
#     # Create the email message
#     msg = MIMEMultipart()
#     msg['From'] = email_address
#     msg['To'] = email_address
#     msg['Subject'] = "Welcome to the company!"
#     body = "Dear {},\n\nWelcome to the company! We are excited to have you on board.\n\nBest regards,\nThe IT Team".format(first_name)
#     msg.attach(MIMEText(body, 'plain'))

#     # Send the email
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(getpass.getpass("Enter your Gmail address: "), getpass.getpass("Enter your Gmail password: "))
#     text = msg.as_string()
#     server.sendmail(email_address, email_address, text)
#     server.quit()

#     print(f"Your new email address, {email_address}, has been created and a welcome email has been sent to it.")
# else:
#     print("Email address creation cancelled.")


# ------------------------------------------------------------------------------------------------------------------

# información personal
# nombre = input("Ingrese su nombre en munisculas: ")
# apellido = input("Ingrese su apellido munisculas: ")

# # creacion del correo empresarial
# correo_empresarial = f"{nombre.lo40wer()}.{apellido.lower()}@cetus.com.co"

# # Mostrar el correo empresarial generado
# print(f"Su correo empresarial es: {correo_empresarial}")

# # Mostrar mensaje de agradecimiento
# print("¡Gracias por utilizar nuestra herramienta de generación de correos empresariales!")

# ---------------------------------------------------------------------------------------------------------------

# rutina de ejercicio

peso = float(input("Ingrese su peso en kilogramos: "))
contextura = input("Ingrese su contextura corporal (delgado, normal o sobrepeso): ").lower()


if peso < 60:
    print("Su peso es bajo, por lo que recomendamos enfocarse en ejercicios de fuerza y resistencia.")
    print("Realice 3 series de 10 repeticiones de sentadillas, flexiones y dominadas.")
elif peso >= 60 and peso <= 80:
    if contextura == "delgado":
        print("Recomendamos un enfoque equilibrado en ejercicios de fuerza, resistencia y flexibilidad.")
        print("Realice 3 series de 10 repeticiones de sentadillas, flexiones, dominadas, abdominales y estiramientos.")
    elif contextura == "normal":
        print("Su contextura corporal es normal, por lo que recomendamos una rutina equilibrada.")
        print("Realice 3 series de 10 repeticiones de sentadillas, flexiones, dominadas, abdominales y estiramientos.")
    elif contextura == "sobrepeso":
        print("Debido a su sobrepeso, recomendamos enfocarse en ejercicios de resistencia y reducción de peso.")
        print("Realice 3 series de 10 repeticiones de sentadillas, flexiones y caminatas de 30 minutos.")
else:
    print("Su peso es muy alto, por lo que recomendamos consultar a un médico antes de comenzar cualquier rutina de ejercicios.")
