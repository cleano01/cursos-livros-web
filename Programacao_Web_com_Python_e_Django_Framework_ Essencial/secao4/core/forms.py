from django import forms
from django.core.mail.message import EmailMessage

from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(label = 'Nome', max_length=100)
    email = forms.CharField(label= 'E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Messagem', widget=forms.Textarea)


    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'nome: {nome}\n\
        Email: {email}\n\
        assunto: {assunto}\n\
        mensgem: {mensagem}'

        mail = EmailMessage(
            subject= 'email enviado via sistema',
            body = conteudo,
            from_email= 'contao@gmail.com',
            to = ['contao@gmail.com',],
            headers= {'Reply-To': email}
        )

        mail.send()


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']


