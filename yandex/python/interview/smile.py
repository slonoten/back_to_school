"""
Сообщение содержит смайлы вида :-))) и :-(((((, нужно удалить смайлы
"""
from typing import Iterable


def remove_smiles(message: Iterable[str]) -> bool:
    """Версия работающая с потоком символов из любого источника"""
    smile_started = False
    mouth_symb = None
    nose_found = False
    result_chunks = []
    possible_smile = []
    for i, ch in enumerate(message):
        if smile_started:
            # Мы внутри смайла
            if mouth_symb:
                # Обрабатываем "рот"
                if ch != mouth_symb:
                    # Рот кончился
                    mouth_symb = None
                    nose_found = False             
                    if ch != ":":
                        smile_started = False
                        result_chunks.append(ch)
                        continue
            elif nose_found:
                if ch in "()":
                    # За "носом" нашли "рот"
                    mouth_symb = ch
            else:
                if ch == '-':
                    nose_found = True
                else:
                    smile_started = False
                    possible_smile = []
                    continue
            possible_smile.append(ch)
        elif ch == ':':
            smile_started = True
            possible_smile.append(ch)
        else:
            result_chunks.append(ch)
    return "".join(result_chunks)


def remove_smiles(message: str) -> bool:
    """Версия с произвольным доступом к строке"""
    non_smile_start_pos = 0
    mouth_symb = None
    result_chunks = []
    for i in range(2, len(message)):
        ch = message[i]
        if mouth_symb:
            # Обрабатываем "рот"
            if ch != mouth_symb:
                # Рот кончился
                mouth_symb = None        
            else:
                non_smile_start_pos = i + 1
            continue
        if message[i - 2: i + 1] in (":-)", ":-("):
            result_chunks.append(message[non_smile_start_pos: i - 2])
            mouth_symb = ch
            continue
    
    result_chunks.append(message[non_smile_start_pos : ])
    return "".join(result_chunks)


assert remove_smiles("zzz:-))))zzz") == "zzzzzz"
assert remove_smiles("") == ""
assert remove_smiles(":-(((") == ""
assert remove_smiles("xxx:-))):-(((ccc") == "xxxccc"                
assert remove_smiles(":-)))xxx:-(((") == "xxx" 
