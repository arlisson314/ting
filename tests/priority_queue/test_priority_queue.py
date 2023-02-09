from ting_file_management.priority_queue import PriorityQueue
import pytest

correct_priority_mock_data = [
    {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": [...],
    },
    {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 11,
        "linhas_do_arquivo": [...]
    }
]

incorrect_priority_mock_data = [
    {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 11,
        "linhas_do_arquivo": [...],
    },
    {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": [...]
    }
]


def test_basic_priority_queueing():
    pq = PriorityQueue()

    assert pq.__len__() == 0

    """ENQUEUE"""

    pq.enqueue(incorrect_priority_mock_data[0])
    assert pq.__len__() == 1

    pq.enqueue(incorrect_priority_mock_data[1])
    assert pq.__len__() == 2

    """DEQUEUE"""

    assert pq.dequeue() == correct_priority_mock_data[0]
    assert pq.dequeue() == correct_priority_mock_data[1]

    """SEARCH"""

    pq.enqueue(correct_priority_mock_data[0])
    pq.enqueue(correct_priority_mock_data[1])

    assert pq.search(0) == correct_priority_mock_data[0]
    assert pq.search(1) == correct_priority_mock_data[1]

    with pytest.raises(IndexError):
        pq.search(3)

    with pytest.raises(IndexError):
        pq.search(-1)
