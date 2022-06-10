import transformers
from transformers import BertModel
from get_source import get_source

model = BertModel.from_pretrained("bert-base-uncased")
target_file = './out.py'
get_source(model, target_file)