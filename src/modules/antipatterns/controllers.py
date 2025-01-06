from http.client import HTTPException
from antipatterns.services import evaluate_code_against_antipatterns

def evaluate_antipattern(code, antipatterns):
    try:
         # Validar la longitud del código
        if len(code) > 250:
            raise HTTPException(
                status_code=400, 
                detail="The code exceeds the maximum allowed length of 250 characters."
            )

        # Llamar al servicio de negocio
        result = evaluate_code_against_antipatterns(code, antipatterns)

        # Devolver respuesta
        return result, 200

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
