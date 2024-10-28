class ExpectedResponses:
    # Ответы для получения данных об ингредиентах
    GET_INGREDIENTS_RESPONSE = {
        "success": True,
        "data": []  # Здесь будет массив данных об ингредиентах
    }

    # Ответы для создания заказа
    CREATE_ORDER_SUCCESS_RESPONSE = {
        "success": True,
        "order": {
            "number": 6257
        },
        "name": "Краторный метеоритный бургер"
    }

    CREATE_ORDER_INVALID_HASH_RESPONSE = {
        "success": False,
        "message": "Internal Server Error"
    }

    CREATE_ORDER_NO_INGREDIENTS_RESPONSE = {
        "success": False,
        "message": "Ingredient ids must be provided"
    }

    # Ответы для восстановления и сброса пароля
    PASSWORD_RESET_SUCCESS_RESPONSE = {
        "success": True,
        "message": "Reset email sent"
    }

    PASSWORD_RESET_INVALID_EMAIL_RESPONSE = {
        "success": False,
        "message": "Email is required"
    }

    PASSWORD_RESET_SUCCESSFUL_RESET_RESPONSE = {
        "success": True,
        "message": "Password successfully reset"
    }

    # Ответы для создания пользователя
    CREATE_USER_SUCCESS_RESPONSE = {
        "success": True,
        "user": {
            "email": "",
            "name": ""
        },
        "accessToken": "Bearer ...",
        "refreshToken": ""
    }

    CREATE_USER_DUPLICATE_RESPONSE = {
            "success": False,
            "message": "User already exists"
    }


    CREATE_USER_MISSING_FIELDS_RESPONSE = {
        "success": False,
        "message": "Email, password and name are required fields"
    }

    # Ответы для авторизации
    LOGIN_SUCCESS_RESPONSE = {
        "success": True,
        "accessToken": "",
        "refreshToken": "",
        "user": {
            "email": "",
            "name": ""
        }
    }

    LOGIN_INVALID_CREDENTIALS_RESPONSE = {
        "success": False,
        "message": "email or password are incorrect"
    }

    # Ответы для выхода из системы
    LOGOUT_SUCCESS_RESPONSE = {
        "success": True,
        "message": "Successful logout"
    }

    # Ответы для обновления токена
    TOKEN_UPDATE_SUCCESS_RESPONSE = {
        "success": True,
        "accessToken": "Bearer ..."
    }

    # Ответы для получения и обновления информации о пользователе
    GET_USER_INFO_SUCCESS_RESPONSE = {
        "success": True,
        "user": {
            "email": "",
            "name": ""
        }
    }

    UPDATE_USER_INFO_SUCCESS_RESPONSE = {
        "success": True,
        "user": {
            "email": "",
            "name": ""
        }
    }

    UPDATE_USER_INFO_UNAUTHORIZED_RESPONSE = {
        "success": False,
        "message": "You should be authorised"
    }

    UPDATE_USER_INFO_EMAIL_EXISTS_RESPONSE = {
        "success": False,
        "message": "User with such email already exists"
    }

    # Ответы для удаления пользователя
    DELETE_USER_SUCCESS_RESPONSE = {
        "success": True,
        "message": "User successfully deleted"
    }

    # Ответы для получения всех заказов
    GET_ALL_ORDERS_SUCCESS_RESPONSE = {
        "success": True,
        "orders": [
            {
                "id": "",
                "ingredients": [],
                "status": "done",
                "number": 0,
                "createdAt": "",
                "updatedAt": ""
            }
        ],
        "total": 1,
        "totalToday": 1
    }

    # Ответы для получения заказов конкретного пользователя
    GET_USER_ORDERS_SUCCESS_RESPONSE = {
        "success": True,
        "orders": [
            {
                "id": "",
                "ingredients": [],
                "status": "done",
                "number": 0,
                "createdAt": "",
                "updatedAt": ""
            }
        ],
        "total": 2,
        "totalToday": 2
    }

    GET_USER_ORDERS_UNAUTHORIZED_RESPONSE = {
        "success": False,
        "message": "You should be authorised"
    }
