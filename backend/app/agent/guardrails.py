def enforce_structure(result:dict)->dict:
    result.setdefault('proposed_orders',[])
    return result
