
from functools import wraps
import time
from typing import Callable, Iterable

def timer(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        total_time = time.perf_counter() - t0
        print(f"[TIMER] {func.__name__} took {total_time:.6f}s")
        return result
    return wrapper

def required_column(requireds: Iterable[str] | None = None):
    
    default = {"name", "age", "city"}

    
    def make_deco(reqs):
        reqs_set = set(reqs) if reqs is not None else default
        def deco(func: Callable):
            @wraps(func)
            def wrapper(rows, *args, **kwargs):
                if rows is None:
                    raise ValueError("Boş veri seti (rows==None).")
                if not isinstance(rows, list) or not rows:
                    # Eğer boş liste ise yine hata verilebilir veya boş dönüş yapılabilir.
                    raise ValueError("Boş veri seti (liste boş).")
                # rows[0] tipinin dict olduğunu varsayıyoruz
                keys = set(rows[0].keys())
                missing = reqs_set - keys
                if missing:
                    raise ValueError(f"Eksik kolonlar: {missing}")
                return func(rows, *args, **kwargs)
            return wrapper
        return deco

   
    if callable(requireds):
        return make_deco(default)(requireds)

    return make_deco(requireds)
