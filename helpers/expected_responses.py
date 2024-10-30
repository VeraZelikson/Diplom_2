class ExpectedResponses:
    CREATE_ORDER_INVALID_HASH_RESPONSE = {
        "success": False,
        "message": "Internal Server Error"
    }

    CREATE_ORDER_NO_INGREDIENTS_RESPONSE = {
        "success": False,
        "message": "Ingredient ids must be provided"
    }

    CREATE_USER_DUPLICATE_RESPONSE = {
            "success": False,
            "message": "User already exists"
    }

    CREATE_USER_MISSING_FIELDS_RESPONSE = {
        "success": False,
        "message": "Email, password and name are required fields"
    }

    LOGIN_INVALID_CREDENTIALS_RESPONSE = {
        "success": False,
        "message": "email or password are incorrect"
    }

    UPDATE_USER_INFO_UNAUTHORIZED_RESPONSE = {
        "success": False,
        "message": "You should be authorised"
    }

    UPDATE_USER_INFO_EMAIL_EXISTS_RESPONSE = {
        "success": False,
        "message": "User with such email already exists"
    }

    GET_USER_ORDERS_UNAUTHORIZED_RESPONSE = {
        "success": False,
        "message": "You should be authorised"
    }
