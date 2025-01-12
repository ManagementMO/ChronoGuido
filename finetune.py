import vertexai
from vertexai.preview.language_models import TuningEvaluationSpec, TextGenerationModel
import os

# Set your API Key (securely!)
os.environ["GOOGLE_API_KEY"] = "AIzaSyBniRanVvZaWIDND2z7V_GVjdMkE3nMBmA"  # Replace with your API key

# TODO: Fill in with your project ID, location, and dataset URI
project = "deltahacks-training"  # Replace with your project ID
location = "us-east1"  # e.g., "us-central1"
dataset_uri = "gs://YOUR-BUCKET-NAME/PATH/TO/training_data.jsonl"  # Your JSONL file in Cloud Storage

vertexai.init(project=project, location=location)

# This is the model that will be fine-tuned
model = TextGenerationModel.from_pretrained("text-bison@002")

# Start the fine-tuning job
model.tune(
    training_data=dataset_uri,
    tuning_evaluation_spec=TuningEvaluationSpec(
        evaluation_data=dataset_uri)  # Optional: Add your evaluation dataset URI
)

print("Fine-tuning job started. Check the status here:")
print(model._job.gca_resource)  # Resource path to monitor the status of your job