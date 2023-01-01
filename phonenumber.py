import phonenumbers
from phonenumbers import geocoder

phone = input('Digite o telefone em um formato +5581983364067')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))