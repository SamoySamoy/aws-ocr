class LLMClient:
    def extract(self, prompt: str) -> dict:
        raise NotImplementedError


class MockBedrockClient(LLMClient):
    def extract(self, prompt: str) -> dict:
        if "ASIA" in prompt:
            return {
                "records": [
                    {
                        "receivedDate": "2025-01-12T00:00:00Z",
                        "clinicName": "ASIA Dental",
                        "visitDate": "2025-01-10T00:00:00Z",
                        "invoiceNo": "ASIA-001",
                        "particular": "Nguyen Van A",
                        "currency": "VND",
                        "amount": 1500000,
                    }
                ]
            }

        return {
            "records": [
                {
                    "receivedDate": "2025-01-11T00:00:00Z",
                    "clinicName": "JGH Hospital",
                    "visitDate": "2025-01-08T00:00:00Z",
                    "invoiceNo": f"JGH-00{i}",
                    "particular": "Patient X",
                    "currency": "VND",
                    "amount": 1000000,
                }
                for i in range(1, 5)
            ]
        }
