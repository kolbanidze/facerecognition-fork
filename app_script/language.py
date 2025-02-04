class Locale:
    def __init__(self, language):
        if language == "ru":
            self.label_variant_app = "Выберите режим регистрации"
            self.button_corp_app = "Корпоративное"
            self.button_local_app = "Локальное"
            self.system_user_name = "Имя пользователя"
            self.system_user_full_name = "Полное имя"
            self.system_password = "Пароль"
            self.system_check_password = "Пароль (проверка)"
            self.info_user_inputs = "Поля для ввода лич. инф."
            self.real_user_name = "Ваше имя"
            self.real_user_last_name = "Ваша фамилия"
            self.real_user_post = "Ваша должность"
            self.real_user_email = "Ваш email"
            self.real_user_phone_number = "Ваш номер телефона"
            self.previous_page = "Предыдущая страница"
            self.next_page = "Следующая страница"
            self.process_scanning = "Процесс сканирования лица"
            self.begin = "Начать"
            self.scan = "Сканировать"
            self.last_page_label = "Регистрация завершена\nСпасибо, что выбрали нас!"
            self.error_too_many_faces = "На фотографии много лиц"
            self.error_face_not_detected = "На фотографии не найдено лицо"
            self.success_face_recognition = "Лицо успешно распознано"
            self.complete = "Завершить"
            self.settings_server_connection = "Настройки"
            self.settings_window_title = "Настройки ⚙️"
            self.db_user_label = "Имя пользователя в базе данных:"
            self.db_user_password_label = "Пароль пользователя в базе данных:"
            self.server_ip_label = "Проверка подключения:"
            self.db_name_label = "Название базы данных:"
            self.bt_server_ip_text = "Проверить"
            self.bt_save_changes_text = "Сохранить изменения"
            self.status_active = "Активен"
            self.status_inactive = "Неактивен"
            self.confirm_text = "Вы уверены, что хотите сохранить изменения?"
            self.yes = "Да"
            self.no = "Нет"
            self.error_fill_in_the_fild = "заполните поле"
            self.error_user_already_exists = "Пользователь уже существует.\nВыбирете другое имя пользователя!"
            self.error_only_latin_letters = 'Поля: "Имя пользователя", "Полное имя" - должны содержать только латинские буквы'
            self.error = "Ошибка"
            self.error_fields_not_fill = "Пожалуйста, заполните все поля."
            self.error_system_user_name_short = 'Поле "Имя пользователя" должно содержать больше трех символов.'
            self.error_password_incorrect_type = 'Поле "Пароль" должно содержать не менее 8 символов,\nа также иметь только буквы латинского алфавита,\nхотя бы одну заглавную букву, прописную букву, спец символ.'
            self.error_system_password_check_different = 'Поля "Пароль" и "Пароль (проверка)" не совпадают.'
            self.error_saving_data = "Произошла ошибка в процессе сохранения данных.\nПопробуйте еще раз."
            self.error_email_already_exists = "Данный адрес электронной почты уже занят."
            self.error_something_went_wrong = "Что-то пошло не так.\nПопробуйте снова."
            self.error_email_incorrect_type = 'Поле "Ваш email" оформлено неправильно.'
            self.error_phone_incorrect_type = 'Поле "Ваш номер телефона" оформлено неправильно.'
            self.error_with_v4l2 = "Извините, произошла проблема при установке пакетов v4l-utils\n;Установите их самостоятельно для корректной работы программы, спасибо."
            self.error_no_camera = "Веб-Камеры не обнаружены."
            self.bt_checking_text = "Проверка..."
            self.loading = "Загрузка"
            self.loading_wait = "Пожалуйста подождите..."

        elif language == "en":
            self.label_variant_app = "Choose type of registration"
            self.button_corp_app = "Corporate"
            self.button_local_app = "Local"
            self.system_user_name = "User name"
            self.system_user_full_name = "Full name"
            self.system_password = "Password"
            self.system_check_password = "Password (check)"
            self.info_user_inputs = "Personal info fields"
            self.real_user_name = "Your name"
            self.real_user_last_name = "Your last name"
            self.real_user_post = "Your position"
            self.real_user_email = "Your email"
            self.real_user_phone_number = "Your phone number"
            self.previous_page = "Previous page"
            self.next_page = "Next page"
            self.process_scanning = "Process scanning face"
            self.begin = "Begin"
            self.scan = "Scan"
            self.last_page_label = "Registration is complete.\nThank you for choosing us!"
            self.error_too_many_faces = "There are too many faces in the photo"
            self.error_face_not_detected = "No face found in the photo"
            self.success_face_recognition = "Face recognized successfully"
            self.complete = "Complete"
            self.settings_server_connection = "Settings"
            self.settings_window_title = "Settings ⚙️"
            self.db_user_label = "Database username:"
            self.db_user_password_label = "Database user password:"
            self.server_ip_label = "Server connection check:"
            self.db_name_label = "Database name:"
            self.bt_server_ip_text = "Check connection"
            self.bt_save_changes_text = "Save changes"
            self.status_active = "Active"
            self.status_inactive = "Inactive"
            self.confirm_text = "Are you sure you want to save the changes?"
            self.yes = "Yes"
            self.no = "No"
            self.error_fill_in_the_fild = "fill in the field"
            self.error_user_already_exists = "User already exists.\nChoose another user name"
            self.error_only_latin_letters = 'Fields: "Username", "Full name", "Password" must contain only latin letters'
            self.error = "Error"
            self.error_fields_not_fill = "Please fill in all fields."
            self.error_system_user_name_short = 'The "User name" field must contain more than three characters.'
            self.error_password_incorrect_type = 'The Password field must contain at least 8 characters,\nas well as only letters of the Latin alphabet, at least one capital letter,\na small letter, and a special character.'
            self.error_system_password_check_different = 'The fields "Password" and "Password (check)" do not match.'
            self.error_saving_data = "An error occurred during the data saving process.\nTry again."
            self.error_email_already_exists = "This email address is already occupied."
            self.error_something_went_wrong = "Something went wrong.\nTry again."
            self.error_email_incorrect_type = 'The "Your email" field has an incorrect format.'
            self.error_phone_incorrect_type = 'The "Your phone number" field has an incorrect format.'
            self.error_with_v4l2 = "Sorry, there was a problem installing the v4l-utils packages;\nInstall them yourself for the program to work correctly, thank you."
            self.error_no_camera = "No webcams found."
            self.bt_checking_text = "Checking..."
            self.loading = "Loading"
            self.loading_wait = "Please wait a moment..."