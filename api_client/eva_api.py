import requests

class EVAAPI:
    BASE_URL = "http://150.214.230.39:8082/api/v1"

    def __init__(self, base_url=None):
        if base_url:
            self.BASE_URL = base_url

    def evaluate_output(self, evaluation_type, outputs):
        """
        Evaluate outputs generated by LLM.
        
        :param evaluation_type: Type of evaluation ("yes_no", "three_reasons", or "wh_question").
        :param outputs: List or single Output object (dict) with expected and generated results.
        :return: Evaluation results.
        """
        response = requests.post(
            f"{self.BASE_URL}/evaluate",
            params={"evaluation_type": evaluation_type},
            json=outputs
        )
        response.raise_for_status()
        return response.json()
