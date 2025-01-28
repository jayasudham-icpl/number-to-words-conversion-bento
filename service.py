import bentoml
import inflect

# Initialize the Inflect engine for number-to-words conversion
p = inflect.engine()

@bentoml.service(name="number_to_words_service")
class NumberToWordsService:
    @bentoml.api
    def convert_number(self, input_data: dict) -> dict:
        try:
            number = input_data.get("number")
            if number is None:
                return {"error": "Missing 'number' in input data"}
            
            words = p.number_to_words(number)
            return {
                "number": number,
                "words": words
            }
        except Exception as e:
            return {"error": str(e)}