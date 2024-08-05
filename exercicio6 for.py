_nome = 'Rafael Silva'
_count = 0;
_qty = 0
for i in range(1, 101):
    _result = i % 2
    if(_result == 0):
        _count += i
        _qty += 1
        print(f'Numbero par {i}')
_meida = _count / _qty
print(f'Media {_meida}')