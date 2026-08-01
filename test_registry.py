from Backend.core.model_registry import ModelRegistry

print("First Call")

model1 = ModelRegistry.get_embedding_model()

print("Second Call")

model2 = ModelRegistry.get_embedding_model()

print("\nSame object:", model1 is model2)