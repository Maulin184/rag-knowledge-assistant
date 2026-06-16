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

        is_hit = bool(
            expected_pages
            &
            retrieved_pages
        )

        if is_hit:
            hits += 1

        print("=" * 50)
        print(f"Question: {question}")
        print(f"Expected pages: {sorted(expected_pages)}")
        print(f"Retrieved pages: {sorted(retrieved_pages)}")

        print(
            f"Result: "
            f"{'HIT' if is_hit else 'MISS'}"
        )
        # ----------------------------------
        # Only show chunk details on MISS
        # ----------------------------------

        if not is_hit:

            print()
            print(
                "Retrieved Chunks:"
            )

            for rank, chunk in enumerate(
                result.retrieved_chunks,
                start=1
            ):

                snippet = (
                    chunk.text
                    .replace("\n", " ")
                    .strip()
                )

                snippet = (
                    snippet[:250]
                    + "..."
                )

                print()

                print(
                    f"Rank #{rank}"
                )

                print(
                    f"Page: {chunk.page}"
                )

                print(
                    f"Chunk ID: "
                    f"{chunk.chunk_id}"
                )

                print(
                    f"Distance: "
                    f"{chunk.distance:.4f}"
                )

                print(
                    f"Snippet: "
                    f"{snippet}"
                )

        print("=" * 80)

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