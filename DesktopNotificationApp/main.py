from plyer import notification

title = 'Morning Call!'
app_name = 'Good Morning!'
message = 'Get Up! And Feed Your Pikachu! '

notification.notify(title = title,
                    app_name = app_name,
                    message = message,
                    app_icon = 'pokemon.ico',
                    timeout = 10,
                    toast = False)