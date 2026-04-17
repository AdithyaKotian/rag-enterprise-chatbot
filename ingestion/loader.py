import os
import pandas as pd
from langchain_core.documents import Document


def load_all_docs(data_path="data"):
    docs = []

    for department in os.listdir(data_path):
        dept_path = os.path.join(data_path, department)

        if not os.path.isdir(dept_path):
            continue

        for file in os.listdir(dept_path):
            file_path = os.path.join(dept_path, file)

            # ----------------------------
            # TEXT FILES
            # ----------------------------
            if file.endswith(".txt"):
                with open(file_path, "r", encoding="utf-8") as f:
                    text = f.read()

                    docs.append(
                        Document(
                            page_content=text,
                            metadata={
                                "department": department,
                                "source": file
                            }
                        )
                    )

            # ----------------------------
            # CSV FILES (FIXED)
            # ----------------------------
            elif file.endswith(".csv"):
                df = pd.read_csv(file_path)

                for i, row in df.iterrows():
                    # 🔥 KEY FIX: include column names
                    text = ", ".join([
                        f"{col}: {row[col]}" for col in df.columns
                    ])

                    docs.append(
                        Document(
                            page_content=text,
                            metadata={
                                "department": department,
                                "source": file,
                                "row": i
                            }
                        )
                    )

    return docs