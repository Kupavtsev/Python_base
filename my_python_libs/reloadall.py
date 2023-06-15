"""
reloadall.py: транзитивная перезагрузка вложенных модулей
"""

import types
from importlib import reload

def status(module):
    print('reloading', module.__name__)

def transitive_reload(module, visited):
    if not module in visited:                       # Пропустить повторное посещение
        status(module)
        reload(module)                              # Перезагрузить дочерние модули
        print(visited)
        visited[module] = None
        for attobj in module.__dict__.values():     # Для всех атрибутов
            if type(attobj) == types.ModuleType:    # Рекурсия, если модуль
                transitive_reload(attobj, visited)

def reload_all(*args):
    visited = []
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)

if __name__ == '__main__':
    import reloadall                                # Тест: перезагрузить самого себя и types
    reload_all(reloadall)