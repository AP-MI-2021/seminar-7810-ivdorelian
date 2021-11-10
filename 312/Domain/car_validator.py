from Domain.car import Car


class CarValidator:

    def validate(self, car: Car):
        valid_comforts = ['standard', 'ridicat', 'premium']
        if car.comfort_level not in valid_comforts:
            raise ValueError('Nivelul de comfort trebuie'
                             f'sa fie unul dintre {valid_comforts}')