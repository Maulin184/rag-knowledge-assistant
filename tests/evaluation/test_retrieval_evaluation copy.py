import json

from backend.dependencies import (
    retrieval_service,
    vector_store
)


DOCUMENT_ID = "doc_001"


def test_retrieval_hit_at_k():

    # ---------------------
    # Load Index
    # ---------------------

    vector_store.load_index(
        DOCUMENT_ID
    )

    # ---------------------
    # Load Dataset
    # ---------------------

    with open(
        "tests/evaluation/evaluation_dataset.json",
        "r",
        encoding="utf-8"
    ) as f:

        dataset = json.load(f)

    total_questions = len(
        dataset
    )

    hits = 0

    # ---------------------
    # Evaluate
    # ---------------------

    for sample in dataset:

        question = sample[
            "question"
        ]

        expected_pages = set(
            sample[
                "expected_pages"
            ]
        )

        result = (
            retrieval_service.retrieve(
                question=question,
                k=4
            )
        )

        retrieved_pages = {

            chunk.page

            for chunk in result.retrieved_chunks
        }

        if (
            expected_pages
            &
            retrieved_pages
        ):
            hits += 1
        print("=" * 50)
        print(f"Question: {question}")
        print(f"Expected pages: {expected_pages}")
        print(f"Retrieved pages: {retrieved_pages}")

    hit_rate = (
        hits /
        total_questions
    )

    print()

    print(
        "=" * 50
    )

    print(
        f"Questions: {total_questions}"
    )

    print(
        f"Hits: {hits}"
    )

    print(
        f"Hit@4: {hit_rate:.2%}"
    )

    print(
        "=" * 50
    )

    assert hit_rate > 0