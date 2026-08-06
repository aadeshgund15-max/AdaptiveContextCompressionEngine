from Backend.evaluation.dataset import EvaluationDataset



def test_dataset_creation():

    dataset = EvaluationDataset()


    dataset.add_sample(
        "Explain retrieval augmented generation",
        "Explain RAG"
    )


    samples = dataset.get_samples()


    assert len(samples) == 1
    assert samples[0]["compressed"] == "Explain RAG"