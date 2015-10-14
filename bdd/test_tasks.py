# coding=utf-8
"""./tasks.feature feature tests."""

import requests
from pytest_bdd import (
    given,
    scenario,
    then,
    when
)

@scenario('./tasks.feature', 'Testar os endpoints da API de Tasks')
def test_testar_os_endpoints_da_api_de_tasks():
    """Testar os endpoints da API de Tasks."""


@given('que eu acesso a raiz da API de Tasks')
def que_eu_acesso_a_raiz_da_api_de_tasks(w):
    """que eu acesso a raiz da API de Tasks."""
    w.r = requests.get('http://localhost:8000')


@given('nessa requisição eu tenho a URL para acessar Tasks')
def nessa_requisição_eu_tenho_a_url_para_acessar_tasks(w):
    """nessa requisição eu tenho a URL para acessar Tasks."""
    w.url = w.r.json()['tasks']
    assert w.url == 'http://localhost:8000/tasks/'


@when('eu acesso essa URL')
def eu_acesso_essa_url(w):
    """eu acesso essa URL."""
    w.tasks = requests.get(w.url)


@then('eu vejo a lista de Tasks')
def eu_vejo_a_lista_de_tasks(w):
    """eu vejo a lista de Tasks."""
    assert len(w.tasks.json()) == 3
    assert w.tasks.json()[0]['status'] == 'Done'


@then('eu crio uma nova Task para Estudar')
def eu_crio_uma_nova_task_para_estudar(w):
    data = {
        "name": "Estudar",
        "owner": "Mario",
        "status": "New"
    }
    w.task = requests.post(w.url, data)
    assert w.task.json()['name'] == 'Estudar'
