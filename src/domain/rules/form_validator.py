# form_validator.py
import re
import streamlit as st


class FormValidator:

    @staticmethod
    def validate_not_empty(value: str, label: str = "This field") -> tuple[bool, str]:
        cleaned = value.strip()
        if not cleaned:
            st.error(f"❌ {label} is required.")
            return False, ""
        return True, cleaned

    @staticmethod
    def validate_zip(zip_code: str) -> tuple[bool, str]:
        if not zip_code:
            return  False  # Do nothing if the field is empty

        if zip_code and not zip_code.isdigit():
            st.error("\u274c ZIP Code must contain only digits.")
            return False

        if len(zip_code) != 5:
            st.error("\u274c US ZIP Code must contain five digits.")
            return False

        st.success("\u2705 ZIP Code is valid!")
        return True, zip_code

    @staticmethod
    def validate_phone(phone: str) -> tuple[bool, str | None]:
        if not phone:
            return  False, None

        # remove all non-digit characters
        digits = re.sub(r"\D", "", phone)

        if len(digits) != 10:
            st.error(f"❌ ERROR! phone number must be ten digits {phone}")
            return False, None

        formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        st.success(f"✅ Phone formatted: {formatted}")

        return True, formatted
