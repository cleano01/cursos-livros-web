from django.db import models
from django.contrib.auth import get_user_model


class Chassi(models.Model):
    numero = models.CharField(("Chassi"), max_length=16)

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero



class Montadora(models.Model):
    nome = models.CharField("Nome", max_length=50)

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return self.nome
    

def set_default_montadora():
    return Montadora.objects.get_or_create(nome='Padrão')[0]


class Carro(models.Model):
    """
    #OneToOneField
    Cada carro so pode se relacionar com um chassi
    e cada chassi so pode se relcaionar com um carro
    
    #ForeignKey (OneToMany)
    Cada carro tem uma montadora,
    mas uma montadora pode 'montar'
    varios carros


    #ManyToMany
    Um carro pode ser dirigido
    por varios motoristas
    e um motoritas pode dirgir diversos 
    carros
    """
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)  
    montadora = models.ForeignKey(Montadora, on_delete=models.SET(set_default_montadora))
    motoristas = models.ManyToManyField(get_user_model())
    modelo =  models.CharField(("Modelo"), max_length=50)
    preco = models.DecimalField(("Preço"), max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.montadora}  {self.modelo}'
    