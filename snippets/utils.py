from snippets.models import PaymentType
from snippets.models import PlanPaymentType


class FooException(Exception):
    def __init__(self, foo):
        self.foo = foo


def PaymentHelper_checkPayment(payment):
    data = {
        "error": False,
        "isValid": True,
        "message": "pagamento válido"
    }

    if payment['type'] == 1:
        data.update({
            "error": True,
            "isValid": False
        })
        if payment['addressStreet'] == "":
            data.update({
                "message": "É preciso preencher um nome de endereço válido"
            })
        elif payment['addressNumber'] == "":
            data.update({
                "message": "É preciso preencher um numero de endereço válido"
            })
        elif payment['addressDistrict'] == "":
            data.update({
                "message": "É preciso preencher um nome de bairro válido"
            })
        elif payment['addressCity'] == "":
            data.update({
                "message": "É preciso preencher um nome de cidade válido"
            })
        elif payment['addressState'] == "":
            data.update({
                "message": "É preciso preencher um nome de estado válido"
            })
        elif payment['addressZipCode'] == "":
            data.update({
                "message": "É preciso preencher um endereço postal válido"
            })
    elif payment['type'] == 2:
        data.update({
            "error": True,
            "isValid": False
        })
        if payment['number'] == "":
            data.update({
                "message": "É preciso preencher um numero de cartão válido"
            })
        elif payment['holder'] == "":
            data.update({
                "message": "É preciso preencher um nome de usuário válido"
            })
        elif payment['date'] == "":
            data.update({
                "message": "É preciso preencher uma data de vencimento válida"
            })
        elif payment['security'] == "":
            data.update({
                "message": "É preciso preencher um código de segurança válido"
            })

    return data


def PaymentHelper_isValid(paymentType, plan):
    data = {
        "error": False,
        "isValid": True,
        "message": ""
    }
    try:
        paymentType_model = PaymentType.objects.filter(id=paymentType.id, status=1)

        if not paymentType_model:
            raise FooException("Método de pagamento inválido e/ou inativo.")

        planPaymentType_model = PlanPaymentType.objects.filter(plan=plan.id)
        if not planPaymentType_model:
            raise FooException("Este plano não aceita este metódo de pagamento")

        data.update({
            "message": "Pagamento válido"
        })

    except FooException as e:
        data.update({
            "message": e.foo
        })

    finally:
        return data


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
