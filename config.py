import os

class Config:
    TOKEN = "8423725996:AAGi92MUk53ZHk8aOAHRj2ywcuTzXWFIHu0"
    SUDO_USER_ID = 6683927711
    DATABASE_URL = os.getenv('DATABASE_URL')
    
    CARD_VALUES = {'Common': 2000, 'Rare': 5000, 'Icon': 25000, 'Ultimate': 100000, 'Supreme': 300000}
    DROP_CHANCES = {'Supreme': 1, 'Ultimate': 10, 'Icon': 14, 'Rare': 35, 'Common': 40}
    EMOJIS = {'Common': '⚪️', 'Rare': '🔵', 'Icon': '🟡', 'Ultimate': '🔴', 'Supreme': '💜'}
