# Контракт модуля хранение данных

## Функции:
save_history(entry: str) -> None
load_history() -> List[str]

## Параметры : 
entry: строка с операцией и результатом
возвращаемое значение: список строк 

## Примеры :
save_history("1 + 1 = 2")
history = load_history() #["1 + 1 = 2"]